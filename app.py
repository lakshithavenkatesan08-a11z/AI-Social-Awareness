from flask import Flask, render_template, request

app = Flask(__name__)

campaigns = {
    "Environment": {
        "message": "Protect nature for a better future.",
        "slogan": "Go Green, Keep It Clean!",
        "caption": "🌍 Save Earth! Plant trees and reduce plastic. #SaveEarth #GoGreen",
        "why": "A clean environment protects people, animals, and plants.",
        "tips": [
            "Plant more trees.",
            "Avoid single-use plastics.",
            "Keep your surroundings clean."
        ]
    },
    "Road Safety": {
        "message": "Follow traffic rules to protect every life.",
        "slogan": "Safety First, Always!",
        "caption": "🚦 Follow traffic rules and save lives! #RoadSafety",
        "why": "Road safety helps prevent accidents and protect lives.",
        "tips": [
            "Wear a helmet.",
            "Use seat belts.",
            "Follow traffic signals."
        ]
    },
    "Water Conservation": {
        "message": "Every drop of water is precious.",
        "slogan": "Save Water, Save Life!",
        "caption": "💧 Save water today for a better tomorrow! #SaveWater",
        "why": "Water conservation helps ensure clean water for the future.",
        "tips": [
            "Turn off taps when not in use.",
            "Fix leaking taps.",
            "Reuse water when possible."
        ]
    },
    "Mental Health": {
        "message": "Your mental health matters. It is okay to ask for help.",
        "slogan": "It's Okay to Talk!",
        "caption": "💚 Be kind, listen, and support one another. #MentalHealthAwareness",
        "why": "Mental health awareness encourages understanding and support.",
        "tips": [
            "Listen without judging.",
            "Talk to someone you trust.",
            "Be kind to yourself and others."
        ]
    }
}


@app.route("/", methods=["GET", "POST"])
def home():
    selected_topic = ""
    campaign = None

    if request.method == "POST":
        selected_topic = request.form.get("topic", "")
        campaign = campaigns.get(selected_topic)

    return render_template(
        "index.html",
        topics=campaigns.keys(),
        selected_topic=selected_topic,
        campaign=campaign
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)