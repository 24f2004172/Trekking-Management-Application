const BASE_URL = 'http://127.0.0.1:5000/api/admin/bookings'

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

export async function getAllBookings () {
  const response = await fetch(BASE_URL, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function updateBooking (id, bookingData) {
  const response = await fetch(
    `http://127.0.0.1:5000/api/admin/booking/${id}`,
    {
      method: 'PUT',
      headers: getHeaders(),
      body: JSON.stringify(bookingData)
    }
  )

  return await handleResponse(response)
}
