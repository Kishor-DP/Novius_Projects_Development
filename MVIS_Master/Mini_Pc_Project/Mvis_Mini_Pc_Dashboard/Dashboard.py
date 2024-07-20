from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Route to get logs from Gridviewtbl.csv
@app.route('/api/Gridviewtbl', methods=['GET'])
def get_logs():
    df = pd.read_csv('Csv_files/Gridviewtbl.csv')
    data = df.to_dict(orient='records')
    return jsonify(data)

# Route to get logs from Mvis_Events.csv
@app.route('/api/mvis-events', methods=['GET'])
def get_mvis_events():
    df = pd.read_csv('Csv_files/Mvis_Events.csv')
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
