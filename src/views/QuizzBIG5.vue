<template>
    <div style="background-color: #567098">
      <b-container class="pt-3 pb-5">
        <h2 class="text-white pt-0 pb-3 py-lg-4">Quizz Big Five</h2>

        <div v-if="quizzIndex < statements.length && !loading && !result">
          <h3 class="d-flex">
            <div class="w-50 text-left">
              <b-button @click="previousQuestion" variant="outline-dark" pill><icon icon="arrow-left"></icon></b-button>
            </div>
            <div class="w-50 text-right">{{ quizzIndex+1 }} / {{ statements.length }}</div>
          </h3>
          <hr>
          <statement-bf v-model="statements[quizzIndex].choice" :text="statements[quizzIndex].text" :on-answer="nextQuestion" class="py-5"></statement-bf>
          <hr>
        </div>

        <div v-else>
          <b-spinner v-if="loading" class="d-block m-auto" variant="light" label="Spinning"></b-spinner>

          <div v-if="!loading && result">
            <h3 class="text-white">{{ result.sigle }}</h3>
            <horizontal-bars :chartdata="chartdata" :options="options"/>
            <b-button @click="restart" class="mt-3" variant="outline-light"><icon icon="redo-alt"></icon> Recommencer</b-button>
          </div>
        </div>
      </b-container>
    </div>
</template>

<script>
import * as axios from 'axios'
export default {
  name: 'QuizzBIG5',
  data () {
    return {
      loading: false,
      result: null,
      quizzIndex: 0,
      statements: [ { text: 'Je suis un gros fêtard.\n', choice: 3 },
                    { text: 'Je me soucie peu des autres.\n', choice: 3 },
                    { text: 'Je suis toujours prêt.\n', choice: 3 },
                    { text: 'Je suis facilement paniqué.\n', choice: 3 },
                    { text: 'J\'utilise un vocabulaire élaboré.\n', choice: 3 },
                    { text: 'Je ne parle pas beaucoup\n', choice: 3 },
                    { text: 'Je m\'intéresse aux autres.\n', choice: 3 },
                    { text: 'Je laisse traîner mes affaires.\n', choice: 3 },
                    { text: 'Je suis calme la plupart du temps\n', choice: 3 },
                    { text: 'J\'ai du mal à comprendre les concepts abstraits.\n', choice: 3 },
                    { text: 'Je me sens bien quand je suis en groupe.\n', choice: 3 },
                    { text: 'J\'insulte les autres\n', choice: 3 },
                    { text: 'Je fais attention aux détails.\n', choice: 3 },
                    { text: 'Je suis de nature inquiète\n', choice: 3 },
                    { text: 'J\'ai une imagination débordante.\n', choice: 3 },
                    { text: 'J\'aime bien resté à l\'écart.\n', choice: 3 },
                    { text: 'Je suis plein d\'empathie\n', choice: 3 },
                    { text: 'Je ruine les choses.\n', choice: 3 },
                    { text: 'Je me sens rarement triste.\n', choice: 3 },
                    { text: 'Je ne suis pas intéressé par les choses abstraites\n', choice: 3 },
                    { text: 'J\'engage la conversation.\n', choice: 3 },
                    { text: 'Chacun ses problèmes.\n', choice: 3 },
                    { text: 'Je fais les corvées en premier.\n', choice: 3 },
                    { text: 'Je suis facilement perturbé.\n', choice: 3 },
                    { text: 'J\'ai des idées excellentes.\n', choice: 3 },
                    { text: 'Je n\'ai pas grand chose à dire.\n', choice: 3 },
                    { text: 'J\'ai un coeur tendre.\n', choice: 3 },
                    { text: 'J\'oublie souvent de remettre les choses à leur place.\n', choice: 3 },
                    { text: 'Je me fâche facilement.\n', choice: 3 },
                    { text: 'Je n\'ai pas d\'imagination\n', choice: 3 },
                    { text: 'Je parle à tout le monde en soirée.\n', choice: 3 },
                    { text: 'Je ne m\'intéresse pas aux autres\n', choice: 3 },
                    { text: 'J\'aime que les choses soient ordonnées.\n', choice: 3 },
                    { text: 'Je change beaucoup d\'humeur.\n', choice: 3 },
                    { text: 'J\'apprends rapidement.\n', choice: 3 },
                    { text: 'Je n\'aime pas attirer l\'attention sur moi.\n', choice: 3 },
                    { text: 'Je prends du temps pour les autres.\n', choice: 3 },
                    { text: 'J\'évite les responsabilités.\n', choice: 3 },
                    { text: 'J\'ai des sauts d\'humeur.\n', choice: 3 },
                    { text: 'J\'utilise des mots élaborés.\n', choice: 3 },
                    { text: 'Je me fiche d\'être le centre d\'intérêt.\n', choice: 3 },
                    { text: 'Je ressens les émotions des autres\n', choice: 3 },
                    { text: 'Je suis un planning.\n', choice: 3 },
                    { text: 'Je suis facilement irrité.\n', choice: 3 },
                    { text: 'Je passe du temps à réflichir.\n', choice: 3 },
                    { text: 'Je suis silencieux autour des gens que je ne connais pas.\n', choice: 3 },
                    { text: 'Je mets les gens à l\'aise\n', choice: 3 },
                    { text: 'Je suis exigent dans mon travail\n', choice: 3 },
                    { text: 'Je me sens souvent triste.\n', choice: 3 },
                    { text: 'J\'ai beaucoup d\'idées.\n', choice: 3 }
      ],
      chartdata: {
        labels: ['Ouverture', 'Conscienciosité', 'Extraversion', 'Agréabilité', 'Névrosisme'],
        datasets: [
          {
            label: '',
            backgroundColor: '#f87979',
            data: [0, 0, 0, 0, 0]
          }
        ]
      },
      options: {
        legend: {
          display: false
        },
        responsive: true,
        maintainAspectRatio: false,
        scales:{
          xAxes: [{
            display: false,
            beginAtZero: true,
            ticks: {
              suggestedMax: 100,
              suggestedMin: 0
            }
          }]
        }
      }
    }
  },
  mounted () {
    this.result = this.$store.getters.getBfResult;
    if (!this.result)
      return;
    this.chartdata = {
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
          data: [this.result.score.O * 100/40, this.result.score.C * 100/40, this.result.score.E * 100/40, this.result.score.A * 100/40, this.result.score.N * 100/40]
        }
      ]
    };
  },
  methods: {
    sendResults () {
        this.loading = true;
        let results = this.statements.map(s => s.choice);

        axios.post(process.env.VUE_APP_API_URL + '/quizBig5Prediction?liste=' + results).then(res => {
          this.$store.commit('setBfResult', res.data);
          this.result = res.data;

          this.chartdata = {
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
               data: [this.result.score.O * 100/40, this.result.score.C * 100/40, this.result.score.E * 100/40, this.result.score.A * 100/40, this.result.score.N * 100/40]
             }
           ]
          };

          this.loading = false;
          this.$store.dispatch('sendProfileToDB');
        }).catch(err => {
          console.log(err);
          this.loading = false;
        });
    },
    nextQuestion() {
      setTimeout(() => {
        this.quizzIndex++;
        if (this.quizzIndex === this.statements.length)
          this.sendResults();
      }, 300);
    },
    previousQuestion() {
      if (this.quizzIndex > 0)
        this.quizzIndex--;
    },
    restart() {
      this.$store.commit('setBfResult', null);
      this.$router.go();
    }
  }
}
</script>

<style lang="scss" scoped>
  hr {
    border-top: 1px solid rgba(255, 255, 255, 0.7);
  }
</style>
