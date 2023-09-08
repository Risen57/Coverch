from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from os import system

app = Flask(__name__)

# Home screen page, displays global info
@app.route("/", methods = ["GET", "POST"])
def home():
    r = requests.get("https://disease.sh/v3/covid-19/all")
    r = r.text
    info = json.loads(r)

    return render_template("index.html", info=info)

@app.route("/countries", methods = ["GET", "POST"])
def countries():
    if request.method == 'POST':
        country = request.form['country'].lower()
        return redirect(url_for('country', country=country))

    return render_template("countries.html")
@app.route("/country", methods=['GET', 'POST'])
def country():
    country = request.form.get('country')
    r = requests.get(f"https://disease.sh/v3/covid-19/countries/{country}")
    print(r)
    r = r.text
    print(r)
    info = json.loads(r)
    print(r)
    print(info["cases"], info["active"], info["deaths"])
    return render_template("countinf.html", info=info)

# # Contry-wise info
# country = input("Enter the name of the country => ").lower()
# print("Loading...")

# r = requests.get(f"https://disease.sh/v3/covid-19/countries/{country}")
# r = r.text
# info = json.loads(r)

# # try:
# #     system('clear')
# #     print(f"""
# #     {country} info:
# #     Total Cases: {info["cases"]}
# #     Active Cases: {info["active"]}
# #     Total Deaths: {info["deaths"]}
# #     """)
# # except KeyError:
# #     print("The country doesn't exist! Check if there's a typo")

# input("Press Enter to continue")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
