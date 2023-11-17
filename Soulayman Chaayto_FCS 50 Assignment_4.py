cities = ["Beirut", "Akkar", "Tyr", "Saida"]
drivers = {
  "ahmad": ["Saida", "Beirut", "Akkar"],
  "khalil": ["Tyr", "Beirut"]
}
def AddCityToRoute(drivers, cities):
  driverName = input("Enter the name of the driver")
  if driverName.lower() in drivers.lower():
      print("Enter: ")
      print("0 to add the city to the beginning of the route ")
      print("-1 To add the city to the end of the route ")
      print("any other number to add the city at that index")
      indexChoice = int(input())
      cityToBeAdded = input("Enter the city you want to add to the route: ")
      flag = 0              #this flag is to determine if we found the cityToBeAdded  in the list of cities
      for i in cities :
         if  i == cityToBeAdded:
          drivers[driverName][indexChoice] = cityToBeAdded
          print("City added at index: ",indexChoice)
          flag = 1
      if flag == 0:
        print("The city you want to add is not registered...")

  else:
    print("Driver is not registered")

def AddCity(cities):
  flag = 0
  city = input("Enter the city you want to add: ")
  for i in cities:
    if i.lower() == city.lower():
      print("City already registered ")
      flag=1
  if flag == 0:
   print("Added the city: ", city)
   return cities.append(city)

def AddDriver(cities, drivers):
  flag = 0
  driverName = input("Enter the name of the Driver to be added: ")
  for i in drivers.keys():
    if i.lower() == driverName.lower():
      print("Driver already registered ")
      flag = 1
      break
  if flag == 0:
   option = -99 #dummy value
   print("enter the route of the driver: ")
   listOfDriverCities=[]
   while option != 2:
    print("enter 1 to continue adding cities to the route.")
    print("enter 2 to stop")
    option = int(input())
    if option == 1:
      cityToBeAdded = input("Enter the city you want to add to the route: ")
      for i in cities :
         if  i == cityToBeAdded:
          listOfDriverCities.append(cityToBeAdded)
          print(cityToBeAdded+" is added ")
    elif option == 2:
        print("Route added, returning to menu... ")
        drivers[driverName] = listOfDriverCities
    else :
        print("invalid option ")

def RemoveCity(drivers):
  driverName = input("Enter the Driver's name:")
  for i in drivers.keys():
    if i.lower() == driverName.lower():
      cityToDelete = input ("Enter the city to be removed from the route: ")
      driverRoute = drivers[driverName]
      for j in driverRoute:
        if j.lower() == cityToDelete:
          drivers[driverName] = driverRoute.remove(cityToDelete)
          print("city removed from route ")
          return
      print("city not found in driver's route ")
  print("Driver is not registered")

def DeliveryCheck(cities, drivers):
  cityToDeliver = input("enter the name of the city")
  driversAvailable = []
  if cityToDeliver in cities:
      for key,value in drivers.items():
        if cityToDeliver in value:
          driversAvailable.append(key)
      if len(driversAvailable) != 0:
         print(driversAvailable)
      else:
         print("There is no drivers that deliver to this city ")
  else:
    print("City is not registered...")


def mainMenu(cities, drivers):
  choice=-99 # dummy value
  while choice !=6:
    print("Enter")
    print("1. To add a city")
    print("2. To add a driver")
    print("3. To add a city to the route of a driver")
    print("4. Remove a city from a driver’s route")
    print("5. To check the deliverability of a package")
    print("6. To close the program")

    choice=int(input())

    if choice == 1:
      print("Adding a new city...")
      AddCity(cities)
    elif choice == 2:
      print("Adding a new driver...")
      AddDriver(cities, drivers)
    elif choice == 3:
      print("Adding a city to the route of a driver...")
      AddCityToRoute(drivers, cities)
    elif choice == 4:
      print("Removing a city from a driver's route...")
      RemoveCity(drivers)
    elif choice == 5:
      print("Checking the deliverability...")
      DeliveryCheck(cities, drivers)
    elif choice == 6:
      print("Program is closing, bye bye.")
    else:
      print("ivalid input")

mainMenu(cities,drivers)