const BASE_URL = 'http://127.0.0.1:5000/api'

function getHeaders () {
  const token = localStorage.getItem('token')
  return {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${token}`
  }
}

async function handleResponse (response) {
  const data = await response.json().catch(() => null)

  if (!response.ok) {
    const error = new Error(data?.message || response.statusText || 'Request failed')
    error.response = { data, status: response.status, statusText: response.statusText }
    throw error
  }

  return data
}

export async function sendReminders () {
  const response = await fetch(`${BASE_URL}/admin/send-reminders`, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function getMonthlyReport () {
  const response = await fetch(`${BASE_URL}/admin/monthly-report`, {
    headers: getHeaders()
  })

  if (!response.ok) {
    await handleResponse(response)
  }

  return await response.text()
}

export async function exportHistory () {
  const response = await fetch(`${BASE_URL}/user/export-history`, {
    headers: getHeaders()
  })

  if (!response.ok) {
    await handleResponse(response)
  }

  return await response.blob()
}

export async function getNotifications () {
  const response = await fetch(`${BASE_URL}/user/notifications`, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function markNotificationAsRead (notificationId) {
  const response = await fetch(
    `${BASE_URL}/user/notifications/${notificationId}/read`,
    {
      method: 'PATCH',
      headers: getHeaders()
    }
  )

  return await handleResponse(response)
}
