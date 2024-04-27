# Student ID 010755535 // C950 Project
from truck import Truck
from package import Package
from hash import ChainingHashTable
from csvReader import loadPackageData, loadAddressData, loadDistanceData
import datetime

packageHash = ChainingHashTable()
loadPackageData('WGUpackages.csv', packageHash)

distanceArray = loadDistanceData('WGUPS Distance Table.csv')
addressArray = loadAddressData('WGUPS Distance Table.csv')

hubAddress = "4001 South 700 East"

# LOAD SOME TRUCKS
truck1 = Truck()
for i in range(1, 40):
    truck1.load(packageHash.search(i))


def distanceBetween(address1, address2):
    a = min(addressArray.index(address1), addressArray.index(address2))
    b = max(addressArray.index(address1), addressArray.index(address2))
    return distanceArray[b][a]


def minDistance(fromAddress, truckPackages):
    nearest = 1000000
    nextAddress = None
    packageID = None
    for parcel in truckPackages:
        distance = distanceBetween(fromAddress, parcel.d_address)
        if float(distance) < nearest:
            nearest = float(distance)
            nextAddress = parcel.d_address
            packageID = parcel.packageID
    return nextAddress, nearest, packageID


def truckDeliverPackages(truck):
    currentAddress = hubAddress
    miles = 0
    # elapsed = datetime.timedelta(hours=0, minutes=0, seconds=0)
    while len(truck.packages) > 0:
        trip = minDistance(currentAddress, truck.packages)
        currentAddress = trip[0]
        miles += trip[1]
        elapsed = datetime.timedelta(hours=miles/18)
        print("Arrived at: {}, total miles: {}, Elapsed Time: {}".format(currentAddress, round(miles, 2), elapsed))
        truck.unload(trip[2])
    # return home
    print(currentAddress)
    miles += float(distanceBetween(currentAddress, hubAddress))
    elapsed = datetime.timedelta(hours=miles / 18)

selection = input("1. Deliver Packages\n2. View Package Status\n3. Quit\n")
while(selection != "3"):
    if(selection == "1"):
        truckDeliverPackages(truck1)
    if(selection == "2"):
        packageNum = input("Enter Package Number to view status: ")
        package = packageHash.search(int(packageNum))
        print("Package destination: " + package.d_address)
    print("---------------------------------------")
    selection = input("1. Deliver Packages\n2. View Package Status\n3. Quit\n")

# for i in addressArray:
#     print(i)
# print(minDistance("4580 S 2300 E",truck1.contents()))
# print(distanceBetween("4580 S 2300 E","5025 State St"))
# CHECK FOR SUCCESSFUL PACKAGE LOAD INTO HASH
# print(packageHash.search(2))
# for i in range(40):
#     print("ID: {} for pkg {}".format(i+1,packageHash.search(i+1)))
