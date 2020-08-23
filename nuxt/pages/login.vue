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

          <v-btn color="secondary" bold>Submit</v-btn>
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
    emailRules: [(v) => !!v || 'E-mail is required'],
  }),
}
</script>
