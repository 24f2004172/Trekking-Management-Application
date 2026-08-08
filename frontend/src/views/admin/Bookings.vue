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
          label: 'User ID',
          key: 'user_id'
        },
        {
          label: 'Trek ID',
          key: 'trek_id'
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
      return this.bookings.filter(booking =>
        booking.id
          .toString()
          .includes(this.searchQuery)
      )
    }
  },

  async mounted () {
    await this.loadBookings()
  },

  methods: {
    async loadBookings () {
      try {
        const response = await getAllBookings()

        this.bookings = response.data
      } catch (error) {
        console.error(error)
      }
    },

    openEditModal (staff) {
      this.selectedBooking = { ...this.booking }

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
