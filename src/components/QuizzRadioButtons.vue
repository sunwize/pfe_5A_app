<template>
    <div class="d-flex m-auto">
      <div @click="check(1)" class="box box1" :style="plain(1)"></div>
      <div @click="check(2)" class="box box2" :style="plain(2)"></div>
      <div @click="check(3)" class="box box3" :style="plain(3)"></div>
      <div @click="check(4)" class="box box4" :style="plain(4)"></div>
      <div @click="check(5)" class="box box5" :style="plain(5)"></div>
      <div @click="check(6)" class="box box6" :style="plain(6)"></div>
      <div @click="check(7)" class="box box7" :style="plain(7)"></div>
    </div>
</template>

<script>
export default {
  name: 'QuizzRadioButtons',
  props: {
    value: Number
  },
  data () {
    return {
      checked: this.value,
      colors: ['#07e679', '#07e679', '#07e679', '#ffff', '#e47777', '#e47777', '#e47777']
    }
  },
  methods: {
    plain (index) {
      if (index === this.value) {
        return 'background-color: ' + this.colors[index - 1]
      } else {
        return ''
      }
    },
    check (index) {
      this.checked = index
      this.$emit('input', index)
    }
  }
}
</script>

<style lang="scss" scoped>
  .box {
    border-radius: 50%;
    border: 3px solid #ffff;
    display: inline-block;
    margin: auto;
    cursor: pointer;
  }

  .box1, .box2, .box3 {
    border: 3px solid #07e679;
  }

  .box5, .box6, .box7 {
    border: 3px solid #e47777;
  }

  .box1, .box7 {
    width: 60px;
    height: 60px;
  }

  .box2, .box6 {
    width: 50px;
    height: 50px;
  }

  .box3, .box5 {
    width: 40px;
    height: 40px;
  }

  .box4 {
    width: 30px;
    height: 30px;
  }
</style>
