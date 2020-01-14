import Vue from 'vue'
import App from './App.vue'
import router from './router'
import '../public/scss/global.scss'

import BootstrapVue from 'bootstrap-vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import QuizzStatement from './components/QuizzStatement'
import QuizzRadioButtons from './components/QuizzRadioButtons'
import Menu from './components/Menu'

Vue.config.productionTip = false

library.add(fas)

Vue.use(BootstrapVue)

Vue.component('statement', QuizzStatement)
Vue.component('quizz-buttons', QuizzRadioButtons)
Vue.component('icon', FontAwesomeIcon)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
