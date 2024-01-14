class TeeShirt:
    def __init__(self, color, inventory_count):
        self.color=color
        self.inventory_count=inventory_count

    def __str__(self):
        return f"The {self.color} of the Tee Shirts have "\
                f"{self.inventory_count} count available"
    def __add__(self,other_self):
        result = self.inventory_count + other_self.inventory_count
        return result


black_shirt = TeeShirt('Black', 14)
white_shirt = TeeShirt('White', 10)

print('color is : ', black_shirt.color)
print('Inventory Count is : ', black_shirt.inventory_count)

print('color is : ', white_shirt.color)
print('Inventory Count is : ', white_shirt.inventory_count)

print(black_shirt)
print(black_shirt + white_shirt)

