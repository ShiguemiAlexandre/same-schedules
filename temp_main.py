from datetime import datetime, timedelta
class Time_equals:
    def __init__(self):
        self.hora0 = 'Horario 00'
        self.hora1 = 'Horario 01'
        self.hora2 = 'Horario 02'
        self.hora3 = 'Horario 03'
        self.hora4 = 'Horario 04'
        self.hora5 = 'Horario 05'
        self.hora6 = 'Horario 06'
        self.hora7 = 'Horario 07'
        self.hora8 = 'Horario 08'
        self.hora9 = 'Horario 09'
        self.hora10 = 'Horario 10'
        self.hora11 = 'Horario 11'
        self.hora12 = 'Horario 12'
        self.hora13 = 'Horario 13'
        self.hora14 = 'Horario 14'        
        self.hora15 = 'Horario 15'
        self.hora16 = 'Horario 16'
        self.hora17 = 'Horario 17'
        self.hora18 = 'Horario 18'
        self.hora19 = 'Horario 19'
        self.hora20 = 'Horario 20'
        self.hora21 = 'Horario 21'
        self.hora22 = 'Horario 22'
        self.hora23 = 'Horario 23'
    

    def time_equal(self):
        minutes_now = self.catch_minutes()
        hours_now = self.catch_hours()
        diff_minutes = self.diff_5minutes()
        if minutes_now == hours_now:
            return (getattr(self, 'hora' + str(hours_now)))
        elif minutes_now <= diff_minutes and minutes_now >= hours_now:    
            return 'Dif 5minutes'
        else:
            return 'Fora de horario'

    def catch_minutes(self):
        time_now = datetime.now()
        minutes_now = time_now.strftime("%M")
        return int(minutes_now)
        
    def catch_hours(self):
        time_now = datetime.now()
        hours_now = time_now.strftime("%H")
        return int(hours_now)

    def diff_5minutes(self):
        now = datetime.now()
        five_hours_diff = now + timedelta(hours=5)
        return five_hours_diff.hour
