const BASE_URL = 'http://127.0.0.1:5000'

export async function getDashboardData () {
  const token = localStorage.getItem('token')
  const response = await fetch(`${BASE_URL}/api/admin/dashboard`, {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  })

  if (!response.ok) {
    console.log('Failed!')
    throw new Error('Unable to fetch dashboard data')
  }

  const result = await response.json()
  return result.data || result
}
