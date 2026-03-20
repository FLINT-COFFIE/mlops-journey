# Write your solution here
from datetime import datetime

time_now = datetime.now()
midsummer = datetime(2026, 6, 26)

difference = midsummer - time_now
print("Midsummer is", difference, "days away")
