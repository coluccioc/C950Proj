class Package:
    # Package definition
    def __init__(self, packageID, d_address, d_deadline, d_city, d_zip_code, weight, notes):
        self.packageID = packageID
        self.d_address = d_address
        self.d_deadline = d_deadline
        self.d_city = d_city
        self.d_zip_code = d_zip_code
        self.weight = weight
        self.notes = notes
        self.departTime = None
        self.deliverTime = None
        self.truck = None

    def __str__(self):
        return f"Package destined for: {self.d_address}"

    # def status(self):
    #     if self.deliverTime is not None:
    #         return f"Package Delivered at: {self.deliverTime}"
    #     elif self.departTime is not None:
    #         return f"Package In Route as of: {self.departTime}"
    #     else:
    #         return "Package is at the Hub"

    def statusAt(self, time):
        if self.departTime is None:
            status = "At the Hub"
        elif self.deliverTime is not None:
            if time >= self.deliverTime:
                status = "Delivered"
            elif time >= self.departTime:
                status = f"In Route on {self.truck}"
            else:
                status = "At the Hub"
        else:
            if time >= self.departTime:
                status = f"In Route on {self.truck}"
            else:
                status = "At the Hub"
        return status
