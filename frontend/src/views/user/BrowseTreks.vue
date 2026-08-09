<template>

<div class="container py-4">

    <div class="mb-4">

        <h2 class="fw-bold">
            Explore Treks
        </h2>

        <p class="text-muted">
            Find your next adventure
        </p>

    </div>

    <!-- Filters -->

    <div class="card shadow-sm border-0 mb-4">

        <div class="card-body">

            <div class="row g-3">

                <div class="col-md-4">

                    <input
                        v-model="search"
                        type="text"
                        class="form-control"
                        placeholder="Search Trek"
                    >

                </div>

                <div class="col-md-4">

                    <select
                        v-model="difficulty"
                        class="form-select"
                    >
                        <option value="">
                            All Difficulties
                        </option>

                        <option value="Easy">
                            Easy
                        </option>

                        <option value="Moderate">
                            Moderate
                        </option>

                        <option value="Hard">
                            Hard
                        </option>

                    </select>

                </div>

                <div class="col-md-4">

                    <input
                        v-model="location"
                        type="text"
                        class="form-control"
                        placeholder="Location"
                    >

                </div>

            </div>

        </div>

    </div>

    <!-- Loading -->

    <div
        v-if="loading"
        class="text-center"
    >
        <div
            class="spinner-border text-success"
            role="status"
        ></div>
    </div>

    <!-- Treks -->

    <div
        v-else
        class="row"
    >

        <div
            v-for="trek in filteredTreks"
            :key="trek.id"
            class="col-lg-4 col-md-6 mb-4"
        >

            <TrekCard
                :trek="trek"
            />

        </div>

    </div>

    <!-- Empty State -->

    <div
        v-if="!loading && filteredTreks.length === 0"
        class="text-center py-5"
    >

        <h5>
            No Treks Found
        </h5>

        <p class="text-muted">
            Try changing your filters.
        </p>

    </div>

</div>

</template>

<script>

import {
//   getDashboard,
  getTreks
//   getTrek,
//   createBooking,
//   getBookings,
//   getHistory,
//   getProfile,
//   updateProfile
} from '@/services/userServiceUser'

import TrekCard from '@/components/user/TrekCard.vue'

export default {

  name: 'BrowseTreks',

  components: {
    TrekCard
  },

  data () {
    return {

      treks: [],

      loading: false,

      search: '',

      difficulty: '',

      location: ''

    }
  },

  computed: {

    filteredTreks () {
      return this.treks.filter(trek => {
        const matchesSearch =
                    trek.trek_name
                      .toLowerCase()
                      .includes(
                        this.search.toLowerCase()
                      )

        const matchesDifficulty =
                    !this.difficulty ||
                    trek.difficulty === this.difficulty

        const matchesLocation =
                    !this.location ||
                    trek.location
                      .toLowerCase()
                      .includes(
                        this.location.toLowerCase()
                      )

        return (
          matchesSearch &&
                    matchesDifficulty &&
                    matchesLocation
        )
      })
    }

  },

  methods: {

    async loadTreks () {
      try {
        this.loading = true

        const response = await getTreks()

        this.treks = response.data || []
      } catch (error) {
        console.error(error)
      } finally {
        this.loading = false
      }
    }

  },

  mounted () {
    this.loadTreks()
  }

}

</script>
