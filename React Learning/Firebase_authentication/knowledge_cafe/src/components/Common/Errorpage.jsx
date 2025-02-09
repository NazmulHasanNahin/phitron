import { Link } from "react-router-dom";
import { Helmet } from "react-helmet-async";

const Errorpage = () => {
  return (
    <div className="flex items-center justify-center min-h-screen">
      <Helmet><title>Error</title></Helmet>
      <div className="text-center p-8 rounded-lg  bg-white">
        <h1 className="text-9xl font-bold text-red-500 animate-bounce">404</h1>
        <h2 className="mt-4 text-3xl font-semibold text-gray-800">Page Not Found</h2>
        <p className="mt-2 text-gray-600">
          Sorry, the page you are looking for does not exist.
        </p>
        <div className="mt-6">
          <Link
            to="/"
            className="px-5 py-3 bg-blue-500 text-white rounded-lg shadow-md hover:bg-blue-600 transition-all duration-300 ease-in-out transform hover:scale-105">
            Go Home
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Errorpage;