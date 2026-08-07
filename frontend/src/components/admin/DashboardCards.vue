<template>
  <div class="row">

    <div class="col-md-3 mb-3">
      <div class="card">
        <div class="card-body text-center">
          <h6>Total Treks</h6>
          <h2>{{ stats.total_treks }}</h2>
        </div>
      </div>
    </div>

    <div class="col-md-3 mb-3">
      <div class="card">
        <div class="card-body text-center">
          <h6>Total Staff</h6>
          <h2>{{ stats.total_staff }}</h2>
        </div>
      </div>
    </div>

    <div class="col-md-3 mb-3">
      <div class="card">
        <div class="card-body text-center">
          <h6>Total Users</h6>
          <h2>{{ stats.total_users }}</h2>
        </div>
      </div>
    </div>

    <div class="col-md-3 mb-3">
      <div class="card">
        <div class="card-body text-center">
          <h6>Total Bookings</h6>
          <h2>{{ stats.total_bookings }}</h2>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'DashboardCards',

  props: {
    stats: {
      type: Object,
      required: true
    }
  }
}
</script>
