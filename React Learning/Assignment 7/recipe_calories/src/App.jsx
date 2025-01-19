import { useState } from 'react';
import './App.css';
import Banner from './component/Bannner/Banner';
import Header from './component/Header/Header';
import Recipes from './component/Recipes/Recipes';
import RecipeText from './component/RecipeText/RecipeText';
import Tables from './component/Tables/Tables';
import { Toaster, toast } from 'react-hot-toast';
import CuCook from './component/CuCook/CuCook';



function App() {
  const [wanttocook, setWanttocook] = useState([]);

  const handleWanttocook = (recipe) => {
    const isAlreadyAdded = wanttocook.some(item => item.recipe_id === recipe.recipe_id);

    if (!isAlreadyAdded) {
      const newWanttocook = [...wanttocook, recipe];
      setWanttocook(newWanttocook);
      toast.success('Recipe added successfully!');
    } else {
      toast.error('This recipe is already added!');
    }
  };



  // 2nd step 
  const [cooking, setCooking] = useState([]);

  const handlecooking = (table) => {

    const updatedWantToCook = wanttocook.filter(item => item.recipe_id !== table.recipe_id);

    const updatedCooking = [...cooking, table];

    setWanttocook(updatedWantToCook);
    setCooking(updatedCooking);
    toast.success('Recipe moved to Cooking!');


  }

  return (
    <>
      <div className='md:max-w-[1380px] mx-auto'>
        <Header />
        <Banner />
        <RecipeText />
        <div className='md:flex md:space-x-6'>
          <Recipes
            handleWanttocook={handleWanttocook}
            className="md:w-2/3 w-full"
          />
          <div>
            <Tables
              handlecooking={handlecooking}
              wanttocook={wanttocook}
              className="md:w-1/3 w-full mt-5 md:mt-0"
            />
            <CuCook
              cooking={cooking}
            ></CuCook>
          </div>
        </div>
      </div>
      <Toaster
        position="top-right"
        toastOptions={{
          success: {
            style: {
              background: '#0be58a',
              color: '#150b2b',
            },
          },
          error: {
            style: {
              background: '#f87171',
              color: '#fff',
            },
          },
        }}
      />

    </>
  );
}

export default App;
