import PropTypes from 'prop-types';

const CuCook = ({ cooking }) => {
  const totalPreparingTime = cooking.reduce((total, recipe) => total + recipe.preparing_time, 0);
  const totalCalories = cooking.reduce((total, recipe) => total + recipe.calories, 0);

  return (
    <div>
      <h1 className="text-3xl text-center my-4">Currently cooking: {cooking.length}</h1>
      <div className="overflow-x-auto">
        <table className="min-w-full table-auto">
          <thead className="sticky top-0 bg-gray-100 z-10">
            <tr className="border-b">
              <th className="px-6 py-3 text-left text-lg font-semibold text-gray-700">
                Recipe Name
              </th>
              <th className="px-6 py-3 text-left text-lg font-semibold text-gray-700">
                Time
              </th>
              <th className="px-6 py-3 text-left text-lg font-semibold text-gray-700">
                Calories
              </th>
            </tr>
          </thead>
          <tbody>
            {cooking.map((recipe) => (
              <tr key={recipe.recipe_id} className="border-b">
                <td className="px-6 py-4 text-sm font-medium text-gray-900">{recipe.recipe_name}</td>
                <td className="px-6 py-4 text-sm text-gray-700">{recipe.preparing_time} mins</td>
                <td className="px-6 py-4 text-sm text-gray-700">{recipe.calories} kcal</td>
              </tr>
            ))}
            <tr className="border-t font-semibold">
              <td className="px-6 py-4 text-sm font-medium text-gray-900">Total</td>
              <td className="px-6 py-4 text-sm text-gray-700">{totalPreparingTime} mins</td>
              <td className="px-6 py-4 text-sm text-gray-700">{totalCalories} kcal</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

CuCook.propTypes = {
  cooking: PropTypes.array.isRequired,
};

export default CuCook;
