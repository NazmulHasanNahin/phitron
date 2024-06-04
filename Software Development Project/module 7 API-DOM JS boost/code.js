// alert("hiii")

// console.log(document.getElementsByTagName("h1"));


const allbox = document.getElementsByClassName("box");
// console.log(allbox);

for (let i = 0; i < allbox.length; i++) {
    const element = allbox[i];
    element.style.backgroundColor = "green";

    if (element.innerText == "box-5") {
        element.style.backgroundColor = "red";
    }
}