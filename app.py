from flask import Flask, render_template, request, jsonify
from chat import get_response

# DO CORS 
from flask import Flask
from flask_cors import CORS



app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})




@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)



    
