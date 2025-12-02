from flask import Flask, jsonify, Response
import random
import matplotlib
matplotlib.use('Agg')  # important pour AlwaysData
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route("/")
def index():
    return "Bienvenue dans votre application de métriques Flask ! 🎯"

@app.route("/temperature")
def temperature():
    value = round(random.uniform(18, 25), 2)
    return jsonify({
        "metric": "temperature",
        "value": value,
        "unit": "°C"
    })

@app.route("/graph")
def graph():
    values = [random.randint(0, 10) for _ in range(10)]

    plt.figure(figsize=(6,4))
    plt.plot(values)
    plt.title("Graphique de test")
    plt.xlabel("Index")
    plt.ylabel("Valeur")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()

    return Response(img.getvalue(), mimetype="image/png")

if __name__ == "__main__":
    app.run()
