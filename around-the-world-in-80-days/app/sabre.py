# File for managing all Sabre API-related functions
import datetime, time
from flask import json
import requests
import config
from app import db
from app.database import Flight


def get_flight_duration(origin, destination):
    """
    Uses the Sabre API to get the flight duration, in minutes, between the origin and destination airports
    """
    url = 'https://api.test.sabre.com/v1.8.5/shop/flights?mode=live'
    data = {
        "OTA_AirLowFareSearchRQ": {
            "OriginDestinationInformation": [
                {
                    "DepartureDateTime": "2015-05-05T00:00:00",
                    "DestinationLocation": {
                        "LocationCode": str(origin)
                    },
                    "OriginLocation": {
                        "LocationCode": str(destination)
                    },
                    "RPH": 1
                }
            ],
            "POS": {
                "Source": [
                    {
                        "RequestorID": {
                            "CompanyName": {
                                "Code": "TN"
                            },
                            "ID": "REQ.ID",
                            "Type": "0.AAA.X"
                        }
                    }
                ]
            },
            "TPA_Extensions": {
                "IntelliSellTransaction": {
                    "RequestType": {
                        "Name": "50ITINS"
                    }
                }
            },
            "TravelerInfoSummary": {
                "AirTravelerAvail": [
                    {
                        "PassengerTypeQuantity": [
                            {
                                "Code": "ADT",
                                "Quantity": 1
                            }
                        ]
                    }
                ]
            }
        }
    }
    headers = {"Content-Type": "application/json",
               "Authorization": config.sabre_access_token}
    response = dict(requests.post(url, data=json.dumps(data), headers=headers).json())
    duration = response["OTA_AirLowFareSearchRS"]["PricedItineraries"]["PricedItinerary"][0]["AirItinerary"]["OriginDestinationOptions"]["OriginDestinationOption"][0]["ElapsedTime"]
    return duration


def get_flight_prices(departure_data):
    """
    Given an origin and destination, return the cost of the flight given the departure time.
    departure_data is of the form [(origin, destination, departure_time), ...]
    """
    url = 'https://api.test.sabre.com/v1.8.5/shop/flights?mode=live'
    departure_data_formatted = []
    for origin, destination, departure_time in departure_data:
        departure_data_formatted.append((origin, destination, departure_time.strftime('%Y-%m-%dT%H:%M:%S')))
    prices = []
    for (origin, destination, formatted_time) in departure_data_formatted:
        data = {
            "OTA_AirLowFareSearchRQ": {
                "OriginDestinationInformation": [{"DepartureDateTime": formatted_time, "DestinationLocation": {"LocationCode": destination}, "OriginLocation": {"LocationCode": origin}, "RPH": 1}],
                "POS": {
                    "Source": [
                        {
                            "RequestorID": {
                                "CompanyName": {
                                    "Code": "TN"
                                },
                                "ID": "REQ.ID",
                                "Type": "0.AAA.X"
                            }
                        }
                    ]
                },
                "TPA_Extensions": {
                    "IntelliSellTransaction": {
                        "RequestType": {
                            "Name": "50ITINS"
                        }
                    }
                },
                "TravelerInfoSummary": {
                    "AirTravelerAvail": [
                        {
                            "PassengerTypeQuantity": [
                                {
                                    "Code": "ADT",
                                    "Quantity": 1
                                }
                            ]
                        }
                    ]
                }
            }
        }
        headers = {"Content-Type": "application/json",
                   "Authorization": config.sabre_access_token}
        print "Debug: attempting to get flight cost between", origin, "and", destination
        response = dict(requests.post(url, data=json.dumps(data), headers=headers).json())
        price = response["OTA_AirLowFareSearchRS"]["PricedItineraries"]["PricedItinerary"][0]["AirItineraryPricingInfo"][0]["ItinTotalFare"]["TotalFare"]["Amount"]
        print "Debug: determined flight cost", price
        prices.append(price)
    return sum(prices)


def download_flight_duration_data():
    """
    Due to the prohibitively slow HackDFW network, and the slowness of Sabre's API, load all of the flight duration data
    into a local SQLite database that can be queried instantly when generating the graph.
    """
    for origin in config.airports:
        for destination in config.airports:
            if origin != destination and not Flight.query.filter_by(flight=origin + "|" + destination).first():
                print "Debug: attempting to get flight duration between", origin, "and", destination
                try:
                    duration = get_flight_duration(origin, destination)
                    print "Debug: determined flight duration", duration
                    flight_duration_1 = Flight(origin, destination, duration)
                    flight_duration_2 = Flight(destination, origin, duration)
                    db.session.add(flight_duration_1)
                    db.session.add(flight_duration_2)
                    db.session.commit()
                except:
                    print "Debug: failed to get flight data between", origin, "and", destination