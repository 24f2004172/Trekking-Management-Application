const BASE_URL = 'http://127.0.0.1:5000/api/admin/staff'

function getHeaders () {
  return {
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjI2NTY4NywianRpIjoiMDRmMWZiMWYtMzdkZS00MDMxLWJkNTQtOTMxOTkyMmQxOGQwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYyNjU2ODcsImNzcmYiOiJkMzYyMDMwOS0xNGE0LTQ3YzYtOTBmMy1kM2NjYjg1MGI0YzIiLCJleHAiOjE3ODYzNTIwODcsInJvbGUiOiJBZG1pbiJ9.g_C---AyTiRSrfLW1KJVbQotQDpRmvMUTs9thC05eV8',
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
