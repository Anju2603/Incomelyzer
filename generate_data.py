import pandas as pd
import random

def generate_data(n):
    data = []
    for _ in range(n):
        Family_size = random.randint(2, 10)
        occupation = random.choice(['Labour', 'Farmer', 'Teacher', 'Doctor', 'Private Job', 'Govt Job', 'Business'])
        House_type = random.choice(['Own', 'Rented'])
        Vehicles = random.randint(0, 2)
        electricity = random.randint(100, 1000)
        Education_level = random.choice(['None', 'Primary', 'Secondary', 'Graduate', 'Post-Graduate'])
        Area = random.choice(['Rural', 'Urban'])

        if occupation == 'Labour':
            income = random.randint(5000, 10000)
        elif occupation == 'Farmer':
            income = random.randint(6000, 12000)
        elif occupation == 'Teacher':
            income = random.randint(12000, 14000)
        elif occupation == 'Doctor':
            income = random.randint(30000, 40000)
        elif occupation == 'Private Job':
            income = random.randint(25000, 30000)
        elif occupation == 'Govt Job':
            income = random.randint(60000, 80000)
        elif occupation == 'Business':
            income = random.randint(70000, 90000)

        if income < 8000:
            bracket = 'BPL'
        elif income < 15000:
            bracket = 'Low'
        elif income < 50000:
            bracket = 'Medium'
        else:
            bracket = 'High'

        data.append([
            Family_size, occupation, House_type, Vehicles, electricity,
            Education_level, Area, income, bracket
        ])
    df=pd.DataFrame(data, columns=[
        'Family_size', 'Occupation', 'HouseType', 'Vehicles', 'ElectricityBill',
        'Education', 'Area', 'Income', 'Bracket'
    ])
    
    return df

df=generate_data(1000)
df.to_csv("income_data.csv", index=False)
print(df.shape)
print(df.head())