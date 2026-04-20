# Write your solution here
import json

#creating a player class to hold the data
class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = goals + assists
        
        
    def __str__(self):
        print(f"{self.name:21}{self.team:5}{self.goals} + {self.assists} = {self.points}")
        
class hockey_statistics_app:
    def __init__(self):
        self.players = []
        
    def load_data(self):
        filename = input("Enter the file name: ")
        try:
            with open(filename) as file:
                data = json.load(file)
                for player in data:
                    self.players.append(Player(**player))
            print(f"read the data of {len(self.players)} players")
        except FileNotFoundError:
            print("File not found")
            
    def execute(self):
        self.load_data()
        
        print("\ncommands:\n")
        print("0 quit")
        print("1 search")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals\n")
        
        while True:
            command = "command: "
            
            if command == "0":
                break
            
            elif command == "1":
                name = input("name: ")
                for player in self.players:
                    if player.name == name:
                        print(player)
            
            elif command == "2":
                team = sorted(list(set(p.team for p in self.players)))
                for team in teams:
                    print(team)
                    
            elif command == "3":
                countries = sorted(list(set(p.nationality for p in self.players)))
                for country in countries:
                    print(country)
                    
            elif command == "4":
                team = input("team: ")
                matching_players = sorted(list(filter(lambda p: p.team == team, self.players)))
                for player in matching_players:
                    print(player)
            
            elif command == "5":
                country = input("country: ")
                matching_players = sorted()
                    
                    
                    
app = hockey_statistics_app()
app.execute()