#flight_schedule.py
import csv

class FlightSchedule():
    def __init__(self):
        self.flights = None
        self.plane_identifiers = None
 
    def read_data_from_file(self):
        with open("flight_data.csv", encoding='utf-8') as file:
            flightreader = csv.reader(file)
            
            for row in flightreader:
                self.flights = row[0]
                #if plane_identfiers == 
                self.plane_identifiers = row[1]
                 
                   
    def determine_longest_flight(self):
        with open("flight_data.csv", encoding='utf-8') as f:
            longest_flight = 0
            for line in f:
                flight_length = line.split(",")
                flight_miles = float(flight_length[4])
                if flight_miles > longest_flight:
                    longest_flight = flight_miles
                    return longest_flight


                    
 # daily_schedule.flights = flights
#    daily_schedule.plane_identifier = plane_identfiers

###   daily_schedule.origin = self.flight_data[2]
##    daily_schedule.destination = self.flight_data[3]
##    daily_schedule.miles = self.flight_data[4]
##    daily_schdeul.passengers = self.flight_data[5]
