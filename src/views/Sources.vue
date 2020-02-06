<template>
    <div class="background pb-3">
      <b-container class="pt-3">
        <h1 class="mb-3">Études et résultats</h1>
        <b-row>
          <b-col cols="12" lg="6">
            <b-card>
              <h4 class="text-dark mb-3">Les équivalences entre MBTI et Big Five</h4>
              <b-img class="image" :src="require('../assets/img/equivalences.png')" rounded></b-img>
            </b-card>
          </b-col>

          <b-col cols="12" lg="6" class="mt-3 mt-lg-0">
            <b-card class="mb-3">
              <h4 class="text-dark mb-3">Résultats</h4>
              <b-list-group class="text-left">
                <div v-for="(value, name, index) in study" :key="name">
                  <b-list-group-item @click="collapse(index)" :class="toggle[index] ? 'text-white' : 'text-dark'" style="cursor: pointer" :active="toggle[index]">
                    <span>{{ name }}</span>
                  </b-list-group-item>
                  <b-collapse :id="'collapse' + index" v-model="toggle[index]">
                    <b-card style="background-color: #273a4e" class="rounded-0">
                      <h5 class="text-center">Moyennes</h5>
                      <horizontal-bars :chartdata="chartdata(value.avg)" :options="options"/>
                      <b-badge class="mx-1" v-for="(sigle, index) in value.sigles" :key="index">{{ sigle }}</b-badge>
                    </b-card>
                  </b-collapse>
                </div>
              </b-list-group>
            </b-card>

            <b-card>
              <h4 class="text-dark mb-3">Sources</h4>
              <b-list-group class="text-left">
                <b-list-group-item v-for="source in sources" :key="source.link" :href="source.link">
                  <icon style="width: 20px" class="mr-1" :icon="source.icon"></icon> <span>{{ source.title }}</span>
                </b-list-group-item>
              </b-list-group>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </div>
</template>

<script>
  import * as axios from 'axios'

  export default {
    name: 'Sources',
    data() {
      return {
        study: null,
        sources: [
          { title: 'Le site des 16 personnalités', icon: 'globe-europe', link: 'https://www.16personalities.com/fr/types-de-personnalite' },
          { title: 'Similar minds', icon: 'globe-europe', link: 'http://similarminds.com/global5/g5-jung.html' },
          { title: 'Training AI to Predict MBTI From Texts', icon: 'globe-europe', link: 'https://medium.com/towards-artificial-intelligence/training-ai-to-predict-myers-briggs-personality-types-from-texts-d4e3d7baf17' },
          { title: 'XGBoost in Python', icon: 'globe-europe', link: 'https://machinelearningmastery.com/xgboost-python-mini-course/' },
          { title: 'Personality detection', icon: ['fab', 'github'], link: 'https://github.com/SenticNet/personality-detection' },
          { title: 'Scrappy with Selenium', icon: ['fab', 'github'], link: 'https://github.com/clemfromspace/scrapy-selenium' },
          { title: 'MBTI CNN based text classifier', icon: ['fab', 'github'], link: 'https://github.com/Neoanarika/MBTI?fbclid=IwAR1uXjPAhxXWrRX4_WxJigK3EGrY3URRhBr0-ocpzB4fgg9rSrGGZP0jQ54' },
          { title: 'Dataset', icon: ['fab', 'kaggle'], link: 'https://www.kaggle.com/datasnaek/mbti-type' },
          { title: 'Predict your Myers-Briggs Personality', icon: ['fab', 'kaggle'], link: 'https://www.kaggle.com/stefanbergstein/byo-tweets-predict-your-myers-briggs-personality' },
        ],
        toggle: [],
        options: {
          legend: {
            display: false
          }
        }
      }
    },
    activated() {
      this.loadDB();
    },
    mounted() {
      this.loadDB();
    },
    methods: {
      loadDB() {
        axios.get(process.env.VUE_APP_API_URL + '/get').then(res => {
          let data = res.data.data;
          this.study = {};
          let obj = {};
          for (let d of data) {
            if (!obj[d.mbti])
              obj[d.mbti] = [];
            obj[d.mbti].push(d.big5);
          }
          for (let key in obj) {
            let A = obj[key].map(e => e.score.A).reduce((a, b) => a+b) / obj[key].length;
            let C = obj[key].map(e => e.score.C).reduce((a, b) => a+b) / obj[key].length;
            let E = obj[key].map(e => e.score.E).reduce((a, b) => a+b) / obj[key].length;
            let N = obj[key].map(e => e.score.N).reduce((a, b) => a+b) / obj[key].length;
            let O = obj[key].map(e => e.score.O).reduce((a, b) => a+b) / obj[key].length;
            let sigles = obj[key].map(e => e.sigle);
            obj[key] = {
              A: A,
              C: C,
              E: E,
              N: N,
              O: O
            };
            this.study[key] = {};
            this.study[key].avg = (obj[key]);
            this.study[key].sigles = sigles.filter((s, i) => sigles.indexOf(s) === i);
            this.toggle.push(false);
          }
          console.log(this.study);
        }).catch(err => {
          console.log(err);
        });
      },
      collapse(index) {
        console.log(index);
        this.toggle[index] = !this.toggle[index];
        this.$forceUpdate();
      },
      chartdata(data) {
        return {
          labels: ['Ouverture', 'Conscienciosité', 'Extraversion', 'Agréabilité', 'Névrosisme'],
          datasets: [
            {
              borderColor: 'red',
              label: 'Big Five',
              backgroundColor: [
                '#32f871',
                '#f87979',
                '#bc9bf8',
                '#7c92f8',
                '#f89946'
              ],
              data: [data.O * 100/40, data.C * 100/40, data.E * 100/40, data.A * 100/40, data.N * 100/40]
            }
          ]
        };
      }
    }
  }
</script>

<style lang="scss" scoped>
  .background {
    margin: 0;
    color: #fff;
    background: rgb(86, 112, 152);
  }

  .image {
    width: 100%;
  }

  a:hover {
    span {
      text-decoration: underline;
    }
    color: white;
    background: #007bff;
    border-color: #007bff;
  }
</style>
