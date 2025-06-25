# Mini Python Projects 🚀

This repository contains a collection of simple, beginner-friendly Python projects that demonstrate basic programming concepts like input/output, conditionals, and functions.

## 📋 Projects

### 1. Daily Mood Tracker
A console-based tool to help users track their mood and get motivational quotes.

### 2. Simple Food Ordering Bot
A text-based food ordering system that calculates total bills with tax and optional delivery charges.

### 3. BMI Calculator
A tool to calculate Body Mass Index (BMI) and provide health feedback based on the BMI range.

### 4. Mini ATM Machine
Simulates an ATM interface allowing users to check balance, deposit, or withdraw money.

### 5. Speeding Fine Calculator
A tool to assess the fine or warning based on the user's entered speed.

## 📦 How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Mini-Python-Projects.git
   cd Mini-Python-Projects


## Run any script:

     Daily Mood Tracker.py


🛠️ Requirements
No external libraries required. These are pure Python scripts designed for educational and demonstration purposes.

🧠 Skills Practiced
User input

Conditional logic

Functions

Loops

Basic math

🏷️ License
This project is licensed under the MIT License.


Made by Arjav Jain 💻
---

## 🚀 Deployment Options

These are **console-based** projects, so "deployment" means making them easy to run:

### 1. 💻 **Local Running (Best for Beginners)**
- Just run via terminal or VS Code:
  ```bash
  python filename.py

2. 📁 Turn into a Simple GUI (Optional Upgrade)
You could use tkinter or PySimpleGUI in future versions for GUI-based interaction.

3. 🌐 Web Deployment (Advanced Option)
Wrap logic into Flask web apps.

Deploy using:
   Replit (easy)
   PythonAnywhere
   Render.com or Vercel (for full apps)

✅ Step 1: requirements.txt (Optional but Useful)

Even though these projects don’t use any external libraries, adding this file helps with deployment readiness.
               # No external packages needed

Later, if you add GUI or web versions, you might include:

            flask
            tkinter
            PySimpleGUI

✅ Step 2: Folder Structure for GitHub
Here’s the structure you should create locally:

Copy code
Mini-Python-Projects/
│
├── mood_tracker.py
├── food_ordering_bot.py
├── bmi_calculator.py
├── mini_atm.py
├── speeding_fine.py
├── README.md
└── requirements.txt

✅ Step 3: GitHub Upload (from your local machine)
🔧 Terminal Commands (in your folder)
bash
Copy code
cd Mini-Python-Projects
git init
git add .
git commit -m "Initial commit with Python projects"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Mini-Python-Projects.git
git push -u origin main

✅ Step 4: Want to Turn One Into a Web App?
Let’s try converting BMI Calculator into a Flask Web App as an example:

📄 bmi_web_app.py

python

from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<title>BMI Calculator</title>
<h2>Enter your details</h2>
<form method="POST">
  Weight (kg): <input name="weight" type="number" step="0.1" required><br>
  Height (m): <input name="height" type="number" step="0.01" required><br>
  <input type="submit" value="Calculate BMI">
</form>
{% if bmi %}
  <h3>Your BMI is: {{ bmi }}</h3>
  <p>{{ status }}</p>
{% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def bmi():
    bmi = status = None
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        bmi = round(weight / (height ** 2), 2)
        if bmi < 18.5:
            status = "You are Underweight."
        elif 18.5 <= bmi < 25:
            status = "You are Normal weight."
        elif 25 <= bmi < 30:
            status = "You are Overweight."
        else:
            status = "You are Obese."
    return render_template_string(TEMPLATE, bmi=bmi, status=status)

if __name__ == "__main__":
    app.run(debug=True)


Install Flask and Run:

pip install flask
python bmi_web_app.py


Then visit http://localhost:5000 in your browser.

✅ Step 5: Optional Deployment Online (Free)

Use Replit
      Create a new Python Repl
      Paste your code
      Add flask in the "Packages"
      Click "Run"
      Replit gives you a live web URL
