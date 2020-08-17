<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <div class="text-center">
        <logo />
        <vuetify-logo />
      </div>
      <v-card>
        <v-card-title class="headline">
          {{ value }}
        </v-card-title>
        <v-btn large @click="sendRequest">send request</v-btn>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import Logo from '~/components/Logo.vue'
import VuetifyLogo from '~/components/VuetifyLogo.vue'

export default {
  components: {
    Logo,
    VuetifyLogo,
  },
  methods: {
    async sendRequest() {
      const response = await this.$axios.$get('http://django:8000/hello')
      this.value = response.message
    },
  },
  async asyncData({ $axios }) {
    // eslint-disable-next-line no-undef
    const response = await $axios.$get('http://django:8000/hello')
    return { value: response.message }
  },
}
</script>
