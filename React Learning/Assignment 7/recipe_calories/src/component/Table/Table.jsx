import PropTypes from 'prop-types';
import { CiClock2 } from 'react-icons/ci';
import { SlFire } from 'react-icons/sl';

const Table = ({ table,handlecooking  }) => {
    const {
        recipe_image,
        recipe_name,
        preparing_time,
        calories,
    } = table;

    return (
        <tr className="border-b hover:bg-gray-50">
            <td className="px-6 py-4 text-sm font-medium text-gray-900">
                <div className="flex items-center gap-4">
                    <img
                        className="w-16 h-16  rounded-md"
                        src={recipe_image}
                        alt={recipe_name}
                    />
                    <span>{recipe_name}</span>
                </div>
            </td>
            <td className="px-6 py-4 text-sm text-gray-700">
                <div className="flex items-center gap-2">
                    <CiClock2 className="text-xl text-gray-700" />
                    <span>{preparing_time} mins</span>
                </div>
            </td>
            <td className="px-6 py-4 text-sm text-gray-700">
                <div className="flex items-center gap-2">
                    <SlFire className="text-xl text-gray-700" />
                    <span>{calories} kcal</span>
                </div>
            </td>
            <td className="px-6 py-4 text-center">
                <button
                onClick={()=>handlecooking(table)}
                    className="px-4 py-2 bg-[#0be58a] hover:bg-[#0acf7d] text-[#150b2b] rounded-full font-medium shadow-lg transition-all duration-300 ease-in-out"
                >
                    Preparing
                </button>
            </td>
        </tr>
    );
};

Table.propTypes = {
    table: PropTypes.object.isRequired,
    handlecooking: PropTypes.array,
};

export default Table;
