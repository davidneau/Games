<template>
  <h1>Bienvenue</h1>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  async mounted() {
      let loggedIn = localStorage.getItem("loggedIn");
      if (loggedIn == "false"){
        window.location.href = "./#/login"
      }
      console.log("aaaa")
    }
});
</script>

<style scoped>

h1{
  color: pink;
  text-align: center;
  font-size: 100px;
}

</style>
