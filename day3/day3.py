def main():
    with open('input') as f:
        content = [x.strip() for x in f.readlines()]

    gamma = ''
    eps = ''

    freq = [{'0': 0, '1': 0} for _ in content[0]]

    for d in content:
        for idx, n in enumerate(d):
            freq[idx][n] += 1
    
    for f in freq:
        if f['0'] > f['1']:
            gamma += '0'
            eps += '1'
        else:
            gamma += '1'
            eps += '0'

    gamma = int(gamma, base=2)
    eps = int(eps, base=2)

    print(gamma * eps)
    
if __name__ == '__main__':
    main()