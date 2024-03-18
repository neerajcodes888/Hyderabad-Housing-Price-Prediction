from flask import Flask, render_template,request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('Final Model')

@app.route('/')
def home():
    return render_template("index.html")




def price_prediction(bhk, property_age, property_size, totalfloors, facing, furnishing, locality, park, waterSupply, number_of_amenities):
    X = np.zeros(98)
    X[0] = bhk
    X[1] = property_age
    X[2] = property_size
    X[3] = totalfloors
    X[97] = number_of_amenities
    
    columns = ['locality', 'facing', 'furnishing', 'parking', 'waterSupply']
    values = [locality, facing, furnishing, park, waterSupply]
    
    for column, value in zip(columns, values):
        if value in range(98):
            X[x.columns.get_loc(value)] = 1
    
    return X

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        pass
    else:
        return render_template("prediction.html")
        














if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')