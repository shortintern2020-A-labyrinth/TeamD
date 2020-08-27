export let axios

export default ({ store, $axios }) => {
  // TODO: ここは環境変数使って
  $axios.defaults.baseURL = 'https://a4shittyo-app-dlukj7emra-an.a.run.app/api/'

  $axios.onRequest((config) => {
    // ここでaxiosのリクエストにtokenをいれる
    config.headers.common.Authorization = store.$auth.getToken('local')
    config.headers.common.Accept = 'application/json'
  })

  $axios.onResponse((response) => {
    return Promise.resolve(response)
  })

  $axios.onError((error) => {
    return Promise.reject(error.response)
  })

  axios = $axios
}
