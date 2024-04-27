# Student ID 010755535 // C950 Project
from truck import Truck
from hash import ChainHashTable
from csvReader import loadPackageData, loadAddressData, loadDistanceData
import datetime

# Initializing the Hash Table, loading CSV data
packageHash = ChainHashTable()
loadPackageData('WGUpackages.csv', packageHash)

# Loading the data from CSV files
distanceArray = loadDistanceData('WGUPS Distance Table.csv')
addressArray = loadAddressData('WGUPS Distance Table.csv')

# Declaring Hub Address for trucks' start/end address
hubAddress = "4001 South 700 East"
# Delivered boolean for flagging completion
delivered = 0

# LOAD SOME TRUCKS
# Truck packages have been manually assigned based on listed requirements. <= 16 packages per truck
truck1List = [1, 4, 7, 13, 14, 15, 16, 20, 21, 29, 30, 34, 37, 39, 40]
truck2List = [3, 5, 6, 10, 11, 12, 18, 23, 25, 26, 31, 32, 36, 38]
truck3List = [2, 8, 9, 17, 19, 22, 24, 27, 28, 33, 35]

# Creating truck objects for each truck
truck1 = Truck("Truck 1")
truck2 = Truck("Truck 2")
truck3 = Truck("Truck 3")

# Each truck load loop has O(n) runtime, n = # of packages
for i in truck1List:
    truck1.load(packageHash.search(i))
for i in truck2List:
    truck2.load(packageHash.search(i))
# Correct Package 9's address
packageHash.search(9).d_address = "410 S State St"
packageHash.search(9).d_zip_code = "84111"

for i in truck3List:
    truck3.load(packageHash.search(i))

# Establish Start Times for each truck based on package requirements
currentDate = datetime.datetime.now()
truck1Start = currentDate.replace(hour=8, minute=0, second=0, microsecond=0)
truck2Start = currentDate.replace(hour=9, minute=5, second=0, microsecond=0)
truck3Start = currentDate.replace(hour=10, minute=20, second=0, microsecond=0)


# Min and Max run in O(1) time since there are 2 elements
# distanceBetween finds the value in the distanceArray for the relationship between address 1 and 2
# distance from a to b = distance from b to a, but the table is populated where b >= a in accessing the array as [b][a]
def distanceBetween(address1, address2):
    a = min(addressArray.index(address1), addressArray.index(address2))
    b = max(addressArray.index(address1), addressArray.index(address2))
    return distanceArray[b][a]


# minDistance runs in O(n) time where n = a truck's packages
# minDistance checks the distance between the current location and all possible next stops to see which is closest
# takes fromAddress and a truck's package list as arguments
def minDistance(fromAddress, truckPackages):
    nearest = 10000000
    nextAddress = None
    packageID = None
    for parcel in truckPackages:
        distance = distanceBetween(fromAddress, parcel.d_address)
        if float(distance) < nearest:
            nearest = float(distance)
            nextAddress = parcel.d_address
            packageID = parcel.packageID
    return nextAddress, nearest, packageID


# Delivery Algorithm. Takes a truck object and its start time as arguments
# This runs in O(n^2) due to the dominant time complexity of the truck's unload function
def truckDeliverPackages(truck, startTime):
    for item in truck.packages:
        packageHash.search(item.packageID).departTime = startTime.time()
        packageHash.search(item.packageID).truck = truck.name
    currentAddress = hubAddress
    miles = 0
    # elapsed = datetime.timedelta(hours=0, minutes=0, seconds=0)
    while len(truck.packages) > 0:
        trip = minDistance(currentAddress, truck.packages)
        currentAddress = trip[0]
        miles += trip[1]
        time = datetime.timedelta(hours=miles / 18) + startTime
        packageHash.search(trip[2]).deliverTime = time.time()
        # print("Arrived at: {}, total miles: {}, Elapsed Time: {}".format(currentAddress, round(miles, 2), elapsed))
        truck.unload(trip[2])
    # return home
    # print(currentAddress)
    miles += float(distanceBetween(currentAddress, hubAddress))
    time = datetime.timedelta(hours=miles / 18) + startTime
    truck.miles = round(miles, 2)
    truck.returnTime = time


def packageStatus(ID, time):
    item = packageHash.search(ID)
    return item.statusAt(time)


# check
selection = input("1. Deliver Packages\n2. View Package Status at Time\n"
                  "3. View All Package Statuses at a Time\n4. Review Mileage\n5. Quit\n")
while selection != "5":
    packageNum = None
    timeInput = None
    if selection == "1":
        if delivered == 0:
            truckDeliverPackages(truck1, truck1Start)
            truckDeliverPackages(truck2, truck2Start)
            truckDeliverPackages(truck3, truck3Start)
            delivered = 1
    elif selection == "2":
        try:
            packageNum = input("Enter Package ID to view its status: ")
            package = packageHash.search(int(packageNum))
            packageID = package.packageID
            try:
                timeInput = input("Enter the time at which you would like to see its status: (HH:MM , 00:00 - 23:59)")
                hours, minutes = timeInput.split(':')
                dateTimeParsed = currentDate.replace(hour=int(hours), minute=int(minutes), second=0, microsecond=0)
                print("Package: " + str(packageID) + " has status: " +
                      package.statusAt(dateTimeParsed.time()) + " at " + timeInput)
            except:
                print("Invalid Time Format. Please use HH:MM , 00:00 - 23:59")
        except:
            print("Invalid Package ID")

    elif selection == "3":
        try:
            timeInput = input("Enter the time at which you would like to see its status: (HH:MM , 00:00 - 23:59)")
            hours, minutes = timeInput.split(':')
            dateTimeParsed = currentDate.replace(hour=int(hours), minute=int(minutes), second=0, microsecond=0)
            displayTable = []
            sortedTable = []
            for bucket in packageHash.table:
                for key, value in bucket:
                    displayTable.append((key, value))
                    sortedTable = sorted(displayTable, key=lambda x: int(x[0]))
            for i in sortedTable:
                print("Package: " + str(i[0]) + " has status: " + i[1].statusAt(
                    dateTimeParsed.time()) + " at " + timeInput)
        except:
            print("Invalid Time Format. Please use HH:MM , 00:00 - 23:59")
    elif selection == "4":

        print("Truck 1 Mileage: " + str(truck1.miles))
        print("Truck 2 Mileage: " + str(truck2.miles))
        print("Truck 3 Mileage: " + str(truck3.miles))
    elif selection == "5":
        print("End")
    else:
        print("Invalid Input. Please choose a number 1-5")
    print("---------------------------------------")
    selection = input("1. Deliver Packages\n2. View Package Status at Time\n"
                      "3. View All Package Statuses at a Time\n4. Review Mileage\n5. Quit\n")

# for i in addressArray:
#     print(i)
# print(minDistance("4580 S 2300 E",truck1.contents()))
# print(distanceBetween("4580 S 2300 E","5025 State St"))
# CHECK FOR SUCCESSFUL PACKAGE LOAD INTO HASH
# print(packageHash.search(2))
# for i in range(40):
#     print("ID: {} for pkg {}".format(i+1,packageHash.search(i+1)))
