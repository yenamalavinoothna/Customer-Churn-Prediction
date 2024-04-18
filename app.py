import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
flask_app=Flask(__name__)
model=pickle.load(open("trained_model.pkl","rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict",methods=["POST"])
def predict():
    f=[float(x) for x in request.form.values()]
    print(f)
    features=[np.array(f)]
    prediction=model.predict(features)
    if prediction[0]==0:
        return render_template("index.html",prediction_text="There will be no churn")
    else:
        return render_template("index.html", prediction_text="There will be churn")
if __name__=="__main__":
    flask_app.run(debug=True)

