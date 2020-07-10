
"""A robot has been given a list of movement instructions. Each instruction
is either left, right, up or down, followed by a distance to move. The
robot starts at 0, 0. You want to calculate where the robot will end up
and return its final position as a list. For example, if the robot is given
the instructions ["right 10", "up 50", "left 30", "down 10"], it will end
up 20 left and 40 up from where it started, so you should return [-20, 40].
"""

from functools import reduce
from typing import List, Tuple

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

def map_dir_to_pair(d_val_str) -> Tuple[int, int]:
    direction, v_str = d_val_str.split(' ')
    val = int(v_str)
    switch = {
        "up": (0, val),
        "down": (0, -val),
        "right": (val, 0),
        "left": (-val, 0)
    }
    return switch[direction]

def add_val(acc, d_val) -> Tuple[int, int]:
    old_left, old_right = acc
    cur_left, cur_right = map_dir_to_pair(d_val)
    return (old_left + cur_left, old_right + cur_right)

def mr_roboto(instructions) -> List[int]:
    return list(reduce(add_val, instructions, (0, 0)))

