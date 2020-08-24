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
            :items="categories"
            :v-model="selectedCategory"
            label="動画カテゴリ"
            outlined
          ></v-select>
        </v-col>

        <!-- TODO: 本当はここは入力フォームを複数個作成するべきたけど、めんどくさくてできていない -->
        <v-col cols="12">
          <v-text-field
            :v-model="keywords"
            label="キーワード(半角コンマ,区切りで複数入力できます)"
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
    uploadFile: {},
  }),
  methods: {
    changeFile(e) {
      const files = e.target.files || e.dataTransfer.files
      // ファイルが選択されたら変数に入れる
      this.uploadFile = files[0]
    },
    async submit() {
      const res = await this.$axios.$post('company/video/')
      console.log(res)
    },
  },
}
</script>
