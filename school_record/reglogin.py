import json

student = {
    "name": "Peter",
    "Roll_no": "0090014",
    "Grade": "A",
    "Age": 20,
    "subjects": [
        "Computer Graphics", "Discrete Mathematics", "Data Structure"
    ]
}

# with open("data.json", "w") as f:
#     json.dump(student, f, indent=4)
text = json.dumps(student, indent=4, sort_keys=True)
# print(text)

with open("data.json") as f:
    text = json.loads(text)
    print(text)
# with open("data.json", "r") as f:
#     text = json.load(f)
#     print(text)

