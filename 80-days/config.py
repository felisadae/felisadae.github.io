# Universal constants and other things

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Location of SQLite database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'durations.db')

airports = ["BKK", "LHR", "CDG", "SIN", "JFK", "TAV", "DXB", "KUL", "HKG", "BCN", "GMP", "MXP", "CIA", "PVG", "AMS",
            "HND", "VIE", "TSA", "RUH", "LAX", "MEX", "IAD", "LAS", "OGG", "SFO", "PCC", "SYD", "GIG", "YVR", "EDI",
            "ZRH", "YUL"]
cities = {'JFK': 'New York', 'BCN': 'Barcelona', 'EDI': 'Edinburgh', 'HND': 'Tokyo', 'CIA': 'Rome', 'TSA': 'Taipei',
          'KUL': 'Kuala Lumpur', 'YUL': 'Montreal', 'PCC': 'Puerto Rico', 'BKK': 'Bangkok', 'SIN': 'Singapore',
          'TAV': 'Istanbul', 'LHR': 'London', 'PVG': 'Shanghai', 'AMS': 'Amsterdam', 'HKG': 'Hong Kong',
          'YVR': 'Vancouver', 'IAD': 'Washington, D.C.', 'GIG': 'Rio de Janeiro', 'GMP': 'Seoul', 'ZRH': 'Zurich',
          'RUH': 'Riyadh', 'CDG': 'Paris', 'VIE': 'Vienna', 'SYD': 'Sydeny', 'MXP': 'Milan', 'DXB': 'Dubai',
          'SFO': 'San Francisco', 'LAX': 'Los Angeles', 'OGG': 'Maui', 'MEX': 'Mexico City', 'LAS': 'Las Vegas'}
airport_codes = {'New York': 'JFK',
                 'Barcelona': 'BCN',
                 'Edinburgh': 'EDI',
                 'Tokyo': 'HND',
                 'Rome': 'CIA',
                 'Taipei': 'TSA',
                 'Kuala Lumpur': 'KUL',
                 'Montreal': 'YUL',
                 'Puerto Rico': 'PCC',
                 'Bangkok': 'BKK',
                 'Singapore': 'SIN',
                 'Istanbul': 'TAV',
                 'London': 'LHR',
                 'Shanghai': 'PVG',
                 'Amsterdam': 'AMS',
                 'Hong Kong': 'HKG',
                 'Vancouver': 'YVR',
                 'Washington, D.C.': 'IAD',
                 'Rio de Janeiro': 'GIG',
                 'Seoul': 'GMP',
                 'Zurich': 'ZRH',
                 'Riyadh': 'RUH',
                 'Paris': 'CDG',
                 'Vienna': 'VIE',
                 'Sydney': 'SYD',
                 'Milan': 'MXP',
                 'Dubai': 'DXB',
                 'San Francisco': 'SFO',
                 'Los Angeles': 'LAX',
                 'Maui': 'OGG',
                 'Mexico City': 'MEX',
                 'Las Vegas': 'LAS'}

sabre_access_token = "Bearer Shared/IDL:IceSess\/SessMgr:1\.0.IDL/Common/!ICESMS\/ACPCRTD!ICESMSLB\/CRT.LB!-0123456789012345678!123456!0!ABCDEFGHIJKLM!E2E-1"