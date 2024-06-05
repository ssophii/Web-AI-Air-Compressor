from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

app = Flask(__name__)

# Load dataset
data = pd.read_csv("Datasets/air-comp.csv", sep=",")
x_data = data.drop(["id", "acmotor"], axis=1)
x_data['bearings'] = [0 if each == "Ok" else 1 for each in data.bearings]
x_data['wpump'] = [0 if each == "Ok" else 1 for each in data.wpump]
x_data['radiator'] = [0 if each == "Clean" else 1 for each in data.radiator]
x_data['exvalve'] = [0 if each == "Clean" else 1 for each in data.exvalve]

splitted_data = np.split(x_data, [20], axis=1)
x_data = splitted_data[0]
y_data = splitted_data[1]

norm_minmaxdata = {'minnorm': [0, 0, 0, 0, 0, 30, 60, 0, 30, 30, 200, 30, 250, 40, 0, 0, 0, 0, 0, 0], 
                   'maxnorm': [3000, 25000, 150, 12, 1800, 100, 200, 6, 150, 200, 275, 80, 320, 50, 2, 2, 12, 2, 2, 10]}
norm_minmax = pd.DataFrame(norm_minmaxdata, columns=['minnorm', 'maxnorm'])
minnorm = norm_minmax.minnorm.values
maxnorm = norm_minmax.maxnorm.values
x_norm = (x_data - minnorm) / (maxnorm - minnorm)

# Load model
model = load_model('Models/model.keras')

# Define interpretation of predicted classes
class_descriptions = {
    0: "Normal: The machine is operating within normal parameters.",
    1: "Warning: The machine shows signs of potential issues and may require maintenance soon.",
    2: "Critical: The machine is at risk of imminent failure and needs immediate attention."
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/model-summary')
def model_summary():
    # Summary of the model
    summary = []
    model.summary(print_fn=lambda x: summary.append(x))
    model_summary = "\n".join(summary)

    # Plot accuracy
    history = pd.read_csv('history.csv')
    plt.plot(history['accuracy'])
    plt.plot(history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.savefig('static/accuracy.png')
    plt.clf()

    # Plot loss
    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.savefig('static/loss.png')
    plt.clf()

    return render_template('model_summary.html', model_summary=model_summary, columns=x_data.columns)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        input_values = []
        for col in x_data.columns:
            input_values.append(float(request.form[col]))

        input_array = np.array(input_values).reshape(1, -1)
        input_norm = (input_array - minnorm) / (maxnorm - minnorm)
        
        prediction = model.predict(input_norm)
        predicted_class = np.argmax(prediction, axis=1)[0]
        class_description = class_descriptions.get(predicted_class, "Unknown")

        return render_template('predict.html', prediction=prediction, predicted_class=predicted_class, class_description=class_description)
    else:
        return render_template('predict_form.html', columns=x_data.columns)

if __name__ == '__main__':
    app.run(debug=True)
