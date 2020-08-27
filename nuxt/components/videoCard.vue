<template>
  <v-card class="mx-auto" max-width="400">
    <v-layout justify-center>
      <a @click="push">
        <v-img max-width="200px" :src="image_src"></v-img>
      </a>
      <!-- 一応youtubeの埋め込み作成 -->
      <!-- <youtube player-width="400" player-height="400" video-id="lG0Ys-2d4MA" /> -->
    </v-layout>
    <v-card-subtitle class="pb-0">{{ video.name }}</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>{{ video.description }}</div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: ['video'],
  data() {
    return {
      image_src: require('@/assets/movie.png'),
    }
  },
  methods: {},
}
</script>
