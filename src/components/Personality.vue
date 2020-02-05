<template>
  <b-card class="text-white">
    <h4 :style="'font-size: ' + (isMobileDevice() ? '1.2em' : '')">{{ personality.title }}</h4>
    <p>{{ personality.sigle }}</p>
    <b-img class="icon m-auto" :src="require(`../assets/img/logos/${personality.img}.svg`)"></b-img>
  </b-card>
</template>

<script>
  export default {
    name: 'Personality',
    props: {
      personality: {
        type: Object,
        required: true
      }
    },
    methods: {
      isMobileDevice() {
        return this.$store.getters.isMobileDevice;
      }
    }
  }
</script>

<style lang="scss" scoped>
  .icon {
    display: block;
    width: 100%;
  }

  .card {
    border-radius: 10px;
    background-color: rgba(50, 68, 93, 0.47);
    border-color: transparent;
    margin-bottom: 1em;
  }

  .card-title {
    font-size: 2em;

    @media (max-width: 1024px) {
      font-size: 1.3em;
    }
  }

  .card-body {
    @media (max-width: 1024px) {
      padding: 0.4em;
    }
  }
</style>
