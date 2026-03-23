# import required libraries
from flask import Flask, request, jsonify   # Flask = API framework, request = get input, jsonify = send JSON response
import pickle                               # used to load trained ML model

# create Flask app instance
app = Flask(__name__)

# load the trained model from file (read binary mode)
model = pickle.load(open('model.pkl', 'rb'))

# home route (test if API is running)
@app.route('/')
def home():
    return "Api is Running"

# prediction route (POST method because we send data)
@app.route("/predict", methods=['POST'])
def predict():
    data = request.json              # get JSON data from request body
    exp = data["experience"]         # extract 'experience' value from input

    result = model.predict([[exp]])  # model expects 2D array → [[value]]

    return jsonify({
        "salary": int(result[0])     # convert prediction to int and return as JSON
    })

# run the app
if __name__ == "__main__":
    app.run(debug=True)              # debug=True = auto reload + error logs