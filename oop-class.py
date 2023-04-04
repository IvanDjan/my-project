class Cat:
    def __init__(self, color, cat_type,):
        self.color = color
        self.cat_type = cat_type
    def set_size(self):
        if self.cat_type == 'indoor':
            print("size is 'small' ")
        else:
            print("size is 'undefined' ")

class Tiger(Cat):
    def set_size(self):
        if self.cat_type == 'wild':
            print("size is 'big' ")
        else:
            print("size is 'undefined' ")


cat = Tiger(color='red', cat_type='wild')
cat.set_size()







