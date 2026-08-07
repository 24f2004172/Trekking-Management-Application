<template>

<div>

    <h2>Dashboard</h2>

    <p class="text-muted">
        Welcome Administrator 👋
    </p>

    <DashboardCards :stats="dashboardData"/>

</div>

</template>

<script>

import DashboardCards from '../../components/admin/DashboardCards.vue'
import { getDashboardData } from '../../services/dashboardService'

export default {

  name: 'Dashboard',

  components: {
    DashboardCards
  },

  data () {
    return {
      dashboardData: {
        total_treks: 0,
        total_staff: 0,
        total_users: 0,
        total_bookings: 0
      }
    }
  },

  async mounted () {
    await this.loadDashboard()
  },

  methods: {

    async loadDashboard () {
      try {
        this.dashboardData = await getDashboardData()
      } catch (error) {
        console.error(error)
      }
    }

  }

}
</script>
