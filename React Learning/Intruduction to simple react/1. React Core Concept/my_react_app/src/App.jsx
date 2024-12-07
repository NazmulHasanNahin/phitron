import './App.css'

function App() {

  function handleclick() {
    alert("nahin named button is clicked")
  }
  return (
    <>
      <h2>first react project to explore</h2> 
      <button onClick={handleclick}>nahin</button>     
    </>
  )
}

export default App
