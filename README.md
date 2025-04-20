# 🧠 MindReader9000

MindReader9000 is an AI pattern prediction web app that attempts to guess your next input based on a learned sequence. 

Built using **Python**, **Flask**, and deployed for free on **Render**, the app handles user input patterns like:
- Arithmetic sequences (e.g. `1, 2, 3...`)
- Alphabetic sequences (e.g. `a, b, c...`)
- Repeating or predictable patterns

### 🔮 How It Works
- Users type in letters or numbers one by one.
- The AI tries to guess what comes next based on prior inputs.
- Feedback is given on whether the guess was correct.
- Users can **reset**, **start a new pattern**, or **end the game**.

### 🧱 Tech Stack
- Python 3.10  
- Flask  
- HTML/CSS (custom neon theme)  
- Deployed via [Render](https://render.com)  
- Version controlled with Git/GitHub

### 💻 Try It Out
🟢 [Live App](https://mindreader9000.onrender.com)

> Note: On free hosting, the server may take a few seconds to spin up.

---

### 🔧 Local Setup
```bash
git clone https://github.com/dobs1993/mindreader9000.git
cd mindreader9000
pip install -r requirements.txt
python app.py
