
class Infer:

    def __init__(self):

        self.number=0

    def detect(self, image):

        self.number+=1
        return self.number

    def get_number(self):

        return self.number