<template>
  <v-card class="mx-auto" max-width="500">
    <v-card-title>企業概要編集</v-card-title>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-text-field v-model="companyName" label="企業名" required></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-textarea v-model="companyDesc" label="企業概要説明" />
          </v-col>

          <v-col cols="12">URL</v-col>

          <v-col cols="12">
            <v-text-field v-model="companyURL" label="企業サイトURL"></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field v-model="goodURL" label="商品販売サイトURL"></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field v-model="googleFormURL" label="GoogleFormURL"></v-text-field>
          </v-col>
        </v-row>
        <v-card-actions>
          <div></div>
          <v-spacer></v-spacer>
          <v-btn color="secondary" bold @click="edit">更新</v-btn>
        </v-card-actions>
      </v-container>
    </v-form>
  </v-card>
</template>

<script>
export default {
  middleware: 'user_auth',
  data: () => ({
    valid: false,
    companyName: '',
    companyDesc: '',
    companyPattern: ['企業サイト', '商品販売サイト', 'googleForm'],
  }),
  methods: {
    async edit() {
      // TODO: とりあえずこれだけ
      const data = {
        name: this.companyName,
        description: this.companyDesc,
      }
      await this.$axios
        .$post('company/register/', data, {
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.$toast.success('修正完了しました!')
        })
        .catch(() => {
          this.$toast.error(
            '申請中にエラーが発生しました。再度送信してください'
          )
        })
    },
  },
}
</script>
