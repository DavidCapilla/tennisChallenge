from Score import score_from_points


class GameController:

    def __init__(self, single_game, announcement_view):
        self.__single_game = single_game
        self.__announcement_view = announcement_view
        self.update_view()

    def wins_point(self, player):
        self.__single_game.score_point(player)
        self.update_view()

    def update_view(self):
        if self.__single_game.has_finished():
            self.__announcement_view.show_winner(self.__single_game.get_winner())
        else:
            server_points = self.__single_game.get_server_points()
            receiver_points = self.__single_game.get_receiver_points()
            self.__announcement_view.show_score(score_from_points(server_points, receiver_points))
