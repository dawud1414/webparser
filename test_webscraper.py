from pathlib import Path

#using pathlib check to see if file exist

file_name = Path("new.csv")
if file_name.exists():
    print("exists") 
else:
    print("does not exist") 