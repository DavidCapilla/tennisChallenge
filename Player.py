class Player:
    def __init__(self, role):
        self.__role = role
        self.points = 0

    def get_role(self):
        return self.__role
