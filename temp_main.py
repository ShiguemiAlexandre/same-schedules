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
        self.future_5hours = 0
        self.past_5hours = 0
        self.user_time_limit = 0
        self.minutes_now = 0
        self.hours_now = 0

    def time_diff(self):
        self.future_5hours = time_now + timedelta(hours=5)
        self.past_5hours = self.future_5hours - timedelta(hours=5)
        self.user_time_limit = int(self.future_5hours.strftime("%H"))


    def minutes_catch(self):
        self.minutes_now = int(time_now.strftime("%M"))
        return self.minutes_now


    def hours_catch(self):
        self.hours_now = int(time_now.strftime("%H"))
        return self.hours_now
    

    def equals_minutes_and_hours(self, time_diff, minutes_catch, hours_catch):
        if self.hours_now == self.minutes_now:
            print(getattr(self, "hora" + str(self.hours_now)))
        elif self.minutes_now <= self.user_time_limit and self.hours_now == self.past_5hours:
            print(getattr(self, "hora" + str(self.hours_now)))
        else:
            print('Nenhum horario compativel')


time_now = datetime.now()
time = Time_equals()
time.time()
