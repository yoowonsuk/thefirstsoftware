class Water:
    boiling_temperature = 100
    freezing_temperature = 0
                
    def __init__(self, temperature):
        self.temperature = temperature
                                    
    def state(self):
        if self.temperature <= self.freezing_temperature:
            return 'solid'
        elif self.freezing_temperature < self.temperature < self.boiling_temperature:
            return 'liquid'
        elif self.temperature > boiling_temperature:
            return 'gas'
                                                                                                                    
                                                                                                            
'''
water = Water(temperature=20)
water.boiling_temperature = 212
water.freezing_temperature = 32
print(water.state())

Compare the above class with the class below.
So, the bottom line is, don't hardcode values in expressions. Store them in variables and use the variables in your code.

'''
