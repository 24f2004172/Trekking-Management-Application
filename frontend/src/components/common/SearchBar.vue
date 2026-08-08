<template>
<div class="mb-3">

    <input
        :value="value"
        @input="$emit('input', $event.target.value)"
        class="form-control"
        :placeholder="placeholder"
    >

</div>
</template>

<script>

export default {

  name: 'SearchBar',

  props: {

    value: {

      type: String,

      default: ''

    },

    placeholder: {

      type: String,

      default: 'Search...'

    }

  }

}

</script>
