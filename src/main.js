import Vue from 'vue'
import App from './App.vue'
import router from './router'
import '../public/scss/global.scss'

import BootstrapVue from 'bootstrap-vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import QuizzStatementMBTI from './components/QuizzStatementMBTI'
import QuizzButton from "./components/QuizzButton"
import QuizzStatementBigF from "./components/QuizzStatementBigF"

Vue.config.productionTip = false

library.add(fas)

Vue.use(BootstrapVue)

Vue.component('statement-mbti', QuizzStatementMBTI)
Vue.component('icon', FontAwesomeIcon)
Vue.component('quizz-button', QuizzButton)
Vue.component('statement-bf', QuizzStatementBigF)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
