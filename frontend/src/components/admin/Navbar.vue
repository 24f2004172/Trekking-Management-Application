<template>

    <nav class="navbar navbar-light bg-white shadow-sm px-4">

        <h4 class="mb-0">
            Admin Dashboard
        </h4>

        <div>

            <strong>Admin</strong>

        </div>

        <button class="btn btn-outline-light w-100" @click="logout">
            Logout
        </button>

    </nav>

</template>

<script>

export default {

  name: 'Navbar',

  methods: {

    logout () {
      localStorage.clear()

      this.$router.push('/')
    }

  }

}

</script>
