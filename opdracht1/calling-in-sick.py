import random

actually_sick = bool(random.randint(0,1))
kinda_sick = bool(random.randint(0,1))
dont_feel_like_it = bool(random.randint(0,1))
sick_days = random.randint(0,10)

if actually_sick == 1 or kinda_sick == 1 or dont_feel_like_it == 1 and sick_days > 0:
    calling_in_sick = True
    print(f"Guys, I'm sick, days left: ", sick_days)
else:
    calling_in_sick = False
    print("What are you talking about, I'm good.")

while(sick_days):
    if sick_days > 0:
        sick_days -= 1
        print(f"I am still sick, cannot come. Days left: " ,sick_days)
    if sick_days == 0:
        print("Hi guys, I'm back in action!")
        break
    
