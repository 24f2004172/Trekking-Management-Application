const BASE_URL = 'http://127.0.0.1:5000/api/staff'

function getHeaders () {
  return {
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjI1NzE4MSwianRpIjoiZDJlYTA4ODgtZjdlNC00MzFiLTlmNzEtNGQzNDE5MTYyYTY2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjUiLCJuYmYiOjE3ODYyNTcxODEsImNzcmYiOiI3NTJmOTM4Yy0xODYyLTQ4YTItYTcxNi0zMTMzZjliOTJiNTMiLCJleHAiOjE3ODYzNDM1ODEsInJvbGUiOiJTdGFmZiJ9.U4P03LpzKkTliAm9TYH35J82JE309EcGU8CFeRbzDjk',
    'Content-Type': 'application/json'
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
