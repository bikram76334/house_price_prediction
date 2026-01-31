import pandas as pd
import random

locations = {
    "Kathmandu": 12000,
    "Pokhara": 9000,
    "Chitwan": 6500,
    "Dhangadi": 5500,
    "Syangja": 4000
}

data = []

for i in range(1000):
    location = random.choice(list(locations.keys()))
    land_area = random.randint(600, 3000)
    floors = random.randint(1, 4)
    bedrooms = random.randint(1, 6)
    bathrooms = random.randint(1, 4)
    windows = random.randint(4, 14)
    doors = random.randint(2, 8)
    cement_bags = random.randint(180, 500)

    rcc = 1
    plumbing = random.choice([0, 1])
    electricity = random.choice([0, 1])

    land_cost = land_area * locations[location]

    construction_cost = floors * land_area * 1800

    material_cost = (
        cement_bags * 420 +
        windows * 3500 +
        doors * 5500
    )

    total_price = (
        land_cost +
        construction_cost +
        material_cost +
        plumbing * 120000 +
        electricity * 80000
    )

    data.append([
        location, land_area, floors, bedrooms, bathrooms,
        windows, doors, cement_bags, rcc, plumbing, electricity,
        land_cost, construction_cost, material_cost, total_price
    ])

columns = [
    "location","land_area_sqft","floors","bedrooms","bathrooms",
    "windows","doors","cement_bags","rcc_structure",
    "plumbing","electricity","land_cost",
    "construction_cost","material_cost","total_price"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("nepal_house_data.csv", index=False)

print("✅ Dataset created: nepal_house_data.csv (1000 rows)")
