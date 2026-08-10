const API_URL = 'http://127.0.0.1:5000/api'

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

export async function login (credentials) {
  const response = await fetch(`${API_URL}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(credentials)
  })

  return await handleResponse(response)
}

export async function register (data) {
  const response = await fetch(`${API_URL}/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })

  return await handleResponse(response)
}

export default {
  login,
  register
}
