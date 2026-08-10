<template>

<div class="container-fluid py-4">

    <div class="dashboard-header d-flex flex-wrap justify-content-between align-items-center gap-3 mb-4 p-4">

      <div>
        <p class="text-uppercase small fw-bold mb-1 dashboard-kicker">Administration</p>
        <h2 class="fw-bold mb-1">Dashboard</h2>
        <p class="mb-0 text-muted">Welcome back, Administrator 👋</p>
      </div>

      <div class="d-flex flex-wrap gap-2">
        <button
          class="btn btn-primary"
          :disabled="sendingReminders"
          @click="triggerReminder"
        >
          {{ sendingReminders ? 'Sending...' : 'Send Daily Reminders' }}
        </button>

        <button
          class="btn btn-outline-warning"
          :disabled="loadingReport"
          @click="openReport"
        >
          {{ loadingReport ? 'Opening report...' : 'Monthly Report' }}
        </button>
      </div>

    </div>

    <DashboardCards :stats="dashboardData" />

</div>

</template>

<script>

import DashboardCards from '../../components/admin/DashboardCards.vue'
import { getDashboardData } from '../../services/dashboardService'
import {
  getMonthlyReport,
  sendReminders
}
  from '@/services/jobService'

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
      },
      sendingReminders: false,
      loadingReport: false
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
    },

    async triggerReminder () {
      try {
        this.sendingReminders = true
        const response = await sendReminders()
        alert(`${response.sent_count} user reminders sent.`)
      } catch (error) {
        alert(error.message || 'Unable to send reminders.')
      } finally {
        this.sendingReminders = false
      }
    },

    async openReport () {
      const reportWindow = window.open('', '_blank')

      if (!reportWindow) {
        alert('Please allow pop-ups to view the monthly report.')
        return
      }

      try {
        this.loadingReport = true
        reportWindow.document.write('<p>Loading monthly report...</p>')

        const report = await getMonthlyReport()
        reportWindow.document.open()
        reportWindow.document.write(report)
        reportWindow.document.close()
      } catch (error) {
        reportWindow.close()
        alert(error.message || 'Unable to load the monthly report.')
      } finally {
        this.loadingReport = false
      }
    }

  }

}
</script>

<style scoped>
.dashboard-header {
  background: linear-gradient(135deg, #effaf3, #ffffff);
  border: 1px solid #d7eee0;
  border-radius: 1rem;
}

.dashboard-kicker {
  color: #198754;
  letter-spacing: 0.08em;
}
</style>
