<template>
  <v-form v-model="valid">
    <nuxt-link to="/company/needs">おすすめタイトル例</nuxt-link>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field v-model="title" label="動画タイトル※" required></v-text-field>
        </v-col>

        <v-col cols="12">
          <v-textarea v-model="description" label="動画詳細説明欄※" required></v-textarea>
        </v-col>

        <v-col cols="4">
          <v-select v-model="selectedCategory" :items="categories" label="動画カテゴリ" outlined></v-select>
        </v-col>

        <v-col cols="8">
          <v-text-field v-model="keywords" label="キーワード(カンマ区切りで複数入力できます)"></v-text-field>
        </v-col>

        <v-col cols="12">
          <v-slider
            v-model="movieNumber"
            color="info"
            min="1"
            max="9"
            thumb-label="always"
            label="動画の数"
            messages="※数を変更すると、全ての動画が初期化されます"
            @change="clearMovie"
          ></v-slider>
        </v-col>

        <v-col v-for="i in movieNumber" :key="i" cols="12">
          <v-card>
            <v-card-title>動画 {{ i }}</v-card-title>
            <v-card-text>
              <v-row>
                <v-col cols="12">
                  <input ref="video" type="file" @change="changeFile($event, i)" />
                </v-col>
                <v-col cols="2">
                  <v-btn @click="requestPreview(i)">プレビュー</v-btn>
                </v-col>
                <v-col cols="10">
                  <video width="640" height="480" :src="previewSrc[i]" controls type="video/mp4" />
                </v-col>
                <v-col cols="8">
                  <v-text-field label="動画に入れるテキスト" @change="addText($event, i)" />
                </v-col>
                <v-col cols="4">
                  <v-select
                    v-model="selectedCategory"
                    :items="textPosition"
                    label="テキストを入れる場所"
                    outlined
                    @change="addPosition($event, i)"
                  ></v-select>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-progress-circular v-if="loading" indeterminate color="primary"></v-progress-circular>
        <v-btn color="info" x-large @click="submit">投稿</v-btn>
      </v-card-actions>
    </v-container>
  </v-form>
</template>

