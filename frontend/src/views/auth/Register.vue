<template>

<div class="container">

    <div class="row vh-100 align-items-center justify-content-center">

        <div class="col-md-6">

            <div class="card shadow">

                <div class="card-body p-4">

                    <h2 class="text-center mb-4">
                        Create Account
                    </h2>

                    <form @submit.prevent="register">

                        <div class="mb-3">

                            <label>Name</label>

                            <input
                                type="text"
                                class="form-control"
                                v-model="form.name"
                                required
                            >

                        </div>

                        <div class="mb-3">

                            <label>Email</label>

                            <input
                                type="email"
                                class="form-control"
                                v-model="form.email"
                                required
                            >

                        </div>

                        <div class="mb-3">

                            <label>Phone</label>

                            <input
                                type="text"
                                class="form-control"
                                v-model="form.phone"
                                required
                            >

                        </div>

                        <div class="mb-4">

                            <label>Password</label>

                            <input
                                type="password"
                                class="form-control"
                                v-model="form.password"
                                required
                            >

                        </div>

                        <button
                            class="btn btn-success w-100"
                            :disabled="loading"
                        >
                            {{
                                loading
                                ? "Creating Account..."
                                : "Register"
                            }}
                        </button>

                    </form>

                    <hr>

                    <div class="text-center">

                        Already have an account?

                        <router-link to="/">
                            Login
                        </router-link>

                    </div>

                </div>

            </div>

        </div>

    </div>

</div>

</template>

<script>

import authService from '@/services/authService'

export default {

  name: 'Register',

  data () {
    return {

      loading: false,

      form: {

        name: '',

        email: '',

        phone: '',

        password: ''

      }

    }
  },

  methods: {

    async register () {
      try {
        this.loading = true

        const response =
                    await authService.register(
                      this.form
                    )

        alert(
          response.message
        )

        this.$router.push('/')
      } catch (error) {
        alert(
          error.response?.data?.message ||
                    error.message ||
                    'Registration Failed'
        )
      } finally {
        this.loading = false
      }
    }

  }

}

</script>

<style scoped>

.card{

    border:none;

    border-radius:16px;

}

</style>
