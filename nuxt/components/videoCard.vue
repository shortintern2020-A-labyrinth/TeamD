<template>
  <v-card class="mx-auto" max-width="400">
    <!-- TODO: 埋め込みでも作るか -->
    <v-layout justify-center>
      <v-img max-width="200px" src="img/movie.png"></v-img>
    </v-layout>
    <v-card-subtitle class="pb-0">{{ video.name }}</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>{{ video.description }}</div>
    </v-card-text>

    <v-card-actions>
      <div></div>
      <v-spacer></v-spacer>
      <v-btn color="info" text>編集 TODO: 消す？</v-btn>
      <v-btn color="error" text>削除 TODO: 消す？</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['video'],
}
</script>
