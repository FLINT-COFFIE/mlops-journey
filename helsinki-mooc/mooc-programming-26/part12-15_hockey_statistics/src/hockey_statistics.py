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
        return f"{self.name:21}{self.team:5}{self.goals:>2} + {self.assists:>2} = {self.points:>3}"
        
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
            command = input("command: ")
            
            if command == "0":
                break
            
            elif command == "1":
                name = input("name: ")
                for player in self.players:
                    if player.name == name:
                        print(player)
            
            elif command == "2":
                teams = sorted(list(set(p.team for p in self.players)))
                for team in teams:
                    print(team)
                    
            elif command == "3":
                countries = sorted(list(set(p.nationality for p in self.players)))
                for country in countries:
                    print(country)
                    
            elif command == "4":
                team = input("team: ")
                matching_players = sorted(list(filter(lambda p: p.team == team, self.players)))
                for player in sorted(matching_players, key = lambda p: p.points, reverse=True):
                    print(player)
            
            elif command == "5":
                country = input("country: ")
                matching_players = sorted(list(filter(lambda p: p.nationality == country, self.players)))
                for player in sorted(matching_players, key = lambda p: p.points, reverse=True):
                    print(player)
            
            elif command == "6":
                number = int(input("How many: "))
                top_players = sorted(self.players, key=lambda p: (p.points, p.goals), reverse=True)
                for i in range(number):
                    print(top_players[i])
                    
            elif command == "7":
                number = int(input("How many: "))
                top_scorers = sorted(self.players, key=lambda p: (p.goals, -p.games), reverse=True)
                for i in range(number):
                    print(top_scorers[i])
                    
app = hockey_statistics_app()
app.execute()