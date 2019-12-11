from collections import namedtuple
import traceback
import math
from operator import attrgetter


def load_file(filename):
    Point = namedtuple('Point', ['x', 'y'])
    Laser = namedtuple('Laser', ['visible_asteroids', 'position'])
    DestroyOrder = namedtuple('DestroyOrder', ['number', 'position'])
    Result = namedtuple('Result', ['field', 'laser', 'destroy_order', 'max_y'])
    with open(filename, 'r') as f:
        data = f.read()
    data = data.split('\n')
    part_one = None
    part_two = None
    field = []
    for line in data:
        if 'RESULT' in line:
            line = line.split(',')
            position = Point(int(line[2]), int(line[3]))
            part_one = Laser(int(line[1]), position)
        elif 'ORDER' in line:
            line = line.split(',')
            orders = line[0].split('|')[1:]
            positions = line[1:]
            part_two = []
            for i in range(len(orders)):
                tmp = positions[i].split('|')
                point = Point(int(tmp[0]), int(tmp[1]))
                destroy_order = DestroyOrder(int(orders[i]), point)
                part_two.append(destroy_order)
        else:
            tmp = []
            for c in line:
                tmp.append(c)
            field.append(tmp)
    asteroids, max_y = get_asteroid_positions_from_field(field)
    return Result(asteroids, part_one, part_two, max_y)


def get_asteroid_positions_from_field(field):
    asteroids = set()
    Point = namedtuple('Point', ['x', 'y'])
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '#':
                asteroids.add(fix_point_coordinates(
                    Point(j, i), len(field) - 1))
    return asteroids, len(field) - 1


def fix_point_coordinates(point, max_y):
    Point = namedtuple('Point', ['x', 'y'])
    return Point(point.x, max_y - point.y)


def undo_coordinate_fix(point, max_y):
    Point = namedtuple('Point', ['x', 'y'])
    return Point(point.x, max_y - point.y)


def undo_set_coordinates(asteroids, max_y):
    return set([undo_coordinate_fix(x, max_y) for x in asteroids])


def get_heading(a, b):
    degrees = math.degrees(math.atan2(b.y-a.y, b.x-a.x))
    heading = (degrees + 270) % 360
    if heading == 0.0:
        heading = 360.0
    return heading


def get_distance(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def target_asteroids(asteroid, asteroids):
    Target = namedtuple('Target', ['heading', 'distance', 'position'])
    seen_asteroids = {}
    for other in asteroids:
        heading = get_heading(asteroid, other)
        distance = get_distance(asteroid, other)
        if heading in seen_asteroids:
            if distance < seen_asteroids[heading].distance:
                seen_asteroids[heading] = Target(heading, distance, other)
        else:
            seen_asteroids[heading] = Target(heading, distance, other)
    destroy_order = []
    for target in seen_asteroids:
        destroy_order.append(seen_asteroids[target])
    return sorted(destroy_order, key=attrgetter('heading'), reverse=True)


def part_one(asteroids, result, max_y):
    max_seen = -1
    max_point = None
    for asteroid in asteroids:
        base_option = set()
        base_option.add(asteroid)
        targets = target_asteroids(asteroid, asteroids - base_option)
        if len(targets) > max_seen:
            max_seen = len(targets)
            max_point = asteroid
    max_point = undo_coordinate_fix(max_point, max_y)
    assert(max_seen == result.visible_asteroids), (max_seen,
                                                   result.visible_asteroids)
    assert(max_point == result.position), (max_point,
                                           result.position)
    print('Part 1:', max_seen)


def part_two(asteroids, laser, result, max_y):
    base = set()
    base.add(fix_point_coordinates(laser.position, max_y))
    asteroids = asteroids - base
    targets = target_asteroids(fix_point_coordinates(
        laser.position, max_y), asteroids)
    eliminated = []
    while len(targets) > 0:
        destroy = set()
        for target in targets:
            destroy.add(target.position)
            eliminated.append(undo_coordinate_fix(target.position, max_y))
        asteroids = asteroids - destroy
        targets = target_asteroids(fix_point_coordinates(
            laser.position, max_y), asteroids)
    if result is not None:
        for check in result:
            if check.position != eliminated[check.number - 1]:
                print('ERROR:', check, eliminated[check.number - 1])
    print('Part 2:', eliminated[199].x * 100 + eliminated[199].y)


def solution(filename):
    data = load_file(filename)
    print('Solution: ' + filename)
    part_one(data.field, data.laser, data.max_y)
    part_two(data.field, data.laser, data.destroy_order, data.max_y)


try:
    solution('input.txt')
except Exception as e:
    print(traceback.format_exc())
