import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '../views/auth/Login.vue'

import AdminLayout from '../layouts/AdminLayout.vue'

import Dashboard from '../views/admin/Dashboard.vue'
import Treks from '../views/admin/Treks.vue'
import Staff from '../views/admin/Staff.vue'
import Users from '../views/admin/Users.vue'
import Bookings from '../views/admin/Bookings.vue'
import Reports from '../views/admin/Reports.vue'

import StaffDashboard from '@/views/staff/StaffDashboard.vue'
import StaffTrekDetails from '@/views/staff/StaffTrekDetails.vue'

Vue.use(VueRouter)

const routes = [

  {
    path: '/',
    component: Login
  },

  {
    path: '/admin',
    component: AdminLayout,

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
    component: StaffDashboard
  },
  {
    path: '/staff/trek/:id',
    name: 'StaffTrekDetails',
    component: StaffTrekDetails
  }
]

export default new VueRouter({

  mode: 'history',

  routes

})
