from flask import Flask,render_template,request
from sklearn.linear_model import LogisticRegression
import joblib


app = Flask(__name__)   # app is the object name.


@app.route('/')
def index():  # put application's code here
    return render_template('index1.html')




#FOR PREDICT.
@app.route('/prediction',methods=['POST','GET'])
def prediction():
        b=[]
        try:
            if request.method=="POST":
                Gender=request.form['Gender']
                Married=request.form['Married']
                Education=request.form['Education']
                Self_Employed=request.form['Self_Employed']
                ApplicantIncome=request.form['Applicant_Income']
                CoapplicantIncome=request.form['Coapplicant_Income']
                LoanAmount=request.form['LoanAmount']
                Loan_Amount_Term=request.form['Loan_Amount_Term']
                Credit_History=request.form['Credit_History']
                Property_Area=request.form['Property_Area']
                b.extend([Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])
                model = joblib.load('lrmodel.pkl')
                y_pred=model.predict([b])
                return render_template('prediction.html',msg="success",op=y_pred)
        except:
            pass
        return render_template('prediction.html')

if __name__ == '__main__':

    app.run(debug=True)