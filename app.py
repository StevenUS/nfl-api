from flask import Flask, json, jsonify
from flask.json import dumps

import nflgame

app = Flask(__name__)


@app.route('/')
def getRushingYds():
    data = {}
    games = nflgame.games(2013, week=1)
    players = nflgame.combine_game_stats(games)
    for p in players.rushing().sort('rushing_yds').limit(5):
        data[str(p)] =   {
                            "rushing attempts": p.rushing_att,
                            "rushing yards": p.rushing_yds,
                            "rushing tds": p.rushing_tds
                        }
    return json.dumps(data)

app.run(debug=True)
