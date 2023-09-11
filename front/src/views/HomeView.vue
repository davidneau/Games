<template>
  <h1>BienvenueModif</h1>
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

      if (window.location.href.includes("127.0.0.1")){
        localStorage.setItem("urlBack", "http://127.0.0.1:5000")
      }
      if (window.location.href.includes("gaminggalaxiemania.com")){
        localStorage.setItem("urlBack", "http://85.31.238.211:5000")
      }

      console.log("urlBack : " + localStorage.getItem("urlBack"))
      
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
