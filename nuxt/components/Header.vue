<template>
  <div>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon
        v-if="$auth.state.loggedIn"
        @click.stop="drawer = !drawer"
      />
      <nuxt-link to="/">
        <v-toolbar-title>
          {{ title }}
        </v-toolbar-title>
      </nuxt-link>
      <v-spacer />
      <v-btn v-if="!$auth.state.loggedIn" to="login" color="primary">
        ログイン
      </v-btn>
      <div v-if="$auth.state.loggedIn">
        <v-btn to="company/postVideo" color="primary">
          動画投稿
        </v-btn>
        <v-btn to="login" color="info" @click="logout">
          ログアウト
        </v-btn>
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
      drawer: false,
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
