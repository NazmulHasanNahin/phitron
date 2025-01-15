import { useEffect, useState } from "react";
import Recipe from "../Recipe/Recipe";
import toast from "react-hot-toast";
import PropTypes from "prop-types"; 

const Recipes = ({ addToWantToCook }) => {
  const [recipes, setRecipes] = useState([]);
  
  useEffect(() => {
    fetch("recipe_data.json")
      .then(res => res.json())
      .then(data => setRecipes(data));
  }, []);

  const showToast = (recipe) => {
    toast.success(`${recipe.recipe_name} added to "Want to Cook"`);
  };

  return (
    <div className="md:w-2/3 my-3">
      <h1 className="text-4xl text-center mb-4">Recipes: {recipes.length}</h1>
      <div className="flex flex-wrap -mx-3">
        {recipes.map((recipe) => (
          <div key={recipe.recipe_id} className="w-full md:w-1/2 px-3 mb-6">
            <Recipe
              recipe={recipe}
              addToWantToCook={addToWantToCook}
              showToast={showToast}
            />
          </div>
        ))}
      </div>
    </div>
  );
};

Recipes.propTypes = {
  addToWantToCook: PropTypes.func.isRequired, 
};

export default Recipes;
