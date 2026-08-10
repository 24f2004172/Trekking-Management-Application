<template>
  <div class="notification-menu">
    <button
      type="button"
      class="btn btn-outline-secondary notification-button"
      aria-label="Show unread notifications"
      :aria-expanded="isOpen.toString()"
      @click="toggleNotifications"
    >
      <span aria-hidden="true">&#128276;</span>
      <span
        v-if="unreadNotifications.length"
        class="badge rounded-pill bg-danger notification-count"
      >
        {{ unreadNotifications.length }}
      </span>
    </button>

    <div
      v-if="isOpen"
      class="card shadow notification-dropdown"
    >
      <div class="card-header fw-bold">Unread notifications</div>

      <div
        v-if="loading"
        class="p-3 text-muted small"
      >
        Loading notifications...
      </div>

      <div
        v-else-if="error"
        class="p-3 text-danger small"
      >
        Unable to load notifications.
      </div>

      <ul
        v-else-if="unreadNotifications.length"
        class="list-group list-group-flush"
      >
        <li
          v-for="item in unreadNotifications"
          :key="item.id"
          class="list-group-item notification-item"
          role="button"
          tabindex="0"
          @click="markAsRead(item)"
          @keydown.enter="markAsRead(item)"
          @keydown.space.prevent="markAsRead(item)"
        >
          {{ item.message }}
        </li>
      </ul>

      <div
        v-else
        class="p-3 text-muted small"
      >
        No unread notifications.
      </div>
    </div>
  </div>
</template>

<script>

import {
  getNotifications,
  markNotificationAsRead
} from '@/services/jobService'

export default {
  name: 'NotificationPanel',

  data () {
    return {
      notifications: [],
      isOpen: false,
      loading: false,
      error: false
    }
  },

  computed: {
    unreadNotifications () {
      return this.notifications.filter(notification => !notification.is_read)
    }
  },

  methods: {
    async loadNotifications () {
      this.loading = true
      this.error = false

      try {
        const response = await getNotifications()
        this.notifications = Array.isArray(response)
          ? response
          : response.data || []
      } catch (error) {
        this.error = true
        console.error(error)
      } finally {
        this.loading = false
      }
    },

    async toggleNotifications () {
      this.isOpen = !this.isOpen

      if (this.isOpen) {
        await this.loadNotifications()
      }
    },

    async markAsRead (notification) {
      try {
        await markNotificationAsRead(notification.id)
        notification.is_read = true
      } catch (error) {
        console.error(error)
      }
    }
  },

  mounted () {
    this.loadNotifications()
  }
}

</script>

<style scoped>
.notification-menu {
  position: relative;
}

.notification-button {
  position: relative;
  font-size: 1.2rem;
  line-height: 1;
}

.notification-count {
  position: absolute;
  top: -0.45rem;
  right: -0.5rem;
  font-size: 0.65rem;
}

.notification-dropdown {
  position: absolute;
  z-index: 1050;
  top: calc(100% + 0.5rem);
  right: 0;
  width: min(22rem, calc(100vw - 2rem));
}

.notification-item {
  cursor: pointer;
}
</style>
