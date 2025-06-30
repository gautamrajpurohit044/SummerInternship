import pandas as pd

# Sample datetime series
dates = pd.Series(pd.date_range(start="2023-01-01", periods=5, freq='D'))
print("Original dates:")
print(dates)

# Extract parts
print("\nYear:", dates.dt.year)
print("Month:", dates.dt.month)
print("Weekday:", dates.dt.day_name())

# Add 7 days
dates_plus7 = dates + pd.Timedelta(days=7)
print("\nDates + 7 days:")
print(dates_plus7)

# Filter dates after a certain date
filtered = dates[dates > '2023-01-03']
print("\nDates after 2023-01-03:")
print(filtered)
