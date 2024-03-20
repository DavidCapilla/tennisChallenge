import unittest

from AnnouncementView import AnnouncementView
from Display import Display
from GameController import GameController
from Player import Player
from SingleGame import SingleGame


class AcceptanceTests(unittest.TestCase):

    def test_increase_score_from_0_0_wins_server(self):
        display, game_controller = self.prepare_state_game(0, 0)
        self.assertEqual("The score is 0:0", display.message)
        game_controller.wins_point("Server")
        self.assertEqual("The score is 15:0", display.message)

    def test_increase_score_from_15_15_wins_receiver(self):
        display, game_controller = self.prepare_state_game(1, 1)
        self.assertEqual("The score is 15:15", display.message)
        game_controller.wins_point("Receiver")
        self.assertEqual("The score is 15:30", display.message)

    def test_increase_score_from_30_30_wins_server(self):
        display, game_controller = self.prepare_state_game(2, 2)
        self.assertEqual("The score is 30:30", display.message)
        game_controller.wins_point("Server")
        self.assertEqual("The score is 40:30", display.message)

    def test_increase_score_from_40_40_wins_receiver(self):
        display, game_controller = self.prepare_state_game(3, 3)
        self.assertEqual("The score is 40:40", display.message)
        game_controller.wins_point("Receiver")
        self.assertEqual("The score is 40:A", display.message)

    def test_increase_score_from_A_40_wins_receiver(self):
        display, game_controller = self.prepare_state_game(4, 3)
        self.assertEqual("The score is A:40", display.message)
        game_controller.wins_point("Receiver")
        self.assertEqual("The score is 40:40", display.message)

    def test_winning_point_from_40_30_wins_server(self):
        display, game_controller = self.prepare_state_game(3, 2)
        self.assertEqual("The score is 40:30", display.message)
        game_controller.wins_point("Server")
        self.assertEqual("Server wins", display.message)

    def test_winning_point_from_40_A_wins_receiver(self):
        display, game_controller = self.prepare_state_game(3, 4)
        self.assertEqual("The score is 40:A", display.message)
        game_controller.wins_point("Receiver")
        self.assertEqual("Receiver wins", display.message)

    def prepare_state_game(self, server_points, receiver_points):
        server = Player("Server")
        server.points = server_points
        receiver = Player("Receiver")
        receiver.points = receiver_points
        game = SingleGame(server, receiver)
        display = Display()
        view = AnnouncementView(display)
        game_controller = GameController(game, view)
        return display, game_controller


if __name__ == '__main__':
    unittest.main()
