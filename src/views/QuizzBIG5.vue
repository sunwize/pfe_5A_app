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
      statements: [ { text: 'Am the life of the party.\n', choice: 3 },
                    { text: 'Feel little concern for others.\n', choice: 3 },
                    { text: 'Am always prepared.\n', choice: 3 },
                    { text: 'Get stressed out easily.\n', choice: 3 },
                    { text: 'Have a rich vocabulary.\n', choice: 3 },
                    { text: 'Dont talk a lot\n', choice: 3 },
                    { text: 'Am interested in people.\n', choice: 3 },
                    { text: 'Leave my belongings around.\n', choice: 3 },
                    { text: 'Am relaxed most of the time\n', choice: 3 },
                    { text: 'Have difficulty understanding abstract ideas.\n', choice: 3 },
                    { text: 'Feel comfortable around people.\n', choice: 3 },
                    { text: 'Insult people\n', choice: 3 },
                    { text: 'Pay attention to details.\n', choice: 3 },
                    { text: 'Worry about things\n', choice: 3 },
                    { text: 'Have a vivid imagination.\n', choice: 3 },
                    { text: 'Keep in the background.\n', choice: 3 },
                    { text: 'Sympathize with others feelings\n', choice: 3 },
                    { text: 'Make a mess of things.\n', choice: 3 },
                    { text: 'Seldom feel blue.\n', choice: 3 },
                    { text: 'Am not interested in abstract ideas\n', choice: 3 },
                    { text: 'Start conversations.\n', choice: 3 },
                    { text: 'Am not interested in other peoples problems.\n', choice: 3 },
                    { text: 'Get chores done right away.\n', choice: 3 },
                    { text: 'Am easily disturbed.\n', choice: 3 },
                    { text: 'Have excellent ideas.\n', choice: 3 },
                    { text: 'Have little to say.\n', choice: 3 },
                    { text: 'Have a soft heart.\n', choice: 3 },
                    { text: 'Often forget to put things back in their proper place.\n', choice: 3 },
                    { text: 'Get upset easily.\n', choice: 3 },
                    { text: 'Do not have a good imagination\n', choice: 3 },
                    { text: 'Talk to a lot of different people at parties.\n', choice: 3 },
                    { text: 'Am not really interested in others\n', choice: 3 },
                    { text: 'Like order.\n', choice: 3 },
                    { text: 'Change my mood a lot.\n', choice: 3 },
                    { text: 'Am quick to understand things.\n', choice: 3 },
                    { text: 'Dont like to draw attention to myself.\n', choice: 3 },
                    { text: 'Take time out for others.\n', choice: 3 },
                    { text: 'Shirk my duties.\n', choice: 3 },
                    { text: 'Have frequent mood swings.\n', choice: 3 },
                    { text: 'Use difficult words.\n', choice: 3 },
                    { text: 'Dont mind being the center of attention.\n', choice: 3 },
                    { text: 'Feel others emotions\n', choice: 3 },
                    { text: 'Follow a schedule.\n', choice: 3 },
                    { text: 'Get irritated easily.\n', choice: 3 },
                    { text: 'Spend time reflecting on things.\n', choice: 3 },
                    { text: 'Am quiet around strangers.\n', choice: 3 },
                    { text: 'Make people feel at ease\n', choice: 3 },
                    { text: 'Am exacting in my work\n', choice: 3 },
                    { text: 'Often feel blue.\n', choice: 3 },
                    { text: 'Am full of ideas.\n', choice: 3 }
      ],
      result: ''
    }
  },
  methods: {
    sendResults () {
      let results = this.statements.map(s => s.choice);
      console.log(results);
    }

  }
}
</script>

<style lang="scss" scoped>
  hr {
    border-top: 1px solid rgba(255, 255, 255, 0.7);
  }
</style>
