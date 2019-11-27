<template>
  <div>
    <b-tabs content-class="mt-3" fill>
      <b-tab title="First" active>
        <b-container>
          <b-card>
            <p>Hallo</p>
          </b-card>
        </b-container>
      </b-tab>
      <b-tab title="Second">

      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .card {
    box-shadow: 0px 0px 30px 0px #cfcfcf;
    border-color: transparent;
    border-radius: 30px;
  }
</style>
