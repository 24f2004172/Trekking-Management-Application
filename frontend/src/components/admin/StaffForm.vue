<template>

<div class="modal-backdrop">

  <div class="modal-container">

    <div class="card">

      <div class="card-header d-flex justify-content-between">

        <h5>
          {{ isEdit ? 'Edit Staff' : 'Add Staff' }}
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
              Name
            </label>

            <input
              v-model="form.name"
              class="form-control"
              required
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              Email
            </label>

            <input
              v-model="form.email"
              class="form-control"
              required
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              Password
            </label>

            <input
              type="password"
              v-model="form.password"
              class="form-control"
              :required="!isEdit"
            >

          </div>

          <div class="mb-3">

            <label class="form-label">
              Phone
            </label>

            <input
              type="number"
              v-model.number="form.phone"
              class="form-control"
              required
            >

          </div>

          <div class="form-check mb-3">
            <input
                type="checkbox"
                v-model="form.is_active"
                class="form-check-input"
            >

            <label class="form-check-label">
                Active
            </label>
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

  name: 'StaffForm',

  props: {

    staff: {
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

      form: {
        id: null,
        name: '',
        email: '',
        password: '',
        phone: '',
        is_active: true
      }
    }
  },

  mounted () {
    if (this.isEdit) {
      this.form = {
        ...this.form,
        ...this.staff
      }

      this.form.password = ''
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
