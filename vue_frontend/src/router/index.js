import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import store from '../store'
import Players from '../views/dashboard/Players.vue'
import Games from '../views/dashboard/Games.vue'
import Game from '../views/dashboard/Game.vue'
import AddGame from '../views/dashboard/AddGame.vue'
import AddUser from '../views/dashboard/AddUser.vue'
import Users from '../views/dashboard/Users.vue'
import NotFound from '../views/NotFound.vue'


const routes = [
  {
    path: '/:pathMatch(.*)*',
    component: NotFound
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  { 
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  { 
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  { 
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { 
      requireLogin: true
    }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  { 
    path: '/dashboard/players',
    name: 'Players',
    component: Players,
    meta: { 
      requireLogin: true
    }
  },

  { 
    path: '/dashboard/games',
    name: 'Games',
    component: Games,
    meta: { 
      requireLogin: true
    }
  },

  { 
    path: '/dashboard/addgame',
    name: 'AddGame',
    component: AddGame,
    // meta: { 
    //   requireLogin: true
    // }
  },

  {
  path: '/dashboard/games/:id',
  name: 'Game',
  component: Game,
},

{
  path: '/dashboard/adduser',
  name: 'AddUser',
  component: AddUser,
},

{
  path: '/dashboard/users/:id',
  name: 'Users',
  component: Users,
  meta: { 
    requireLogin: true
  }
},

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => { 
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) { 
    next('/log-in')
  } else { 
    next()
  }
})

export default router
