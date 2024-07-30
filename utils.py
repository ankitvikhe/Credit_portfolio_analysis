import pandas as pd
import numpy as np
import pickle
import json


class Loan_Prediction():
    def pickle_files(self):
        with open("Project_data.json","r") as f:
            self.data = json.load(f)

        with open("rf_model.pkl","rb") as f:
            self.model = pickle.load(f)

    def main_prediction(self,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
        self.pickle_files()

        test_array = np.zeros(11)

        test_array[0]  = self.data["Gender"][Gender]
        test_array[1]  = self.data["Married"][Married]
        test_array[2]  = self.data["Dependents"][Dependents]
        test_array[3]  = self.data["Education"][Education]
        test_array[4]  = self.data["Self_Employed"][Self_Employed]
        test_array[5]  = ApplicantIncome
        test_array[6]  = CoapplicantIncome
        test_array[7]  = LoanAmount
        test_array[8]  = Loan_Amount_Term
        test_array[9]  = Credit_History
        test_array[10] = self.data["Property_Area"][Property_Area]

        print("Test_Array : ",test_array)

        prediction = self.model.predict([test_array])
        print("Actual Prediction :",prediction[0])

        if prediction[0] == 0:
            print("Loan Decline")
            return "Loan Decline"
        
        else :
            print("Loan Approved")
            return "Loan Approved"


