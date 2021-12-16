def main():
    with open('input') as f:
        content = f.readlines()

    commands = [x.split(' ') for x in content]

    horiz = 0
    depth = 0

    for cmd, value in commands:
        if cmd == 'forward':
            horiz += int(value)
        elif cmd == 'down':
            depth += int(value)
        elif cmd == 'up':
            depth -= int(value)

    print(horiz, depth)
    print(horiz * depth)

if __name__ == '__main__':
    main()