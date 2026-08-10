const BASE_URL = 'http://127.0.0.1:5000/api/staff'

function getHeaders () {
  const token = localStorage.getItem('token')
  return {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${token}`
  }
}

export async function getDashboard () {
  const response = await fetch(`${BASE_URL}/dashboard`, {
    headers: getHeaders()
  })

  if (!response.ok) {
    throw new Error('Unable to fetch staff dashboard')
  }

  const result = await response.json()
  return result.data || result
}

export async function getTrekDetails (trekId) {
  const response = await fetch(`${BASE_URL}/trek/${trekId}/details`, {
    headers: getHeaders()
  })

  if (!response.ok) {
    throw new Error('Unable to fetch trek details')
  }

  const result = await response.json()
  return result.data || result
}

export async function getParticipants (trekId) {
  const response = await fetch(`${BASE_URL}/trek/${trekId}/participants`, {
    headers: getHeaders()
  })

  if (!response.ok) {
    throw new Error('Unable to fetch participants')
  }

  const result = await response.json()
  return result.data || result
}

export async function updateStatus (trekId, status) {
  const response = await fetch(`${BASE_URL}/trek/${trekId}/status`, {
    method: 'PUT',
    headers: getHeaders(),
    body: JSON.stringify({ status })
  })

  if (!response.ok) {
    const err = await response.json().catch(() => ({}))
    throw new Error(err.message || 'Unable to update status')
  }

  const result = await response.json()
  return result.data || result
}
