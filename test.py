#
# Python console app for debugging methods and DB calls
#


import GeoGuessing

# rows = GeoGuessing.Games.getLeaderboard()

rows = GeoGuessing.Games.getGamesCount()

print(rows)