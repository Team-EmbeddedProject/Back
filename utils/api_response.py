from flask import jsonify
from datetime import datetime

def format_response(data):
    return jsonify({'result': 'success', 'data': data})

def format_error_response(error, status_code=500):
    return jsonify({'result': 'error', 'message': str(error)}), status_code
