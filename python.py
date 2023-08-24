class FlightTable:
    def __init__(self):
        self.matches = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"},
        ]

    def list_matches_by_team(self, team_name):
        matching_matches = []
        for match in self.matches:
            if match["Team 01"] == team_name or match["Team 02"] == team_name:
                matching_matches.append(match)
        return matching_matches

    def list_matches_by_location(self, location):
        matching_matches = []
        for match in self.matches:
            if match["Location"] == location:
                matching_matches.append(match)
        return matching_matches

    def list_matches_by_timing(self, timing):
        matching_matches = []
        for match in self.matches:
            if match["Timing"] == timing:
                matching_matches.append(match)
        return matching_matches

def main():
    flight_table = FlightTable()

    while True:
        print("Search Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            team_name = input("Enter the team name: ")
            matching_matches = flight_table.list_matches_by_team(team_name)
        elif choice == '2':
            location = input("Enter the location: ")
            matching_matches = flight_table.list_matches_by_location(location)
        elif choice == '3':
            timing = input("Enter the timing: ")
            matching_matches = flight_table.list_matches_by_timing(timing)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        print("Matching Matches:")
        for match in matching_matches:
            print(f"Location: {match['Location']}, Team 01: {match['Team 01']}, Team 02: {match['Team 02']}, Timing: {match['Timing']}")

if __name__ == "__main__":
    main()
