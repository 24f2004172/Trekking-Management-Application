<template>

<div class="sidebar">

    <h3 class="logo">
        Trek Manager
    </h3>

    <ul>
        <li v-for="item in menuItems" :key="item.path">
            <router-link :to="item.path">
                {{ item.name }}
            </router-link>
        </li>

        <div class="sidebar-footer mt-auto pt-4 text-center">
            <button class="btn btn-outline-light w-10" @click="logout">
                Logout
            </button>
        </div>
    </ul>

</div>

</template>

<script>

export default {

  name: 'Sidebar',
  data () {
    return {
      menuItems: [
        { name: 'Dashboard', path: '/admin' },
        { name: 'Treks', path: '/admin/treks' },
        { name: 'Staff', path: '/admin/staff' },
        { name: 'Users', path: '/admin/users' },
        { name: 'Bookings', path: '/admin/bookings' },
        { name: 'Reports', path: '/admin/reports' }
      ]
    }
  },

  methods: {
    logout () {
      localStorage.clear()
      this.$router.push('/')
    }
  }
}

</script>

<style scoped>

.sidebar{

    width:250px;

    background:#212529;

    color:white;

    min-height:100vh;

}

.logo{

    text-align:center;

    padding:20px;

}

ul{

    list-style:none;

    padding:0;

}

li{

    padding:15px 25px;

}

a{

    color:white;

    text-decoration:none;

    display:block;

}

.router-link-exact-active{

    background:#0d6efd;

    border-radius:5px;

}

</style>
