<template>

<div class="container py-4">

    <h2 class="fw-bold mb-4">
        Trek History
    </h2>

    <div
        v-if="history.length === 0"
        class="text-center py-5"
    >
        <h5>No completed treks yet</h5>
    </div>

    <div class="row">

        <div
            class="col-lg-4 mb-4"
            v-for="item in history"
            :key="item.id"
        >

            <div class="card shadow-sm border-0">

                <img
                    :src="item.trek_image"
                    class="history-image"
                >

                <div class="card-body">

                    <h5>
                        {{ item.trek_name }}
                    </h5>

                    <span
                        class="badge bg-success"
                    >
                        Completed
                    </span>

                </div>

            </div>

        </div>

    </div>

</div>

</template>

<script>

import {
  getHistory
} from '@/services/userServiceUser'

export default {

  data () {
    return {

      history: []

    }
  },

  async mounted () {
    const response = await getHistory()

    this.history = response.data || []
  }

}

</script>

<style scoped>

.history-image{

    height:220px;
    object-fit:cover;

}

</style>
