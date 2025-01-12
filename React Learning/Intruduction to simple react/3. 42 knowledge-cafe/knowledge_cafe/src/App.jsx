import { useState } from 'react'
import './App.css'
import Blogs from './components/Blogs/Blogs'
import Bookmarks from './components/Bookmarks/Bookmarks'
import Header from './components/Header/Header'

function App() {

  const [bookmarks, SetBookmarks] = useState([]);

  const handleAddToBookmark = blog => {
    const newBookmarks = [...bookmarks, blog];
    SetBookmarks(newBookmarks);
  }
  return (

    <div className='max-w-7xl mx-auto'>
      <Header></Header>
      <div className='md:flex'>
        <Blogs handleAddToBookmark={handleAddToBookmark} ></Blogs>
        <Bookmarks bookmarks={bookmarks}></Bookmarks>
      </div>


    </div>
  )
}

export default App
