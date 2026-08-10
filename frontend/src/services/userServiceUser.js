const BASE_URL = 'http://127.0.0.1:5000/api/user'

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
    const error = new Error(
      data?.message || response.statusText || 'Request failed'
    )
    error.response = {
      data,
      status: response.status,
      statusText: response.statusText
    }
    throw error
  }

  return data
}

export async function getDashboard () {
  const response = await fetch(`${BASE_URL}/dashboard`, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function getTreks (params = {}) {
  const query = new URLSearchParams(params).toString()
  const url = query ? `${BASE_URL}/treks?${query}` : `${BASE_URL}/treks`

  const response = await fetch(url, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function getTrek (id) {
  const response = await fetch(`${BASE_URL}/trek/${id}`, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function createBooking (payload) {
  const response = await fetch(`${BASE_URL}/bookings`, {
    method: 'POST',
    headers: getHeaders(),
    body: JSON.stringify(payload)
  })

  return await handleResponse(response)
}

export async function getBookings () {
  const response = await fetch(`${BASE_URL}/bookings`, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function cancelBooking (id) {
  const response = await fetch(`${BASE_URL}/booking/${id}/cancel`, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function getHistory () {
  const response = await fetch(`${BASE_URL}/history`, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function getProfile () {
  const response = await fetch(`${BASE_URL}/profile`, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function updateProfile (payload) {
  const response = await fetch(`${BASE_URL}/profile`, {
    method: 'PUT',
    headers: getHeaders(),
    body: JSON.stringify(payload)
  })

  return await handleResponse(response)
}
