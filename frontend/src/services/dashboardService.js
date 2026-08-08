const BASE_URL = 'http://127.0.0.1:5000'

export async function getDashboardData () {
  // const token = localStorage.getItem('token')
  const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NjIwNTA5MiwianRpIjoiNmQ2YzJmYmYtMTZkYi00ODllLThlM2YtMjI2N2VkNzc1NzM3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODYyMDUwOTIsImNzcmYiOiJmZDY5OGVjNi0yOTE5LTQ5MWEtOTNiMy1lMGFjY2RjYmYwMzMiLCJleHAiOjE3ODYyMzM4OTIsInJvbGUiOiJBZG1pbiJ9.SHLjc4LIwxX9PZC5eWpyxWB776ExTxWxmBHpp3IBIko'

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
