<template>
  <span>
      <v-navigation-drawer app v-model="drawer" dark style="border: solid 2px">
          <v-list>
              <v-list-item link to='/'>
                  Acceuil
              </v-list-item>
              <v-list-item link to='/AcceuilPetitBac'>
                  Petit Bac
              </v-list-item>
              <v-list-item @click = "logOff()">
                  Déconnexion
              </v-list-item>
          </v-list>
      </v-navigation-drawer>

      <v-app-bar app color="blue darken-4" dark>
          <v-app-bar-nav-icon @click="drawer = !drawer" v-if="loggedIn"></v-app-bar-nav-icon>
      </v-app-bar>    
  </span>
</template>

<script>
import axios from 'axios';

export default {
    name: 'AppNavigation',
    data(){
        return {
            drawer: false,
            loggedIn: true,
        }
    },
    methods: {
        logOff() {
            console.log(JSON.parse(localStorage.getItem("player")))
            axios.post(localStorage.getItem("urlBack") + "/users/logOff", {login: JSON.parse(localStorage.getItem("player"))["login"]})
            .then((response) => {
                console.log(response.data)
                window.location.href = "./#/login"
            })
            .catch((error) => console.log(error))
        }
    },
    mounted(){
        if (window.location.href.includes("login")){this.loggedIn = false}
    }
}
</script>