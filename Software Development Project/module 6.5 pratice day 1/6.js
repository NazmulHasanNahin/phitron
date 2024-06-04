const fncTofindBig = (array) => {
    let biggestname = array[0];
    for (let i = 0; i < array.length; i++) {
        const element = array[i];
        if (element.length > biggestname.length) {
            biggestname = element;
        }
    }
    return biggestname;

}

var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];
const optname = fncTofindBig(friends)
console.log(optname);