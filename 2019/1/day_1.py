def get_puzzle_input():
    with open('day_1.txt', 'r') as f:
        data = f.read()
    return data


def process_module_mass_list(data):
    return data.split()


def calculate_required_fuel(mass):
    return int(mass) // 3 - 2


def calculate_required_fuel_with_fuel(mass):
    total_fuel = 0
    added_fuel = calculate_required_fuel(mass)
    while added_fuel > 0:
        total_fuel += added_fuel
        added_fuel = calculate_required_fuel(added_fuel)
    return total_fuel


def day_1(data):
    print("Part 1:", sum(map(calculate_required_fuel, data)))
    print("Part 2:", sum(map(calculate_required_fuel_with_fuel, data)))


day_1(process_module_mass_list(get_puzzle_input()))
