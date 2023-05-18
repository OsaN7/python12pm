students = [
    {
        "name": "Mark", "age": 23, "address": {
        "country": [
            {"name": "USA"},
            {"name": "Nepal"}
        ]}
    },
    {
        "name": "Hari", "age": 50,
        "address": {"country": 
            [
                {"name": "India"},
                {"name": "China" }
            ]
        }
    }
]
# print(type(students))
for n in students:
    print(n["name"])
    print(n["address"]["country"][0]["name"])
# print(f'name is:', students[0]["name"])
# print(f'name is:', students[0]["name"], "address:", students[0]["address"]["country"]["name"])

        