from flask import session, Response, render_template, request
from flask_restful import Resource
import json
from models.ai import grid, best_route


class Environment(Resource):

    def post(self):

        start_location = int(request.form['start_location'])
        base_location = int(request.form['base_location'])
        astronauts = int(request.form['astronauts'])
        desert_storm_1 = int(request.form['desert_storm_1'])
        desert_storm_2 = int(request.form['desert_storm_2'])
        desert_storm_3 = int(request.form['desert_storm_3'])
        desert_storm_4 = int(request.form['desert_storm_4'])
        desert_storms = [desert_storm_1, desert_storm_2, desert_storm_3, desert_storm_4]

        env_dict = {'start_location': start_location, 'base_location': base_location,
                    'astronauts': astronauts, 'desert_storm_1': desert_storm_1, 'desert_storm_2': desert_storm_2,
                    'desert_storm_3': desert_storm_3, 'desert_storm_4': desert_storm_4}

        env_set = {start_location, base_location, astronauts, desert_storm_1, desert_storm_2, desert_storm_3, desert_storm_4}

        ## Check if unique
        if len(env_set) < 7:
            return {'error': 'Objects should be placed on distinct tiles'}


        ## Check if there's a distance to prevent stucking
        for i in desert_storms:
            if abs(i - astronauts) < 2 or abs(i - start_location) < 2 or abs(i - start_location) < 2:
                return {'error': 'Desert Storms should be placed at least one tile from the other objects'}

        session['env_dict'] = env_dict
        session['desert_storms'] = desert_storms

        return env_dict


class Pathfinder(Resource):

    def post(self):

        env_dict = session.get('env_dict')
        desert_storms = session.get('desert_storms')

        reward_grid = grid(8)

        starting_location = env_dict['start_location']
        ending_location = env_dict['base_location']
        collection = env_dict['astronauts']
        desert_storm_1, desert_storm_2, desert_storm_3, desert_storm_4 = desert_storms

        # Returns List
        path = best_route(starting_location, collection,
                          desert_storm_1, desert_storm_2,
                          desert_storm_3, desert_storm_4,
                          ending_location, reward_grid)

        # my_path_json = json.dumps(path)
        str_path = [ str(element) for element in path ]
        env_dict['path'] = str_path
        return env_dict
        # return Response(render_template('algorithms/route.html', env_dict=env_dict, path=path, mimetype='text/html'))
