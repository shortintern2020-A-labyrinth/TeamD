<template>
  <div>
    <v-app-bar :clipped-left="clipped" fixed app>
      <nuxt-link to="/company">
        <v-toolbar-title>{{ title }}</v-toolbar-title>
      </nuxt-link>
      <v-spacer />
      <v-btn v-if="!$auth.state.loggedIn" to="/login" color="primary">ログイン</v-btn>
      <div v-if="$auth.state.loggedIn">
        <v-btn to="/company/postVideo" color="primary">動画投稿</v-btn>
        <v-btn to="/company/edit" color="info">企業概要編集</v-btn>
        <v-btn to="/logout" color="info" @click="logout">ログアウト</v-btn>
      </div>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$auth.logout()
    },
  },
  data() {
    return {
      clipped: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/',
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: '/inspire',
        },
      ],
      miniVariant: false,
      title: 'RakutenPV',
    }
  },
}
</script>
