from package import Package
class Truck:
    def __init__(self):
        self.packages = []

    def contents(self):
        return self.packages

    def load(self, package):
        self.packages.append(package)

    def unload(self, packageID):
        for package in self.packages:
            if package.packageID == packageID:
                self.packages.remove(package)
                return package

