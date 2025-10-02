from flask import Flask, render_template, request, url_for 
import pickle

app = Flask(__name__)

#load the model
deploy_model = pickle.load(open('savedmodel.sav', 'rb'))

#create homepage to display
@app.route('/')
def home():
    result = ''
    result2 = ''
    return render_template('price.html', **locals())

#function to take inputs and create a prediction
@app.route('/price', methods=['POST', 'GET'])
def price():
    GrLivArea = float(request.form['GrLivArea'])
    LotArea = float(request.form['LotArea'])
    OverallQual = float(request.form['OverallQual'])
    MortgageOwed = float(request.form['MortgageOwed'])
    result = int(deploy_model.predict([[GrLivArea, LotArea, OverallQual]])[0])
    result2 = int(result * .94 - MortgageOwed)
    return render_template('price.html', **locals())

#Creating an about page 
@app.route('/about')
def about():
    return render_template('about.html', **locals())

#Create page for resume
@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True) 



