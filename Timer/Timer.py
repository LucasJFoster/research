import time

my_time = int(input("Enter the time in seconds: "))

# This here is how the counter . To get the counter to go down instead of up you do -1 to make it go up use +1
for x in range(my_time, 0, -1):
# This calculates how many seconds there are
    seconds = x % 60
# This calculates minutes by using secconds
    minutes = int(x / 60) % 60
# This calculates hours by using secconds
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")

