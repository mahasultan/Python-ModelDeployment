from flask import Flask, request, jsonify
from predict import predict # importing

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/predict', methods=['POST'])
def predict_route():
    try:
        request_data = request.get_json()
        print("Starting to predict:")
        result = predict(request_data)
        print("Finished to predicting:")

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)  