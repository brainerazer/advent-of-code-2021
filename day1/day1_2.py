def main():
    with open('input') as f:
        content = [int(x) for x in f.readlines()]

    windows = list(zip(content, content[1:], content[2:]))
    counter = 0
    for prev_item, item in zip(windows[:-1], windows[1:]):
        if sum(item) > sum(prev_item):
            counter += 1

    print(counter)

if __name__ == '__main__':
    main()