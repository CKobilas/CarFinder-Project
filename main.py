# Define Allowed Vehicles List
Allowed_Vehicles_List = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Define function to print allowed vehicles
def print_allowed_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in Allowed_Vehicles_List:
        print(vehicle)
      
# Define function to display menu
def display_menu():
  print("\n************************************\n\
  AutoCountry Vehicle Finder v0.2\n************************************")
  print("\n1. PRINT all Authorized Vehicles")
  print("2. SEARCH for Authorized Vehicle")
  print("3. Exit")

# Define function to get user input on searched vehicle
def search_vehicle():
  search = input("\nPlease Enter the full Vehicle name: ")
  if search in Allowed_Vehicles_List:
    print(search, "is an authorized vehicle")
  else:
    print(search, "is not an authorized vehicle, if you received this in error please check the spelling and try again")
  
# Define main function
def main():
    while True:
        display_menu()
        choice = input("\nPlease Enter the following number below from the following menu: ")
        if choice == '1':
            print_allowed_vehicles()
        elif choice == '2':
            search_vehicle()
        elif choice == '3':
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
  main()
