bill = []

while True:
    a = int(input('''
       1. Create Bill
       2. Display Item Prices and Total
       3. Display Total
       4. Exit\nChoose an option: '''))

    if a == 1:
        n = int(input("Enter number of items: "))
        bill = []
        for i in range(n):
            element = int(input(f"Enter price of item {i+1}: rs."))
            bill.append(element)
        print(f"Bill : {bill}")

    elif a == 2:
            print("\nItem-wise Prices:")
            for i in range(len(bill)):
                price = bill[i]
                print(f"Item {i + 1} : rs.{price}")
            print(f"Total Bill Amount: ₹{sum(bill)}")

    elif a == 3:
            print(f"Total Bill Amount: ₹{sum(bill)}")

    elif a == 4:
        print("Exited,thank you to use")
        break

    else:
        print("Enter a valid input.")
