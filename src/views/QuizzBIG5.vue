<template>
    <div style="background-color: #567098">
      <b-container class="pt-3 pb-5">
        <div v-for="statement in statements" :key="statement.text">
          <statement-bf v-model="statement.choice" :text="statement.text" class="py-4"></statement-bf>
          <hr>
        </div>
        <b-button @click="sendResults" class="mt-3" variant="info" size="lg" pill>Soumettre</b-button>
      </b-container>
      <div v-if="result" class="pt-3 pb-5">
          <p class="text-white">Your personality: {{ result }} </p>
      </div>

    </div>

</template>

<script>
import * as axios from 'axios'
export default {
  name: 'QuizzBIG5',
  data () {
    return {
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
                    { text: 'Eviter les responsabilités.\n', choice: 3 },
                    { text: 'Avoir des sauts d\'humeur.\n', choice: 3 },
                    { text: 'Utiliser des mots élaborés.\n', choice: 3 },
                    { text: 'Je me fiche d\'être le centre d\'intérêt.\n', choice: 3 },
                    { text: 'Je ressens les émotions des autres\n', choice: 3 },
                    { text: 'Je suis un planning.\n', choice: 3 },
                    { text: 'Je suis facilement irrité.\n', choice: 3 },
                    { text: 'Je passe du temps à réflichir.\n', choice: 3 },
                    { text: 'Je suis silencieux autour des gens que je ne connais pas.\n', choice: 3 },
                    { text: 'Je mets les gens à l\'aise\n', choice: 3 },
                    { text: 'Je suis exigent dans mon travail\n', choice: 3 },
                    { text: 'Je me sens triste souvent.\n', choice: 3 },
                    { text: 'J\'ai beaucoup d\'idées.\n', choice: 3 }
      ],
      result: ''
    }
  },
  methods: {
    sendResults () {
      let results = this.statements.map(s => s.choice);
      console.log(results);
       axios.post('http://localhost:5000/quizBig5Prediction?liste=' + results).then(res => {
        console.log(res)
        this.result = res.data
      }).catch(err => {
        console.log(err)
      })
    }

  }
}
</script>

<style lang="scss" scoped>
  hr {
    border-top: 1px solid rgba(255, 255, 255, 0.7);
  }
</style>
