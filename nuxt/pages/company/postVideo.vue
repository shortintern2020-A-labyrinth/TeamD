<template>
  <v-form v-model="valid">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field
            v-model="title"
            label="動画タイトル※"
            required
          ></v-text-field>
        </v-col>

        <v-col cols="12">
          <v-textarea
            v-model="description"
            :counter="10"
            label="動画詳細説明欄※"
            required
          ></v-textarea>
        </v-col>

        <v-col cols="12">
          <v-select
            v-model="selectedCategory"
            :items="categories"
            label="動画カテゴリ"
            outlined
          ></v-select>
        </v-col>

        <!-- TODO: 本当はここは入力フォームを複数個作成するべきたけど、めんどくさくてできていない -->
        <v-col cols="12">
          <v-text-field
            v-model="keywords"
            label="キーワード(半角スペース区切りで複数入力できます)"
          ></v-text-field>
        </v-col>

        <v-col cols="4">
          <v-file-input
            label="動画※"
            filled
            prepend-icon="mdi-movie"
            @change="changeFile"
          ></v-file-input>
        </v-col>
        <v-col cols="8">
          動画プレビュー画面
        </v-col>
      </v-row>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn color="secondary" bold @click="submit">Submit</v-btn>
      </v-card-actions>
    </v-container>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    valid: false,
    title: '',
    description: '',
    categories: ['競馬', '伝統工芸'],
    selectedCategory: '',
    // カンマ区切りのkeywordが複数個入力されている
    keywords: '',
    companyID: 1,
    uploadFiles: [],
  }),
  methods: {
    changeFile(file) {
      // ファイルが選択されたら変数に入れる
      this.uploadFiles[0] = file
    },

    async submit() {
      const formData = new FormData()
      formData.append('title', this.title)
      formData.append('description', this.description)
      // TODO: とりあえず固定値を入力している
      formData.append('category_id', 1)
      // TODO: とりあえず固定値を入力している
      formData.append('company_id', 1)

      // keywordsのset
      const keywords = this.keywords.split(' ')
      for (let i = 0; i < keywords.length; i++) {
        const keyword = keywords[i]
        formData.append('keywords[]', keyword)
      }

      // moviesのset
      for (let i = 0; i < this.uploadFiles.length; i++) {
        const movie = this.uploadFiles[i]
        formData.append('movies[]', movie)
      }

      await this.$axios
        .$post('company/video/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then((response) => {
          console.log(response.data.status)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>
