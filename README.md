# 🚗 Driver Behaviour Analysis (v1.0)

## 📌 Overview
This project analyzes driving data to detect unsafe driving behavior using sensor data such as acceleration and gyroscope readings.
The raw data was downloaded from Kaggle, you can have a look at the sensor data in 
-data/raw/carla_driver_data.csv

Version 1 focuses on identifying:
- ⚠️ Harsh Braking
- ⚡ Harsh Acceleration

### Version 2 is still on the works and will be updated very soon

---

## 🧠 How it works
- Reads multiple `.csv` files from `data/raw/`
- Cleans the data (removes invalid values)
- Filters realistic sensor ranges
- Calculates time from sampling rate
- Detects events based on thresholds:
  - Harsh braking → `accelX < -3`
  - Harsh acceleration → `accelX > 3`
- Applies cooldown logic to avoid duplicate detections
- Saves results into:
  - `data/processed/braking_log.csv`
  - `data/processed/acceleration_log.csv`

---

## 📂 Project Structure
driver-behaviour-analysis/
```
│
├── data/
│ ├── raw/ # Input CSV files
│ └── processed/ # Output event logs
│
├── src/
│ └── main.py # Main analysis script
│
└── README_v1.0.md
```
---
#### Note - This is a project i have taken to deepen my python and frameworks knowledge.
# REMEMBER - THE BEST WAY TO LEARN SOMETHING, IS BY DOING SOMETHING
---
HAVE A NICE DAY