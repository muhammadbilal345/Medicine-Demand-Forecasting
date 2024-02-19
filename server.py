import util
import pandas as pd
from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)

@app.route('/predict_sales', methods=['GET', 'POST'])
def sales_prediction():
    drug_name = request.args.get('drug')
    n_years = int(request.args.get('year'))

    pred_sales = util.predict_sales(drug_name, n_years)
    reviews, ratings = util.get_reviews_and_ratings(drug_name, pd.read_csv('sentiments.csv'))

    print(f'drug_name: {drug_name}')
    print(f'n_years: {n_years}')

    response = {
        'predictions': pred_sales.to_dict('records'),
        'reviews': reviews,
        'ratings': ratings
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
