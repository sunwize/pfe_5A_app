import Vue from 'vue'
import VueRouter from 'vue-router'

import home from './views/Home'
import QuizzMBTI from './views/QuizzMBTI'
import QuizzBIG5 from "./views/QuizzBIG5"

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
      path: `/quizz-mbti`,
      name: `quizz-mbti`,
      component: QuizzMBTI
    },
    {
      path: `/quizz-big5`,
      name: `quizz-big5`,
      component: QuizzBIG5
    }
  ]
})
