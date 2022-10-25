from time import sleep
from approver import Approver


class Director(Approver):
    def approve_100yen(self):
        sleep(10)
        return "OK"

    def approve_3000yen(self):
        sleep(10)
        return "OK"
