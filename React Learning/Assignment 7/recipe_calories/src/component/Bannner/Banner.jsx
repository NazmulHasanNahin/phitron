const Banner = () => {
    return (
        <div className="relative m-4">
            {/* Image */}
            <div className="flex justify-center items-center">
                <img
                    className="w-full h-[400px] md:h-[600px] lg:h-[700px] object-cover rounded-lg" // Dynamic height for different screen sizes
                    src="https://i.ibb.co.com/DRNCxZJ/Rectangle-1.png"
                    alt="Centered Image"
                />
            </div>

            {/* Overlay Text and Buttons */}
            <div className="absolute inset-0 flex flex-col justify-center items-center text-center p-4 bg-black bg-opacity-40 rounded-lg">
                <div className="max-w-[90%] md:max-w-[60%]">
                    <h2 className="text-2xl md:text-4xl font-bold  text-white mb-4 md:max-w-3xl max-w-xl">
                        Discover an exceptional cooking class tailored for you!
                    </h2>
                    <p className="text-base  text-white mb-6 md:max-w-3xl max-w-xl ">
                        We ve unraveled cooking class themes, each offering a unique journey through tastes, traditions, and innovation.
                    </p>
                    <div className="flex justify-center md:justify-center md:gap-4 gap-2 mt-6">
                        <button className="bg-[#0BE58A] text-black px-6 py-3 rounded-full hover:bg-green-500 transition">
                            Explore Now
                        </button>
                        <button className="bg-transparent text-white border border-white px-6 py-3 rounded-full hover:bg-gray-200 hover:text-black transition">
                            Our Feedback
                        </button>

                    </div>

                </div>
            </div>
        </div>
    );
};

export default Banner;
