<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
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
