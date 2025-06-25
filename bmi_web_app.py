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
