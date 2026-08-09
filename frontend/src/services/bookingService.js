const BASE_URL = 'http://127.0.0.1:5000/api/admin/bookings'

function getHeaders () {
  return {
    'Content-Type': 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjI2NTY4NywianRpIjoiMDRmMWZiMWYtMzdkZS00MDMxLWJkNTQtOTMxOTkyMmQxOGQwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYyNjU2ODcsImNzcmYiOiJkMzYyMDMwOS0xNGE0LTQ3YzYtOTBmMy1kM2NjYjg1MGI0YzIiLCJleHAiOjE3ODYzNTIwODcsInJvbGUiOiJBZG1pbiJ9.g_C---AyTiRSrfLW1KJVbQotQDpRmvMUTs9thC05eV8'
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
