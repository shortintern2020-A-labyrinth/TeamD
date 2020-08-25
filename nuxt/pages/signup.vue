<template>
  <v-card class="mx-auto" max-width="500">
    <v-card-title>
      サインアップ
    </v-card-title>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-text-field
              v-model="companyName"
              label="企業名※"
              required
            ></v-text-field>
          </v-col>

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
              append-icon="mdi-eye-off"
              type="password"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-textarea v-model="companyDesc" label="企業概要説明" />
          </v-col>

          <v-col cols="12">
            URL
          </v-col>

          <v-col cols="4">
            <v-select
              :items="companyPattern"
              :v-model="selectedComapnyPatten"
              label="URLの種類"
              outlined
            ></v-select>
          </v-col>
          <v-col cols="8">
            <v-text-field
              v-model="password"
              :counter="10"
              label="URL"
              required
            ></v-text-field>
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
    selectedComapnyPatten: '',
    emailRules: [(v) => !!v || 'E-mail is required'],
    companyPattern: ['企業サイト', '商品販売サイト'],
  }),
  methods: {
    async signup() {
      // TODO: とりあえずこれだけ
      const data = {
        email: this.email,
        password: this.password,
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
          this.$toast.success('登録メールを送りました！承認してください')
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
