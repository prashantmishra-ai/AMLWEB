from flask import Flask, render_template, request
import json
import urllib.request
app = Flask(__name__)
job = ["technician", "unknown", "blue-collar", "admin.","housemaid", "retired","services", "entrepeneur", "unemployed", "management", "self-employed", "student"]
marital = ["married","divorced", "single", "unknown"]
education = ["high.school","unknown","basic.9y", "professional.course", "university.degree", "basic.4y","basic.6y","illiterate"]
housing=["no", "unknown","yes"]
default = ["no", "unknown","yes"]
loan = ["no", "unknown","yes"]
contact = ["cellular", "telephone"]
month = ["may","jun","jul","aug","oct","nov","apr","mar","sep","dec"]
poutcome = ["failure","nonexistent","success"]

@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method) == "GET":
        return render_template("index.html", job=job, marital=marital, education=education, housing=housing, default=default, loan=loan, contact=contact, month=month, poutcome=poutcome)
    elif (request.method) == "POST":
       data =  {
      "Inputs": {
        "data": [
          {
            "age": request.form.get("age"),
            "job": request.form.get("job"),
            "marital": request.form.get("marital"),
            "education": request.form.get("education"),
            "default": request.form.get("default"),
            "housing": request.form.get("housing"),
            "loan": request.form.get("loan"),
            "contact": request.form.get("contact"),
            "month": request.form.get("month"),
            "duration": request.form.get("duration"),
            "campaign": request.form.get("campaign"),
            "pdays": request.form.get("pdays"),
            "previous": request.form.get("previous"),
            "poutcome": request.form.get("poutcome"),
            "emp.var.rate": request.form.get("emp.var.rate"),
            "cons.price.idx": request.form.get("cons.price.idx"),
            "cons.conf.idx": request.form.get("cons.conf.idx"),
            "euribor3m": request.form.get("euribor3m"),
            "nr.employed": request.form.get("nr.employed")
          }
        ]
      },
      "GlobalParameters": {
        "method": "predict"
      }
    }

    body = str.encode(json.dumps(data))
    url = 'http://b1938ad5-c932-455d-8d1f-9b56a24ff51a.eastus2.azurecontainer.io/score'
    api_key = ''
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    response = urllib.request.urlopen(req)
    result = response.read()
    dict_str = json.loads(result.decode("UTF-8"))
    my_data = dict_str
    output = my_data.get("Results")[0]
    return render_template("index.html", output=output)
    
app.run(port=3000, host='0.0.0.0')