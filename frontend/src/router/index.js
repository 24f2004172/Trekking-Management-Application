import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '../views/auth/Login.vue'
import Register from '../views/auth/Register.vue'

import AdminLayout from '../layouts/AdminLayout.vue'

import Dashboard from '../views/admin/Dashboard.vue'
import Treks from '../views/admin/Treks.vue'
import Staff from '../views/admin/Staff.vue'
import Users from '../views/admin/Users.vue'
import Bookings from '../views/admin/Bookings.vue'
import Reports from '../views/admin/Reports.vue'

import StaffDashboard from '@/views/staff/StaffDashboard.vue'
import StaffTrekDetails from '@/views/staff/StaffTrekDetails.vue'

import UserLayout from '@/layouts/UserLayout.vue'
import BrowseTreks from '@/views/user/BrowseTreks.vue'
import TrekDetails from '@/views/user/TrekDetails.vue'
import MyBookings from '@/views/user/MyBookings.vue'
import UserDashboard from '@/views/user/UserDashboard.vue'
import History from '@/views/user/History.vue'
import Profile from '@/views/user/Profile.vue'

Vue.use(VueRouter)

const routes = [

  {
    path: '/',
    component: Login
  },

  {
    path: '/register',
    component: Register
  },

  {
    path: '/admin',
    component: AdminLayout,
    meta: {
      requiresAuth: true,
      role: 'Admin'
    },

    children: [

      {
        path: '',
        component: Dashboard
      },

      {
        path: 'treks',
        component: Treks
      },

      {
        path: 'staff',
        component: Staff
      },

      {
        path: 'users',
        component: Users
      },

      {
        path: 'bookings',
        component: Bookings
      },

      {
        path: 'reports',
        component: Reports
      }

    ]
  },

  {
    path: '/staff/dashboard',
    name: 'StaffDashboard',
    component: StaffDashboard,
    meta: {
      requiresAuth: true,
      role: 'Staff'
    }
  },
  {
    path: '/staff/trek/:id',
    name: 'StaffTrekDetails',
    component: StaffTrekDetails,
    meta: {
      requiresAuth: true,
      role: 'Staff'
    }
  },

  {
    path: '/user',
    component: UserLayout,
    meta: {
      requiresAuth: true,
      role: 'Trekker'
    },

    children: [

      {
        path: 'dashboard',
        component: UserDashboard
      },

      {
        path: 'treks',
        component: BrowseTreks
      },

      {
        path: 'trek/:id',
        component: TrekDetails
      },

      {
        path: 'bookings',
        component: MyBookings
      },

      {
        path: 'history',
        component: History
      },

      {
        path: 'profile',
        component: Profile
      }

    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  const role = localStorage.getItem('role')

  // Auto redirect logged-in users away from login/register
  if (
    token &&
    (
      to.path === '/' ||
      to.path === '/register'
    )
  ) {
    if (role === 'Admin') {
      next('/admin')
    } else if (role === 'Staff') {
      next('/staff/dashboard')
    } else if (role === 'Trekker') {
      next('/user/dashboard')
    } else {
      next('/')
    }

    return
  }

  // Check if route requires authentication
  const requiresAuth = to.matched.some(
    record => record.meta.requiresAuth
  )

  if (requiresAuth && !token) {
    next('/')
    return
  }

  // Get required role from matched routes
  const requiredRole = to.matched.find(
    record => record.meta.role
  )?.meta.role

  if (
    requiredRole &&
    role !== requiredRole
  ) {
    if (role === 'Admin') {
      next('/admin')
    } else if (role === 'Staff') {
      next('/staff/dashboard')
    } else if (role === 'Trekker') {
      next('/user/dashboard')
    } else {
      next('/')
    }

    return
  }

  next()
})

export default router
