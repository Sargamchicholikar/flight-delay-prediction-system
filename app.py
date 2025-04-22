from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle
import os
from datetime import datetime

app = Flask(__name__)

# Load the model
# Note: In a real implementation, you would have a trained model saved as pickle file
# For demonstration purposes, we'll create a placeholder prediction function
# model_path = os.path.join('models', 'random_forest_model.pkl')
# model = pickle.load(open(model_path, 'rb'))

def predict_delay(features):
    """
    Placeholder function for delay prediction.
    In a real implementation, this would use the loaded model.
    """
    # This is a mock prediction - in reality you would use:
    # prediction = model.predict([features])
    
    # Simulating a prediction based on input features
    hour = features.get('hour', 12)
    
    # Higher delays in late afternoon/evening
    if 15 <= hour <= 21:
        base_delay = 25
    else:
        base_delay = 10
    
    # Add carrier effect
    carrier_effect = {
        'UA': 5,  # United tends to have more delays
        'AA': 3,  # American Airlines moderate delays
        'DL': 0,  # Delta better performance
        'B6': 2   # JetBlue moderate delays
    }
    
    carrier = features.get('carrier', 'UA')
    delay = base_delay + carrier_effect.get(carrier, 0)
    
    # Add distance effect
    distance = features.get('distance', 1000)
    if distance > 1500:
        delay += 10
    elif distance < 500:
        delay -= 5
    
    # Add day of week effect (0=Monday, 6=Sunday)
    day_of_week = features.get('day_of_week', 0)
    if day_of_week in [0, 4]:  # Monday or Friday
        delay += 8
    
    # Add randomness to simulate model prediction variance
    delay += np.random.normal(0, 5)
    
    return max(0, delay)  # Ensure no negative delays

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form data
            carrier = request.form['carrier']
            origin = request.form['origin']
            dest = request.form['dest']
            
            # Parse datetime
            dep_datetime_str = request.form['dep_datetime']
            dep_datetime = datetime.strptime(dep_datetime_str, '%Y-%m-%dT%H:%M')
            
            hour = dep_datetime.hour
            day_of_week = dep_datetime.weekday()  # 0=Monday, 6=Sunday
            month = dep_datetime.month
            
            # Calculate distance (mock calculation for demo)
            # In real app, you would have a lookup table or API for airport distances
            distance_lookup = {
                ('JFK', 'LAX'): 2475,
                ('JFK', 'SFO'): 2586,
                ('JFK', 'ORD'): 740,
                ('LGA', 'ATL'): 762,
                ('LGA', 'MIA'): 1097,
                ('EWR', 'DEN'): 1605,
                ('EWR', 'DFW'): 1372,
            }
            
            distance = distance_lookup.get((origin, dest), 1000)  # Default if not found
            
            # Create feature dictionary
            features = {
                'carrier': carrier,
                'origin': origin,
                'dest': dest,
                'hour': hour,
                'day_of_week': day_of_week,
                'month': month,
                'distance': distance
            }
            
            # Make prediction
            predicted_delay = predict_delay(features)
            
            # Format for display
            prediction_result = {
                'delay': round(predicted_delay, 1),
                'factors': []
            }
            
            # Add explanation factors
            if hour >= 15 and hour <= 21:
                prediction_result['factors'].append('Evening departure (higher delay risk)')
            
            if day_of_week in [0, 4]:
                prediction_result['factors'].append('Monday/Friday flight (busy travel day)')
                
            if distance > 1500:
                prediction_result['factors'].append('Long-haul flight (>1500 miles)')
                
            if carrier == 'UA':
                prediction_result['factors'].append('Carrier historically has higher delays')
            
            return render_template('result.html', prediction=prediction_result, features=features)
            
        except Exception as e:
            return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
