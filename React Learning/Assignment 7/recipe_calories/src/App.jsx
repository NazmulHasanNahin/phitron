import './App.css'
import Banner from './component/Bannner/Banner'
import Header from './component/Header/Header'
import Recipes from './component/Recipes/Recipes'
import RecipeText from './component/RecipeText/RecipeText'

function App() {

  return (
    <>
      <div className='max-w-7xl mx-auto'>
      <Header></Header>
      <Banner></Banner>
      <RecipeText></RecipeText>
      <div>
        <Recipes></Recipes>
      </div>
      </div>
    </>
  )
}

export default App
