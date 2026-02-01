document.getElementById("file-input").onchange = function(event) {
    let reader = new FileReader();
    reader.onload = function(e) {
        let img = document.getElementById("uploaded-image");
        img.src = e.target.result;
        img.style.display = "block";
    };
    reader.readAsDataURL(event.target.files[0]);
};

document.getElementById("upload-form").onsubmit = async function(event) {
    event.preventDefault();
    
    let formData = new FormData(this);
    let response = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    let result = await response.json();
    document.getElementById("result").innerText = result.prediction || result.error;
};
