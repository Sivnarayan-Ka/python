import csv

industries = {
    "FinTech":0,
    "Information Technology":0,
    "Consumer Technology":0,
    "Health and Wellness":0,
    "Accounting":0,
    "Automation":0,
    "other":0
}

with open("startup_funding.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        industry = row[3]
        print(f"industry is {industry}")
        if industry in industries.keys():
            industries[industry] += 1
        else:
            industries["other"] += 1 


print(industries)

for indrus in industries:
    print(f"{indrus}: {industries[indrus]}")