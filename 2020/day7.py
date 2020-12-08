with open(f'day7_input.txt') as f:
    entries = [line.strip() for line in f]

def part1(entries):
    bag_policy = helper(entries)
    valid_outer = set()
    next_check = {'shiny gold'}
    while True:
        check_now = next_check
        next_check = set()
        for outer_bag in bag_policy:
            #print()
            #print(f'{outer_bag=}')
            for bag_to_check in check_now:
                #print()
                #print(f'{bag_to_check=}')
                #print(f'bag_policy[{outer_bag}]={bag_policy[outer_bag]}')
                #print(f'check if bag is not in {valid_outer=}')
                if bag_to_check in bag_policy[outer_bag]:
                    print(f'{bag_to_check=} is in bag_policy[{outer_bag}]={bag_policy[outer_bag]}')
                    next_check.add(outer_bag)
        if not next_check:
            break
        else:
            valid_outer.update(next_check)
    print(valid_outer)
    return len(valid_outer)

def part2(entries):
    # helper = dict of dict of all bags, eg:
    # {'shiny gold : {'pale maroon': 2, 'pale purple': 5, 'posh brown': 4, 'dotted turquoise': 1}, ...}
    bag_policy = helper(entries)
    def rec(bag_name, how_often):
        return sum(rec(key, value * how_often) for key, value in bag_policy[bag_name].items()) + how_often

    return rec('shiny gold', 1) - 1 # minus outer bag

def part2_iter(entries):
    bag_policy = helper(entries)
    sum_ = -1 # we need to find out how many bags are IN shiny gold, so sum = -1 to exclude shiny gold itself
    bags_to_open = {
        'shiny gold': 1
    }
    i = 0
    while len(bags_to_open) > 0: #while there are still bags to open
        #print(f'round {i}')
        #i += 1
        #print(f'{bags_to_open=}')

        new_bags_to_open = {}
        # open bags
        for outer_bag, number_of_outer_bags in bags_to_open.items():
            #print(bag_policy[outer_bag])
            for inner_bag, number_of_inner_bags in bag_policy[outer_bag].items():
                # add bags to temporary list of bags to open
                if inner_bag in new_bags_to_open:
                    new_bags_to_open[inner_bag] += number_of_outer_bags * number_of_inner_bags
                else:
                    new_bags_to_open[inner_bag] = number_of_outer_bags * number_of_inner_bags
            # add sum of values to sum_
            sum_ += number_of_outer_bags
        # replace old bags to open with new ones.
        bags_to_open = new_bags_to_open
    return sum_


def helper(entries):
    def helper_helper(entry):
        entry = [x.strip() for x in entry.split('bags contain', 1)]
        outer_bag = entry[0]

        if entry[1].startswith('no'):
            return outer_bag, {}
        else:
            contains = entry[1].split(',')
            contains[-1] = contains[-1][:-1]  # get rid of the `.`
            contains[:] = [bag.split() for bag in contains]
            for bag in contains:
                bag.pop(-1)
            d = {}
            for bag in contains:
                bag_name = ' '.join(bag[1:])
                bag_number = int(bag[0])
                d[bag_name] = bag_number
            return outer_bag, d

    bag_policy = {}
    for entry in entries:
        key, value = helper_helper(entry)
        bag_policy[key] = value

    return bag_policy


if __name__ == '__main__':
    print(part2_iter(entries))