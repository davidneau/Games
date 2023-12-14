<template>
  <h1 id="debug">Bienvenue</h1>
</template>

<script>
import axios from "axios"
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  methods: {
    updateRoom(){
      axios.get(localStorage.getItem("urlBack") + "/updateRoom/" +  JSON.parse(localStorage.getItem("player"))["login"] + "/home")
      .then((response) => {
        console.log(response.data)
      })
    },
  },
  async mounted() {
      let loggedIn = localStorage.getItem("loggedIn");

      localStorage.setItem("hasReloaded", "false")

      if (window.location.href.includes("127.0.0.1") || window.location.href.includes("localhost")){
        localStorage.setItem("urlBack", "http://127.0.0.1:5000")
      }
      if (window.location.href.includes("gaminggalaxiemania.com")){
        localStorage.setItem("urlBack", "http://85.31.238.211:5000")
      }

      console.log("urlBack : " + localStorage.getItem("urlBack"))
      if (loggedIn != "true"){
        window.location.href = "./#/login"
      }

      this.updateRoom()
    }
});
</script>

<style scoped>

h1{
  color: pink;
  text-align: center;
  font-size: 100px;
}

@media only screen and (max-width: 600px) {
  h1 {
    font-size: 40px;
  }
}

</style>
