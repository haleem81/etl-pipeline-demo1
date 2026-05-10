data = [
 {"name":" haleem ", "age":"25", "salary":"50000"},
 {"name":"john", "age":"17", "salary":"40000"}
]

cleaned_data = []

for row in data:
    row["name"] = row["name"].strip().title()
    row["age"] = int(row["age"])
    row["salary"] = int(row["salary"])

    if row["age"] < 18:
        continue

    cleaned_data.append(row)

print(cleaned_data)