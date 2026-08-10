const BASE_URL = 'http://127.0.0.1:5000/api/admin/treks'

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

export async function getAllTreks () {
  const response = await fetch(BASE_URL, {
    headers: getHeaders()
  })

  return await handleResponse(response)
}

export async function addTrek (trek) {
  const response = await fetch(BASE_URL, {
    method: 'POST',
    headers: getHeaders(),
    body: JSON.stringify(trek)
  })

  return await handleResponse(response)
}

export async function updateTrek (id, trek) {
  const response = await fetch(`${BASE_URL}/${id}`, {
    method: 'PUT',
    headers: getHeaders(),
    body: JSON.stringify(trek)
  })

  return await handleResponse(response)
}

export async function deleteTrek (id) {
  const response = await fetch(`${BASE_URL}/${id}`, {
    method: 'DELETE',
    headers: getHeaders()
  })

  return await handleResponse(response)
}
