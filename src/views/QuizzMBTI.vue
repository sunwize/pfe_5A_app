<template>
    <div style="background-color: #567098">
      <b-container class="pt-3 pb-5">
        <h2 class="text-white pt-0 pb-3 py-lg-4">Quizz MBTI</h2>

        <div v-if="quizzIndex < statements.length && !loading && !result">
          <h3 class="d-flex">
            <div class="w-50 text-left">
              <b-button @click="previousQuestion" variant="outline-dark" pill><icon icon="arrow-left"></icon></b-button>
            </div>
            <div class="w-50 text-right">{{ quizzIndex+1 }} / {{ statements.length }}</div>
          </h3>
          <hr>
          <statement-mbti v-model="statements[quizzIndex].choice" :text="statements[quizzIndex].text" :on-answer="nextQuestion" class="py-5"></statement-mbti>
          <hr>
        </div>
        <div v-else>
          <b-spinner v-if="loading" class="d-block m-auto" variant="light" label="Spinning"></b-spinner>

          <b-row v-if="result && !loading">
            <b-col cols="12" lg="3">
              <personality :personality="result"></personality>
            </b-col>
            <b-col cols="12" lg="9">
              <p class="text-justify text-white">{{ result.desc }}</p>
            </b-col>
          </b-row>
          <b-button v-if="result && !loading" @click="restart" class="mt-3" variant="outline-light"><icon icon="redo-alt"></icon> Recommencer</b-button>
        </div>
      </b-container>
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
      quizzIndex: 0,
      statements: [
      { text: 'Votre énergie est multipliée si vous avez passé du temps avec un groupe.\n', choice: 4 },
      { text: 'Vous passez souvent du temps à explorer des idées irréalistes et irréalisables, mais aussi intriguantes.\n', choice: 4 },
      { text: 'Vos itinéraires de voyage sont généralement planifiés à l’avance.\n', choice: 4 },
      { text: 'Vous pensez souvent à ce que vous auriez dû dire dans une conversation après qu elle a eu lieu.\n', choice: 4 },
      { text: 'Si vos amis sont vraiment tristes à propos d’une situation, vous êtes plus susceptible de leur offrir un soutien émotionnel que de leur suggérer des solutions au problème.\n', choice: 4 },
      { text: 'Les gens peuvent rarement vous déranger.\n', choice: 4 },
      { text: 'Habituellement, vous ne lancez pas les conversations.\n', choice: 4 },
      { text: 'Être capable de développer un plan et de s’y tenir est la partie la plus importante de chaque projet.\n', choice: 4 },
      { text: 'Vous vous inquiétez rarement si vous avez fait bonne impression sur quelqu un que vous avez rencontré.\n', choice: 4 },
      { text: 'Ce serait un défi pour vous de passer le week-end tout seul sans vous ennuyer.\n', choice: 4 },
      { text: 'Vous êtes plus une personne qui s intéresse aux détails qu une personne qui a une vue d ensemble.\n', choice: 4 },
      { text: 'Vous êtes très affectueux avec les gens qui vous sont chers.\n', choice: 4 },
      { text: 'Au travail et au domicile, votre environnement de vie est assez ordonné.\n', choice: 4 },
      { text: 'Vous êtes toujours gêné par les erreurs que vous avez faites il y a longtemps.\n', choice: 4 },
      { text: 'Si la pièce est remplie de monde, vous restez près des murs et évitez le centre.\n', choice: 4 },
      { text: 'La logique est généralement plus importante que les sentiments lorsqu’il s’agit de prendre des décisions importantes.\n', choice: 4 },
      { text: 'Lorsque vous recherchez un film à regarder, vous pouvez passer des siècles à parcourir le catalogue.\n', choice: 4 },
      { text: 'Vous avez des facilités à rester serein(e) et concentré(e), même lorsque certaines situations donnent lieu à une certaine pression.\n', choice: 4 },
      { text: 'Lorsque vous faites partie d un groupe de personnes que vous ne connaissez pas, vous n avez aucun problème à vous lancer directement dans leur conversation.\n', choice: 4 },
      { text: 'Lorsque vous dormez, vos rêves ont tendance à être bizarres, fantastiques et irréels.\n', choice: 4 },
      { text: 'À votre avis, il est parfois acceptable de marcher sur les autres pour avancer dans la vie.\n', choice: 4 },
      { text: 'Vous êtes dévoué et concentré sur vos objectifs, vous ne détournez que rarement.\n', choice: 4 },
      { text: 'Si vous faites une erreur, vous avez tendance à commencer à douter de vous-même, de vos capacités ou de vos connaissances.\n', choice: 4 },
      { text: 'Vous avez des difficultés à vous présenter à d’autres personnes.\n', choice: 4 },
      { text: 'Vous perdez généralement de l intérêt pour une discussion lorsqu elle devient philosophique.\n', choice: 4 },
      { text: 'Vous ne vous laisseriez jamais pleurer devant les autres.\n', choice: 4 },
      { text: 'Vous vous sentez plus attiré par des endroits animés et bondés que par des endroits plus calmes et intimes.\n', choice: 4 },
      { text: 'Vous aimez discuter de différents points de vue et théories sur ce à quoi le monde pourrait ressembler à l avenir.\n', choice: 4 },
      { text: 'Lorsqu il s agit de faire des décisions importantes, vous écoutez principalement votre cœur plutôt que votre cerveau.\n', choice: 4 },
      { text: 'Vous ne pouvez pas vous imaginer consacrer votre vie à l étude de quelque chose que vous ne pouvez pas voir, toucher ou ressentir.\n', choice: 4 },
      { text: 'Vous préférez généralement prendre votre revanche plutôt que de pardonner.\n', choice: 4 },
      { text: 'Vous prenez souvent des décisions sur un coup de tête.\n', choice: 4 },
      { text: 'Le temps que vous passez seul finit souvent par être plus intéressant et satisfaisant que le temps que vous passez avec d autres personnes.\n', choice: 4 },
      { text: 'Vous essayez souvent d interpréter le vrai sens ou le message d une chanson ou d un film.\n', choice: 4 },
      { text: 'Vous savez toujours exactement ce que vous voulez.\n', choice: 4 },
      { text: 'Vous repensez rarement aux choix que vous avez faits et vous vous demandez ce que vous auriez pu faire différemment.\n', choice: 4 },
      { text: 'Lorsque vous êtes dans un lieu public, vous restez généralement dans les endroits les plus calmes et moins encombrées.\n', choice: 4 },
      { text: 'Vous avez tendance à vous concentrer sur les réalités actuelles plutôt que sur les possibilités futures.\n', choice: 4 },
      { text: 'Vous avez des difficultés à ressentir de l’empathie pour les sentiments des autres.\n', choice: 4 },
      { text: 'Lorsque vous commencez un projet, vous préférez prendre autant de décisions à l avance que possible.\n', choice: 4 },
      { text: 'Lorsque vous savez que quelqu un a une grande estime de vous, vous vous demandez également combien de temps il faudra avant qu il soit déçu de vous.\n', choice: 4 },
      { text: 'Vous vous sentez à l aise de marcher vers quelqu un que vous trouvez intéressant et d entamer une conversation.\n', choice: 4 },
      { text: 'Vous imaginez souvent diverses idées ou scénarios dans votre tête.\n', choice: 4 },
      { text: 'Vous prenez soin de vous en premier et les autres viennent en second.\n', choice: 4 },
      { text: 'Vous avez des difficulté à établir un programme personnel et à vous y tenir.\n', choice: 4 },
      { text: 'Votre humeur peut changer très rapidement.\n', choice: 4 },
      { text: 'Vous réfléchissez souvent aux raisons de l’existence humaine.\n', choice: 4 },
      { text: 'Vous parlez souvent de vos propres sentiments et émotions.\n', choice: 4 },
      { text: 'Vous avez des plans détaillés de formation ou de développement de carrière s étalant sur plusieurs années dans le futur.\n', choice: 4 },
      { text: 'Vous restez rarement bloqué sur vos regrets.\n', choice: 4 },
      { text: 'Passer du temps dans une atmosphère dynamique avec beaucoup de monde rapidement vous fait sentir épuisé et a besoin d une escapade.\n', choice: 4 },
      { text: 'Vous vous voyez plus réaliste que visionnaire.\n', choice: 4 },
      { text: 'Vous avez des facilités à ressentir de l’empathie pour quelqu un qui a vécu quelque chose que vous n avez jamais vécu.\n', choice: 4 },
      { text: 'Votre style de travail s’approche plus de pics d’énergie aléatoires que d’une approche méthodique et organisée.\n', choice: 4 },
      { text: 'Vos émotions vous contrôlent plus que vous ne les contrôlez.\n', choice: 4 },
      { text: 'Après une semaine longue et épuisante, une soirée amusante est exactement ce dont vous avez besoin.\n', choice: 4 },
      { text: 'Vous vous demandez souvent comment les progrès technologiques peuvent changer la vie quotidienne.\n', choice: 4 },
      { text: 'Vous vous inquiétez souvent des conséquences de vos actions sur les autres.\n', choice: 4 },
      { text: 'Vous respectez toujours les engagements que vous avez pris même si vous changez d avis. \n', choice: 4 },
      { text: 'Vous vous sentez rarement en manque d assurance et de confiance en soi.\n', choice: 4 },

      ]
    }
  },
  mounted () {
    let result = this.$store.getters.getMbtiResult;
    if (result)
      this.result = this.$store.getters.getPersonalities.filter(p => p.sigle.toLowerCase() === result.toLowerCase()).pop();
  },
  methods: {
    sendResults () {
      this.loading = true;
      let results = [];

      for (let statement of this.statements)
        results.push(statement.choice);

      axios.post(process.env.VUE_APP_API_URL + '/quizMbtiPrediction?liste=' + results).then(res => {
        this.$store.commit('setMbtiResult', res.data);
        this.result = this.$store.getters.getPersonalities.filter(p => p.sigle.toLowerCase() === res.data.toLowerCase()).pop();
        console.log(this.result);
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
      this.$store.commit('setMbtiResult', null);
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
