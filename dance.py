
"""A robot has been given a list of movement instructions. Each instruction
is either left, right, up or down, followed by a distance to move. The
robot starts at 0, 0. You want to calculate where the robot will end up
and return its final position as a list. For example, if the robot is given
the instructions ["right 10", "up 50", "left 30", "down 10"], it will end
up 20 left and 40 up from where it started, so you should return [-20, 40].
"""

from functools import reduce

"""Old
def add_val(acc, d_val):
    direction, v = d_val.split(' ')
    val = int(v)
    switch = {
        "up": [0, val],
        "down": [0, -val],
        "right": [val, 0],
        "left": [-val, 0]
    }
    add_val = switch[direction]
    return [acc[0] + add_val[0], acc[1] + add_val[1]]

def mr_roboto(instructions):
    return reduce(add_val, instructions, [0, 0])
"""

def map_dir_to_pair(direction, v_str):
    val = int(v_str)
    switch = {
        "up": (0, val),
        "down": (0, -val),
        "right": (val, 0),
        "left": (-val, 0)
    }
    return switch[direction]

def add_val(acc, d_val):
    direction, str_val = d_val.split(' ')
    parsed_val = map_dir_to_pair(direction, str_val)
    return (acc[0] + parsed_val[0], acc[1] + parsed_val[1])

def mr_roboto(instructions):
    return list(reduce(add_val, instructions, (0, 0)))

