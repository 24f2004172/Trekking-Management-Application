<template>
  <div class="container py-4" v-if="trek">

    <!-- Hero Section -->
    <div class="card border-0 shadow-lg overflow-hidden mb-4">

      <img
        :src="trek.image_url"
        class="hero-image"
        :alt="trek.trek_name"
      >

    </div>

    <!-- Trek Information -->

    <div class="row">

      <div class="col-lg-8">

        <div class="card shadow-sm border-0">

          <div class="card-body">

            <h2 class="fw-bold mb-3">
              {{ trek.trek_name }}
            </h2>

            <div class="mb-3">

              <span class="badge bg-success me-2">
                {{ trek.difficulty }}
              </span>

              <span class="badge bg-primary">
                {{ trek.duration }} Days
              </span>

            </div>

            <p class="fs-5">
              📍 {{ trek.location }}
            </p>

            <hr>

            <h5>Description</h5>

            <p class="text-muted">
              Experience the beauty of
              {{ trek.trek_name }}
              and explore breathtaking landscapes,
              mountain trails, and unforgettable views.
            </p>

          </div>

        </div>

      </div>

      <!-- Booking Panel -->

      <div class="col-lg-4">

        <div class="card shadow-sm border-0 sticky-top">

          <div class="card-body">

            <h4 class="fw-bold mb-3">
              Trek Booking
            </h4>

            <p>
              Available Slots:
              <strong class="text-success">
                {{ trek.available_slots }}
              </strong>
            </p>

            <p>
              Status:
              <span
                class="badge"
                :class="statusClass"
              >
                {{ trek.status }}
              </span>
            </p>

            <div class="mb-3">

              <label class="form-label">
                Number of People
              </label>

              <input
                v-model.number="numberOfPeople"
                type="number"
                min="1"
                :max="trek.available_slots"
                class="form-control"
              >

            </div>

            <button
              class="btn btn-success w-100"
              :disabled="bookingLoading"
              @click="bookTrek"
            >
              {{
                bookingLoading
                  ? 'Booking...'
                  : 'Book Trek'
              }}
            </button>

          </div>

        </div>

      </div>

    </div>

  </div>

  <div
    v-else
    class="text-center mt-5"
  >

    <div
      class="spinner-border text-success"
      role="status"
    ></div>

  </div>
</template>

<script>

import {
  getTrek,
  createBooking
} from '@/services/userServiceUser'

export default {

  name: 'TrekDetails',

  data () {
    return {

      trek: null,

      numberOfPeople: 1,

      bookingLoading: false

    }
  },

  computed: {

    statusClass () {
      if (this.trek?.status === 'Open') { return 'bg-success' }

      if (this.trek?.status === 'Closed') { return 'bg-warning text-dark' }

      return 'bg-secondary'
    }

  },

  methods: {

    async loadTrek () {
      try {
        const trekId =
          this.$route.params.id

        const response =
          await getTrek(trekId)

        this.trek =
          response.data || []
      } catch (error) {
        console.error(error)
      }
    },

    async bookTrek () {
      try {
        this.bookingLoading = true

        await createBooking({
          trek_id: this.trek.id,
          number_of_people:
            this.numberOfPeople
        })

        alert('Booking Successful!')

        // this.$router.push(
        //   '/user/bookings'
        // )
      } catch (error) {
        alert(
          error.response?.data?.message ||
          'Booking Failed'
        )
      } finally {
        this.bookingLoading = false
      }
    }

  },

  mounted () {
    this.loadTrek()
  }

}
</script>

<style scoped>

.hero-image{
  width:100%;
  height:450px;
  object-fit:cover;
}

</style>
