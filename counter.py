class InstanceCounter():
    count = 0
    def __init__(self):
            InstanceCounter.count +=1
            self.id =InstanceCounter.count 
    def reset():
        InstanceCounter.count = 0 
