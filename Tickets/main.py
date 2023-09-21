# This is the main file which is where the tickets will be made. 
from Ticket import Make_Ticket

Num_o_tic = int(input("How many tickets do you want to make: "))
Tic_List = []

for i in range(Num_o_tic):
    count = len(Tic_List)
    count += 2001

    newTicket = Make_Ticket()
    Tic_List.append(newTicket)

    print(count)

# this will ask what ticket you wnat to open. Right now the only ticket that can be opned is that last one that was made
class Open_ticket:
    Opened_tic = int(input("What ticket do you want to open? Ticket Number please "))
    if Opened_tic != count:
        print("Void Input")
    else:
        print(newTicket.main_problem())

        if newTicket.prob == "change password":
            (newTicket.new_pw())

        if newTicket.prob != "change password":
            (newTicket.No_reply())
            answer = input("Do you have a response? yes/no ")
            if answer == "yes":
                (newTicket.Have_Response())
            else:
                (newTicket.No_reply())
