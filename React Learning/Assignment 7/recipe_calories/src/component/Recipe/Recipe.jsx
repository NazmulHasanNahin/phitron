import PropTypes from "prop-types";

const Recipe = ({recipe}) => {

    const {recipe_image, recipe_id, recipe_name, short_description, ingredients, preparing_time, calories
    }=recipe;

    return (
        <div>
           <h2 className="text-5xl mb-4">{recipe_name}</h2>
        </div>
    );
};

Recipe.propTypes = {
    recipe: PropTypes.object.isRequired,
}


export default Recipe;