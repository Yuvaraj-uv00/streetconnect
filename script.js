const API = "http://127.0.0.1:5000";

function addVendor() {
    fetch(API + "/add_vendor", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: document.getElementById("name").value,
            food: document.getElementById("food").value,
            location: document.getElementById("location").value
        })
    }).then(res => res.json())
      .then(data => alert(data.message));
}

function getVendors() {
    fetch(API + "/get_vendors")
    .then(res => res.json())
    .then(data => {
        let list = document.getElementById("list");
        list.innerHTML = "";
        data.forEach(v => {
            let li = document.createElement("li");
            li.innerText = v[1] + " - " + v[2];
            list.appendChild(li);
        });
    });
}
