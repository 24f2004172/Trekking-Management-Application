<template>

<div class="container py-4">

    <!-- Welcome -->

    <div class="mb-4">

        <h2 class="fw-bold">
            Welcome, Trekker 👋
        </h2>

        <p class="text-muted">
            Discover your next adventure
        </p>

    </div>

    <!-- Stats -->

    <div class="row mb-5">

        <div class="col-md-4 mb-3">

            <div class="card border-0 shadow-sm stat-card">

                <div class="card-body text-center">

                    <h2 class="fw-bold text-success">
                        {{ stats.available_treks }}
                    </h2>

                    <p class="mb-0 text-muted">
                        Available Treks
                    </p>

                </div>

            </div>

        </div>

        <div class="col-md-4 mb-3">

            <div class="card border-0 shadow-sm stat-card">

                <div class="card-body text-center">

                    <h2 class="fw-bold text-primary">
                        {{ stats.active_bookings }}
                    </h2>

                    <p class="mb-0 text-muted">
                        Active Bookings
                    </p>

                </div>

            </div>

        </div>

        <div class="col-md-4 mb-3">

            <div class="card border-0 shadow-sm stat-card">

                <div class="card-body text-center">

                    <h2 class="fw-bold text-warning">
                        {{ stats.completed_treks }}
                    </h2>

                    <p class="mb-0 text-muted">
                        Completed Treks
                    </p>

                </div>

            </div>

        </div>

    </div>

    <!-- Featured Treks -->

    <div class="d-flex justify-content-between align-items-center mb-3">

        <h4 class="fw-bold">
            Featured Treks
        </h4>

        <router-link
            to="/user/treks"
            class="btn btn-outline-success"
        >
            View All
        </router-link>

    </div>

    <div class="row mb-5">

        <div
            class="col-lg-4 col-md-6 mb-4"
            v-for="trek in featuredTreks"
            :key="trek.id"
        >

            <TrekCard :trek="trek" />

        </div>

    </div>

    <!-- Recent Bookings -->

    <div class="d-flex justify-content-between align-items-center mb-3">

        <h4 class="fw-bold">
            Recent Bookings
        </h4>

        <router-link
            to="/user/bookings"
            class="btn btn-outline-primary"
        >
            View All
        </router-link>

    </div>

    <div
        v-if="recentBookings.length === 0"
        class="card shadow-sm border-0"
    >

        <div class="card-body text-center">

            <p class="text-muted mb-0">
                No bookings yet
            </p>

        </div>

    </div>

    <div
        v-else
        class="row"
    >

        <div
            class="col-lg-4 col-md-6 mb-4"
            v-for="booking in recentBookings"
            :key="booking.id"
        >

            <div class="card border-0 shadow-sm booking-card">

                <img
                    :src="booking.trek_image"
                    class="card-img-top booking-image"
                >

                <div class="card-body">

                    <h5>
                        {{ booking.trek_name }}
                    </h5>

                    <p class="text-muted small">
                        {{ formatDate(booking.booking_date) }}
                    </p>

                    <span
                        class="badge"
                        :class="statusClass(booking.booking_status)"
                    >
                        {{ booking.booking_status }}
                    </span>

                </div>

            </div>

        </div>

    </div>

</div>

</template>

<script>

import {
  getDashboard
} from '@/services/userServiceUser'
import TrekCard from '@/components/user/TrekCard.vue'

export default {

  name: 'UserDashboard',

  components: {
    TrekCard
  },

  data () {
    return {

      stats: {

        available_treks: 0,

        active_bookings: 0,

        completed_treks: 0

      },

      featuredTreks: [],

      recentBookings: []

    }
  },

  methods: {

    async loadDashboard () {
      try {
        const response = await getDashboard()

        const data = response.data || []

        this.stats = data.stats

        this.featuredTreks = data.available_treks_list

        this.recentBookings = data.recent_bookings
      } catch (error) {
        console.error(error)
      }
    },

    formatDate (date) {
      return new Date(date)
        .toLocaleDateString()
    },

    statusClass (status) {
      if (status === 'Booked') { return 'bg-success' }

      if (status === 'Completed') { return 'bg-primary' }

      if (status === 'Cancelled') { return 'bg-danger' }

      return 'bg-secondary'
    }

  },

  mounted () {
    this.loadDashboard()
  }

}

</script>

<style scoped>

.stat-card{
    border-radius:16px;
}

.booking-card{
    transition:.3s;
}

.booking-card:hover{
    transform:translateY(-5px);
}

.booking-image{
    height:180px;
    object-fit:cover;
}

</style>
