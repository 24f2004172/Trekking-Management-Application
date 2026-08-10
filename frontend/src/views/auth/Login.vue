<template>

<div class="container">

    <div class="row vh-100 align-items-center justify-content-center">

        <div class="col-md-5">

            <div class="card shadow">

                <div class="card-body p-4">

                    <h2 class="text-center mb-4">
                        TrekMate Login
                    </h2>

                    <form @submit.prevent="login">

                        <div class="mb-3">

                            <label>Email</label>

                            <input
                                type="email"
                                class="form-control"
                                v-model="email"
                                required
                            >

                        </div>

                        <div class="mb-3">

                            <label>Password</label>

                            <input
                                type="password"
                                class="form-control"
                                v-model="password"
                                required
                            >

                        </div>

                        <button
                            class="btn btn-success w-100"
                            :disabled="loading"
                        >

                            {{
                                loading
                                ? "Logging In..."
                                : "Login"
                            }}

                        </button>

                        <hr>

                        <div class="text-center">

                          Don't have an account?

                          <router-link to="/register">
                            Register
                          </router-link>

                        </div>

                    </form>

                </div>

            </div>

        </div>

    </div>

</div>

</template>

<script>
import {
  login
} from '@/services/authService'

export default {
  data () {
    return {
      email: '',
      password: ''
    }
  },

  methods: {
    async login () {
      try {
        const response = await login({
          email: this.email,
          password: this.password
        })

        localStorage.setItem(
          'token',
          response.token
        )

        localStorage.setItem(
          'role',
          response.user.role
        )

        localStorage.setItem(
          'user',
          JSON.stringify(
            response.user
          )
        )

        const role = response.user.role

        if (role === 'Admin') {
          this.$router.push(
            '/admin'
          )
        } else if (role === 'Staff') {
          this.$router.push(
            '/staff/dashboard'
          )
        } else {
          this.$router.push(
            '/user/dashboard'
          )
        }
      } catch (error) {
        alert(
          'Invalid Credentials'
        )
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
