<template>
    <div style="background-color: #567098">
      <b-container class="pt-3 pb-5">
        <div v-for="statement in statements" :key="statement.text">
          <statement-bf v-model="statement.choice" :text="statement.text" class="py-5"></statement-bf>
          <hr>
        </div>
        <b-button @click="sendResults" class="mt-3" variant="info" size="lg" pill>Valider</b-button>
      </b-container>

      <b-modal id="modal-bf" title="Big Five Résultat" size="lg" hide-footer>
        <b-spinner v-if="loading" class="d-block m-auto" variant="light" label="Spinning"></b-spinner>

        <div v-if="result && !loading">
          <h3 class="text-center">{{ result }}</h3>
          <horizontal-bars :chartdata="chartdata" :options="options"/>
          <b-button @click="hideModal" class="float-right px-3" variant="info" pill>Ok</b-button>
        </div>
      </b-modal>
    </div>
</template>

<script>
import * as axios from 'axios'
export default {
  name: 'QuizzBIG5',
  data () {
    return {
      loading: false,
      result: '',
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
        labels: ['L\'ouverture à l\'expérience', 'La conscienciosité', 'L\'extraversion', 'L\'agréabilité', 'Le névrosisme'],
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
  methods: {
    sendResults () {
        this.loading = true;
        this.$bvModal.show('modal-bf');
        let results = this.statements.map(s => s.choice);
        console.log(results);

        axios.post('http://localhost:5000/quizBig5Prediction?liste=' + results).then(res => {
          console.log(res);
          this.$store.commit('setBfResult', res.data.score);
          this.result = res.data.sigle;
          let score = res.data.score;

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
               data: [score.O * 100/40, score.C * 100/40, score.E * 100/40, score.A * 100/40, score.N * 100/40]
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
    hideModal() {
      this.$bvModal.hide('modal-bf');
    }
  }
}
</script>

<style lang="scss" scoped>
  hr {
    border-top: 1px solid rgba(255, 255, 255, 0.7);
  }
</style>
