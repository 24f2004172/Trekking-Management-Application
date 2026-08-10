<template>

    <div class="container py-4">

        <div class="mb-4">

            <h2 class="fw-bold">
                My Bookings
            </h2>

            <button
                class="btn btn-success"
                @click="downloadCSV"
            >
                Export CSV
            </button>

            <p class="text-muted">
                Track all your trekking adventures
            </p>

        </div>

        <div v-if="loading" class="text-center py-5">
            <div class="spinner-border text-success" role="status"></div>
        </div>

        <div v-else-if="bookings.length === 0" class="text-center py-5">

            <h5>
                No Bookings Yet
            </h5>

            <p class="text-muted">
                Book your first trek and start exploring.
            </p>

            <router-link to="/user/treks" class="btn btn-success">
                Browse Treks
            </router-link>

        </div>

        <div v-else class="row">

            <div class="col-lg-4 col-md-6 mb-4" v-for="booking in bookings" :key="booking.id">

                <div class="card h-100 shadow-sm border-0 booking-card">

                    <img :src="booking.trek_image" class="card-img-top booking-image">

                    <div class="card-body">

                        <h5 class="fw-bold">
                            {{ booking.trek_name }}
                        </h5>

                        <p class="text-muted">
                            Booking Date:
                            {{
                                formatDate(
                                    booking.booking_date
                                )
                            }}
                        </p>

                        <p>
                            People:
                            <strong>
                                {{ booking.number_of_people }}
                            </strong>
                        </p>

                        <div class="mb-2">

                            <span class="badge me-2" :class="bookingStatusClass(
                                booking.booking_status
                            )
                                ">
                                {{ booking.booking_status }}
                            </span>

                            <span class="badge" :class="paymentStatusClass(
                                booking.payment_status
                            )
                                ">
                                {{ booking.payment_status }}
                            </span>

                            <button v-if="booking.booking_status === 'Booked'"
                                class="btn btn-outline-danger btn-sm mt-3" @click="cancelBooking(booking.id)">
                                Cancel Booking
                            </button>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>

</template>

<script>

import {
  getBookings,
  cancelBooking
} from '@/services/userServiceUser'
import { exportHistory } from '@/services/jobService'

export default {

  name: 'MyBookings',

  data () {
    return {

      bookings: [],

      loading: false

    }
  },

  methods: {

    async loadBookings () {
      try {
        this.loading = true

        const response = await getBookings()

        this.bookings = response.data || []
      } catch (error) {
        console.error(error)
      } finally {
        this.loading = false
      }
    },

    async downloadCSV () {
      try {
        const blob = await exportHistory()

        const url = window.URL.createObjectURL(blob)

        const link = document.createElement('a')

        link.href = url

        link.download = 'trek_history.csv'

        link.click()

        window.URL.revokeObjectURL(url)
      } catch (error) {
        console.log(error)
      }
    },

    async cancelBooking (id) {
      if (!confirm('Cancel this booking?')) return
      await cancelBooking(id)
      this.loadBookings()
    },

    formatDate (dateString) {
      return new Date(
        dateString
      ).toLocaleDateString()
    },

    bookingStatusClass (status) {
      if (status === 'Booked') { return 'bg-success' }

      if (status === 'Completed') { return 'bg-primary' }

      if (status === 'Cancelled') { return 'bg-danger' }

      return 'bg-secondary'
    },

    paymentStatusClass (status) {
      if (status === 'Paid') { return 'bg-success' }

      if (status === 'Pending') { return 'bg-warning text-dark' }

      return 'bg-secondary'
    }

  },

  mounted () {
    this.loadBookings()
  }

}

</script>

<style scoped>
.booking-card {
    transition: .3s;
}

.booking-card:hover {
    transform: translateY(-5px);
}

.booking-image {
    height: 220px;
    object-fit: cover;
}
</style>
