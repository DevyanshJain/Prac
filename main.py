import json
import os

def load_marks():
    file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    # Convert list of dicts to a name:marks dictionary
    return {entry['name']: entry['marks'] for entry in data}

student_marks = load_marks()

def handler(request, response):
    names = request.query.getlist('name')
    marks = [student_marks.get(name, None) for name in names]
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    response.body = json.dumps({"marks": marks})
    return response
