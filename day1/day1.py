def main():
    with open('input') as f:
        content = [int(x) for x in f.readlines()]

    counter = 0
    for prev_item, item in zip(content[:-1], content[1:]):
        if item > prev_item:
            counter += 1

    print(counter)

if __name__ == '__main__':
    main()