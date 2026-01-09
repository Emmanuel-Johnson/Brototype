This short script computes the number of hours remaining until the next midnight (start of tomorrow). It rounds the result to 2 decimal places and prints the current time, the next midnight, and the computed hours.

```python
from datetime import datetime, timedelta

now = datetime.now()
now = now.replace(microsecond=0)

after_one_day = now + timedelta(days=1)
after_one_day = after_one_day.replace(hour=0, minute=0, second=0, microsecond=0)

print(now)
print(after_one_day)

diff = after_one_day - now
ts = diff.total_seconds()
result = round(ts / 3600, 2)
print(result)
```

Usage: save to a `.py` file and run with Python 3. The script prints the current timestamp, the next midnight timestamp, and the hours remaining until then (rounded).