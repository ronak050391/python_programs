import geocoder
from math import sin, cos, sqrt, atan2, radians


class Driver:
    rides_dict = {}

    def __init__(self, driver_name):
        self.driver_name = driver_name

    def getAvailableRides(self):
        if len(self.rides_dict) == 0:
            print("No rides available at the moment.")
        else:
            print("Available rides: ", self.rides_dict)

    def acceptRide(self):
        # approximate radius of earth in km
        R = 6373.0
        d_lat = float(input("Enter your latitude location: "))
        d_lon = float(input("Enter your longitude location: "))
        for key, value in self.rides_dict.items():
            lat1 = radians(value[0][0])
            lon1 = radians(value[0][1])
            lat2 = radians(d_lat)
            lon2 = radians(d_lon)
            lon_diff = lon2 - lon1
            lat_diff = lat2 - lat1
            b = sin(lat_diff / 2)**2 + cos(lat1) * cos(lat2) * sin(lon_diff / 2)**2
            c = 2 * atan2(sqrt(b), sqrt(1 - b))
            distance = R * c
            print("{} is {}kms far from you, do you want to accept ride?(Accept/Reject): ".format(key, round(distance, 2)))
            ride_s = input()
            if ride_s.upper() == "ACCEPT":
                self.rides_dict[key].append(self.driver_name)
                self.rides_dict[key][1] = "Accepted"
                print("Congrats, you have accepted {}`s ride.".format(key))
                break
            elif ride_s.upper() == "REJECT":
                self.rides_dict[key][1] = "Rejected"
                if len(self.rides_dict) == 1:
                    print("Please wait for another rider to request a ride.")


class User(Driver):
    def __init__(self, user_name):
        self.user_name = user_name

    def setLocation(self):
        g = geocoder.ip('me')
        return g

    def requestRide(self, g):
        Driver.rides_dict[self.user_name] = [g.latlng, "Requested"]
        print("Ride is requested for you, please wait for a driver to accept.")

    def isRideAccepted(self,user_name):
        if Driver.rides_dict[self.user_name][1] == "Accepted":
            print("\nCongrats your ride is accepted by Driver {}.".format(Driver.rides_dict[self.user_name][2]))
        elif Driver.rides_dict[self.user_name][1] == "Rejected":
            print("Sorry, your ride is rejected by Driver {}.".format(Driver.rides_dict[self.user_name][2]))


print("Welcome to Driver User Matching Program..!!")
a = True
while a is True:
    i = input("Provide your inputs(Driver/User): ")
    if i.upper() == "DRIVER":
        a = False
        name = input("Enter your name: ")
        driver_obj = Driver(name)
        driver_obj.getAvailableRides()
        if len(Driver.rides_dict.keys())>=1:
            driver_obj.acceptRide()
    elif i.upper() == "USER":
        a = False
        name = input("Enter your name: ")
        user_obj = User(name)
        if name in Driver.rides_dict.keys():
            user_obj.isRideAccepted(name)
        else:
            print("\nWelcome {}, taking your current location.".format(name))
            g = user_obj.setLocation()
            user_obj.requestRide(g)
    else:
        a = True
        print("\nPlease enter correct input.\n")
    j = input("\nDo you want to continue?(Yes/No) ")
    if j.upper() == "YES":
        a = True
    elif j.upper() == "NO":
        break
    else:
        print("Sorry, I am going to exit as you have entered wrong input.")
