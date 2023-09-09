import { createRouter, createWebHashHistory } from 'vue-router'
import PetitBac from '../views/PetitBac.vue'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/login.vue'
import RegistrationView from '../views/registration.vue'
import AcceuilPetitBacView from '../views/AcceuilPetitBac.vue'

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
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router