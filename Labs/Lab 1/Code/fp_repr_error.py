

def sum_to_ten_break(step):
    x = 0
    while x != 10:
        x = x + step
        if x > 10:
            break
    return x


def sum_to_ten_round(step):
    x = 0
    while round(x, 10) != 10:
        x = x + step


if __name__ == '__main__':
    steps = [0.1, 0.5]
    for s in steps:
        print(f'Sum to ten using break: {sum_to_ten_break(s)}, step: {s}')
        print(f'Sum to ten using round: {sum_to_ten_round(s)}, step: {s}')
