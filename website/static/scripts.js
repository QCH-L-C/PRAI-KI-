function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response-output").innerText = data.response;
    })
    .catch(error => {
        document.getElementById("response-output").innerText = "Fehler: " + error;
    });
}

function loadData(storageType) {
    fetch(`/view/${storageType}?user=Satoramy`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Zugriff verweigert! Nur Satoramy darf die Daten sehen.");
            }
            return response.json();
        })
        .then(data => {
            const container = document.getElementById(`${storageType}net-data`);
            container.innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            alert(error.message);
        });
}
