import PropTypes from "prop-types";
import { CiClock2 } from "react-icons/ci";
import { SlFire } from "react-icons/sl";

const Recipe = ({ recipe, addToWantToCook, showToast }) => {
  const { recipe_image, recipe_name, short_description, ingredients, preparing_time, calories } = recipe;

  const handleAddToWantToCook = () => {
    addToWantToCook(recipe);
    showToast(recipe);
  };

  return (
    <div className="w-[420px] h-auto p-6 rounded-2xl border-2 border-gray-200 flex flex-col my-5 gap-6">
      <img className="w-[331px] h-[400px] object-cover rounded-2xl" src={recipe_image} alt={recipe_name} />
      <div className="flex flex-col w-full gap-4">
        <div className="flex flex-col gap-2">
          <h2 className="text-[#282828] text-xl font-semibold">{recipe_name}</h2>
          <p className="text-[#878787] text-base">{short_description}</p>
        </div>
        <div className="border-t border-gray-200 w-full"></div>
        <div className="flex flex-col gap-4">
          <h3 className="text-[#282828] text-lg font-medium">Ingredients</h3>
          <ul className="text-[#878787] text-lg leading-loose list-disc pl-5">
            {ingredients.map((ingredient, index) => (
              <li key={index}>{ingredient}</li>
            ))}
          </ul>
        </div>
        <div className="border-t border-gray-200 w-full"></div>
        <div className="flex justify-between items-center w-full">
          <div className="flex">
            <div className="text-[#282828]/80 text-base">
              <div className="flex items-center gap-1 text-gray-700 mx-4">
                <CiClock2 className="text-xl" />
                <span className="text-base font-medium">{preparing_time} minutes</span>
              </div>
            </div>
            <div className="flex items-center gap-1 text-gray-700">
              <SlFire className="text-xl" />
              <span className="text-base font-medium">{calories} cal</span>
            </div>
          </div>
        </div>
        <div>
          <button
            onClick={handleAddToWantToCook}
            className="px-6 py-2 bg-[#0be58a] hover:bg-[#0acf7d] text-[#150b2b] rounded-full font-medium shadow-lg transition-all duration-300 ease-in-out transform hover:scale-105"
          >
            Want to Cook
          </button>
        </div>
      </div>
    </div>
  );
};

Recipe.propTypes = {
  recipe: PropTypes.object.isRequired,
  addToWantToCook: PropTypes.func.isRequired,
  showToast: PropTypes.func.isRequired,
};

export default Recipe;
