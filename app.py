from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    units = int(request.form["units"])

    if units <= 100:
        energy_charge = units * 5
        message = "Great! You are an energy saver!"

    elif units <= 200:
        energy_charge = (100 * 5) + ((units - 100) * 7)
        message = "Not bad! Try saving a little more!"

    else: 
        energy_charge = (100 * 5) + (100 * 7) + ((units - 200) * 10)
        message = "Whoa! Your electricity usage is high!"

    service_charge = 50
    total_bill = energy_charge + service_charge

    return render_template(
        "index.html",
        units=units,
        energy_charge=energy_charge,
        service_charge=service_charge,
        bill=total_bill,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
