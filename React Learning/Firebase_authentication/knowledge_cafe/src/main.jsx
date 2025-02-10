import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import {  HelmetProvider } from 'react-helmet-async';
import './index.css'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Main from './components/Layouts/Main';
import Home from './components/Home/Home';
import Errorpage from './components/Common/ErrorPage';
import Login from './components/Login/Login';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Main></Main>,
    errorElement: <Errorpage></Errorpage>,
    children: [
      {
        path: '/',
        element: <Home></Home>,
      },
      {
        path: '/login',
        element: <Login></Login>,
      },
    ]
  },
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <HelmetProvider>
      <RouterProvider router={router} />
    </HelmetProvider>
  </StrictMode>,
)
