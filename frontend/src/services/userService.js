const BASE_URL = 'http://127.0.0.1:5000/api/admin/users'

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

export async function getAllUsers () {
  const response = await fetch(BASE_URL, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function updateUserStatus (id, isActive) {
  const response = await fetch(
    `http://127.0.0.1:5000/api/admin/user/${id}`,
    {
      method: 'PUT',
      headers: getHeaders(),
      body: JSON.stringify({
        is_active: isActive
      })
    }
  )

  return await handleResponse(response)
}
