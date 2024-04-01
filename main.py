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
  AutoCountry Vehicle Finder v0.1\n************************************")
  print("\n1. PRINT all Authorized Vehicles")
  print("2. Exit")
  
# Define main function
def main():
    while True:
        display_menu()
        choice = input("\nPlease Enter the following number below from the following menu: ")
        if choice == '1':
            print_allowed_vehicles()
        elif choice == '2':
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
  main()
