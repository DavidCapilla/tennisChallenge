class SingleGame:

    def __init__(self, server, receiver):
        self.server = server
        self.receiver = receiver

    def has_finished(self):
        if abs(self.server.points - self.receiver.points) < 2:
            return False
        elif self.server.points >= 4 or self.receiver.points >= 4:
            return True

    def get_winner(self):
        if self.has_finished():
            return self.server if self.server.points > self.receiver.points else self.receiver
        return None

    def get_server_points(self):
        return self.server.points

    def get_receiver_points(self):
        return self.receiver.points

    def score_point(self, player):
        if player == "Server":
            self.server.points += 1
        elif player == "Receiver":
            self.receiver.points += 1
        else:
            raise ValueError("Invalid player")
