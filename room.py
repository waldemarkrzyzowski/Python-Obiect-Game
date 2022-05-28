class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None

    def set_character(self, new_character):
        self.character = new_character
    
    def get_character(self):
        return self.character 
        
    #Here is a method to set the description of the room:

    def set_description(self,room_description):
        self.description = room_description

    #Here is a method to get the description of the room:

    def get_description(self):
        return self.description

    def set_name(self,name):
        self.names = name

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.name + " linked rooms :" + repr(self.linked_rooms) )

    # display all of the rooms linked to the current room object
    def get_details(self):
        print(self.name)
        print('-----------------')
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The  " + room.get_name() + " is " + direction)

    def move(self,direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
