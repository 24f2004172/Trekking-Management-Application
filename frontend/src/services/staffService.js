const BASE_URL = 'http://127.0.0.1:5000/api/admin/staff'

function getHeaders () {
  return {
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjIwNTA5MiwianRpIjoiNmQ2YzJmYmYtMTZkYi00ODllLThlM2YtMjI2N2VkNzc1NzM3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYyMDUwOTIsImNzcmYiOiJmZDY5OGVjNi0yOTE5LTQ5MWEtOTNiMy1lMGFjY2RjYmYwMzMiLCJleHAiOjE3ODYyMzM4OTIsInJvbGUiOiJBZG1pbiJ9.SHLjc4LIwxX9PZC5eWpyxWB776ExTxWxmBHpp3IBIko',
    'Content-Type': 'application/json'
  }
}

export async function getAllStaffs () {
  const response = await fetch(BASE_URL, {
    headers: getHeaders()
  })

  return await response.json()
}

export async function addStaff (staff) {
  const response = await fetch(BASE_URL, {
    method: 'POST',
    headers: getHeaders(),
    body: JSON.stringify(staff)
  })

  return await response.json()
}

export async function updateStaff (id, staff) {
  const response = await fetch(`${BASE_URL}/${id}`, {
    method: 'PUT',
    headers: getHeaders(),
    body: JSON.stringify(staff)
  })

  return await response.json()
}

export async function deleteStaff (id) {
  const response = await fetch(`${BASE_URL}/${id}`, {
    method: 'DELETE',
    headers: getHeaders()
  })

  return await response.json()
}
