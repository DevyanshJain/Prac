import csv
import json
import os

# Load marks from the CSV file once at cold start
def load_marks():
    marks = {}
    file_path = os.path.join(os.path.dirname(__file__), 'marks.csv')
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            marks[row['name']] = int(row['mark'])
    return marks

# This will be loaded once per serverless cold start
student_marks = load_marks()

def handler(request, response):
    # Get all 'name' query parameters
    names = request.query.getlist('name')
    marks = [student_marks.get(name, None) for name in names]
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    response.body = json.dumps({"marks": marks})
    return response
