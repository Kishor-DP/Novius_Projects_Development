from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Read the CSV file
    df = pd.read_csv('Csv_files/Gridviewtbl.csv')
    
    # Convert the DataFrame to HTML
    data = df.to_html(classes='table table-striped', index=False)
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
