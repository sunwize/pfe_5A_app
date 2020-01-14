import Vue from 'vue'
import VueRouter from 'vue-router'

import home from './views/Home'
import QuizzMBTI from './views/QuizzMBTI'

Vue.use(VueRouter)

export default new VueRouter({
  mode: `history`,
  routes: [
    {
      path: `/`,
      name: `home`,
      component: home
    },
    {
      path: `/quizz`,
      name: `quizz`,
      component: QuizzMBTI
    }
  ]
})
