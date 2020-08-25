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
    // こっちだとデータが送信されていなくて、emailとpasswordが入らない
    login() {
      const sendData = {
        email: this.email,
        password: this.password,
      }
      try {
        this.$auth.login('local', { data: sendData })
      } catch (error) {
        console.log(error)
      }
    },

    // こっちなら行けるけど、authモジュールがloginを認識されてくれない
    // async login() {
    //   const data = {
    //     email: this.email,
    //     password: this.password,
    //   }
    //   await this.$axios
    //     .$post('company/login/', data, {
    //       headers: {
    //         'Content-Type': 'application/json',
    //       },
    //     })
    //     .then((response) => {
    //       this.$auth.setToken('local', response.token)
    //       this.$router.push('/company/')
    //     })
    //     .catch((error) => {
    //       console.log(error)
    //     })
    // },
  },
}
</script>
