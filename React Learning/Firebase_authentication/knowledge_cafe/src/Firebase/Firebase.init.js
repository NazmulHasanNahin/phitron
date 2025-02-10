// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyA6I1nAn1Zh-wKZS5W73sGdNhIlFyAfrdk",
  authDomain: "simple-react-auth-first.firebaseapp.com",
  projectId: "simple-react-auth-first",
  storageBucket: "simple-react-auth-first.firebasestorage.app",
  messagingSenderId: "862445687411",
  appId: "1:862445687411:web:25be98dcb7783f8d829006"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export default auth;