<script>
export default {
  middleware: 'user_auth',
  created() {
    this.$axios
      .$get('categories/')
      .then((response) => {
        this.categories = response.map((row) => {
          return row.name
        })
        this.categoryIDs = response.map((row) => {
          return row.id
        })
        this.selectedCategory = this.categories[0]
      })
      .catch(() => {
        this.$toast.error('データ取得時にエラーが発生しました')
      })
  },
  data: () => ({
    previewSrc: [''],
    loading: false,
    valid: false,
    title: '',
    description: '',
    selectedCategory: '',
    categories: [],
    categoryIDs: [],
    textPosition: ['中央', '下'],
    // 空白区切りのkeywordが複数個入力されている
    keywords: '',
    companyID: 1,
    uploadFiles: [null],
    uploadFileTexts: [''],
    uploadFileTextPositions: [''],
    movieNumber: 1,
  }),
  methods: {
    changeFile(event, index) {
      // ファイルが選択されたら変数に入れる
      this.uploadFiles[index - 1] = event.target.files[0]
    },

    addText(text, index) {
      this.uploadFileTexts[index - 1] = text
      console.log(this.uploadFileTexts)
    },

    addPosition(text, index) {
      this.uploadFileTextPositions[index - 1] = text
      console.log(this.uploadFileTextPositions)
    },

    clearMovie() {
      for (let i = 0; i < this.movieNumber; i++) {
        const video = this.$refs.video[i]
        video.type = 'text'
        video.type = 'file'
      }

      // 初期化
      const arr = Array(this.movieNumber)
      this.uploadFiles = arr

      // 長さ以上であれば、切り取るし、短ければ追加する
      if (this.uploadFileTexts.length > this.movieNumber) {
        this.uploadFileTexts = this.uploadFileTexts.slice(0, this.movieNumber)
      } else if (this.uploadFileTexts.length < this.movieNumber) {
        const diff = this.movieNumber - this.uploadFileTexts.length
        for (let i = 0; i < diff; i++) {
          this.uploadFileTexts.push('')
        }
      }

      if (this.uploadFileTextPositions.length > this.movieNumber) {
        this.uploadFileTextPositions = this.uploadFileTextPositions.slice(
          0,
          this.movieNumber
        )
      } else if (this.uploadFileTextPositions.length < this.movieNumber) {
        const diff = this.movieNumber - this.uploadFileTextPositions.length
        for (let i = 0; i < diff; i++) {
          this.uploadFileTextPositions.push('')
        }
      }

      if (this.previewSrc.length > this.movieNumber) {
        this.previewSrc = this.previewSrc.slice(0, this.movieNumber)
      } else if (this.previewSrc.length < this.movieNumber) {
        const diff = this.movieNumber - this.previewSrc.length
        for (let i = 0; i < diff; i++) {
          this.previewSrc.push('')
        }
      }
    },

    async requestPreview(i) {
      const index = i - 1
      const formData = new FormData()
      formData.append('token', this.$auth.getToken('local'))
      // カンマ区切りにして一つの文字列にして送信する
      const keyword = this.keywords.replace(' ', ',')
      formData.append('keywords', keyword)

      // moviesのset && validation
      const movie = this.uploadFiles[index]
      if (movie === null || movie === undefined) {
        this.$toast.error('動画を登録してください')
        return
      }
      formData.append('movies', movie)

      const position = this.uploadFileTextPositions[index]
      if (position === null || position === '') {
        this.$toast.error('テキストを入れる場所を設定してください')
        return
      }
      formData.append('insert_position', position)

      const text = this.uploadFileTexts[index]
      if (text === null || text === '') {
        this.$toast.error('テキストを挿入してください')
        return
      }
      formData.append('insert_text', text)

      this.loading = true
      await this.$axios
        .$post('company/material/preview/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then((response) => {
          this.loading = false
          this.previewSrc[i] = 'data:video/mp4;base64,' + response
          this.$toast.success('ok')
        })
        .catch((error) => {
          console.log(error)
          this.$toast.error('Preview動画作成に失敗しました')
          this.loading = false
        })
    },

    async submit() {
      const formData = new FormData()
      if (this.title === '') {
        this.$toast.error('動画タイトルを登録してください')
        return
      }
      formData.append('title', this.title)

      if (this.description === null) {
        this.$toast.error('動画詳細説明を登録してください')
        return
      }
      formData.append('description', this.description)

      if (this.selectedCategory === '') {
        this.$toast.error('カテゴリを登録してください')
        return
      } else if (this.selectedCategory === 'ショートムービー') {
        formData.append('category_id', 18)
      } else if (this.selectedCategory === '教育') {
        formData.append('category_id', 27)
      } else if (this.selectedCategory === 'ドキュメンタリー') {
        formData.append('category_id', 35)
      }

      formData.append('token', this.$auth.getToken('local'))
      // カンマ区切りにして一つの文字列にして送信する
      const keyword = this.keywords.replace(' ', ',')
      formData.append('keywords', keyword)

      // moviesのset && validation
      for (let i = 0; i < this.uploadFiles.length; i++) {
        const movie = this.uploadFiles[i]
        if (movie === null || movie === undefined) {
          this.$toast.error('登録していない動画があります')
          return
        }
        formData.append('movies', movie)
      }

      // 一応長さチェック
      if (
        this.uploadFiles.length !== this.uploadFileTexts.length ||
        this.uploadFiles.length !== this.uploadFileTextPositions.length
      ) {
        this.$toast.error(
          '処理にエラーがあります。画面をリロードして再度記入してください'
        )
        return
      }

      for (let i = 0; i < this.uploadFileTextPositions.length; i++) {
        const position = this.uploadFileTextPositions[i]
        formData.append('insert_position', position)
      }

      for (let i = 0; i < this.uploadFileTexts.length; i++) {
        const text = this.uploadFileTexts[i]
        formData.append('insert_text', text)
      }

      this.loading = true
      await this.$axios
        .$post('company/video/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then((response) => {
          console.log(response)
          this.$toast.success('投稿に作成しました！！！')
        })
        .catch((error) => {
          console.log(error)
          this.$toast.error('投稿に失敗しました')
        })
      this.loading = false
    },
  },
}
</script>
