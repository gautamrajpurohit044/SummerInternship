import csv


address_book = [
    ["name", "address", "mobile", "email"],
    ["Gautam Rajpurohit", "Jaipur", "9876543210", "gautam@example.com"],
    ["Ravi Sharma", "Udaipur", "9123456780", "ravi@example.com"],
    ["Anjali Mehta", "Jodhpur", "9012345678", "anjali@example.com"]
]

with open("address_book.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(address_book)

print("CSV file 'address_book.csv' created successfully.")
