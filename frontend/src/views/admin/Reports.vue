<template>
  <div>

    <h2>Reports</h2>

    <div class="row">

      <div class="col-md-3">
        <div class="card">
          <div class="card-body">
            <h5>Total Treks</h5>
            <h2>{{ total_treks }}</h2>
          </div>
        </div>
      </div>

      <div class="col-md-3">
        <div class="card">
          <div class="card-body">
            <h5>Total Staff</h5>
            <h2>{{ total_staff }}</h2>
          </div>
        </div>
      </div>

      <div class="col-md-3">
        <div class="card">
          <div class="card-body">
            <h5>Total Users</h5>
            <h2>{{ total_users }}</h2>
          </div>
        </div>
      </div>

      <div class="col-md-3">
        <div class="card">
          <div class="card-body">
            <h5>Total Bookings</h5>
            <h2>{{ total_bookings }}</h2>
          </div>
        </div>
      </div>

    </div>

  </div>
</template>

<script>

import { getDashboardData } from '../../services/dashboardService'

export default {
  data: function () {
    return {
      total_treks: 0,
      total_staff: 0,
      total_users: 0,
      total_bookings: 0
    }
  },

  async mounted () {
    await this.loadDashboard()
  },

  methods: {

    async loadDashboard () {
      try {
        const response = await getDashboardData()
        this.total_treks = response.data.total_treks || 0
        this.total_staff = response.data.total_staff || 0
        this.total_users = response.data.total_users || 0
        this.total_bookings = response.data.total_bookings || 0
      } catch (error) {
        console.error(error)
      }
    }

  }
}

</script>
