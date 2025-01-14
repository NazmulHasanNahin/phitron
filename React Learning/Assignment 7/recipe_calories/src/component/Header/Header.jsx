import { useState } from "react";
import { RxAvatar } from "react-icons/rx";
import { RxHamburgerMenu } from "react-icons/rx";

const Header = () => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    return (
        <header className="p-4">
            <div className="flex flex-col md:flex-row justify-between items-center">
                


                {/* Logo (Title) */}
                <div className="mb-4 md:mb-0 flex">
                    <div className="flex md:hidden justify-between">
                        <button
                            onClick={() => setIsMenuOpen(!isMenuOpen)}
                            className="text-2xl mr-4" 
                        >
                            <RxHamburgerMenu/> 
                        </button>
                    </div>
                    <div>
                    <h2 className="text-xl font-bold text-center md:text-left">Recipe Calories</h2>
                    </div>
                </div>

                {/* Nav */}
                <nav className="mb-4 md:mb-0">
                    <div
                        className={`flex flex-col md:flex-row gap-4 md:gap-12 text-center ${isMenuOpen ? "block" : "hidden"
                            } md:block`}
                    >
                        <button className="hover:bg-gray-200 px-4 py-2 rounded-md transition-all">
                            Home
                        </button>
                        <button className="hover:bg-gray-200 px-4 py-2 rounded-md transition-all">
                            Recipes
                        </button>
                        <button className="hover:bg-gray-200 px-4 py-2 rounded-md transition-all">
                            About
                        </button>
                        <button className="hover:bg-gray-200 px-4 py-2 rounded-md transition-all">
                            Search
                        </button>
                    </div>
                </nav>

                {/* Search Bar & Avatar */}
                <div className="flex items-center gap-4 w-full md:w-auto">
                    <input
                        type="text"
                        placeholder="Search"
                        className="flex-1 px-4 py-2 bg-gray-200 text-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-black"
                    />
                    {/* Avatar */}
                    <RxAvatar
                        className="bg-[#0BE58A] text-white w-10 h-10 flex items-center justify-center rounded-full"
                    />
                </div>
            </div>
        </header>
    );
};

export default Header;
