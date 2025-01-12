import PropTypes from 'prop-types'
import Bookmark from '../Bookmark/Bookmark';


const Bookmarks = ({bookmarks}) => {
    return (
        <div className="md:w-1/3 bg-gray-300 ml-4 my-3">
           <h2 className='text-4xl text-center my-3' >Bookmarked Blogs: {bookmarks.length}</h2>
           {
                bookmarks.map(bookmark =>  <Bookmark key={bookmark.id} bookmark={bookmark}></Bookmark>)
           }
        </div>
    );
};

Bookmarks.propTypes={
    bookmarks: PropTypes.array
}

export default Bookmarks;