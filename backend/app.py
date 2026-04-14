from flask import Flask, request, jsonify
from flask_cors import CORS
from vulnerabilities.missing_security_headers import scan_security_headers

app = Flask(__name__)
CORS(app)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    target = data.get('target', '')
    
    if not target:
        return jsonify({'error': 'Target is required'}), 400
    
    if not target.startswith(('http://', 'https://')):
        target = 'https://' + target
    
    result = scan_security_headers(target)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)