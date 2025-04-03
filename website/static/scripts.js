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
