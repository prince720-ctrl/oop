class Pod:
    #class variable
    members = {}

    #class constructor method

    def __init__(self, leader, cell):
        Pod.members [leader] = cell

    #method to add members and numbers to dictionary
    def add_member(self, member_to_add, cell_number):
        Pod.members [member_to_add] = cell_number

    #class method to print pod leaders and cell numbers

    def display_members(self):
        print("\n")
        for Pod.members, number in Pod.members.items():
            print(Pod.members, number)

    #prompt the pod leader name and number

leader = input("Whos is the leader?")
cell = input("What is the leader's cell number")

    #initialize the pod dictionary with the leader's name and number
pod = Pod(leader, cell)
pod.add_member(leader, cell)


amount = input("How many members would you like to add?")

for i in (0,amount):
    member = input("What is the member's name? ")
    cell = input("What is their cell number? ")
    pod.add_member(member, cell)
    
pod.display_members()


    
       



        
