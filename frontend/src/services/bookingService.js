const BASE_URL = 'http://127.0.0.1:5000/api/admin/bookings'

function getHeaders () {
  return {
    'Content-Type': 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjIwNTA5MiwianRpIjoiNmQ2YzJmYmYtMTZkYi00ODllLThlM2YtMjI2N2VkNzc1NzM3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYyMDUwOTIsImNzcmYiOiJmZDY5OGVjNi0yOTE5LTQ5MWEtOTNiMy1lMGFjY2RjYmYwMzMiLCJleHAiOjE3ODYyMzM4OTIsInJvbGUiOiJBZG1pbiJ9.SHLjc4LIwxX9PZC5eWpyxWB776ExTxWxmBHpp3IBIko'
  }
}

export async function getAllBookings () {
  const response = await fetch(BASE_URL, {
    headers: getHeaders()
  })

  return await response.json()
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

  return await response.json()
}
