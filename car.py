class Car:
    """Class Car lab"""
    
    def __init__(self, name = 'General', model = 'GM', car_type = 'saloon'):
        self.name = name
        self.model = model
        self.num_of_doors = 4
        self.num_of_wheels = 4
        self.car_type = car_type
        self.speed = 0
        self.motion_speed = 0
        #if self.name is 'Porshe'or self.name is 'Koenigsegg', then self.num_of_doors is 2
        if (self.name == 'Porshe') or (self.name == 'Koenigsegg'):
            self.num_of_doors = 2
        #if self.car_type is 'trailer', then self.num_of_wheels is 8
        if self.car_type == 'trailer':
            self.num_of_wheels = 8   
             
    #Awaiting clarification on this method    
    def drive(self, motion_speed):
        """Method to find speed of moving car"""
        if motion_speed == 7:
            self.speed = 77
        elif motion_speed == 3:
            self.speed = 1000
        return self
            

    def is_saloon(self):
        """Method to determine whether the car is saloon or not"""
        if self.car_type != 'trailer':
            return True
        return False

toyota = Car('Toyota', 'Corolla')
print(toyota.name)

