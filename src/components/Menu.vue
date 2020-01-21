<template>
  <b-navbar sticky toggleable="lg" type="dark" style="background-color: #273a4e">
    <b-navbar-brand to="/">MBTI personnality study</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/quizz-mbti" :active="$route.path === '/quizz-mbti'">Quizz MBTI</b-nav-item>
        <b-nav-item to="/quizz-big5" :active="$route.path === '/quizz-big5'">Quizz Big Five</b-nav-item>
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
