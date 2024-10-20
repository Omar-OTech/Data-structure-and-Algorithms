class Block:
        def __init__(self, dimensions):
            self.width = dimensions[0]
            self.length = dimensions[1]
            self.height = dimensions[2]
        def get_width(self):
            return self.width
        def get_length(self):
            return self.length
        def get_height(self):
            return self.height
        def get_volume(self):
            return self.width * self.length * self.height
        # To get the surface area (SA)=2lw+2lh+2hw
        def get_surface_area(self):
            return 2 * (self.length * self.width) + 2 * (self.length * self.height) + 2 * (self.height * self.width)



block1 = Block([2,2,2])
print(block1.get_width())            # 2
print(block1.get_length())           # 2
print(block1.get_height())           # 2
print(block1.get_volume())           # 8
print(block1.get_surface_area())     # 24