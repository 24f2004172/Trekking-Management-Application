<template>
  <div>

    <PageHeader title="User Management" subtitle="Manage all users" />

    <SearchBar v-model="searchQuery" placeholder="Search user..." />

    <DataTable :columns="columns" :rows="filteredUsers">
      <template v-slot:actions="{ row }">

        <button v-if="row.is_active" class="btn btn-warning btn-sm" @click="toggleStatus(row)">
          Deactivate
        </button>

        <button v-else class="btn btn-success btn-sm" @click="toggleStatus(row)">
          Activate
        </button>

      </template>
    </DataTable>

  </div>
</template>

<script>
import PageHeader from '../../components/common/PageHeader.vue'
import SearchBar from '../../components/common/SearchBar.vue'
import DataTable from '../../components/common/DataTable.vue'

import {
  getAllUsers,
  updateUserStatus
} from '../../services/userService'

export default {
  name: 'Users',

  components: {
    PageHeader,
    SearchBar,
    DataTable
  },

  data () {
    return {
      users: [],

      searchQuery: '',

      selectedUsers: {},

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
          label: 'Role',
          key: 'role'
        }
      ]
    }
  },

  computed: {
    filteredUsers () {
      return this.users.filter(user =>
        user.name
          .toLowerCase()
          .includes(this.searchQuery.toLowerCase())
      )
    }
  },

  async mounted () {
    await this.loadUsers()
  },

  methods: {
    async loadUsers () {
      try {
        const response = await getAllUsers()

        this.users = response.data
      } catch (error) {
        console.error(error)
      }
    },

    async toggleStatus (user) {
      try {
        await updateUserStatus(
          user.id,
          !user.is_active
        )

        await this.loadUsers()
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
