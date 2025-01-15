import { useState } from 'react';
import './App.css';
import Banner from './component/Bannner/Banner';
import Header from './component/Header/Header';
import Recipes from './component/Recipes/Recipes';
import Tables from './component/Tables/Tables';
import { Toaster, toast } from "react-hot-toast"; // Import 'toast' here

function App() {
  const [wantToCook, setWantToCook] = useState([]);
  const [currentlyCooking, setCurrentlyCooking] = useState([]);

  const addToWantToCook = (recipe) => {
    if (!wantToCook.find((r) => r.recipe_id === recipe.recipe_id)) {
      setWantToCook([...wantToCook, recipe]);
    } else {
      toast.error(`${recipe.recipe_name} is already in the list.`); // This works now since 'toast' is imported
    }
  };

  const moveToCooking = (recipe) => {
    setWantToCook(wantToCook.filter((r) => r.recipe_id !== recipe.recipe_id));
    setCurrentlyCooking([...currentlyCooking, recipe]);
  };

  const removeFromWantToCook = (recipeId) => {
    setWantToCook(wantToCook.filter((r) => r.recipe_id !== recipeId));
  };

  const totalTime = wantToCook.reduce((total, recipe) => total + recipe.preparing_time, 0);
  const totalCalories = wantToCook.reduce((total, recipe) => total + recipe.calories, 0);

  return (
    <>
      <div className="max-w-7xl mx-auto">
        <Header />
        <Banner />
        <div className="md:flex">
          <Recipes addToWantToCook={addToWantToCook} />
          <Tables
            wantToCook={wantToCook}
            currentlyCooking={currentlyCooking}
            moveToCooking={moveToCooking}
            removeFromWantToCook={removeFromWantToCook}
            totalTime={totalTime}
            totalCalories={totalCalories}
          />
        </div>
      </div>
      <Toaster /> {/* Add the Toaster component to render the toasts */}
    </>
  );
}

export default App;
