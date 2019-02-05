#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:15:02 2019

@author: hienh
"""

import json
import requests
import sqlite3
from math import sin, cos, sqrt, atan2, radians


def getDb():
    try:
        conn = sqlite3.connect('phonebook.db')
        cursor = conn.cursor()
        return cursor
    except:
        return False

# def closeDb():
#     try:
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(e)


def getBusinessPostcode():
      db= getDb()
      query = db.execute(""" SELECT
                            businessphonebook.id,
                            businessphonebook.business_name,
                            businessphonebook.city,
                            businessphonebook.country,
                            businessphonebook.postcode,

                            postcodes1.longitude,
                            postcodes1.latitude,

                            businessphonebook.tel,
                            businessphonebook.business_category


                            FROM businessphonebook

                            INNER JOIN postcodes1 ON (businessphonebook.postcode = postcodes1.postcode)

                            """)
      results = query.fetchall()
      return results
getBusinessPostcode()

def get_user_postcode():
    user_postcode = input('Please enter your postcode:').upper().replace(' ','')
    endpoint_postcode = "https://api.postcodes.io/postcodes/"
    postcode_url= endpoint_postcode+user_postcode
    post_response= requests.get(postcode_url).json()
    if post_response['status'] == 200:
            lon = post_response['result']['longitude']
            lat =post_response['result']['latitude']

            return lon,lat
    else:
        print("Please enter correct postcode")

def distance(lat1,long1,lat2,long2):
    R = 6373.0 # approximate radius of earth in km
    dlon = radians(long2) - radians(long1)
    dlat = radians(lat2) - radians(lat1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    a=abs(a)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    hdist = R * c
    return hdist




def filterPostcodes():
    database = getBuisnessPostcode()
    user_log_lat = list(get_user_postcode())
    busi = {}
    for row in database:
       business_lat_lat= list(row[5:7])
       dist = distance(user_log_lat[0],user_log_lat[1],float(business_lat_lat[0]),float(business_lat_lat[1]))
       busi[row[1]]= dist
    sorted_by_distance = sorted(busi.items(), key=lambda kv: kv[1])
    top50 = sorted_by_distance[:51]
    return top50



def desplay50():
    category_list = []
    top50 = filterPostcodes()
    database = getBuisnessPostcode()
    for values in top50:
        for data in database:
            if values[0] == data[1]:
                category_list.append(data)

    for row in category_list:
        print(row)


desplay50()


#- enter postcode/ category
#- find relevant and closest store
