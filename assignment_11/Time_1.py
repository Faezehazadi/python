class Time:
    def __init__(self , hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()

    def show(self):
        print(self.hour ,":", self.minute ,":", self.second)

    def sum(self , other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new, m_new, s_new)
        return result
    
    def sub(self , other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new, m_new, s_new)
        return result
    
    def second_to_time(self,second):
        c_hour = second // 3600
        remain = second - 3600 * c_hour
        c_min = remain // 60
        c_sec = remain - 60 * c_min
        result = Time(c_hour, c_min, c_sec)
        return result
    
    def time_to_second(self, other):
        c_sec = other.hour * 3600 + other.minute * 60 + other.second
        result = c_sec
        return result

    def convert_to_timeZone(self):
        t=Time(3, 30, 0)
        teh_time=self.sum(t)
        return teh_time
    
    def fix(self):

        if self.second >= 60:
            self.second -= 60
            self.minute +=1

        if self.minute >= 60:
            self.minute -= 60
            self.hour +=1

        if self.minute < 0:
            self.minute += 60
            self.hour -= 1

        if self.second < 0:
            self.second += 60
            self.minute -= 1

t1 = Time(3, 4 , 31)
t1.show()        
t2 = Time(7, 31 , 4)
t2.show()
t3 = t1.sum(t2)
t3.show()

teh_time = t1.convert_to_timeZone()
teh_time.show()
seconds = teh_time.time_to_second()
print("Seconds : ", seconds)
time = Time.seconds_to_time(5600) 
time.show()
