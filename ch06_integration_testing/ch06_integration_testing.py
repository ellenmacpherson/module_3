#Integration testing looks for critical functions that other function rely on.
#End-to-end testing to do with event flow and UX. Last stage of testing

from functionalities import *

class TestFunctions(self):

    def test_check_db():
        self.checked = self.check_db()
        return self.checked

    def test_get_db(self):
        self.test_check_db()
        if self.checked:
            connected = self.query_db
            if connected:
                self.connected = True
                return self.connected
            else:
                self.connected = False
                return self.connected
        else:
            print ('Database does not exist.')


    def test_queryDB(self):
        query = "SELECT * FROM business_table"
        results = self.query_db()
        if results:
            self.query = True
        else:
            self.query = False

    def run_tests(self):
        self.test_check_db()
        self.test_get_db()
        seld.test_queryDB()
