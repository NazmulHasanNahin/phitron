import PropTypes from "prop-types";
import { CiClock2 } from "react-icons/ci";
import { SlFire } from "react-icons/sl";

const Recipe = ({ recipe, handleWanttocook }) => {
    const { recipe_image, recipe_name, short_description, ingredients, preparing_time, calories } = recipe;

    return (
        <div className="w-full h-auto p-4 rounded-xl border border-gray-200 shadow-md flex flex-col my-5 gap-4">
            <img className="w-full h-[280px] object-cover rounded-lg" src={recipe_image} alt={recipe_name} />
            <div className="flex flex-col w-full gap-3">
                <div className="flex flex-col gap-1">
                    <h2 className="text-[#282828] text-lg font-semibold">{recipe_name}</h2>
                    <p className="text-[#878787] text-sm">{short_description}</p>
                </div>
                <div className="border-t border-gray-200 w-full"></div>
                <div className="flex flex-col gap-2">
                    <h3 className="text-[#282828] text-md font-medium">Ingredients</h3>
                    <ul className="text-[#878787] text-sm leading-relaxed list-disc pl-5">
                        {ingredients.map((ingredient, index) => (
                            <li key={index}>{ingredient}</li>
                        ))}
                    </ul>
                </div>
                <div className="border-t border-gray-200 w-full"></div>
                <div className="flex justify-between items-center w-full">
                    <div className="flex gap-4">
                        <div className="flex items-center gap-1 text-gray-700">
                            <CiClock2 className="text-lg" />
                            <span className="text-sm font-medium">{preparing_time} min</span>
                        </div>
                        <div className="flex items-center gap-1 text-gray-700">
                            <SlFire className="text-lg" />
                            <span className="text-sm font-medium">{calories} kcal</span>
                        </div>
                    </div>
                </div>
                <div className="mt-3">
                    <button
                        onClick={() => handleWanttocook(recipe)}
                        className="px-4 py-2 bg-[#0be58a] text-[#150b2b] rounded-full font-medium shadow-lg">
                        Want to Cook
                    </button>
                </div>
            </div>
        </div>
    );
};

Recipe.propTypes = {
    recipe: PropTypes.object.isRequired,
    handleWanttocook: PropTypes.func,
};

export default Recipe;
