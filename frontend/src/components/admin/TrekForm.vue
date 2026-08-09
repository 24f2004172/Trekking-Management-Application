<template>

<div class="modal-backdrop">

  <div class="modal-container">

    <div class="card">

      <div class="card-header d-flex justify-content-between">

        <h5>
          {{ isEdit ? 'Edit Trek' : 'Add Trek' }}
        </h5>

        <button
          class="btn btn-sm btn-secondary"
          @click="$emit('close')"
        >
          X
        </button>

      </div>

      <div class="card-body">

        <form @submit.prevent="submitForm">

          <div class="mb-3">

            <label class="form-label">
              Trek Name
            </label>

            <input
              v-model="form.trek_name"
              class="form-control"
              required
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              Location
            </label>

            <input
              v-model="form.location"
              class="form-control"
              required
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              Description
            </label>

            <textarea
              v-model="form.description"
              class="form-control"
            />
          </div>

          <div class="mb-3">

            <label class="form-label">
              Difficulty
            </label>

            <select
              v-model="form.difficulty"
              class="form-select"
              required
            >
              <option value="">
                Select Difficulty
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

          <div class="mb-3">

            <label class="form-label">
              Duration (Days)
            </label>

            <input
              type="number"
              v-model.number="form.duration"
              class="form-control"
              required
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              Total Slots
            </label>

            <input
              type="number"
              v-model.number="form.total_slots"
              class="form-control"
              required
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              Available Slots
            </label>

            <input
              type="number"
              v-model.number="form.available_slots"
              class="form-control"
              required
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              Assigned Staff ID
            </label>

            <input
              type="number"
              v-model.number="form.assigned_staff_id"
              class="form-control"
              required
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              Start Date
            </label>

            <input
              type="date"
              v-model="form.start_date"
              class="form-control"
              required
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              End Date
            </label>

            <input
              type="date"
              v-model="form.end_date"
              class="form-control"
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              Trek Image
            </label>

            <select
              v-model="form.image_url"
              class="form-select"
              required
            >
              <option value="">
                Select Image
              </option>

              <option
                v-for="image in imageOptions"
                :key="image.value"
                :value="image.value"
              >
                {{ image.label }}
              </option>

            </select>

            <div
              v-if="form.image_url"
              class="mt-2"
            >
              <img
                :src="form.image_url"
                alt="Selected trek image"
                class="img-fluid rounded"
                style="max-height: 140px; object-fit: cover;"
              >
            </div>

          </div>

          <div class="mb-3">

            <label class="form-label">
              Status
            </label>

            <select
              v-model="form.status"
              class="form-select"
            >
              <option value="">
                Select Status
              </option>

              <option value="Pending">
                Pending
              </option>

              <option value="Approved">
                Approved
              </option>

              <option value="Open">
                Open
              </option>

              <option value="Closed">
                Closed
              </option>

              <option value="Completed">
                Completed
              </option>

            </select>

          </div>

          <button
            class="btn btn-primary"
            type="submit"
          >
            Save
          </button>

          <button
            class="btn btn-secondary ms-2"
            type="button"
            @click="$emit('close')"
          >
            Cancel
          </button>

        </form>

      </div>

    </div>

  </div>

</div>

</template>

<script>

export default {

  name: 'TrekForm',

  props: {

    trek: {
      type: Object,
      default: () => ({})
    },

    isEdit: {
      type: Boolean,
      default: false
    }

  },

  data () {
    return {

      imageOptions: [
        { label: 'Hampta', value: '/images/hampta.jpg' },
        { label: 'Beach', value: '/images/beach.jpg' },
        { label: 'Everest', value: '/images/everest.jpg' },
        { label: 'Jagannath', value: '/images/jagannath.jpg' },
        { label: 'Jaipur', value: '/images/jaipur.jpg' },
        { label: 'Kedarnath', value: '/images/kedarnath.jpg' },
        { label: 'Rameshwaram', value: '/images/rameshwaram.jpg' },
        { label: 'Roopkund', value: '/images/roopkund.jpg' },
        { label: 'Valley of Flowers', value: '/images/valley-of-flowers.jpg' }
      ],

      form: {
        id: null,
        trek_name: '',
        location: '',
        description: '',
        difficulty: '',
        duration: null,
        total_slots: null,
        available_slots: null,
        assigned_staff_id: null,
        start_date: '',
        end_date: '',
        image_url: '/images/hampta.jpg',
        status: ''
      }

    }
  },

  mounted () {
    if (this.isEdit) {
      this.form = {
        ...this.form,
        ...this.trek,
        image_url: this.trek.image_url || '/images/hampta.jpg'
      }

      if (this.form.start_date) {
        this.form.start_date =
          this.form.start_date.substring(0, 10)
      }

      if (this.form.end_date) {
        this.form.end_date =
          this.form.end_date.substring(0, 10)
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

<style scoped>

.modal-backdrop {

  position: fixed;

  top: 0;

  left: 0;

  width: 100%;

  height: 100%;

  background: rgba(0,0,0,0.5);

  display: flex;

  justify-content: center;

  align-items: center;

}

.modal-container {

  width: 700px;

  max-height: 90vh;

  overflow-y: auto;

}

</style>
