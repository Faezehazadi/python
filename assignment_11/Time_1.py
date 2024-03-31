class Time:
    def __init__(self, hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()


    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new, m_new, s_new)
        return result


    def sub(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new, m_new, s_new)
        return result
    

    def second_to_time(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1
            while self.minute >= 60:
                self.minute -= 60
                self.hour += 1
        result = Time(self.hour, self.minute, self.second)
        return result
    

    def time_to_second(self):
        self.second = self.hour * 3600 + self.minute * 60 + self.second
        result = self.second
        return result
    

    def gmt_to_tehran(self):
        tehran_h = self.hour + 3
        tehran_m = self.minute + 30
        tehran_s = self.second
        result = Time(tehran_h, tehran_m, tehran_s)
        return result
    

    def show(self):
        print (self.hour, ":", self.minute, ":", self.second)


    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
            
        if self.minute < 0:
            self.minute += 60
            self.hour -= 1    

        if self.second < 0:
            self.second += 60
            self.minute -= 1



h_1 = int(input("🔸 enter first hour:"))
m_1 = int(input("🔸 enter first Min:"))
s_1 = int(input("🔸 enter first Sec:")) 

h_2 = int(input("🔸 enter second hour:"))
m_2 = int(input("🔸 enter second Min:"))
s_2 = int(input("🔸 enter second Sec:")) 
 

t1 = Time(h_1, m_1, s_1)
print("First time:")
t1.show() 

t2 = Time(h_2, m_2, s_2)
print("Second time:")
t2.show()

t3 = t1.sum(t2)
print("Sum:")
t3.show()

t4 = t1.second_to_time()
print("Second_to_time:")
t4.show()

t5=t2.time_to_second()
print("Time_to_second:")
print(t5)

tehran_time = t1.gmt_to_tehran()
print("Gmt_to_tehran:")
tehran_time.show()