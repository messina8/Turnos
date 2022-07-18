from gestor_turnos import client
from gestor_turnos import vehicle
import datetime


class Turn:
    def __int__(self, date, cl, ve, motive):
        self.date = date
        self.client = cl
        self.vehicle = ve
        self.motive = motive

    def __str__(self):
        print(self.date)
