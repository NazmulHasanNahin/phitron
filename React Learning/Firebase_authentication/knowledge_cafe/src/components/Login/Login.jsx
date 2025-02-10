import { Helmet } from "react-helmet-async";
import { GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import auth from "../../Firebase/Firebase.init";

const Login = () => {
    const provider = new GoogleAuthProvider();

    const handleGoogleSignIn =()=>{
        signInWithPopup(auth,provider)
        .then((result)=>{
            console.log(result);
        })
        .catch((error)=>{
            console.log("Error", error);
        })

    }

    return (
        <div>
            <Helmet><title>Login</title></Helmet>

            <button onClick={handleGoogleSignIn} className="btn bg-red-200 btn-ghost" >Login With Google</button>
        </div>
    );
};

export default Login;