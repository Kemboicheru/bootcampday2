class Car(object):
    name = ''
    model = ''
    cartype = 'saloon'
    num_of_doors = 4
    num_of_wheels = 4
    def __init__(self,carmodel = 'GM',carname = 'General',cartype = ''):
        self.name = carname
        self.model = carmodel
        
        if self.model.lower() == 'porshe' or self.model.lower() == 'koenigsegg':
            self.num_of_doors = 2

        if cartype.lower() == "trailer":
            self.cartype = 'trailer'
            self.num_of_wheels = 8
            
        
        
     
