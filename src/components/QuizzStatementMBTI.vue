<template>
  <div>
    <h4 class="text-white mb-4">{{ text }}</h4>
    <b-row>
      <b-col cols="10" class="d-flex m-auto">
        <h5 class="m-0 m-auto" style="color: #07e679">D'accord</h5>

        <quizz-button class="choice" @click.native="checked = 1" :size="10" color="#07e679" :checked="checked === 1"></quizz-button>
        <quizz-button class="choice" @click.native="checked = 2" :size="8" color="#07e679" :checked="checked === 2"></quizz-button>
        <quizz-button class="choice" @click.native="checked = 3" :size="6" color="#07e679" :checked="checked === 3"></quizz-button>
        <quizz-button class="choice" @click.native="checked = 4" :size="4" color="#ffff" :checked="checked === 4"></quizz-button>
        <quizz-button class="choice" @click.native="checked = 5" :size="6" color="#e47777" :checked="checked === 5"></quizz-button>
        <quizz-button class="choice" @click.native="checked = 6" :size="8" color="#e47777" :checked="checked === 6"></quizz-button>
        <quizz-button class="choice" @click.native="checked = 7" :size="10" color="#e47777" :checked="checked === 7"></quizz-button>

        <h5 class="text-left m-0 m-auto" style="color: #e47777">Pas d'accord</h5>
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
  .choice {
    display: inline-block;
    margin: auto;
  }
</style>
