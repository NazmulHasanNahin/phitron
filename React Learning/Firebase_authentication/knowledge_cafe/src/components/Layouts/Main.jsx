import { Outlet } from "react-router-dom";
import Nav from "../Common/Nav";


const Main = () => {
    return (
        <div>
            <div className="max-w-7xl mx-auto">
                <Nav></Nav>
                <Outlet></Outlet>
            </div>
        </div>
    );
};

export default Main;