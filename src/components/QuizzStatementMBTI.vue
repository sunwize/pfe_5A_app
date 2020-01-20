<template>
  <div>
    <h4 class="text-white mb-4">{{ text }}</h4>
    <b-row>
      <b-col cols="12" lg="10" class="d-flex m-auto">
        <h5 v-if="!isMobileDevice()" class="m-0 m-auto" style="color: #07e679">D'accord</h5>

        <quizz-button class="choice" @click.native="check(1)" :size="10" color="#07e679" :checked="value === 1"></quizz-button>
        <quizz-button class="choice" @click.native="check(2)" :size="8" color="#07e679" :checked="value === 2"></quizz-button>
        <quizz-button class="choice" @click.native="check(3)" :size="6" color="#07e679" :checked="value === 3"></quizz-button>
        <quizz-button class="choice" @click.native="check(4)" :size="4" color="#ffff" :checked="value === 4"></quizz-button>
        <quizz-button class="choice" @click.native="check(5)" :size="6" color="#e47777" :checked="value === 5"></quizz-button>
        <quizz-button class="choice" @click.native="check(6)" :size="8" color="#e47777" :checked="value === 6"></quizz-button>
        <quizz-button class="choice" @click.native="check(7)" :size="10" color="#e47777" :checked="value === 7"></quizz-button>

        <h5 v-if="!isMobileDevice()" class="text-left m-0 m-auto" style="color: #e47777">Pas d'accord</h5>
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
    onAnswer: {
      type: Function,
      default: () => {}
    },
    value: Number
  },
  methods: {
    check (index) {
      this.$emit('input', index);
      this.onAnswer();
    },
    isMobileDevice() {
      return this.$store.getters.isMobileDevice;
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
