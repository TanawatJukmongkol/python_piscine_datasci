from datetime import datetime as dt

time = dt.now()
ts = time.timestamp()

print(f"Seconds since January 1, 1970: {ts} or {ts:e} in scientific notation")
print(time.strftime("%b %d %Y"))
