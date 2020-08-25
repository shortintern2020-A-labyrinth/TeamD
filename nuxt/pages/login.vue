<template>
  <v-card class="mx-auto" max-width="500">
    <v-card-title>
      ログイン
    </v-card-title>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="メールアドレス※"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-text-field
              v-model="password"
              :counter="10"
              append-icon="mdi-eye-off"
              type="password"
              label="パスワード※"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-card-actions>
          <v-btn text small to="signup">サインアップ</v-btn>

          <v-spacer></v-spacer>

          <v-btn color="secondary" bold @click="login">Submit</v-btn>
        </v-card-actions>
      </v-container>
    </v-form>
  </v-card>
</template>

<script>
export default {
  // loginされたら、/companyにリダイレクトされる
  middleware({ store, redirect }) {
    if (store.$auth.loggedIn) {
      redirect('/company/')
    }
  },
  data: () => ({
    valid: false,
    password: '',
    email: '',
    emailRules: [(v) => !!v || 'E-mail is required'],
  }),
  methods: {
    async login() {
      const data = {
        email: this.email,
        password: this.password,
      }
      this.$toast.show('ログイン中...')
      await this.$axios
        .$post('company/login/', data, {
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          this.$toast.success('認証成功！！！')
          this.$auth.setToken('local', response.token)
          // TODO: これでユーザー登録しないとisLoggedINが認証されない
          this.$auth.setUser({ name: 'hogehoge' })
          this.$router.push('/company/')
        })
        .catch((error) => {
          console.log(error)
          this.$toast.error('認証エラーが発生しました')
        })
    },
  },
}
</script>
