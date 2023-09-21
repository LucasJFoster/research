# This is the back end which hold all of the info for how the tickets are made
class Make_Ticket:
# This here will ask for your basic info
    def __init__(self):

        self.prob = None
        self.name = input(
            "Whats your name? ")

        self.email = input(
            "Email Address ")

        self.user_id = input(
            "Staff ID ")

        print("")
# this is how the code will understand your Issue
    def main_problem(self):
        self.prob = input(
            "What is your Issue? ").lower()
# if your isses is to change password it will take you here. this will give you a new password using your name and ID
    def new_pw(self):
        if self.prob == "change password":
            ticket_done = 0
            ticket_done += 1
            tickets_created = 0
            tickets_created += 1
            Nw_password = (self.name[0:3]), (self.user_id[0:2])
            x = "".join(Nw_password)
            print(f'Ticket Stats \n')
            print(f'Ticket Created: {tickets_created}')
            print(f'Tickets To Solve: 0')
            print(f'Ticket Solved: {ticket_done}\n')

            ticket_person = [

                f'Ticket Creator: {self.name}',
                f'Staff ID: {self.user_id}',
                f'Email Address: {self.email}',
                f"new password is: {x}",
                'Response: New Password Provided',
            ]
            result = "\n".join(ticket_person)
            print(result)
# if your isses sint change password youll be taken here. this will just add your ticket to a counter that will be needed to be solved
    def No_reply(self):
        if Make_Ticket != "change password":
            ticket_need = 0
            ticket_need += 1
            tickets_created = 0
            tickets_created += 1
            print(f'Ticket Stats \n')
            print(f'Ticket Created: {tickets_created}')
            print(f'Tickets To Solve: {ticket_need}')
            print(f'Ticket Solved: 0\n')
            print(f'Ticket Creator: {self.name}')

        ticket_person = [
            f'Staff ID: {self.user_id}',
            f'Email Address: {self.email}',
            f'Description: {self.prob}',
            'Response: Not Yet Provided \n',

        ]
        result = "\n".join(ticket_person)
        print(result)
# if your isses wasnt change password but you have a way to fix the isses youll be able to put it in here if you say yes to have response
    def Have_Response(self):
        ticket_done = 0
        ticket_done += 1
        tickets_created = 0
        tickets_created += 1
        print(f'Ticket Creator: {self.name}')
        print(f'Description of problem : {self.prob}')
        new_resp = input("Whats the Response? ")
        print("")
        ticket_person = [
            f'Ticket Stats \n',
            f'Ticket Created: {tickets_created}',
            f'Tickets To Solve: 0',
            f'Ticket Solved: {ticket_done}\n',

            f'Staff ID: {self.user_id}',
            f'Email Address: {self.email}',
            f'Old Description of problem : {self.prob}',
            f'New Response: {new_resp}',

        ]
        result = "\n".join(ticket_person)
        print(result)
