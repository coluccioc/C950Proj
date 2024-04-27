# Truck class used to hold packages and mileage information
class Truck:
    def __init__(self, name):
        self.name = name
        self.packages = []
        self.returnTime = None
        self.miles = None

    # O(1)
    def load(self, package):
        self.packages.append(package)

    # O(n^2), n = # of packages
    def unload(self, packageID):
        for package in self.packages:
            if package.packageID == packageID:
                self.packages.remove(package)
                return package
