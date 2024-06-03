



const heist_selection = (array) => {
    let biggestname = array[0];
    for (let i = 0; i < array.length; i++) {
        const element=array[i];
        if(element.length>biggestname.length){
            biggestname=element;
        }
    }
    return biggestname;

}


const character = ["Trevor", "Lester", "Fabien", "Rachael" , "Martin madrazo","Bradly"];
const heist = heist_selection(character)

console.log(heist);
