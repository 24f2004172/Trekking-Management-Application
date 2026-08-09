<template>

<div class="container mt-4">

    <PageHeader
        title="Manage Trek"
        subtitle="Participants and Status"
    />

    <div class="card mb-4">

        <div class="card-body">

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

        const data = await getParticipants(trekId)

        this.participants = data
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
