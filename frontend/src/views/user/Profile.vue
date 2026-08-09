<template>

<div class="container py-4">

    <div class="row justify-content-center">

        <div class="col-md-6">

            <div class="card shadow-sm border-0">

                <div class="card-body">

                    <h3 class="mb-4">
                        My Profile
                    </h3>

                    <div class="mb-3">

                        <label>Name</label>

                        <input
                            v-model="form.name"
                            class="form-control"
                        >

                    </div>

                    <div class="mb-3">

                        <label>Email</label>

                        <input
                            v-model="form.email"
                            class="form-control"
                            readonly
                        >

                    </div>

                    <div class="mb-3">

                        <label>Mobile</label>

                        <input
                            v-model="form.phone"
                            class="form-control"
                        >

                    </div>

                    <button
                        class="btn btn-success"
                        @click="updateProfile"
                    >
                        Update Profile
                    </button>

                </div>

            </div>

        </div>

    </div>

</div>

</template>

<script>

import {
  getProfile,
  updateProfile
} from '@/services/userServiceUser'

export default {

  data () {
    return {

      form: {}

    }
  },

  methods: {

    async loadProfile () {
      const response = await getProfile()

      this.form = response.data || []
    },

    async updateProfile () {
      await updateProfile(this.form)

      alert('Profile Updated')
    }

  },

  mounted () {
    this.loadProfile()
  }

}

</script>
