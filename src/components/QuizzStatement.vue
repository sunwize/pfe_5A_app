<template>
  <div>
    <h4 class="mb-5 text">{{ text }}</h4>
    <b-row>
      <b-col cols="3" class="text-right m-auto">
        <h5 class="m-0 indicator" style="color: #07e679">D'accord</h5>
      </b-col>
      <b-col cols="6">
        <quizz-buttons v-model="checked"></quizz-buttons>
      </b-col>
      <b-col cols="3" class="m-auto">
        <h5 class="text-left m-0 indicator" style="color: #e47777">Pas d'accord</h5>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'QuizzStatement',
  props: {
    text: {
      type: String,
      required: true
    },
    value: Number
  },
  data () {
    return {
      checked: this.value
    }
  },
  watch: {
    checked (val) {
      this.$emit('input', val)
    }
  }
}
</script>

<style lang="scss" scoped>
  .text {
    color: rgba(255, 255, 255, 0.8);
  }

  .indicator {
    letter-spacing: 1px;
    font-weight: bold;
  }
</style>
