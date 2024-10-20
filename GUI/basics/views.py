from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Create your views here.
def index(request):
  return render(request,'index.html')






from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import math

def is_valid_number(value):
    try:
        float_value = float(value)
        return not (math.isnan(float_value) or math.isinf(float_value))
    except ValueError:
        return False

def iris(request):
    if request.method == 'POST':
        area_code = request.POST.get('area_code')
        locality_code = request.POST.get('locality_code')
        region_code = request.POST.get('region_code')
        height = request.POST.get('height')
        diameter = request.POST.get('diameter')
        species = request.POST.get('species')

        # Check if all inputs are valid numeric values or None
        if not all(is_valid_number(val) or val is None for val in [area_code, locality_code, region_code, height, diameter, species]):
            return render(request, 'iris.html', {'error_message': 'Invalid input. Please enter valid numeric values.'})

        # Convert valid inputs to float, keeping None values as None
        area_code = float(area_code) if area_code is not None else None
        locality_code = float(locality_code) if locality_code is not None else None
        region_code = float(region_code) if region_code is not None else None
        height = float(height) if height is not None else None
        diameter = float(diameter) if diameter is not None else None
        species = float(species) if species is not None else None

        # Load the dataset
        path = "D:\\B.tech\\karnadu intership\\py\\final project\\sir\\16_flowerclassrecognition\\iris.csv"
        data = pd.read_csv(path)

        # Separate features (X) and target variable (y)
        inputs = data.drop(['Class'], axis=1)
        output = data['Class']

        # Split the dataset
        x_train, x_test, y_train, y_test = train_test_split(inputs, output, train_size=0.8)

        # Train the model
        model = GaussianNB(var_smoothing=1e-9)  # Adjust var_smoothing if needed
        model.fit(x_train, y_train)

        # Make prediction
        result = model.predict([[area_code, locality_code, region_code, height, diameter, species]])

        return render(request, 'iris.html', {'result': result[0]})

    return render(request, 'iris.html')