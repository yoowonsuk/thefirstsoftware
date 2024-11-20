class Matter:
    freezing_temperature = None
    boiling_temperature = None
    def __init__(self, temperature):
        self.temperature = temperature
                                    
    def state(self):
        if self.temperature <= self.freezing_temperature:
            return 'solid'
        elif self.freezing_temperature < self.temperature < self.boiling_temperature:
            return 'liquid'
        elif self.temperature > self.boiling_temperature:
            return 'gas'

class Water(Matter):
    freezing_temperature = 0
    boiling_temperature = 100
                                                                                                                        
    def __init__(self, temperature):
        super().__init__(temperature)
                                                                                                                                            
class Mercury(Matter):
    freezing_temperature = -38.831
    boiling_temperature =356.7
                                                                                                                                                            
    def __init__(self, temperature):
        super().__init__(temperature)
                                                                                                                                                                                
water = Water(-1)
print(water.state())
mercury = Mercury(-1)
print(mercury.state())
