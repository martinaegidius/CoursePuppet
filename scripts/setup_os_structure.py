import os

#TODO: Make this as a shell script instead, and then use the shell script for the complete pipeline. 

OUTPUT_DIR_PRIVATE = "solutions_RAW"
OUTPUT_DIR_PUBLIC = "solutions_filtered"

print("Setting up directory structure for filtering...")
os.makedirs(OUTPUT_DIR_PRIVATE,exist_ok=True)
os.makedirs(OUTPUT_DIR_PUBLIC,exist_ok=True)
print("Directory structure build success!")
