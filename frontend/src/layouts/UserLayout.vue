<template>

    <div class="d-flex">

        <!-- Sidebar -->

        <div class="sidebar">

            <div class="sidebar-header">

                <h4 class="fw-bold text-white">
                    🏔 TrekMate
                </h4>

            </div>

            <ul class="nav flex-column mt-4">

                <li class="nav-item">

                    <router-link to="/user/dashboard" class="nav-link">
                        <i class="bi bi-speedometer2 me-2"></i>
                        Dashboard
                    </router-link>

                </li>

                <li class="nav-item">

                    <router-link to="/user/treks" class="nav-link">
                        <i class="bi bi-map me-2"></i>
                        Browse Treks
                    </router-link>

                </li>

                <li class="nav-item">

                    <router-link to="/user/bookings" class="nav-link">
                        <i class="bi bi-journal-check me-2"></i>
                        My Bookings
                    </router-link>

                </li>

                <li class="nav-item">

                    <router-link to="/user/history" class="nav-link">
                        <i class="bi bi-clock-history me-2"></i>
                        History
                    </router-link>

                </li>

                <li class="nav-item">

                    <router-link to="/user/profile" class="nav-link">
                        <i class="bi bi-person me-2"></i>
                        Profile
                    </router-link>

                </li>

            </ul>

            <div class="sidebar-footer mt-auto pt-4">

                <button class="btn btn-outline-light w-100" @click="logout">
                    Logout
                </button>

            </div>

        </div>

        <!-- Main Content -->

        <div class="content-area">

            <router-view />

        </div>

    </div>

</template>

<script>
export default {
  methods: {

    logout () {
      localStorage.clear()

      this.$router.push('/login')
    }

  }
}
</script>

<style scoped>
.sidebar {

    width: 260px;

    min-height: 100vh;

    background: linear-gradient(180deg,
            #198754,
            #157347);

    padding: 20px;

    position: fixed;

}

.sidebar-header {

    text-align: center;

    padding-bottom: 15px;

    border-bottom: 1px solid rgba(255,
            255,
            255,
            0.2);

}

.nav-link {

    color: white;

    margin-bottom: 10px;

    border-radius: 10px;

    padding: 12px;

    transition: 0.3s;

}

.nav-link:hover {

    background-color: rgba(255,
            255,
            255,
            0.15);

    color: white;

}

.router-link-active {

    background-color: white;

    color: #198754 !important;

    font-weight: bold;

}

.content-area {

    margin-left: 260px;

    width: calc(100% - 260px);

    min-height: 100vh;

    background-color: #f8f9fa;

    padding: 30px 25px;

}

.sidebar {
    display: flex;
    flex-direction: column;
}

.sidebar-footer {
    margin-top: auto;
}
</style>
