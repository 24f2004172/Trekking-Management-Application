<template>
  <div>

    <PageHeader title="Staff Management" subtitle="Manage all staffs" button-text="Add Staff"
      @button-click="openAddModal" />

    <SearchBar v-model="searchQuery" placeholder="Search Staff..." />

    <DataTable :columns="columns" :rows="filteredStaff">
      <template v-slot:actions="{ row }">

        <button class="btn btn-sm btn-warning me-2" @click="openEditModal(row)">
          Edit
        </button>

        <button class="btn btn-sm btn-danger" @click="removeStaff(row.id)">
          Delete
        </button>

      </template>
    </DataTable>

    <!-- Staff Form Modal -->
    <StaffForm v-if="showModal" :staff="selectedStaff" :is-edit="isEdit" @close="showModal = false" @save="saveStaff" />

  </div>
</template>

<script>
import PageHeader from '../../components/common/PageHeader.vue'
import SearchBar from '../../components/common/SearchBar.vue'
import DataTable from '../../components/common/DataTable.vue'
import StaffForm from '../../components/admin/StaffForm.vue'

import {
  getAllStaffs,
  addStaff,
  updateStaff,
  deleteStaff
} from '../../services/staffService'

export default {
  name: 'Staff',

  components: {
    PageHeader,
    SearchBar,
    DataTable,
    StaffForm
  },

  data () {
    return {
      staff: [],

      searchQuery: '',

      showModal: false,

      isEdit: false,

      selectedStaff: {},

      columns: [
        {
          label: 'ID',
          key: 'id'
        },
        {
          label: 'Name',
          key: 'name'
        },
        {
          label: 'Email',
          key: 'email'
        },
        {
          label: 'Phone',
          key: 'phone'
        },
        {
          label: 'Status',
          key: 'is_active'
        }
      ]
    }
  },

  computed: {
    filteredStaff () {
      return this.staff.filter(staff =>
        staff.name
          .toLowerCase()
          .includes(this.searchQuery.toLowerCase())
      )
    }
  },

  async mounted () {
    await this.loadStaff()
  },

  methods: {
    async loadStaff () {
      try {
        const response = await getAllStaffs()

        this.staff = response.data
      } catch (error) {
        console.error(error)
      }
    },

    openAddModal () {
      this.selectedStaff = {}

      this.isEdit = false

      this.showModal = true
    },

    openEditModal (staff) {
      this.selectedStaff = { ...staff }

      this.isEdit = true

      this.showModal = true
    },

    async saveStaff (staffData) {
      try {
        if (this.isEdit) {
          await updateStaff(staffData.id, staffData)
        } else {
          await addStaff(staffData)
        }

        this.showModal = false

        await this.loadStaff()
      } catch (error) {
        console.error(error)
      }
    },

    async removeStaff (id) {
      const confirmed = window.confirm(
        'Are you sure you want to delete this trek?'
      )

      if (!confirmed) {
        return
      }

      try {
        await deleteStaff(id)

        await this.loadStaff()
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
