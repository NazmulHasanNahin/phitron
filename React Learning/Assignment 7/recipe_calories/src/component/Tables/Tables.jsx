import PropTypes from "prop-types";

const Tables = ({
    wantToCook,
    currentlyCooking,
    moveToCooking,
    removeFromWantToCook,
    totalTime,
    totalCalories,
}) => {
    return (

        <div className="w-1/3 p-5">
            <h2 className="text-2xl font-bold mb-4">Want to Cook: {wantToCook.length}</h2>
            <div className="bg-white shadow-lg rounded-lg p-4 mb-8">
                {wantToCook.length > 0 ? (
                    <table className="w-full">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Time</th>
                                <th>Calories</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            {wantToCook.map((recipe) => (
                                <tr key={recipe.recipe_id}>
                                    <td>{recipe.recipe_name}</td>
                                    <td>{recipe.preparing_time} min</td>
                                    <td>{recipe.calories} cal</td>
                                    <td>
                                        <button
                                            onClick={() => moveToCooking(recipe)}
                                            className="bg-green-500 text-white px-4 py-1 rounded"
                                        >
                                            Preparing
                                        </button>
                                        <button
                                            onClick={() => removeFromWantToCook(recipe.recipe_id)}
                                            className="bg-red-500 text-white px-4 py-1 rounded ml-2"
                                        >
                                            Remove
                                        </button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                ) : (
                    <p>No recipes added yet</p>
                )}
            </div>

            <h2 className="text-2xl font-bold mb-4">Currently Cooking: {currentlyCooking.length}</h2>
            <div className="bg-white shadow-lg rounded-lg p-4">
                {currentlyCooking.length > 0 ? (
                    <table className="w-full">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Time</th>
                                <th>Calories</th>
                            </tr>
                        </thead>
                        <tbody>
                            {currentlyCooking.map((recipe) => (
                                <tr key={recipe.recipe_id}>
                                    <td>{recipe.recipe_name}</td>
                                    <td>{recipe.preparing_time} min</td>
                                    <td>{recipe.calories} cal</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                ) : (
                    <p>No recipes are currently being cooked</p>
                )}
            </div>

            <div className="mt-4">
                <p>Total Preparation Time: {totalTime} minutes</p>
                <p>Total Calories: {totalCalories} calories</p>
            </div>
        </div>
    );
};

// Prop validation
Tables.propTypes = {
    wantToCook: PropTypes.arrayOf(
        PropTypes.shape({
            recipe_id: PropTypes.string.isRequired,
            recipe_name: PropTypes.string.isRequired,
            preparing_time: PropTypes.number.isRequired,
            calories: PropTypes.number.isRequired,
        })
    ).isRequired,

    currentlyCooking: PropTypes.arrayOf(
        PropTypes.shape({
            recipe_id: PropTypes.string.isRequired,
            recipe_name: PropTypes.string.isRequired,
            preparing_time: PropTypes.number.isRequired,
            calories: PropTypes.number.isRequired,
        })
    ).isRequired,

    moveToCooking: PropTypes.func.isRequired,
    removeFromWantToCook: PropTypes.func.isRequired,

    totalTime: PropTypes.number.isRequired,
    totalCalories: PropTypes.number.isRequired,
};

export default Tables;
