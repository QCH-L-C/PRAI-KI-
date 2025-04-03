from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home Route für die Website
@app.route("/")
def home():
    return render_template("index.html")

# Chat-Route für die PRAI-Chatbox
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    # Beispielantwort von PRAI (kann mit KI-Integration erweitert werden)
    response = f"PRAI sagt: '{user_input}' wurde empfangen und verarbeitet."
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
