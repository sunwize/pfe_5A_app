<template>
  <div class="background">
    <b-container class="header" fluid>
      <h1 class="title">MBTI personnality study</h1>
    </b-container>
    <b-container class="pt-3">
      <b-row>
        <b-col cols="6" md="3" v-for="personality in personalities" :key="personality.title">
          <b-card :title="personality.title" @click="openModal(personality)">
            <b-img class="icon m-auto" :src="require(`../assets/img/logos/${personality.img}.svg`)"></b-img>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <b-container class="footer" fluid>
      <h2 class="m-auto py-3">Footer</h2>
    </b-container>
    <b-modal id="personality-modal" size="xl" :title="selectedPersonality.title" hide-footer>
      <div class="p-3">
        <b-row class="pb-4">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </b-row>
        <b-row>
          <b-col cols="12" md="6" class="m-auto text-center">
            <h3>Words popularity</h3>
            <b-img class="img-thumbnail" :src="require('../assets/img/example_words.png')"></b-img>
          </b-col>
          <b-col cols="12" md="6" class="m-auto text-center">
            <h3>Words variance</h3>
            <b-img class="img-thumbnail" :src="require('../assets/img/example_graph.png')"></b-img>
          </b-col>
        </b-row>
      </div>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: 'Home',
  computed: {
    selectedPersonality: function () {
      if (this.modalPersonality === null) {
        return this.personalities[0]
      } else {
        return this.modalPersonality
      }
    }
  },
  data: function () {
    return {
      personalities: [
        { title: 'Architecte', desc: '', img: 'intj-architect' },
        { title: 'Logicien', desc: '', img: 'intp-logician' },
        { title: 'Commandant', desc: '', img: 'entj-commander' },
        { title: 'Innovateur', desc: '', img: 'entp-debater' },
        { title: 'Avocat', desc: '', img: 'infj-advocate' },
        { title: 'Médiateur', desc: '', img: 'infp-mediator' },
        { title: 'Protagoniste', desc: '', img: 'enfj-protagonist' },
        { title: 'Inspirateur', desc: '', img: 'enfp-campaigner' },
        { title: 'Logisticien', desc: '', img: 'intp-logician' },
        { title: 'Défenseur', desc: '', img: 'isfj-defender' },
        { title: 'Directeur', desc: '', img: 'estj-executive' },
        { title: 'Consul', desc: '', img: 'esfj-consul' },
        { title: 'Virtuose', desc: '', img: 'istp-virtuoso' },
        { title: 'Aventurier', desc: '', img: 'isfp-adventurer' },
        { title: 'Entrepreneur', desc: '', img: 'estp-entrepreneur' },
        { title: 'Amuseur', desc: '', img: 'esfp-entertainer' }
      ],
      modalPersonality: null
    }
  },
  methods: {
    openModal: function (personality) {
      this.modalPersonality = personality
      this.$bvModal.show('personality-modal')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .background {
    margin: 0;
    color: #fff;
    //background: linear-gradient(-15deg, rgba(232, 131, 212, 0.53), rgba(82, 238, 0, 0.53), rgba(37, 185, 231, 0.53), rgba(247, 194, 19, 0.55));
    //background-size: 400% 400%;
    background: rgb(86, 112, 152);
    animation: gradientBG 15s ease infinite;
  }

  @keyframes gradientBG {
    0% {
      background-position: 0% 25%;
    }
    20% {
      background-position: 0% 50%;
    }
    40% {
      background-position: 50% 50%;
    }
    60% {
      background-position: 100% 50%;
    }
    80% {
      background-position: 50% 50%;
    }
    100% {
      background-position: 0% 25%;
    }
  }

  .header {
    background: rgba(46, 68, 91, 0.73);
  }

  .title {
    padding-top: 0.5em;
    padding-bottom: 0.5em;
    font-size: 4em;

    @media (max-width: 1024px) {
      font-size: 2em;
    }
  }

  .icon {
    display: block;
    width: 100%;
    height: 100%;
  }

  .card {
    border-radius: 10px;
    background-color: rgba(50, 68, 93, 0.47);
    border-color: transparent;
    margin-bottom: 1em;
    transition: transform .1s ease-out;
  }

  .card:hover {
    transform: translate(0, -10px);
    cursor: pointer;
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

  .footer {
    background: rgba(46, 68, 91, 0.73);
  }
</style>
