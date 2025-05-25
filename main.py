import json
import os

def load_marks():
    file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-pthon.json')
    with open(file_path, 'r') as f:
        return json.load(f)

student_marks = load_marks()

def handler(request, response):
    names = request.query.getlist('name')
    marks = [student_marks.get(name, None) for name in names]
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    response.body = json.dumps({"marks": marks})
    return response
