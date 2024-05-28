from flask import Flask, render_template, request, jsonify, send_file
import os
import requests

app = Flask(__name__)

CONFIG = {
    'api_key': os.getenv('OPENAI_API_KEY', 'APIKEY'),
    'api_url': 'https://api.openai.com/v1/chat/completions'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json.get('message')
    response = send_to_openai(user_input)
    return jsonify({'response': response})

def send_to_openai(text):
    headers = {
        'Authorization': f'Bearer {CONFIG["api_key"]}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': text}],
        'max_tokens': 150
    }
    try:
        response = requests.post(CONFIG['api_url'], headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        return response_json['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Request error occurred: {req_err}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
