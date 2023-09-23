<template>
  <h1 id="debug"></h1>
  <h1 id="debug2"></h1>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  async mounted() {
      let loggedIn = localStorage.getItem("loggedIn");
      document.getElementById("debug").innerText = loggedIn
      if (loggedIn != "true"){
        document.getElementById("debug2").innerText = "loggedin true"
        window.location.href = "./#/login"
      }

      localStorage.setItem("hasReloaded", "false")

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
