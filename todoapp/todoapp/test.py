start = {
    "id": 1,
    "username": "django",
    "first_name": "alex",
    "last_name": "fox",
    "email": "25"
}

end = {
    "id": 1,
    "username": "gopa",
    "first_name": "alex",
    "last_name": "gopa",
    "email": "dsad@dfds.23"
}

for i,j in start.items():
    print(i, j)
    end[i] = j


print(f' это энд {end}')