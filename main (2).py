import random
lucky_number=random.randint(1,50)


if lucky_number<=10:
  fortune="you will have a sunny day "
elif lucky_number>10 and lucky_number<20:
  fortune="you will get married "
elif lucky_number>20 and lucky_number<30:
  fortune="you will get children "
elif lucky_number>30 and lucky_number<40:
  fortune="you will experience love "
elif lucky_number>40 and lucky_number<45:
  fortune="you will taste happiness"
else:
  fortune="you will have a laugh and experience joy"
  
print(fortune+"your lucky number is " +str(lucky_number))

print(f"{fortune}your lucky number is {lucky_number}")