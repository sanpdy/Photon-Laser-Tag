# required imports
import threading

# inter-reference classes
from src.Server import UDPServer
from db.PlayerDB import PlayerDB
from src.ui import ui_start

# Program Object for program inter-references (like server to ui or Player object to ui)
class Program:
    def __init__(self):
        # initialize program objects/inter-references
        self.database = PlayerDB()  # initialize database connection
        self.udp_server = UDPServer(("127.0.0.1", 7500), ("127.0.0.1", 7501))  # set server sockets transmit over 7500, receive over 7501

        # setup listening thread for udp socket
        try:
            self.udp_thread = threading.Thread(target=self.udp_handler, daemon=True)
            print("Starting UDP Daemon")
            self.udp_thread.start()
        except Exception:
            print(Exception)

        # initialize player lists, will hold player objects
        self.red_team = []
        self.green_team = []
        print("Starting UI")
        # start ui (frontend)
        ui_start(self)

    # Player object to hold player_id & equipment_id together
    class Player:
        def __init__(self, player_id, codename, equipment_id):
            self.player_id = player_id
            self.codename = codename
            self.equipment_id = equipment_id

    # Function for Thread that handles udp receive
    def udp_handler(self):
        while True:
            try:
                # get received message from udp server
                message = self.udp_server.receive_message()
                player_attacking, player_hit = message.split(':')
                player_attacking = int(player_attacking)
                player_hit = int(player_hit)
                # !REPLACE WITH RELEVANT CODE!
                #self.udp_server.transmit_message(str(player_hit))
            except Exception as e:
                print("Error in udp_handler / udp daemon: ", e)

    # Function to insert players to teams and avoid duplicates
    def add_team_player(self, player: Player, team: str) -> bool:
        #choose team that play will be added to, either "red" for red_team or "green" for green_team
        active_team: list
        if team == "red":
            active_team = self.red_team
        elif team == "green":
            active_team = self.green_team
        else:
            print("ERROR: add_team_player: Invalid Team List")
            return False #return early if incorrect team input given

        #check for player in either team
        already_in_game: bool = False
        player_id = player.player_id # don't lookup given player_id each check
        #only check lists if it has players in it
        if len(self.red_team) > 0:
            for member in self.red_team:
                if player_id == member.player_id:
                    already_in_game = True
        if len(self.green_team) > 0:
            for member in self.green_team:
                if player_id == member.player_id:
                    already_in_game = True

        # return true if player was added to team or false if the player is already in the game
        if not already_in_game:
            active_team.append(player)
            return True
        else:
            return False

    # function to remove a specific player by id from team(s)
    def remove_team_player(self, player_id, team: str = "both") -> bool:
        # defaults to searching both teams, but can specify a single team if aware of team player was added to
        check_red_team: bool = False
        check_green_team: bool = False
        if team == "both":
            check_red_team = True
            check_green_team = True
        elif team == "red":
            check_red_team = True
        elif team == "green":
            check_green_team = True
        else:
            print("ERROR: remove_team_player: Invalid Team Selection")
            return False

        # check through team list to find and remove given player_id (removes player from both teams if they are somehow in both teams)
        player_removed: bool = False  # boolean to return to detemine if player was removed (true) or player was not removed/not in teams (false)
        if check_red_team:
            for member in self.red_team:
                if player_id == member.player_id:
                    self.red_team.remove(member)
                    player_removed = True
        if check_green_team:
            for member in self.green_team:
                if player_id == member.player_id:
                    self.green_team.remove(member)
                    player_removed = True

        return player_removed

    # function to clear team_lists
    def clear_teams(self):
        self.red_team.clear()
        self.green_team.clear()


# starts program
if __name__ == "__main__":
    main = Program()