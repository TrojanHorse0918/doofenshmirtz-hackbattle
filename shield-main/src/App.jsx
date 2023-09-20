import './app.css'
import Login from './Components/LoginPage/LoginPage'
import Register from './Components/RegisterPage/RegisterPage'
import Home from './Components/Home/Home'

import{
  createBrowserRouter,
  RouterProvider
}from 'react-router-dom'

const router = createBrowserRouter([
  {
    path: '/',
    element: <div><Login/></div>
  },
  {
    path: '/register',
    element: <div><Register/></div>
  },
  {
    path: '/home',
    element: <div><Home /></div>
  }
])

function App() {

  return (
    <div>
      <RouterProvider router={router}/>
    </div>
  )
}

export default App
