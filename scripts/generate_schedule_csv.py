from glob import glob 
import re 
import os 
from datetime import datetime
import csv

if __name__=="__main__":
    filename = "schedule.csv"
    if os.path.exists(filename):
        print(f"{filename} already exists in project root. Please change directly in the csv.")
    else:
        all_exercises = glob("exercises/RAW/**")
        #all_exercises = [re.sub(r'\-.*', '', x.split("/")[-1]) for x in all_exercises] #option A: remove everything after trailing dash, i.e. ex1, ex2a, ex2b... 
        all_exercises = [x.split("/")[-1] for x in all_exercises]
        all_exercises.sort()
        TEMPLATE_DATETIME = [f"2026-01-{x+1} 00:00" for x in range(len(all_exercises))] #"YYYY-MM-DD HH:MM"

        output = []
        for a, b in zip(all_exercises,TEMPLATE_DATETIME):
            output.append([a,b])
        with open("schedule.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(output)
        print(f"Generated example {filename}")
        

        
        