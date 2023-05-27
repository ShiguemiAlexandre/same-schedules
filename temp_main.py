from datetime import datetime, timedelta
class Time_equals:
    def __init__(self):
        self.hora00 = 'Horario 00'
        self.hora01 = 'Horario 01'
        self.hora02 = 'Horario 02'
        self.hora03 = 'Horario 03'
        self.hora04 = 'Horario 04'
        self.hora05 = 'Horario 05'
        self.hora06 = 'Horario 06'
        self.hora07 = 'Horario 07'
        self.hora08 = 'Horario 08'
        self.hora09 = 'Horario 09'
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
        # now = datetime.now()
        minutes_now = self.catch_minutes()
        hours_now = self.catch_hours()
        diff_minutes = self.diff_5minutes()
        if minutes_now == hours_now:
            print(getattr(self, 'hora' + str(hours_now)))
        elif minutes_now <= diff_minutes and minutes_now >= hours_now:    
            print('Diferença de 5 minutos')
        else:
            print('Fora de horario')

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

time = Time_equals()
date = datetime.now()
print(time.time_equal())

# Hora será 5 horas a mais e será comparada com os minutos