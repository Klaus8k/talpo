
def result(args: dict):
    return args['size_x'] * args['size_y']

class Culc_offset:
    def __init__(self, args):
        self.calculation = args[0]
        self.size_x = args[1]
        self.size_y = args[2]
        self.weigth = args[3]

    def culc_130(self):
        return self.size_x * self.size_y

    def culc_170(self):
        return self.size_x * self.size_y * 2

    def culc_300(self):
        return self.size_x * self.size_y * 100

