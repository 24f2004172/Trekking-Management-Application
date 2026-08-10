<template>
  <div>

    <PageHeader title="Booking Management" subtitle="Manage all bookings" />

    <SearchBar v-model="searchQuery" placeholder="Search booking..." />

    <DataTable :columns="columns" :rows="filteredBookings">
      <template v-slot:actions="{ row }">

        <button class="btn btn-warning btn-sm" @click="openEditModal(row)">
          Update
        </button>

      </template>
    </DataTable>

    <BookingForm v-if="showModal" :booking="selectedBooking" @close="showModal = false" @save="saveBooking" />

  </div>
</template>

<script>
import PageHeader from '../../components/common/PageHeader.vue'
import SearchBar from '../../components/common/SearchBar.vue'
import DataTable from '../../components/common/DataTable.vue'
import BookingForm from '../../components/admin/BookingForm.vue'

import {
  getAllBookings,
  updateBooking
} from '../../services/bookingService'

export default {
  name: 'Users',

  components: {
    PageHeader,
    SearchBar,
    DataTable,
    BookingForm
  },

  data () {
    return {
      bookings: [],

      showModal: false,

      searchQuery: '',

      selectedBooking: {},

      columns: [
        {
          label: 'ID',
          key: 'id'
        },
        {
          label: 'User',
          key: 'user_display'
        },
        {
          label: 'Trek',
          key: 'trek_display'
        },
        {
          label: 'People',
          key: 'number_of_people'
        },
        {
          label: 'Booking Status',
          key: 'booking_status'
        },
        {
          label: 'Payment Status',
          key: 'payment_status'
        }
      ]
    }
  },

  computed: {
    filteredBookings () {
      const query = this.searchQuery.toLowerCase()

      return this.bookings.filter(booking => {
        return [
          booking.id,
          booking.user_display,
          booking.trek_display
        ].some(value => String(value).toLowerCase().includes(query))
      })
    }
  },

  async mounted () {
    await this.loadBookings()
  },

  methods: {
    async loadBookings () {
      try {
        const response = await getAllBookings()

        this.bookings = response.data.map(booking => ({
          ...booking,
          user_display: `${booking.user_id} | ${booking.user_name || 'Unknown user'}`,
          trek_display: `${booking.trek_id} | ${booking.trek_name || 'Unknown trek'}`
        }))
      } catch (error) {
        console.error(error)
      }
    },

    openEditModal (booking) {
      this.selectedBooking = { ...booking }

      this.showModal = true
    },

    async saveBooking (bookingData) {
      await updateBooking(
        bookingData.id,
        bookingData
      )

      this.showModal = false

      await this.loadBookings()
    }
  }
}
</script>
