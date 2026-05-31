from datetime import datetime

name = input("Enter your name: ")
print("Welcome,", name)

print("1. Study Tips")
print("2. Motivation Quote")
print("3. Current Date and Time")

choice = input("Enter choice: ")

if choice == "1":
    print("Study Tip: Practice coding daily.")
elif choice == "2":
    print("Success comes from consistent effort.")
elif choice == "3":
    print(datetime.now())
else:
    print("Invalid choice")
