import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load IPL data
def load_data(matches_file, deliveries_file):
    try:
        matches = pd.read_csv(matches_file)
        deliveries = pd.read_csv(deliveries_file)
        return matches, deliveries
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure the files 'matches.csv' and 'deliveries.csv' are in the correct directory.")
        return None, None

# Display basic information about the datasets
def explore_data(matches, deliveries):
    if matches is not None and deliveries is not None:
        print("Matches Dataset Info:")
        print(matches.info())
        print("\nDeliveries Dataset Info:")
        print(deliveries.info())

        print("\nFirst 5 rows of Matches Dataset:")
        print(matches.head())
        print("\nFirst 5 rows of Deliveries Dataset:")
        print(deliveries.head())

# Predict top teams by wins
def predict_top_teams(matches):
    if matches is not None:
        top_teams = matches['winner'].value_counts()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_teams.values, y=top_teams.index, palette='viridis')
        plt.title("Top Teams by Wins")
        plt.xlabel("Number of Wins")
        plt.ylabel("Teams")
        plt.show()
        print("Predicted Top Teams by Wins:")
        print(top_teams.head(10))

# Predict top players by runs
def predict_top_players(deliveries):
    if deliveries is not None:
        # Standardize column names to avoid case or whitespace issues
        deliveries.columns = deliveries.columns.str.strip().str.lower()
        if 'batter' in deliveries.columns and 'batsman_runs' in deliveries.columns:
            top_players = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False)
            plt.figure(figsize=(10, 6))
            sns.barplot(x=top_players.head(10).values, y=top_players.head(10).index, palette='coolwarm')
            plt.title("Top Players by Runs")
            plt.xlabel("Total Runs")
            plt.ylabel("Players")
            plt.show()
            print("Predicted Top Players by Runs:")
            print(top_players.head(10))
        else:
            print("Error: 'batsman' or 'batsman_runs' column not found in deliveries dataset.")

# Predict top bowlers by wickets
def predict_top_bowlers(deliveries):
    if deliveries is not None:
        # Standardize column names to avoid case or whitespace issues
        deliveries.columns = deliveries.columns.str.strip().str.lower()
        if 'bowler' in deliveries.columns and 'dismissal_kind' in deliveries.columns:
            wicket_deliveries = deliveries[deliveries['dismissal_kind'].notnull()]
            top_bowlers = wicket_deliveries['bowler'].value_counts().head(10)
            plt.figure(figsize=(10, 6))
            sns.barplot(x=top_bowlers.values, y=top_bowlers.index, palette='Blues')
            plt.title("Top Bowlers by Wickets")
            plt.xlabel("Total Wickets")
            plt.ylabel("Bowlers")
            plt.show()
            print("Predicted Top Bowlers by Wickets:")
            print(top_bowlers)
        else:
            print("Error: 'bowler' or 'dismissal_kind' column not found in deliveries dataset.")

# Analyze which team has the most wins
def analyze_team_with_most_wins(matches):
    if matches is not None:
        team_wins = matches['winner'].value_counts()
        most_wins_team = team_wins.idxmax()
        print(f"The team with the most wins is: {most_wins_team} with {team_wins.max()} wins.")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=team_wins.head(10).values, y=team_wins.head(10).index, palette='spring')
        plt.title("Teams with Most Wins")
        plt.xlabel("Number of Wins")
        plt.ylabel("Teams")
        plt.show()


def analyze_venues(matches):
    top_venues = matches['venue'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_venues.values, y=top_venues.index, palette='plasma')
    plt.title("Most Successful Venues")
    plt.xlabel("Number of Matches")
    plt.ylabel("Venues")
    plt.show()

# Analyze match results
def analyze_match_results(matches):
    result_types = matches['winner'].value_counts()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=result_types.index, y=result_types.values, palette='magma')
    plt.title("Match Results Distribution")
    plt.xlabel("Result Type")
    plt.ylabel("Count")
    plt.show()

# Main function to run the analysis
def main():
    matches_file = "matches.csv"  # Replace with the actual file path
    deliveries_file = "deliveries.csv"  # Replace with the actual file path

    matches, deliveries = load_data(matches_file, deliveries_file)

    if matches is not None and deliveries is not None:
        explore_data(matches, deliveries)

        print("\nPredicting top teams by wins...")
        predict_top_teams(matches)

        print("\nPredicting top players by runs...")
        predict_top_players(deliveries)

        print("\nPredicting top bowlers by wickets...")
        predict_top_bowlers(deliveries)

        print("\nAnalyzing the team with the most wins...")
        analyze_team_with_most_wins(matches)

        print("\nAnalyzing most successful venues...")
        analyze_venues(matches)

        print("\nAnalyzing match results distribution...")
        analyze_match_results(matches)

if __name__ == "__main__":
    main()
