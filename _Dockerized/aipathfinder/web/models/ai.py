import numpy as np


### GENERATE 64x64 possible movements grid (1 - possible, 0 - impossible )

def grid(edge):
    full_grid = []
    for n in range(0, edge ** 2):
        grid = [0] * edge ** 2
        for i, j in enumerate(grid):
            if n % edge == 0:
                if i == n + 1 or i == n + edge or i == n - edge:
                    grid[i] = 1
            elif (n + 1) % edge == 0:
                if i == n + edge or i == n - 1 or i == n - edge:
                    grid[i] = 1
            else:
                if i == n + 1 or i == n + edge or i == n - 1 or i == n - edge:
                    grid[i] = 1
        full_grid.append(grid)

    return full_grid


def find_route(starting_location, ending_location, desert_storm_1,
               desert_storm_2, desert_storm_3, desert_storm_4, reward_grid):
    alpha = 0.75
    gamma = 0.9

    R_new = np.copy(reward_grid)
    R_new[ending_location, ending_location] = 1000
    R_new[desert_storm_1, desert_storm_1] = 0
    R_new[desert_storm_2, desert_storm_2] = 0
    R_new[desert_storm_3, desert_storm_3] = 0
    R_new[desert_storm_4, desert_storm_4] = 0
    Q = np.array(np.zeros([64, 64]))

    for i in range(10000):
        current_state = np.random.randint(0, 64)
        playable_actions = []
        for j in range(64):
            if j not in {desert_storm_1, desert_storm_2, desert_storm_3, desert_storm_4}:
                if R_new[current_state, j] > 0:
                    playable_actions.append(j)
        next_state = np.random.choice(playable_actions)
        TD = R_new[current_state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state, ])] - Q[
            current_state, next_state]
        Q[current_state, next_state] = Q[current_state, next_state] + alpha * TD

    route = [starting_location]
    next_location = starting_location
    while next_location != ending_location:
        next_location = np.argmax(Q[starting_location, ])
        route.append(next_location)
        starting_location = next_location
    return route


def best_route(starting_location, collection,
               desert_storm_1, desert_storm_2,
               desert_storm_3, desert_storm_4,
               ending_location, reward_grid):
    return find_route(starting_location, collection, desert_storm_1, desert_storm_2, desert_storm_3, desert_storm_4,
                      reward_grid) + find_route(collection, ending_location, desert_storm_1, desert_storm_2,
                                                desert_storm_3, desert_storm_4, reward_grid)[1:]
