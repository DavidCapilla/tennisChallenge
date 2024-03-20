class AnnouncementView:

    def __init__(self, display):
        self.__display = display

    def show_winner(self, player):
        self.__display.show(player.get_role() + " wins")

    def show_score(self, score):
        self.__display.show("The score is " + score.get_score())
