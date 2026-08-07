const BASE_URL = 'http://127.0.0.1:5000/api/admin/treks'

function getHeaders () {
  return {
    Authorization: `Bearer ${localStorage.getItem('token')}`,
    'Content-Type': 'application/json'
  }
}

export async function getAllTreks () {
  const response = await fetch(BASE_URL, {
    headers: getHeaders()
  })

  return await response.json()
}

export async function addTrek (trek) {
  const response = await fetch(BASE_URL, {
    method: 'POST',
    headers: getHeaders(),
    body: JSON.stringify(trek)
  })

  return await response.json()
}

export async function updateTrek (id, trek) {
  const response = await fetch(`${BASE_URL}/${id}`, {
    method: 'PUT',
    headers: getHeaders(),
    body: JSON.stringify(trek)
  })

  return await response.json()
}

export async function deleteTrek (id) {
  const response = await fetch(`${BASE_URL}/${id}`, {
    method: 'DELETE',
    headers: getHeaders()
  })

  return await response.json()
}