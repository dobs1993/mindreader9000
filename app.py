from flask import Flask, render_template, request, redirect, url_for, session
from predictor import PatternGuesser
from sequence_detector import detect_arithmetic_pattern

print("🚀 Flask is booting...")


app = Flask(__name__)
app.secret_key = 'your-secret-key'

guesser = PatternGuesser()
sequence = []
correct = 0
total = 0
last_result = None  # Store result separately

@app.route("/", methods=["GET", "POST"])
def index():
    global sequence, correct, total, last_result

    if request.method == "POST":
        user_input = request.form["user_input"].strip().lower()

        prediction = guesser.predict_next(sequence)
        if prediction == "?":
            prediction = detect_arithmetic_pattern(sequence)

        if prediction and user_input:
            if prediction == user_input:
                last_result = "✅ Correct!"
                correct += 1
            else:
                last_result = "❌ Wrong guess."
            total += 1

        sequence.append(user_input)
        guesser.train(sequence)
        return redirect(url_for("index"))

    # GET request — predict before user types
    prediction = guesser.predict_next(sequence)
    if prediction == "?":
        prediction = detect_arithmetic_pattern(sequence)

    return render_template("index.html", prediction=prediction,
                           guess_result=last_result,
                           correct=correct, total=total)


@app.route("/reset")
def reset():
    global sequence, correct, total, last_result
    sequence = []
    last_result = None
    return redirect(url_for("index"))

@app.route("/new")
def new_pattern():
    global sequence, last_result
    sequence = []
    last_result = None
    return redirect(url_for("index"))

@app.route("/end")
def end_game():
    global sequence, correct, total, last_result
    sequence = []
    correct = 0
    total = 0
    last_result = "🛑 Game ended."
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)