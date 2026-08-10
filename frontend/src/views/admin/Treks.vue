<template>
  <div>

    <PageHeader
      title="Trek Management"
      subtitle="Manage all trekking events"
      button-text="Add Trek"
      @button-click="openAddModal"
    />

    <SearchBar
      v-model="searchQuery"
      placeholder="Search Trek..."
    />

    <DataTable
      :columns="columns"
      :rows="filteredTreks"
    >
      <template v-slot:actions="{ row }">

        <button
          class="btn btn-sm btn-warning me-2"
          @click="openEditModal(row)"
        >
          Edit
        </button>

        <button
          class="btn btn-sm btn-danger"
          @click="removeTrek(row.id)"
        >
          Delete
        </button>

      </template>
    </DataTable>

    <!-- Trek Form Modal -->
    <TrekForm
      v-if="showModal"
      :trek="selectedTrek"
      :is-edit="isEdit"
      :staff-members="staffMembers"
      @close="showModal = false"
      @save="saveTrek"
    />

  </div>
</template>

<script>
import PageHeader from '../../components/common/PageHeader.vue'
import SearchBar from '../../components/common/SearchBar.vue'
import DataTable from '../../components/common/DataTable.vue'
import TrekForm from '../../components/admin/TrekForm.vue'

import {
  getAllTreks,
  addTrek,
  updateTrek,
  deleteTrek
} from '../../services/trekService'
import { getAllStaffs } from '../../services/staffService'

export default {
  name: 'Treks',

  components: {
    PageHeader,
    SearchBar,
    DataTable,
    TrekForm
  },

  data () {
    return {
      treks: [],

      staffMembers: [],

      searchQuery: '',

      showModal: false,

      isEdit: false,

      selectedTrek: {},

      columns: [
        {
          label: 'ID',
          key: 'id'
        },
        {
          label: 'Trek Name',
          key: 'trek_name'
        },
        {
          label: 'Location',
          key: 'location'
        },
        {
          label: 'Difficulty',
          key: 'difficulty'
        },
        {
          label: 'Slots',
          key: 'available_slots'
        },
        {
          label: 'Status',
          key: 'status'
        }
      ]
    }
  },

  computed: {
    filteredTreks () {
      return this.treks.filter(trek =>
        trek.trek_name
          .toLowerCase()
          .includes(this.searchQuery.toLowerCase())
      )
    }
  },

  async mounted () {
    await Promise.all([
      this.loadTreks(),
      this.loadStaff()
    ])
  },

  methods: {
    async loadTreks () {
      try {
        const response = await getAllTreks()

        this.treks = response.data
      } catch (error) {
        console.error(error)
      }
    },

    async loadStaff () {
      try {
        const response = await getAllStaffs()
        this.staffMembers = response.data || []
      } catch (error) {
        console.error(error)
      }
    },

    openAddModal () {
      this.selectedTrek = {}

      this.isEdit = false

      this.showModal = true
    },

    openEditModal (trek) {
      this.selectedTrek = { ...trek }

      this.isEdit = true

      this.showModal = true
    },

    async saveTrek (trekData) {
      try {
        if (this.isEdit) {
          await updateTrek(trekData.id, trekData)
        } else {
          await addTrek(trekData)
        }

        this.showModal = false

        await this.loadTreks()
      } catch (error) {
        console.error(error)
      }
    },

    async removeTrek (id) {
      const confirmed = window.confirm(
        'Are you sure you want to delete this trek?'
      )

      if (!confirmed) {
        return
      }

      try {
        await deleteTrek(id)

        await this.loadTreks()
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
