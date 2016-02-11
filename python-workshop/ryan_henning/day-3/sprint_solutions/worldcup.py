from datetime import datetime
import os
import sys
import re


class WorldCupResults(object):

    def __init__(self, directory):
        '''
        INPUT:
            directory: str

        '''
        self.data = self._read_all(directory)


    def _read_all(self, directory):
        '''
        INPUT: string
        OUTPUT: list of tuples

        Given the directory where the data is stored,
        read the data from the directory and return as a list of tuples.
        '''
        data = []
        for filename in os.listdir(directory):
            data.append(self._read_game_info(os.path.join(directory, filename)))
        return data


    def _read_game_info(self, filename):
        '''
        INPUT: string
        OUTPUT: tuple of string, string, string, int, int

        Given the filename of a game, return the time, team names and score for the
        game. Return these values:

            time: string representing time of game
            team1: first team name
            team2: second team name
            score1: score of first team
            score2: score of second team
        '''
        # Read the file.
        with open(filename) as file:
            contents = file.read()

        # Use regular expression matching to parse the 5 values from the file contents.
        # See: https://docs.python.org/2/library/re.html#simulating-scanf
        parse = re.search("(.*)\n(.*)\n(.*)\n(.*) - (.*)\n(\d*)-(\d*)", contents)
        time = parse.group(1)
        team1 = parse.group(4)
        team2 = parse.group(5)
        score1 = int(parse.group(6))
        score2 = int(parse.group(7))
        return (time, team1, team2, score1, score2)


    def _display_game(self, time, team, other, team_score, other_score):
        '''
        INPUT: string, string, string, int, int
        OUTPUT: string

        Given the time, names of the teams and score, return a one line string
        presentation of the results.
        '''
        return "{0} {1} ({2}) - {3} ({4})".format(time, team, team_score, other, other_score)


    def display_summary(self, team, detailed=False):
        '''
        INPUT: string, bool
        OUTPUT: string

        Return a string containing the summary of results for the given team.
        This includes # games played, # wins, # losses, # ties, and # goals
        scored.

        If detailed is True, also include in the string all the games for the
        given team.
        '''
        output = '-' * 60 + "\n"
        played = 0
        wins = 0
        losses = 0
        ties = 0
        goals = 0
        for time, team1, team2, score1, score2 in self.data:
            if team1 == team or team2 == team:
                played += 1
                if score1 == score2:
                    ties += 1
                    goals += score1
                elif score1 > score2:
                    if team1 == team:
                        wins += 1
                        goals += score2
                    else:
                        losses += 1
                        goals += score1
                else:  # score2 > score1
                    if team2 == team:
                        wins += 1
                        goals += score1
                    else:
                        losses += 1
                        goals += score2
                if detailed:
                    output += self._display_game(time, team1, team2, score1, score2) + "\n"
        if detailed:
            output += ' ' * 20 + '-' * 20 + "\n"
        output += "played:{0} wins:{1} losses:{2} ties:{3} goals:{4}".format(
                played, wins, losses, ties, goals) + "\n"
        return output

def main():
    '''
    Get the directory name and team name from the arguments given. If arguments
    are valid, display the summary of results. Otherwise, exit the program.
    '''
    error_message = "Usage: python worldcup.py directory team\n" \
                    "       e.g. python worldcup.py worldcup USA"
    if len(sys.argv) != 3:
        print error_message
        exit()
    directory = sys.argv[1]
    if not os.path.exists(directory):
        print "{0} is not a valid directory.".format(directory)
        print error_message
        exit()
    team = sys.argv[2]
    wc = WorldCupResults(directory)
    print wc.display_summary(team, detailed=True)


if __name__ == '__main__':
    main()
