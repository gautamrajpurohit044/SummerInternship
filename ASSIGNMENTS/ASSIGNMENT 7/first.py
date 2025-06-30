import re

# Email validation
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "test@example.com"
print(re.match(email_pattern, email))

# Mobile number validation (10 digits)
mobile_pattern = r'^\d{10}$'
mobile = "9876543210"
print(re.match(mobile_pattern, mobile))

# Alphanumeric string
alphanumeric_pattern = r'^[a-zA-Z0-9]+$'
text = "abc123XYZ"
print(re.match(alphanumeric_pattern, text))

# Extract all numbers from text
text_with_numbers = "Order 123 shipped on 2023-01-01"
numbers = re.findall(r'\d+', text_with_numbers)
print(numbers)
