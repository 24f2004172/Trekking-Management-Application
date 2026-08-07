<template>
  <div class="admin-layout">

    <Sidebar />

    <div class="main-content">

      <Navbar />

      <div class="page-content">
        <router-view />
      </div>

    </div>

  </div>
</template>

<script>
import Sidebar from '../components/admin/Sidebar.vue'
import Navbar from '../components/admin/Navbar.vue'

export default {
  name: 'AdminLayout',

  components: {
    Sidebar,
    Navbar
  }
}
</script>

<style scoped>

.admin-layout{
  display:flex;
  min-height:100vh;
  background:#f5f7fa;
}

.main-content{
  flex:1;
  display:flex;
  flex-direction:column;
}

.page-content{
  padding:25px;
}

</style>
