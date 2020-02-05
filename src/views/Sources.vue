<template>
    <div class="background pb-3">
      <b-container class="pt-3">
        <h1 class="mb-3">Sources d'études</h1>
        <b-row>
          <b-col cols="12" lg="6">
            <b-card>
              <h4 class="text-dark mb-3">Les équivalences entre MBTI et Big Five</h4>
              <b-img class="image" :src="require('../assets/img/equivalences.png')" rounded></b-img>
            </b-card>
          </b-col>
          <b-col cols="12" lg="6" class="mt-3 mt-lg-0">
            <b-card>
              <h4 class="text-dark">Articles</h4>
              <b-list-group class="text-left">
                <b-list-group-item v-for="source in sources" :key="source.link" :href="source.link">
                  <icon style="width: 20px" class="mr-1" :icon="source.icon"></icon> {{ source.title }}
                </b-list-group-item>
              </b-list-group>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </div>
</template>

<script>
  export default {
    name: 'Sources',
    data() {
      return {
        sources: [
          { title: 'Le site des 16 personnalités', icon: 'globe-europe', link: 'https://www.16personalities.com/fr/types-de-personnalite' },
          { title: 'Similar minds', icon: 'globe-europe', link: 'http://similarminds.com/global5/g5-jung.html' },
          { title: 'Training AI to Predict MBTI From Texts', icon: 'globe-europe', link: 'https://medium.com/towards-artificial-intelligence/training-ai-to-predict-myers-briggs-personality-types-from-texts-d4e3d7baf17' },
          { title: 'XGBoost in Python', icon: 'globe-europe', link: 'https://machinelearningmastery.com/xgboost-python-mini-course/' },
          { title: 'Personality detection', icon: ['fab', 'github'], link: 'https://github.com/SenticNet/personality-detection' },
          { title: 'Scrappy with Selenium', icon: ['fab', 'github'], link: 'https://github.com/clemfromspace/scrapy-selenium' },
          { title: 'MBTI CNN based text classifier', icon: ['fab', 'github'], link: 'https://github.com/Neoanarika/MBTI?fbclid=IwAR1uXjPAhxXWrRX4_WxJigK3EGrY3URRhBr0-ocpzB4fgg9rSrGGZP0jQ54' },
          { title: 'Kaggle Dataset', icon: ['fab', 'kaggle'], link: 'https://www.kaggle.com/datasnaek/mbti-type' },
          { title: 'Kaggle : Predict your Myers-Briggs Personality', icon: ['fab', 'kaggle'], link: 'https://www.kaggle.com/stefanbergstein/byo-tweets-predict-your-myers-briggs-personality' },
        ]
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

  a {
    &:hover {
      text-decoration: underline;
      color: white;
      background: #007bff;
      border-color: #007bff;
    }
  }
</style>
