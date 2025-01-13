import PropTypes from "prop-types";
import { FaRegBookmark } from "react-icons/fa";


const Blog = ({ blog , handleAddToBookmark,handleMarkAsRead}) => {

    const {id, title, cover_image, author_name, author_img, posted_date, reading_time, hashtag } = blog;
    return (
        <div className="mb-20">
            <img className="w-full mb-7" src={cover_image} alt={`image of ${title}`} />
            <div className="flex justify-between">
                <div className="flex mb-4">
                    <img className="w-12" src={author_img} alt="" />
                    <div className="ml-4">
                        <h2 className="font-bold">{author_name}</h2>
                        <p>{posted_date}</p>
                    </div>
                </div>
                <div>
                    <span className="mr-1">{reading_time} min read</span>
                    <button onClick={()=> handleAddToBookmark(blog)}><FaRegBookmark></FaRegBookmark></button>
                </div>
            </div>
            <h2 className="text-5xl mb-4">{title}</h2>
            <div className="m-1">
                <p>{hashtag}</p>
            </div>
            <div>
                <button onClick={()=>handleMarkAsRead(id,reading_time)} className="text-[#6047EC] text-[18px] font-medium leading-normal underline underline-offset-auto decoration-solid decoration-skip-ink-none decoration-auto">
                    Mark as read
                </button>

            </div>

        </div>


    );
};

Blog.propTypes = {
    blog: PropTypes.object.isRequired,
    handleAddToBookmark: PropTypes.func,
    handleMarkAsRead:PropTypes.func
}

export default Blog;






