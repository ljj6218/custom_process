import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import './plugins/clipboard.js'
import './plugins/axios.js'

import './style/index.css'

import router from './router'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
