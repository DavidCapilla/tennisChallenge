def player_score_from_points(player_points, other_player_points):
    if player_points == 0:
        return "0"
    elif player_points == 1:
        return "15"
    elif player_points == 2:
        return "30"
    elif player_points == 3:
        return "40"
    elif player_points > 3:
        if player_points == other_player_points:
            return "40"
        elif player_points - other_player_points == -1:
            return "40"
        elif player_points - other_player_points == 1:
            return "A"
    raise ValueError("Invalid points")


def score_from_points(server_points, receiver_points):
    server_score = player_score_from_points(server_points, receiver_points)
    receiver_score = player_score_from_points(receiver_points, server_points)
    return Score(server_score + ":" + receiver_score)


class Score:

    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score
