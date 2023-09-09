<template>
  <v-app class="main">
    <AppNavigation></AppNavigation>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import AppNavigation from '@/components/AppNavigation'

export default {
  name: 'App',
  components: {
    AppNavigation,
  },

  data: () => ({
    //
  }),
}
</script>

<style scoped>

.main{
  background-color: black;
}

</style>