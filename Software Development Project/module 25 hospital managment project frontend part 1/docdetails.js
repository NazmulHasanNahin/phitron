const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");
    fetch(`https://testing-8az5.onrender.com/doctor/list/${param}`)
        .then(res => res.json())
        .then((data) => displayDeteails(data));


    fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
    .then((res)=>res.json())
    .then((data)=>{
        doctordisplayReview(data);
    });

};
const displayDeteails = (doctor) => {
    const parent = document.getElementById("doc-details");
    const div=document.createElement("div");
    div.classList.add("doc-details-container");
    div.innerHTML=`
    <div class="doc-img">
            <img src=${doctor.image} alt="">
        </div>
    <div class="mx-5 doc-info">
        <h1 class="doc-name fw-bolder">${doctor.full_name}</h1>
        ${
            doctor.specialization.map((item)=>{
                return `<button class="doc-details-btn">${item}</button>`
            })
        }
        </br>
        ${
            doctor.designation.map((item)=>{
                return `<h2 class="doc-details-btn-desig fw-bold">${item}</h2>`
            })
        }
        <p class="des-dc w-50">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nisi hic dignissimos asperiores
            placeat
            perferendis nostrum distinctio quibusdam assumenda quasi eos.</p>
        <h4 class="fee-amnt">Fees:${doctor.fee}</h4>
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Take Appointment
        </button>
    </div>
    `;
    parent.appendChild(div);
}


const doctordisplayReview = (reviews) => {
    reviews.forEach((review) => {
        const parent = document.getElementById("doc-details-review");
        const div = document.createElement("div");
        div.classList.add("review-card");
        div.innerHTML = `
            <img src="./images/review-img.png" alt="">
            <h4 class="fw-bold" style="font-family: 'DM Sans'; color: #007e85;">${review.reviewer}</h4>
            <p>${review.body.slice(0, 80)}
            </p>
            <h6>${review.rating}</h6>
        `;
        parent.appendChild(div)
    })
}

getparams();