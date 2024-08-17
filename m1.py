from os import system
from time import sleep



class Time :
     def __init__(self,hour,minute,second) -> None:
          self.hour=hour
          self.minute=minute
          self.second=second
          self.max_second=60
          self.max_minute=60
          self.max_hour=24


     def get_hour(self):
               return self.hour
          

     def get_minute(self):
       return self.minute

     def get_second(self):
       return self.second

     def set_hour(self,new_hour):
       self.hour=new_hour

     def set_minute(self,new_minute):
       self.minute=new_minute


     def set_second(self,new_second):
         self.second=new_second
     
     def set_time(self,hour,minute,second):
         self.hour=hour
         self.minute-minute
         self.second=second

     def tostring(self):
         return '%02d : %02d : %02d '%(self.hour,self.minute,self.second)
     

     def nextsecond(self):
         
         
         self.second+=1

         if self.second == self.max_second:
             self.second=0
             self.minute+=1

             if self.minute == self.max_minute:
                 self.max_minute=0
                 self.max_hour+=1

                 if self.hour==self.max_hour:
                     self.hour=0

             

time=Time(0,0,0)

while True:
    system("cls")
    print(time.tostring())
    time.nextsecond()
    sleep(1)





          