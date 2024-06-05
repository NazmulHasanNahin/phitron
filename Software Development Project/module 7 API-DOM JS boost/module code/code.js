// alert("hiii")

// console.log(document.getElementsByTagName("h1"));


// const allbox = document.getElementsByClassName("box");
// // console.log(allbox);

// for (let i = 0; i < allbox.length; i++) {
//     const element = allbox[i];
//     element.style.backgroundColor = "green";

//     if (element.innerText == "box-5") {
//         element.style.backgroundColor = "red";
//     }
// }

document.getElementById("add-btn").addEventListener
    ("click", (event) => {
        const inputValue = document.getElementById("input-box").value;
        // console.log(inputValue);

        const container = document.getElementById("coment-container");

        const p = document.createElement("p");

        p.classList.add("child");

        p.innerText = inputValue;

        container.appendChild(p);

        document.getElementById("input-box").value = "";

        const all_text = document.getElementsByClassName("child");


        for (const element of all_text) {
            element.addEventListener("click", (e) => {
                e.target.parentNode.removeChild(element);
            })
        }

    });




fetch("https://jsonplaceholder.typicode.com/users")
    .then(res => res.json())
    .then(data => {
        displayData(data);
    })

const displayData = (userData) => {
    const container = document.getElementById("user-data-conatiner");

    userData.forEach(user => {
        const div = document.createElement("div");
        div.classList.add("user");

        div.innerHTML = `
        <h4>title</h4>
        <p>description</p>
        <button>details</button>

        `
        container.appendChild(div);

    });
}