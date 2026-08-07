<template>
  <div class="d-flex justify-content-between align-items-center mb-4">

    <div>
      <h2 class="mb-1">{{ title }}</h2>
      <p
        v-if="subtitle"
        class="text-muted mb-0"
      >
        {{ subtitle }}
      </p>
    </div>

    <button
      v-if="buttonText"
      class="btn btn-primary"
      @click="$emit('button-click')"
    >
      {{ buttonText }}
    </button>

  </div>
</template>

<script>
export default {
  name: 'PageHeader',

  props: {
    title: {
      type: String,
      required: true
    },

    subtitle: {
      type: String,
      default: ''
    },

    buttonText: {
      type: String,
      default: ''
    }
  }
}
</script>
