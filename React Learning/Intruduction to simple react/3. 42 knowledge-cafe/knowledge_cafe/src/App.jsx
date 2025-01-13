import { useState } from 'react'
import './App.css'
import Blogs from './components/Blogs/Blogs'
import Bookmarks from './components/Bookmarks/Bookmarks'
import Header from './components/Header/Header'

function App() {

  const [bookmarks, SetBookmarks] = useState([]);

  const [readingTime,setreadingTime]=useState(0);

  const handleAddToBookmark = blog => {
    const newBookmarks = [...bookmarks, blog];
    SetBookmarks(newBookmarks);
  }

  const handleMarkAsRead = (id,time) =>{
    setreadingTime(readingTime + time)
    // console.log("removed",id);
    const remainingBookmarks=bookmarks.filter(bookmark => bookmark.id !== id);
    SetBookmarks(remainingBookmarks);
  }
  return (

    <div className='max-w-7xl mx-auto'>
      <Header></Header>
      <div className='md:flex'>
        <Blogs handleMarkAsRead={handleMarkAsRead} handleAddToBookmark={handleAddToBookmark} ></Blogs>
        <Bookmarks bookmarks={bookmarks} readingTime={readingTime} ></Bookmarks>
      </div>


    </div>
  )
}

export default App
