from random import shuffle


def myprint(field):
    for row in reversed(field):
        print("".join(str(i) for i in row))
    print("\n")


def move(pos, dx, dy):
    return pos[0] + dx, pos[1] + dy


def get_neighbours(pos, size):
    neighbours = (
        move(pos, 0, 1),
        move(pos, 1, 0),
        move(pos, 1, -1),
        move(pos, 0, -1),
        move(pos, -1, 0),
        move(pos, -1, 1)
    )
    return (n for n in neighbours if 0 <= n[0] < size[0] and 0 <= n[1] < size[1])


def verify_neighbours(my_pos, next_pos, field, size):
    for n in get_neighbours(next_pos, size):
        if n != my_pos and field[n[0]][n[1]] == 1:
            return False
    return True


def step(pos, field, size):
    field[pos[0]][pos[1]] = 1
    neighbours = list(get_neighbours(pos, size))
    shuffle(neighbours)
    for n in neighbours:
        if n == (size[0] - 1, size[1] - 1):
            field[n[0]][n[1]] = 1
            myprint(field)
            return True
    for n in neighbours:
        if field[n[0]][n[1]] == 0 and verify_neighbours(pos, n, field, size):
            if step(n, field, size):
                return True
    field[pos[0]][pos[1]] = 0


def generate_random_path(max_y, max_x):
    size = (max_y, max_x)
    field = [[0] * size[1] for i in range(size[0])]
    step((0, 0), field, size)
    return field

