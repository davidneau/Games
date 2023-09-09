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
              <v-list-item link to='/login'>
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
export default {
    name: 'AppNavigation',
    data(){
        return {
            drawer: false,
            loggedIn: true,
        }
    },
    mounted(){
        console.log(localStorage.getItem("loggedIn"))
        if (window.location.href.includes("login")){this.loggedIn = false}
    }
}
</script>