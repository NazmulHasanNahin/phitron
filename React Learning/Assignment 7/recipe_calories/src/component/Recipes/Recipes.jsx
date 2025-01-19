import { useEffect, useState } from "react";
import Recipe from "../Recipe/Recipe";
import PropTypes from "prop-types";

const Recipes = ({ handleWanttocook }) => {
    const [recipes, setRecipes] = useState([]);

    useEffect(() => {
        fetch("recipe_data.json")
            .then((res) => res.json())
            .then((data) => setRecipes(data));
    }, []);

    return (
        <div className="md:w-3/4 my-3">
            <h1 className="text-4xl text-center mb-4">Recipes: {recipes.length}</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 px-4">
                {recipes.map((recipe) => (
                    <Recipe
                        key={recipe.recipe_id}
                        handleWanttocook={handleWanttocook}
                        recipe={recipe}
                    />
                ))}
            </div>
        </div>
    );
};

Recipes.propTypes = {
    handleWanttocook: PropTypes.func,
};

export default Recipes;
