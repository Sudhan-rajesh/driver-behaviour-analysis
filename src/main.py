import pandas as pd
import os
import matplotlib.pyplot as plt

folder_path = "data/raw"

braking_log = []
acceleration_log = []


for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path , file)

        data = pd.read_csv(file_path, index_col=0)
        

        # replace invalid values with NaN
        data.replace([-99.9 , 99.9], pd.NA, inplace=True)
        # remove row in NA
        data.dropna(inplace=True)
        # add condition
        condition=(
            (data["accelX"].between(-9, 9)) &
            (data["accelY"].between(-10, 10)) & 
            (data["accelZ"].between(8 , 12)) &
            (data["gyroZ"].between(-50, 50))
        )
        data = data[condition]

        data.reset_index(drop=True, inplace=True)
        # convert objext to float
        data = data.astype(float, errors="ignore")
        data["time"] = data.index * 0.1

        # detect harsh braking
        braking = data[data["accelX"]< -3].copy()

        # cooldown logic
        braking["time_diff"] = braking["time"].diff()

        braking_events = braking[
            (braking["time_diff"].isna()) |
            (braking["time_diff"] > 1.0)
        ]
        
        # store events
        for _, row in braking_events.iterrows():

            print(f"harsh braking at {row['time']:.2f}s")
            
            braking_log.append({
                "file": file,
                "time": round(row["time"], 2),
                "events": "harsh_braking",
                "driver": row["class"]
            })
        # harsh acceleration
        acceleration = data[data["accelX"]> 3].copy()

        #cooldown logic
        acceleration["time_diff"] = acceleration["time"].diff()

        acceleration_events = acceleration[
            (acceleration["time_diff"].isna()) |
            (acceleration["time_diff"] > 1.0)
        ]
        #store events
        for _, row in acceleration_events.iterrows():
            print(f"harsh acceleration at {row['time']:.2f}s")

            acceleration_log.append({
                "file": file,
                "acceleration": round(row["accelX"], 2),
                "time": round(row["time"], 2),
                "events": "harsh_acceleration",
                "driver": row["class"],
            })

print(data["accelX"].describe())
braking_df = pd.DataFrame(braking_log)
braking_df.to_csv("data/processed/braking_log.csv", index = False)

acceleration_df = pd.DataFrame(acceleration_log)
acceleration_df.to_csv("data/processed/acceleration_log.csv", index = False)
        
        

