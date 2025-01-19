import PropTypes from 'prop-types';
import Table from '../Table/Table';

const Tables = ({ wanttocook , handlecooking}) => {
    return (
        <div className="overflow-x-auto mt-6">
            <h1 className="text-4xl text-center">Want to cook: 0{wanttocook.length}</h1>
            <div className="overflow-y-auto max-h-[500px]"> 
                <table className="min-w-full mt-4">
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
                            <th className="px-6 py-3 text-center text-lg font-semibold text-gray-700">
                                Action
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {wanttocook.map((recipe) => (
                            <Table 
                            key={recipe.recipe_id}
                            table={recipe}
                            handlecooking={handlecooking}
                             />
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

Tables.propTypes = {
    wanttocook: PropTypes.array.isRequired,
    handlecooking: PropTypes.array,
};

export default Tables;
