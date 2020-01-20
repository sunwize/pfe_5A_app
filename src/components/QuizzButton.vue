<template>
    <div class="circle" :style="style"></div>
</template>

<script>
    export default {
        name: "QuizzButton",
        props: {
          size: {
            type: Number,
            default: 1
          },
          color: {
            type: String,
            default: '#ffff'
          },
          checked: {
            type: Boolean,
            required: true
          }
      },
      computed: {
          style() {
            return 'width: ' + this.width() * this.size + 'px;'
            + 'height: ' + this.width() * this.size + 'px;'
            + 'border: 3px solid ' + this.color + ';'
            + this.plain;
          },
          plain() {
              return this.checked === true ? 'background-color: ' + this.color + ';' : '';
          }
      },
      methods: {
          width() {
            return this.$store.getters.isMobileDevice ? 6 : 10;
          }
      }
    }
</script>

<style lang="scss" scoped>
  .circle {
    border-radius: 50%;
    cursor: pointer;
  }
</style>
