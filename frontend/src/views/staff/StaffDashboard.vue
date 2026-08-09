<template>

<div class="container mt-4">

    <PageHeader
        title="Staff Dashboard"
        subtitle="Manage assigned treks"
    />

    <SearchBar
        v-model="search"
        placeholder="Search Trek..."
    />

    <DataTable
        :columns="columns"
        :rows="filteredTreks"
    >

        <template #actions="{ row }">

            <router-link
                :to="`/staff/trek/${row.id}`"
                class="btn btn-sm btn-primary"
            >
                Manage
            </router-link>

        </template>

    </DataTable>

</div>

</template>

<script>

import {
  getDashboard
} from '@/services/staffServiceStaff'

import PageHeader from '@/components/common/PageHeader.vue'
import SearchBar from '@/components/common/SearchBar.vue'
import DataTable from '@/components/common/DataTable.vue'

export default {

  components: {
    PageHeader,
    SearchBar,
    DataTable
  },

  data () {
    return {

      search: '',

      treks: [],

      columns: [

        {
          key: 'trek_name',
          label: 'Trek'
        },

        {
          key: 'registered_users',
          label: 'Registered Users'
        },

        {
          key: 'available_slots',
          label: 'Available Slots'
        },

        {
          key: 'status',
          label: 'Status'
        }

      ]

    }
  },

  computed: {

    filteredTreks () {
      return this.treks.filter(trek =>
        trek.trek_name
          .toLowerCase()
          .includes(this.search.toLowerCase())
      )
    }

  },

  async mounted () {
    try {
      const data = await getDashboard()

      this.treks = data
    } catch (err) {
      console.error(err)
    }
  }

}

</script>
