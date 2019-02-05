#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:44:33 2019

@author: hienh
"""

from searchdb import *





class TestSearch():

#    def getBusinessDB(self):
#        self.getDb = self.getDb()
#        return self.getDb
##
    def test_get_user_postcode(self):
        self.postcode = get_user_postcode()
        if self.postcode:
            return True
        else:
            return False

    def test_getuser_geolocation(self):
        if self.postcode:
            geolocation = getuser_geolocation() #Second input prompt
            if geolocation:
                return True
            else:
                print ('Could not retrieve geolocation')
                return False
        else:
            return "post code does not exist"



    def run_tests(self):
#       print(self.getBusinessDB())
        print(self.test_get_user_postcode())
        print(self.test_getuser_geolocation())


if __name__ == "__main__":
    newTest = TestSearch()
    newTest.run_tests()
