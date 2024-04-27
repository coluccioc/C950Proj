class Package:
    # Package definition
    def __init__(self, packageID, d_address, d_deadline, d_city, d_zip_code, weight, d_status):
        self.packageID = packageID
        self.d_address = d_address
        self.d_deadline = d_deadline
        self.d_city = d_city
        self.d_zip_code = d_zip_code
        self.weight = weight
        self.d_status = d_status

    def __str__(self):
        return f"Package destined for: {self.d_city}"

    def info(self):
        print("Hi, I am headed for "+self.d_city)
