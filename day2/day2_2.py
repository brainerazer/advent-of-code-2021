def main():
    with open('input') as f:
        content = f.readlines()

    commands = [x.split(' ') for x in content]

    horiz = 0
    depth = 0
    aim = 0

    for cmd, value in commands:
        if cmd == 'forward':
            horiz += int(value)
            depth += aim * int(value)
        elif cmd == 'down':
            aim += int(value)
        elif cmd == 'up':
            aim -= int(value)

    print(horiz, depth)
    print(horiz * depth)

if __name__ == '__main__':
    main()