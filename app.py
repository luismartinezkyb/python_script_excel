from flask import Flask, request, jsonify
import openpyxl
import requests
import base64

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        workbook = openpyxl.load_workbook(file)
        worksheet = workbook.active
        data = []
        # return jsonify({'message': 'File uploaded successfully', 'data': worksheet.to_})
        for row in worksheet.iter_rows(values_only=True):
            data_row = {}
            app.logger.info(row)

            for index, value in enumerate(row, start=1):
                data_row[index] = value
            data.append(data_row)
        
        return jsonify({'message': 'File uploaded successfully'})

        for item in data:
            image_url = item.get(2)
            if image_url:
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    image_base64 = base64.b64encode(image_response.content).decode('utf-8')
                    processed_item = {**item, 'image_base64': f"data:image/jpeg;base64,{image_base64}"}
                    processed_data.append(processed_item)
        
        return jsonify({'message': 'File uploaded successfully', 'data': processed_data})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

