<template>
  <div id="app">
    <Menu></Menu>
    <router-view></router-view>
  </div>
</template>

<script>
  import Menu from './components/Menu'

  export default {
    name: 'app',
    components: {
      Menu
    }
  }
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Muli&display=swap');

#app {
  font-family: 'Muli', sans-serif;
  text-align: center;
  color: #2c3e50;
}
</style>
