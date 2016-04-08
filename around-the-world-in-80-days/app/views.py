import datetime, time
from flask import request
import flask
from app import app

import config, graph, sabre


@app.route('/get_path')
def get_path_from_origin():
    """
    Given the name of a city as input, pass it the path finding algorithm and return the path in JSON as the result.
    """
    input_origin = request.args.get("origin", None)
    cities_to_avoid = request.args.get("cities_to_avoid", [])
    cities_to_visit = request.args.get("cities_to_visit", [])
    if cities_to_avoid:
        cities_to_avoid = cities_to_avoid.split(",")
    if cities_to_visit:
        cities_to_visit = cities_to_visit.split(",")
    n_cities = request.args.get("n_cities", 10)
    if input_origin:
        # Look up what city the user entered
        origin = None
        for city in config.cities.values():
            if input_origin.lower() in city.lower() or city.lower() in input_origin.lower():
                origin = config.airport_codes[city]
                break
        if not origin:
            return flask.jsonify({"error": True})
        path = graph.path_finder(origin, cities_to_visit, cities_to_avoid, int(n_cities))
        duration = graph.calculate_total_duration(path)
        json = {
            "origin_airport": origin,
            "origin_city": config.cities[origin],
            "path": list(path),
            "duration": duration,
            "error": False
        }
        return flask.jsonify(**json)
    else:
        return "Error: invalid origin"


@app.route('/get_price')
def get_price_from_path():
    """
    Given a path, find the total cost of the path.
    """
    origin = request.args.get("origin", None)
    cities_to_avoid = request.args.get("cities_to_avoid", [])
    cities_to_visit = request.args.get("cities_to_visit", [])
    start_date = datetime.datetime.fromtimestamp(time.time())
    if cities_to_avoid:
        cities_to_avoid = cities_to_avoid.split(",")
    if cities_to_visit:
        cities_to_visit = cities_to_visit.split(",")
    n_cities = request.args.get("n_cities", 10)
    if origin:
        price = graph.estimate_total_price(graph.path_finder(origin, cities_to_visit, cities_to_avoid, n_cities), start_date)
        json = {
            "price": price
        }
        return flask.jsonify(**json)
    else:
        return "Error: invalid origin"


@app.route('/update_database')
def download_to_database():
    """
    Updates the database.
    """
    sabre.download_flight_duration_data()
    return "Done"


@app.route('/show_graph')
def show_graph():
    """
    Show the graph currently stored in the database.
    """
    return str(graph.generate_graph())


@app.route('/')
def index():
    return app.send_static_file("index_new.html")
