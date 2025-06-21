from flask import Flask, render_template, request, redirect, url_for, send_file
from scraper import scrape_website
import pandas as pd
from io import BytesIO
import json
import time
from waitress import serve


app = Flask(__name__)

# Default elements to scrape (can be modified by user)
DEFAULT_ELEMENTS = {
    'titles': 'h1, h2, h3',
    'paragraphs': 'p',
    'links': 'a'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        custom_elements = request.form.get('elements')
        
        # Parse custom elements if provided
        elements = DEFAULT_ELEMENTS
        if custom_elements:
            try:
                elements = json.loads(custom_elements)
                if not isinstance(elements, dict):
                    elements = DEFAULT_ELEMENTS
            except:
                elements = DEFAULT_ELEMENTS
        
        # Scrape the website
        result = scrape_website(url, elements)
        
        if result['status'] == 'success':
            return render_template('results.html', 
                                data=result['data'], 
                                url=result['url'],
                                elements=elements)
        else:
            return render_template('index.html', 
                                error=result['message'])
    
    return render_template('index.html')

@app.route('/export', methods=['POST'])
def export_data():
    data = request.form.get('data')
    export_type = request.form.get('export_type')
    
    try:
        data_dict = json.loads(data)
        df = pd.DataFrame.from_dict(data_dict, orient='index').transpose()
        
        if export_type == 'csv':
            output = BytesIO()
            df.to_csv(output, index=False)
            output.seek(0)
            timestamp = int(time.time())
            return send_file(
                output,
                mimetype='text/csv',
                as_attachment=True,
                download_name=f'scraped_data_{timestamp}.csv'
            )
            
        elif export_type == 'json':
            output = BytesIO()
            df.to_json(output, orient='records', indent=2)
            output.seek(0)
            timestamp = int(time.time())
            return send_file(
                output,
                mimetype='application/json',
                as_attachment=True,
                download_name=f'scraped_data_{timestamp}.json'
            )
            
    except Exception as e:
        return redirect(url_for('index'))

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
if __name__ == '__main__':
    print("🟢 Starting Flask application...")  # Debug line
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
        print("🔴 Server stopped unexpectedly!")  # Will show if crashes
    except Exception as e:
        print(f"💥 CRASH: {str(e)}")