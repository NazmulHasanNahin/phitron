const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");
    if (param) {
        loadTime(param);
        fetchDoctorDetails(param);
        fetchDoctorReviews(param);
    }
};

const fetchDoctorDetails = (param) => {
    fetch(`https://testing-8az5.onrender.com/doctor/list/${param}`)
        .then(res => res.json())
        .then(displayDetails)
        .catch(error => console.error('Error fetching doctor details:', error));
};

const displayDetails = (doctor) => {
    const parent = document.getElementById("doc-details");
    const div = document.createElement("div");
    div.classList.add("doc-details-container");
    div.innerHTML = `
        <div class="doc-img">
            <img src=${doctor.image} alt="Doctor Image">
        </div>
        <div class="mx-5 doc-info">
            <h1 class="doc-name fw-bolder">${doctor.full_name}</h1>
            ${doctor.specialization.map(item => `<button class="doc-details-btn">${item}</button>`).join('')}
            <br>
            ${doctor.designation.map(item => `<h2 class="doc-details-btn-desig fw-bold">${item}</h2>`).join('')}
            <p class="des-dc w-50">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nisi hic dignissimos asperiores placeat perferendis nostrum distinctio quibusdam assumenda quasi eos.</p>
            <h4 class="fee-amnt">Fees: ${doctor.fee}</h4>
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Take Appointment</button>
        </div>
    `;
    parent.appendChild(div);
};

const fetchDoctorReviews = (param) => {
    fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
        .then(res => res.json())
        .then(doctordisplayReview)
        .catch(error => console.error('Error fetching doctor reviews:', error));
};

const doctordisplayReview = (reviews) => {
    const parent = document.getElementById("doc-details-review");
    reviews.forEach((review) => {
        const div = document.createElement("div");
        div.classList.add("review-card");
        div.innerHTML = `
            <img src="./images/review-img.png" alt="Review Image">
            <h4 class="fw-bold" style="font-family: 'DM Sans'; color: #007e85;">${review.reviewer}</h4>
            <p>${review.body.slice(0, 80)}</p>
            <h6>${review.rating}</h6>
        `;
        parent.appendChild(div);
    });
};

const loadTime = (id) => {
    fetch(
      `https://testing-8az5.onrender.com/doctor/availabletime/?doctor_id=${id}`
    )
      .then((res) => res.json())
      .then((data) => {
        data.forEach((item) => {
          const parent = document.getElementById("time-container");
          const option = document.createElement("option");
          option.value = item.id;
          option.innerText = item.name;
          parent.appendChild(option);
        });
        console.log(data);
      });
  };

const handleAppointment = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");
    const status = document.getElementsByName("status");
    const selected = Array.from(status).find((button) => button.checked);
    const symptom = document.getElementById("symptom");
    const time = document.getElementById("time-container");
    const selectedTime = time.options[time.selectedIndex];
    const patient_id = localStorage.getItem("patient_id");
    const info = {
        appointment_type: selected.value,
        appointment_status: "Pending",
        time: selectedTime.value,
        symptom: symptom,
        cancel: false,
        patient: patient_id,
        doctor: param,
    };

    console.log(info);
    fetch("https://testing-8az5.onrender.com/appointment/", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(info),
    })
        .then((res) => res.json())
        .then((data) => {
            window.location.href = `pdf.html?doctorId=${param}`;
            // handlePdf();
            // console.log(data);
        });
};


const loadPatientID = () => {
    const user_id = localStorage.getItem("user_id");

    fetch(`https://testing-8az5.onrender.com/patient/list/?user_id=${user_id}`)
        .then((res) => res.json())
        .then((data) => {
            localStorage.setItem("patient_id", data[0].id);
        });
};

const loadAllAppointments = () => {
    const patient_id = localStorage.getItem("patient_id");
    if (patient_id) {
        fetch(`https://testing-8az5.onrender.com/appointment/?patient_id=${patient_id}`)
            .then(res => res.json())
            .then((data) => {
                console.log('Appointments:', data);
            })
            .catch(error => console.error('Error fetching appointments:', error));
    } else {
        console.error('No patient ID found in local storage');
    }
};

loadPatientID();
getparams();
loadAllAppointments();
