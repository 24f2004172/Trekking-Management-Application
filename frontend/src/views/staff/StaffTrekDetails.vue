<template>

<div class="container mt-4">

    <PageHeader
        title="Manage Trek"
        subtitle="Participants and Status"
    />

    <div class="card mb-4">

        <div class="card-body">

            <div v-if="trek" class="d-flex align-items-center gap-3 mb-3">

                <img
                    v-if="trek.image_url"
                    :src="trek.image_url"
                    alt="Trek image"
                    class="rounded"
                    style="width: 120px; height: 80px; object-fit: cover;"
                >

                <div>
                    <h5 class="mb-1">{{ trek.trek_name }}</h5>
                    <p class="text-muted mb-0">Current status: {{ selectedStatus }}</p>
                </div>

            </div>

            <label class="form-label">
                Trek Status
            </label>

            <select
                v-model="selectedStatus"
                class="form-select"
            >

                <option>Pending</option>
                <option>Approved</option>
                <option>Open</option>
                <option>Closed</option>
                <option>Completed</option>

            </select>

            <button
                class="btn btn-success mt-3"
                @click="putStatus"
            >
                Update Status
            </button>

        </div>

    </div>

    <DataTable
        :columns="participantColumns"
        :rows="participants"
    />

</div>

</template>

<script>

import {
  getTrekDetails,
  getParticipants,
  updateStatus
} from '@/services/staffServiceStaff'

import PageHeader from '@/components/common/PageHeader.vue'
import DataTable from '@/components/common/DataTable.vue'

export default {

  components: {
    PageHeader,
    DataTable
  },

  data () {
    return {

      trek: null,

      participants: [],

      selectedStatus: 'Open',

      participantColumns: [

        {
          key: 'name',
          label: 'Name'
        },

        {
          key: 'email',
          label: 'Email'
        },

        {
          key: 'phone',
          label: 'Phone'
        }

      ]

    }
  },

  methods: {

    async loadParticipants () {
      try {
        const trekId = this.$route.params.id

        const [trekData, participantData] = await Promise.all([
          getTrekDetails(trekId),
          getParticipants(trekId)
        ])

        this.trek = trekData
        this.participants = participantData
        this.selectedStatus = this.trek?.status || 'Open'
      } catch (err) {
        console.error(err)
      }
    },

    async putStatus () {
      try {
        const trekId = this.$route.params.id

        await updateStatus(
          trekId,
          this.selectedStatus
        )

        alert('Status Updated')
      } catch (err) {
        console.error(err)
      }
    }

  },

  mounted () {
    this.loadParticipants()
  }

}

</script>
