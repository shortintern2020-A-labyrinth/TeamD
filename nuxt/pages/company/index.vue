<template>
  <v-container>
    <div class="text-h4">投稿動画一覧</div>
    <v-row>
      <v-col v-for="video in videos" :key="video.id" cols="4">
        <VideoCard :video="video"></VideoCard>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import VideoCard from '../../components/videoCard'

export default {
  middleware: 'user_auth',
  created() {
    this.$axios
      .$get('company/video/')
      .then((response) => {
        this.videos = response.videos
      })
      .catch(() => {
        this.$toast.error('データ取得時にエラーが発生しました')
      })
  },
  components: {
    VideoCard,
  },
  data: () => ({
    videos: [],
  }),
  // created() {
  //   this.$axios
  //     .$get('company/login/', {
  //       headers: {
  //         'Content-Type': 'application/json',
  //       },
  //     })
  //     .then((response) => {
  //       this.videos = response.videos
  //     })
  //     .catch(() => {
  //       this.$toast.error('データ取得時にエラーが発生しました')
  //     })
  // },
}
</script>
