<template>
  <v-card class="mx-auto" max-width="500">
    <v-card-title>サインアップ</v-card-title>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-text-field v-model="companyName" label="企業名※" required></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-text-field v-model="email" :rules="emailRules" label="メールアドレス※" required></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-text-field
              v-model="password"
              :counter="10"
              label="パスワード※"
              append-icon="mdi-eye-off"
              type="password"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-textarea v-model="companyDesc" label="企業概要説明" />
          </v-col>
          <v-col cols="12">
            <v-row>
              <v-col cols="12">URL</v-col>

              <v-col cols="12">
                <v-text-field v-model="companyURL" label="企業サイトURL"></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="ecURL" label="商品販売サイトURL"></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="googleFormURL" label="GoogleFormURL"></v-text-field>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <v-card-actions>
          <v-btn text small to="login">ログイン</v-btn>

          <v-spacer></v-spacer>

          <v-btn color="secondary" bold @click="signup">Submit</v-btn>
        </v-card-actions>
      </v-container>
    </v-form>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    valid: false,
    password: '',
    email: '',
    companyName: '',
    companyDesc: '',
    companyURL: '',
    ecURL: '',
    googleFormURL: '',
    selectedComapnyPatten: '',
    emailRules: [(v) => !!v || 'E-mail is required'],
  }),
  methods: {
    async signup() {
      const data = {
        email: this.email,
        password: this.password,
        name: this.companyName,
        description: this.companyDesc,
        urls: [
          { type: 1, value: this.companyURL },
          { type: 2, value: this.ecURL },
          { type: 3, value: this.googleFormURL },
        ],
      }
      await this.$axios
        .$post('company/register/', data, {
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.$toast.success(
            '企業側にメールを送りました！承認されるのをお待ちください'
          )
        })
        .catch((error) => {
          console.log(error)
          this.$toast.error(
            '申請中にエラーが発生しました。再度送信してください'
          )
        })
    },
  },
}
</script>
