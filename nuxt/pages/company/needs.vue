<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card class="mx-auto" tile>
          <v-card-title>若者向けのタイトル例</v-card-title>
          <v-row>
            <v-col cols="6">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>商品紹介</v-list-item-title>
                  <v-list-item-subtitle>〇〇のここがすごい</v-list-item-subtitle>
                  <v-list-item-subtitle>〇〇の作り方</v-list-item-subtitle>
                  <v-list-item-subtitle>木でパズルを作成する伝統工芸品：〇〇の紹介</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-col>
            <v-col cols="6">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>製作工程</v-list-item-title>
                  <v-list-item-subtitle>〇〇の製作の裏側、裏側に迫る</v-list-item-subtitle>
                  <v-list-item-subtitle>日本伝統工芸の作り方〜〇〇〜</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-col>
            <v-col cols="6">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>働き方</v-list-item-title>
                  <v-list-item-subtitle>伝統工芸職人は忙しい？ 〇〇の製作者の1日</v-list-item-subtitle>
                  <v-list-item-subtitle>〇〇の製作者の年収は？</v-list-item-subtitle>
                  <v-list-item-subtitle>職業紹介 〜日本伝統工芸 〇〇〜</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col cols="12">
        <v-card class="mx-auto" tile>
          <v-card-title>外国人向けのタイトル例</v-card-title>
          <v-row>
            <v-col cols="4">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Single-line item</v-list-item-title>
                  <v-list-item-subtitle>consectetur adipiscing elit.</v-list-item-subtitle>
                  <v-list-item-subtitle>consectetur adipiscing elit.</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-col>
            <v-col cols="4">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Single-line item</v-list-item-title>
                  <v-list-item-subtitle>consectetur adipiscing elit.</v-list-item-subtitle>
                  <v-list-item-subtitle>consectetur adipiscing elit.</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-col>
            <v-col cols="4">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Single-line item</v-list-item-title>
                  <v-list-item-subtitle>consectetur adipiscing elit.</v-list-item-subtitle>
                  <v-list-item-subtitle>consectetur adipiscing elit.</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  middleware: 'user_auth',
  data: () => ({
    videos: [],
  }),
}
</script>
