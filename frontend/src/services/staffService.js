const BASE_URL = 'http://127.0.0.1:5000/api/admin/staff'

function getHeaders () {
  return {
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjI2NTY4NywianRpIjoiMDRmMWZiMWYtMzdkZS00MDMxLWJkNTQtOTMxOTkyMmQxOGQwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYyNjU2ODcsImNzcmYiOiJkMzYyMDMwOS0xNGE0LTQ3YzYtOTBmMy1kM2NjYjg1MGI0YzIiLCJleHAiOjE3ODYzNTIwODcsInJvbGUiOiJBZG1pbiJ9.g_C---AyTiRSrfLW1KJVbQotQDpRmvMUTs9thC05eV8',
    'Content-Type': 'application/json'
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

export async function getAllStaffs () {
  const response = await fetch(BASE_URL, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function addStaff (staff) {
  const response = await fetch(BASE_URL, {
    method: 'POST',
    headers: getHeaders(),
    body: JSON.stringify(staff)
  })

  return await handleResponse(response)
}

export async function updateStaff (id, staff) {
  const response = await fetch(`${BASE_URL}/${id}`, {
    method: 'PUT',
    headers: getHeaders(),
    body: JSON.stringify(staff)
  })

  return await handleResponse(response)
}

export async function deleteStaff (id) {
  const response = await fetch(`${BASE_URL}/${id}`, {
    method: 'DELETE',
    headers: getHeaders()
  })

  return await handleResponse(response)
}
