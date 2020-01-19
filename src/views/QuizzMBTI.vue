<template>
    <div style="background-color: #567098">
      <b-container class="pt-3 pb-5">
        <div v-for="(statement, index) in statements" :key="statement.text">
          <div :ref="'mbti' + index">
            <statement-mbti @click.native="scroll(index)" v-model="statement.choice" :text="statement.text" class="py-5"></statement-mbti>
            <hr>
          </div>
        </div>
        <b-button ref="test" @click="sendResults" class="mt-3" variant="info" size="lg" pill>Valider</b-button>
      </b-container>

      <b-modal id="modal-mbti" title="MBTI Résultat" hide-footer>
        <b-spinner v-if="loading" class="d-block m-auto" variant="light" label="Spinning"></b-spinner>

        <div v-if="result && !loading">
          <personality :personality="result"></personality>
          <p class="text-justify">{{ result.desc }}</p>
          <b-button @click="hideModal" class="float-right px-3" variant="info" pill>Ok</b-button>
        </div>
      </b-modal>
    </div>
</template>

<script>
import * as axios from 'axios'
export default {
  name: 'QuizzMBTI',
  data () {
    return {
      loading: false,
      result: null,
      statements: [ { text: 'Vous avez des difficultés à vous présenter à d’autres personnes.\n', choice: 4 },
                    { text: 'Vous êtes souvent si perdu(e) dans vos pensées que vous ignorez ou oubliez votre entourage.\n', choice: 4 },
                    { text: 'Vous essayez de répondre dès que possible à vos e-mails et ne supportez pas d’avoir une boîte de messagerie mal organisée.\n', choice: 4 },
                    { text: 'Vous avez des facilités à rester serein(e) et concentré(e), même lorsque certaines situations donnent lieu à une certaine pression.\n', choice: 4 },
                    { text: 'Habituellement, vous ne lancez pas les conversations.\n', choice: 4 },
                    { text: 'Vous entreprenez rarement des actions par simple curiosité.\n', choice: 4 },
                    { text: 'Vous vous sentez supérieur(e) aux autres.\n', choice: 4 },
                    { text: 'Pour vous, être organisé(e) est plus important qu’être flexible.\n', choice: 4 },
                    { text: 'Vous êtes généralement très motivé(e) et plein(e) d’énergie.\n', choice: 4 },
                    { text: 'Gagner un débat vous importe moins que d’avoir la certitude que personne n’est contrarié.\n', choice: 4 },
                    { text: 'Vous avez souvent l’impression de devoir vous justifier auprès de vos pairs.\n', choice: 4 },
                    { text: 'Au travail et au domicile, votre environnement de vie est assez ordonné.\n', choice: 4 },
                    { text: 'Cela ne vous dérange pas d’être le centre de l’attention.\n', choice: 4 },
                    { text: 'Vous considérez votre esprit comme plus pratique que créatif.\n', choice: 4 },
                    { text: 'Les gens peuvent rarement vous contrarier.\n', choice: 4 },
                    { text: 'Vos itinéraires de voyage sont généralement planifiés à l’avance.\n', choice: 4 },
                    { text: 'Vous avez des difficultés à ressentir de l’empathie pour les sentiments des autres.\n', choice: 4 },
                    { text: 'Votre humeur peut changer très rapidement.\n', choice: 4 },
                    { text: 'Au cours d’une discussion, la vérité doit passer avant la susceptibilité de chacun.\n', choice: 4 },
                    { text: 'Vous vous inquiétez rarement des conséquences de vos actions sur vos pairs.\n', choice: 4 },
                    { text: 'Votre style de travail s’approche plus de pics d’énergie aléatoires que d’une approche méthodique et organisée.\n', choice: 4 },
                    { text: 'Vous êtes souvent envieux(-se) des autres.\n', choice: 4 },
                    { text: 'Un livre ou un jeu vidéo de qualité sont souvent mieux qu’une soirée mondaine.\n', choice: 4 },
                    { text: 'Être capable de développer un plan et de s’y tenir est la partie la plus importante de chaque projet.\n', choice: 4 },
                    { text: 'Vous ne vous laissez distraire que rarement par vos rêves et pensées.\n', choice: 4 },
                    { text: 'Vous êtes souvent perdu(e) dans vos pensées lorsque vous marchez dans la nature.\n', choice: 4 },
                    { text: 'Si quelqu’un ne répond pas rapidement à votre e-mail, vous vous inquiétez et vous demandez si vous avez dit quelque chose de mal.\n', choice: 4 },
                    { text: 'En tant que parent, vous préféreriez voir votre enfant devenir gentil plutôt qu’intelligent.\n', choice: 4 },
                    { text: 'Vous ne laissez pas les autres influencer vos actions.\n', choice: 4 },
                    { text: 'Vos rêves ont tendance à se concentrer sur le monde réel et ses événements.\n', choice: 4 },
                    { text: 'Il vous faut peu de temps pour vous impliquer dans les activités sociales de votre nouveau lieu de travail.\n', choice: 4 },
                    { text: 'Vous êtes plus du genre à improviser naturellement qu’à tout planifier minutieusement.\n', choice: 4 },
                    { text: 'Vos émotions vous contrôlent plus que vous ne les contrôlez.\n', choice: 4 },
                    { text: 'Vous appréciez d’aller à des soirées déguisées ou de participer à des jeux de rôle.\n', choice: 4 },
                    { text: 'Vous passez souvent du temps à explorer des idées irréalistes et irréalisables, mais aussi intriguantes.\n', choice: 4 },
                    { text: 'Vous préféreriez improviser que passer de temps sur la construction d’un plan détaillé.\n', choice: 4 },
                    { text: 'Vous êtes une personne relativement calme et réservée.\n', choice: 4 },
                    { text: 'Si vous aviez une entreprise, vous trouveriez difficile de licencier des employés loyaux mais qui n’atteignent pas leurs objectifs.\n', choice: 4 },
                    { text: 'Vous réfléchissez souvent aux raisons de l’existence humaine.\n', choice: 4 },
                    { text: 'La logique est généralement plus importante que les sentiments lorsqu’il s’agit de prendre des décisions importantes.\n', choice: 4 },
                    { text: 'Il est plus important de maintenir un choix de possibilités ouvert plutôt que d’avoir une liste de choses à faire.\n', choice: 4 },
                    { text: 'Si vos amis sont vraiment tristes à propos d’une situation, vous êtes plus susceptible de leur offrir un soutien émotionnel que de leur suggérer des solutions au problème.\n', choice: 4 },
                    { text: 'Vous vous sentez rarement inquiet(-ète).\n', choice: 4 },
                    { text: 'Vous n’avez aucune difficulté à établir un programme personnel et à vous y tenir.\n', choice: 4 },
                    { text: 'En travail d’équipe, il est plus important d’avoir raison que d’être coopératif.\n', choice: 4 },
                    { text: 'Vous pensez que les opinions de tous doivent être respectées, indépendamment du fait qu’elles soient justifiées ou non par des faits.\n', choice: 4 },
                    { text: 'Votre énergie est multipliée si vous avez passé du temps avec un groupe.\n', choice: 4 },
                    { text: 'Vous perdez fréquemment vos affaires.\n', choice: 4 },
                    { text: 'Vous vous considérez comme très stable au niveau émotionnel.\n', choice: 4 },
                    { text: 'Votre esprit regorge constamment d’idées et de plans à explorer.\n', choice: 4 },
                    { text: 'Vous ne vous considérez pas comme un rêveur / une rêveuse.\n', choice: 4 },
                    { text: 'Vous avez des difficultés à vous détendre lorsque vous parlez devant de nombreuses personnes.\n', choice: 4 },
                    { text: 'Généralement, vous vous fiez davantage à votre expérience qu’à votre imagination.\n', choice: 4 },
                    { text: 'Vous vous souciez trop de ce que pensent les gens.\n', choice: 4 },
                    { text: 'Si la pièce est remplie de monde, vous restez près des murs et évitez le centre.\n', choice: 4 },
                    { text: 'Vous avez tendance à tout remettre à plus tard jusqu’à ce qu’il ne reste plus assez de temps pour tout faire.\n', choice: 4 },
                    { text: 'Vous vous sentez très anxieux(-se) dans les situations stressantes.\n', choice: 4 },
                    { text: 'Vous croyez qu’il est plus gratifiant d’être apprécié(e) par les autres que d’être puissant(e).\n', choice: 4 },
                    { text: 'Vous avez toujours été intéressé(e) par les sujets ambigus et atypiques (par ex. : livres, art, films indépendants).\n', choice: 4 },
                    { text: 'Vous prenez souvent l’initiative dans les situations sociales.\n', choice: 4 }
      ]
    }
  },
  methods: {
    sendResults () {
      this.loading = true;
      this.$bvModal.show('modal-mbti');
      let results = [];

      for (let statement of this.statements)
        results.push(statement.choice);

      console.log(results);
      axios.post('http://localhost:5000/quizMbtiPrediction?liste=' + results).then(res => {
        console.log(res);
        this.$store.commit('setMbtiResult', res.data);
        this.result = this.$store.getters.getPersonalities.filter(p => p.sigle.toLowerCase() === res.data.toLowerCase()).pop();
        this.loading = false;
        this.$store.dispatch('sendProfileToDB');
      }).catch(err => {
        console.log(err);
        this.loading = false;
      });
    },
    scroll(index) {
      index++;
      let next = 'mbti' + index;

      if (!this.$refs[next])
        return;

      this.$refs[next][0].scrollIntoView({ behavior: 'smooth' });
    },
    hideModal() {
      this.$bvModal.hide('modal-mbti');
    }
  }
}
</script>

<style lang="scss" scoped>
  hr {
    border-top: 1px solid rgba(255, 255, 255, 0.7);
  }
</style>
