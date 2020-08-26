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
  components: {
    VideoCard,
  },
  data: () => ({
    videos: [
      { id: 1, title: 'sample', description: 'hogehoge' },
      { id: 2, title: 'sample', description: 'hogehoge' },
      { id: 3, title: 'sample', description: 'hogehoge' },
    ],
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
