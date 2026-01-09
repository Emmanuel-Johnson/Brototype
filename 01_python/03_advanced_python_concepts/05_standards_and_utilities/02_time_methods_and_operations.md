In Python, time-related operations are handled primarily by the built-in `time` and `datetime` modules. Use `time` for low-level timestamps and performance measurements, and `datetime` for human-readable date/time manipulation and arithmetic.

## 1. The `time` module

The `time` module works with Unix timestamps (seconds since Jan 1, 1970 UTC).

Important methods:

- `time.time()` — current time as a float (seconds since epoch). Common for measuring execution time.
    ```py
    import time
    start = time.time()
    # ... work ...
    elapsed = time.time() - start
    ```
- `time.sleep(seconds)` — pause execution.
    ```py
    time.sleep(2)  # sleep 2 seconds
    ```
- `time.ctime(timestamp=None)` — convert timestamp to readable string (defaults to now).
    ```py
    time.ctime()
    ```
- `time.localtime(timestamp=None)` / `time.gmtime(timestamp=None)` — convert timestamp to structured time (local / UTC).
- `time.strftime(format, struct_time)` — format structured time with format codes like `%Y`, `%m`, `%d`, `%H`, `%M`, `%S`.

Use `time` for performance benchmarking, delays, retries, and low-level timestamp operations.

## 2. The `datetime` module

`datetime` is preferred for most application-level date/time tasks.

Key classes:
- `datetime` — date and time together (`datetime.datetime`)
- `date` — date only (`datetime.date`)
- `time` — time only (`datetime.time`)
- `timedelta` — duration (`datetime.timedelta`)

## 3. Getting current date and time

- `datetime.now()` — local date and time
- `datetime.utcnow()` — UTC date and time

Example:
```py
from datetime import datetime
now_local = datetime.now()
now_utc = datetime.utcnow()
```

## 4. Date and time formatting

- `strftime()` — format a `datetime` into a string
    ```py
    now = datetime.now()
    now.strftime("%Y-%m-%d %H:%M:%S")
    ```
- `strptime()` — parse a formatted string into a `datetime`
    ```py
    from datetime import datetime
    dt = datetime.strptime("2026-01-09 12:34:56", "%Y-%m-%d %H:%M:%S")
    ```

Common uses: parsing API date strings, formatting timestamps for UI.

## 5. Time arithmetic using `timedelta`

`timedelta` allows adding/subtracting durations and computing differences.

Examples:
```py
from datetime import datetime, timedelta
now = datetime.now()
later = now + timedelta(days=2, hours=3)
diff = later - now  # timedelta
```

Typical uses: expiry calculations, session timeouts, deadline tracking.

## 6. Comparing date and time

`datetime` objects support standard comparisons: `<`, `>`, `==`, `!=`. This enables checks like expiration, validation of ranges, and sorting timestamps.

Example:
```py
if datetime.now() > expiry_datetime:
        print("Expired")
```

## 7. Common interview/use-case mappings

- Measuring execution time → `time.time()`
- Delays and retries → `time.sleep()`
- Current timestamp → `datetime.now()`
- Formatting dates → `strftime()`
- Date differences → `timedelta`

Conclusion

Use `time` for low-level timestamping and performance measurements. Use `datetime` for readable date/time operations, formatting, parsing, and arithmetic — it is more flexible for most real-world applications.
