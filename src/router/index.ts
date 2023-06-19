import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import DriversPage from '@/views/DriversPage.vue'
import RacesPage from '@/views/RacesPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/drivers',
      name: 'drivers',
      component: DriversPage,
    },
    {
      path: '/races',
      name: 'races',
      component: RacesPage,
    }
  ]
})

export default router
