<template>
  <b-navbar sticky toggleable="lg" type="dark" style="background-color: #273a4e">
    <b-navbar-brand to="/">MBTI personnality study</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/quizz-mbti" :active="$route.path === '/quizz-mbti'">Quizz MBTI <b-badge v-if="$store.getters.getMbtiResult === null" variant="warning">New</b-badge></b-nav-item>
        <b-nav-item to="/quizz-big5" :active="$route.path === '/quizz-big5'">Quizz Big Five <b-badge v-if="$store.getters.getBfResult === null" variant="warning">New</b-badge></b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-item to="/sources" :active="$route.path === '/sources'">Sources <icon icon="info-circle"></icon></b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
  export default {
    name: 'Menu'
  }
</script>

<style scoped>

</style>
