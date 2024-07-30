from flask import Flask,request,render_template,jsonify
from utils import Loan_Prediction

app = Flask(__name__)

LP = Loan_Prediction()

@app.route("/",methods =["GET","POST"])
def loan_predict():
    inputs = request.form

    Gender             = inputs["Gender"]
    Married            = inputs["Married"]
    Dependents         = inputs["Dependents"]
    Education          = inputs["Education"]
    Self_Employed      = inputs["Self_Employed"]
    ApplicantIncome    = eval(inputs["ApplicantIncome"])
    CoapplicantIncome  = eval(inputs["CoapplicantIncome"])
    LoanAmount         = eval(inputs["LoanAmount"])
    Loan_Amount_Term   = eval(inputs["Loan_Amount_Term"])
    Credit_History     = eval(inputs["Credit_History"])
    Property_Area      = inputs["Property_Area"]

    final_prediction = LP.main_prediction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)

    print([final_prediction])
    return [final_prediction]

if __name__ =="__main__":
    app.run(host="0.0.0.0",port = 5003,debug=True)

