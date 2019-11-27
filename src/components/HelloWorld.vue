<template>
  <div class="background">
    <h1 class="title">MBTI personnality study</h1>
    <b-container>
      <b-row>
        <b-col cols="6" md="3" v-for="personality in personalities" :key="personality.title">
          <b-card :title="personality.title">
            <b-img class="icon m-auto" :src="require(`../assets/img/${personality.img}.svg`)"></b-img>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
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
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .background {
    margin: 0;
    font-family: "Exo", sans-serif;
    color: #fff;
    background: linear-gradient(-15deg, rgba(232, 131, 212, 0.53), rgba(82, 238, 0, 0.53), rgba(37, 185, 231, 0.53), rgba(247, 194, 19, 0.55));
    background-size: 400% 400%;
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

  .title {
    padding-top: 0.8em;
    padding-bottom: 0.8em;
    margin-bottom: 0.5em;
    font-size: 4em;
    background: rgba(0, 0, 0, 0.29);

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
    background-color: rgba(36, 30, 3, 0.10);
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
      font-size: 1.4em;
    }
  }

  .card-body {
    @media (max-width: 1024px) {
      padding: 0.4em;
    }
  }
</style>
