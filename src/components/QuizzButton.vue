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
            return 'width: ' + 10 * this.size + 'px;'
            + 'height: ' + 10 * this.size + 'px;'
            + 'border: 3px solid ' + this.color + ';'
            + this.plain;
          },
          plain() {
              return this.checked === true ? 'background-color: ' + this.color + ';' : '';
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
