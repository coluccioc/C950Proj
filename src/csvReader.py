import csv
from package import Package

def loadPackageData(fileName, hashTable):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)
        for package in packageData:
            packageID = int(package[0])
            packageAddress = package[1]
            packageCity = package[2]
            packageZip = package[4]
            packageDeadline = package[5]
            packageWeight = package[6]
            packageNotes = package[7]

            newPackage = Package(packageID, packageAddress, packageDeadline, packageCity, packageZip, packageWeight, packageNotes)
            hashTable.insert(packageID, newPackage)


def loadDistanceData(fileName):
    distanceArray = []
    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        next(distanceData)
        for row in distanceData:
            distance = row[2:29]
            distanceArray.append(distance)
    return distanceArray

def loadAddressData(fileName):
    addressArray = []
    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=',')
        next(distanceData)
        for row in distanceData:
            distance = row[0].split('\n')[1].strip().replace(",","")
            addressArray.append(distance)
    return addressArray

dArray = loadDistanceData('WGUPS Distance Table.csv')
aArray = loadAddressData('WGUPS Distance Table.csv')
for rows in dArray:
    print(rows)
for rows in aArray:
    print(rows)
