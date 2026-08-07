const BASE_URL = 'http://127.0.0.1:5000'

export async function getDashboardData () {
  // const token = localStorage.getItem('token')
  const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjEwNDg3MiwianRpIjoiNzJlNjdhODYtYTRjMS00ODBjLWJkZWQtY2MzNDg3ZjY3YmE1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYxMDQ4NzIsImNzcmYiOiJiNzhmOWY1Ni00YmFkLTRjMzAtYTAyMS0wOGZkMWI4NjA3ZDciLCJleHAiOjE3ODYxMzM2NzIsInJvbGUiOiJBZG1pbiJ9.cMfJquG-Smh5eR2I_6aVDYsDkyg5-KRBpELt8TkrMN4'

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
