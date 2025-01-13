import PropTypes from 'prop-types'
import Bookmark from '../Bookmark/Bookmark';


const Bookmarks = ({bookmarks,readingTime}) => {
    return (
        
        <div className="md:w-1/3 bg-gray-300 ml-4 my-3">
            <div>
                <h3 className="text-4xl p-4 text-center">Reading Time: {readingTime}</h3>
            </div>
           <h2 className='text-4xl text-center my-3' >Bookmarked Blogs: {bookmarks.length}</h2>
           {
                bookmarks.map((bookmark,idx) =>  <Bookmark key={idx} bookmark={bookmark}></Bookmark>)
           }
        </div>
    );
};

Bookmarks.propTypes={
    bookmarks: PropTypes.array,
    readingTime : PropTypes.number
}

export default Bookmarks;