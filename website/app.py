from flask import Flask, render_template, request, jsonify
import dns_diagnosis

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

@app.route("/dns_status")
def dns_status():
    domain = "rfof-network.org"
    diagnosis_result = dns_diagnosis.diagnose_domain(domain)
    instructions = dns_diagnosis.troubleshooting_instructions()
    cache_status = dns_diagnosis.flush_dns_cache()
    return jsonify({
        "domain": domain,
        "cache_status": cache_status,
        "diagnosis": diagnosis_result,
        "troubleshooting_instructions": instructions
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

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



from flask import Flask, jsonify, render_template
import dns_diagnosis

app = Flask(__name__)

@app.route("/")
def index():
    # Hier wird das kombinierte Template (z.B. index.html) geladen,
    # das Deine Sandbox und Statusinformationen anzeigt.
    return render_template("index.html")

@app.route("/dns_status")
def dns_status():
    domain = "rfof-network.org"
    diagnosis_result = dns_diagnosis.diagnose_domain(domain)
    instructions = dns_diagnosis.troubleshooting_instructions()
    cache_status = dns_diagnosis.flush_dns_cache()
    return jsonify({
        "domain": domain,
        "cache_status": cache_status,
        "diagnosis": diagnosis_result,
        "troubleshooting_instructions": instructions
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


