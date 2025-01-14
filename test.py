
import GeoGuessing

#
# Python console app for debugging methods and DB calls
#

# rows = GeoGuessing.Games.getLeaderboard()
# rows = GeoGuessing.Games.getGamesCount()

game = {
    "name": "Andr",
    "points": 111
}

GeoGuessing.Games.saveGame(game)


#print(rows)