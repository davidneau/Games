import { createRouter, createWebHashHistory } from 'vue-router'
import PetitBac from '../views/PetitBac.vue'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/login.vue'
import RegistrationView from '../views/registration.vue'
import AcceuilPetitBacView from '../views/AcceuilPetitBac.vue'
import PlanetD from '../views/planetD.vue'
import testFBX from '../views/fbxTest.vue'

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/petitbac',
    name: 'PetitBac',
    component: PetitBac
  },
  {
    path: '/acceuilPetitBac',
    name: 'acceuilPetitBac',
    component: AcceuilPetitBacView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/registration',
    name: 'registration',
    component: RegistrationView
  },
  {
    path: '/testFBX',
    name: 'testFBX',
    component: testFBX
  },
  {
    path: '/PlanetD',
    name: 'PlanetD',
    component: PlanetD
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router