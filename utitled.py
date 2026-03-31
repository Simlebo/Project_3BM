from datetime import datetime
import pandas as pd

now = datetime.now()
start_datetime = datetime(now.year, now.month, now.day, 8, 0, 0) 
current_time_offset = 0
base_time = pd.Timestamp(start_datetime)

step_time = []
for i in range(0,3):
    step_time.append((base_time + pd.Timedelta(minutes=current_time_offset)).to_pydatetime())
    current_time_offset += 30
print(step_time)