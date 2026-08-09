<template>

<div class="card shadow-sm text-center">

    <div class="card-body">

        <h2>{{ value }}</h2>

        <h6 class="text-muted">
            {{ title }}
        </h6>

    </div>

</div>

</template>

<script>
export default {
  props: {
    title: String,
    value: [String, Number]
  }
}
</script>
