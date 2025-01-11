import { useEffect, useState } from "react";

const Blogs = () => {

    const [blogs,setBlogs] = useState([]);

    useEffect(()=>{
        fetch("blog.json")
        .then(res => res.json())
        .then( data => setBlogs(data))
        // .then( data => console.log(data))
    } ,[])

    return (
        <div>
           
        </div>
    );
};

export default Blogs;