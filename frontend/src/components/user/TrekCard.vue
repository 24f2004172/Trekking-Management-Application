<template>
  <div class="card trek-card h-100 shadow-sm border-0">

    <img
      :src="trek.image_url"
      class="card-img-top trek-image"
      :alt="trek.trek_name"
    />

    <div class="card-body d-flex flex-column">

      <h5 class="fw-bold mb-2">
        {{ trek.trek_name }}
      </h5>

      <p class="text-muted mb-2">
        📍 {{ trek.location }}
      </p>

      <div class="mb-3">

        <span class="badge bg-success me-2">
          {{ trek.difficulty }}
        </span>

        <span class="badge bg-primary">
          {{ trek.duration }} Days
        </span>

      </div>

      <div class="mb-3">

        <small class="text-muted">
          Available Slots
        </small>

        <h6 class="fw-bold text-success">
          {{ trek.available_slots }}
        </h6>

      </div>

      <router-link
        :to="`/user/trek/${trek.id}`"
        class="btn btn-outline-success mt-auto"
      >
        View Details
      </router-link>

    </div>

  </div>
</template>

<script>
export default {
  name: 'TrekCard',

  props: {
    trek: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>

.trek-card{
  transition: all 0.3s ease;
  border-radius: 15px;
  overflow: hidden;
}

.trek-card:hover{
  transform: translateY(-6px);
}

.trek-image{
  height: 220px;
  object-fit: cover;
}

</style>
