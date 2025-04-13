def find_distance(target_x: int, target_y: int):
    layer = 0
    prev_layer, curr_layer = set(), set([(0, 0)])
    while (target_x, target_y) not in curr_layer:
        next_layer = set()
        for (x, y) in curr_layer:
            for next_cell in moves(x, y):
                if next_cell not in prev_layer:
                    next_layer.add(next_cell)
        prev_layer, curr_layer = curr_layer, next_layer
        layer += 1
    return layer


def moves(x: int, y: int):
    return [(x - 2, y + 1), (x - 2, y - 1),
            (x - 1, y + 2), (x - 1, y - 2),
            (x + 1, y + 2), (x + 1, y - 2),
            (x + 2, y + 1), (x + 2, y - 1)]
