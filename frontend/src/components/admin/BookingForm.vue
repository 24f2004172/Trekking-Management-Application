<template>
  <div class="modal-backdrop">
    <div class="modal-container">

      <div class="card">

        <div class="card-header d-flex justify-content-between">
          <h5>Update Booking</h5>

          <button
            class="btn btn-sm btn-secondary"
            @click="$emit('close')"
          >
            X
          </button>
        </div>

        <div class="card-body">

          <div class="mb-3">
            <label class="form-label">
              Booking Status
            </label>

            <select
              v-model="form.booking_status"
              class="form-select"
            >
              <option value="Booked">Booked</option>
              <option value="Cancelled">Cancelled</option>
              <option value="Completed">Completed</option>
            </select>
          </div>

          <div class="mb-3">
            <label class="form-label">
              Payment Status
            </label>

            <select
              v-model="form.payment_status"
              class="form-select"
            >
              <option value="Pending">Pending</option>
              <option value="Paid">Paid</option>
              <option value="Failed">Failed</option>
            </select>
          </div>

          <button
            class="btn btn-primary"
            @click="submitForm"
          >
            Save
          </button>

          <button
            class="btn btn-secondary ms-2"
            @click="$emit('close')"
          >
            Cancel
          </button>

        </div>

      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'BookingForm',

  props: {
    booking: {
      type: Object,
      required: true
    }
  },

  data () {
    return {
      form: {
        id: this.booking.id,
        booking_status: this.booking.booking_status,
        payment_status: this.booking.payment_status
      }
    }
  },

  methods: {
    submitForm () {
      this.$emit('save', this.form)
    }
  }
}
</script>
