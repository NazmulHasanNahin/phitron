import { Link, useLocation } from "react-router-dom";

const Nav = () => {
    const location = useLocation();
    const isActive = (path) => location.pathname === path;

    return (
        <div>
            <div className="navbar bg-base-100">
                <div className="navbar-start">
                    <div className="dropdown">
                        <div tabIndex={0} role="button" className="btn btn-ghost lg:hidden">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                className="h-5 w-5"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="2"
                                    d="M4 6h16M4 12h8m-8 6h16" />
                            </svg>
                        </div>
                        <ul
                            tabIndex={0}
                            className="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
                            <div className="navbar-center">
                                <ul className="menu menu-horizontal px-1 space-x-1">
                                    <li>
                                        <Link
                                            to="/"
                                            className={`btn ${isActive("/") ? "bg-[#23be0a] text-white" : "btn-ghost"}`}>
                                            Home
                                        </Link>
                                    </li>
                                    <li>
                                        <Link
                                            to="/listed-books"
                                            className={`btn ${isActive("/listed-books") ? "bg-[#23be0a] text-white" : "btn-ghost"}`}>
                                            Listed Books
                                        </Link>
                                    </li>
                                    <li>
                                        <Link
                                            to="/pages-to-read"
                                            className={`btn ${isActive("/pages-to-read") ? "bg-[#23be0a] text-white" : "btn-ghost"}`}>
                                            Pages to Read
                                        </Link>
                                    </li>
                                </ul>
                            </div>
                        </ul>
                    </div>
                    <Link to="/" className="text-2xl font-bold text-gray-800">Book Vault</Link>
                </div>
                {/* here start for pc */}
                <div className="navbar-center hidden lg:flex">
                    <ul className="menu menu-horizontal px-1">
                        <div className="navbar-center">
                            <ul className="menu menu-horizontal px-1 space-x-4">
                                <li>
                                    <Link
                                        to="/"
                                        className={`btn ${isActive("/") ? "bg-[#23be0a] text-white" : "btn-ghost"}`}>
                                        Home
                                    </Link>
                                </li>
                                <li>
                                    <Link
                                        to="/listed-books"
                                        className={`btn ${isActive("/listed-books") ? "bg-[#23be0a] text-white" : "btn-ghost"}`}>
                                        Listed Books
                                    </Link>
                                </li>
                                <li>
                                    <Link
                                        to="/pages-to-read"
                                        className={`btn ${isActive("/pages-to-read") ? "bg-[#23be0a] text-white" : "btn-ghost"}`}>
                                        Pages to Read
                                    </Link>
                                </li>
                            </ul>
                        </div>
                    </ul>
                </div>
                <div className="navbar-end space-x-2">
                    <div className="p-2 bg-[#23be0a] rounded-lg justify-center items-center gap-2.5 inline-flex">
                        <Link to="/login" className="text-center text-white text-lg font-semibold font-['Work Sans']">Sign In</Link>
                    </div>
                    <div className="p-2 bg-[#59c6d2] rounded-lg justify-center items-center gap-2.5 inline-flex">
                        <button className="text-center text-white text-lg font-semibold font-['Work Sans']">Sign Up</button>
                    </div>
                </div>
            </div>
        </div>

    );
};

export default Nav;