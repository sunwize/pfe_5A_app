<template>
  <div class="background">
    <b-container class="header" fluid>
      <b-container>
        <h2 class="m-auto py-3 text-left">Analyse textuelle</h2>
        <h3 class="text-left">Décrivez-vous en quelques lignes en ANGLAIS :</h3>
        <b-form-textarea
          id="textarea"
          v-model="text"
          placeholder="..."
          rows="3"
          max-rows="6"
        ></b-form-textarea>
        <div class="text-right pb-3">
          <form @submit.prevent="sendText">
            <b-button type="submit" variant="outline-light" class="mt-2">Analyser</b-button>
          </form>
        </div>
        <div v-if="result" class="text-left pb-2">
          <p>Your personality: {{ result.PERSONNALITE }} </p>
          <p>INTROVERSION: {{ result.INTROVERTED }}</p>
          <p>INTUITION: {{ result.INTUTIVE }}</p>
          <p>JUDGEMENT: {{ result.JUDGEMENTAL }}</p>
          <p>REFLEXION: {{ result.THINKING }}</p>
        </div>
        </b-container>
    </b-container>
    <b-container class="pt-3">
      <h3 class="text-left mb-3">Les traits de personnalités Big Five</h3>
      <b-row>
        <b-col cols="12" lg="6">
          <b-card title="Ouverture" class="trait">
            <span>Appréciation de l'art, de l'émotion, de l'aventure, des idées peu communes ou des idées nouvelles, curiosité et imagination</span>
          </b-card>
        </b-col>
        <b-col cols="12" lg="6">
          <b-card title="Conscienciosité" class="trait">
            <span>Autodiscipline, respect des obligations, organisation plutôt que spontanéité ; orienté vers des buts</span>
          </b-card>
        </b-col>
        <b-col cols="12" lg="6">
          <b-card title="Extraversion" class="trait">
            <span>Energie, émotions positives, tendance à chercher la stimulation et la compagnie des autres</span>
          </b-card>
        </b-col>
        <b-col cols="12" lg="6">
          <b-card title="Agréabilité" class="trait">
            <span>Une tendance à être compatissant et coopératif plutôt que soupçonneux et antagonique envers les autres</span>
          </b-card>
        </b-col>
        <b-col cols="12" lg="6">
          <b-card title="Névrosisme" class="trait">
            <span>Contraire de stabilité émotionnelle : tendance à éprouver facilement des émotions désagréables comme la colère, l'inquiétude ou la dépression, vulnérabilité</span>
          </b-card>
        </b-col>
      </b-row>
      <h3 class="text-left mb-3">Types de personnalitées selon MBTI</h3>
      <b-row>
        <b-col cols="6" md="3" v-for="personality in personalities" :key="personality.title">
          <personality @click.native="openModal(personality)" :personality="personality" class="personality"></personality>
        </b-col>
      </b-row>
    </b-container>

    <b-modal id="personality-modal" size="xl" :title="selectedPersonality.title" hide-footer>
      <div class="p-3">
        <b-row class="pb-4">
          {{selectedPersonality.sigle}} {{selectedPersonality.desc}}
        </b-row>
        <b-row>
          <b-col cols="8" class="mx-auto">
            <h3 class="text-center">Les mots récurrents</h3>
            <b-img class="img-thumbnail" :src="require('../assets/img/cloudwords/' + selectedPersonality.sigle.toLowerCase() + '.png')"></b-img>
          </b-col>
        </b-row>
      </div>
    </b-modal>
  </div>
</template>

<script>
import * as axios from 'axios'

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
      personalities: this.$store.getters.getPersonalities,
      modalPersonality: null,
      text: '',
      result: null
    }
  },
  methods: {
    openModal(personality) {
      this.modalPersonality = personality;
      this.$bvModal.show('personality-modal');
    },
    sendText () {
      axios.post(process.env.VUE_APP_API_URL + '/textPrediction?text=' + this.text).then(res => {
        console.log(res)
        this.result = res.data
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .background {
    margin: 0;
    color: #fff;
    background: rgb(86, 112, 152);
  }

  .personality {
    transition: transform .1s ease-out;
  }

  .personality:hover {
    transform: translate(0, -10px);
    cursor: pointer;
  }

  .header {
    padding-top: 0.5em;
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

  .footer {
    background: rgba(46, 68, 91, 0.73);
  }

  .trait {
    color: white;
    background-color: rgba(0, 0, 0, 0.25);
    text-align: left;
    border: none;
    margin-bottom: 1em;
  }
</style>
