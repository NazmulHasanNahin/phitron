import { useEffect, useState } from "react";
import Recipe from "../Recipe/Recipe";




const Recipes = () => {

    const [recipes,setRecipes]= useState([]);

    useEffect(()=>{
        fetch("recipe_data.json")
        .then(res => res.json())
        .then(data => setRecipes(data))
    } ,[])




    return (
        <div className="md:w-2/3 my-3">
           <h1 className="text-4xl mb-4">Blogs:{recipes.length}</h1>
           {
                recipes.map(recipe => <Recipe
                    key={recipe.recipe_id}
                    recipe={recipe}
                    
                
                >   
                </Recipe>)
           }
        </div>
    );
};

export default Recipes;