def most_freq_bit(datalist, bit_number):
    zeros = 0
    ones = 0

    for item in datalist:
        if item[bit_number] == '1':
            ones += 1
        else:
            zeros += 1

    return '0' if zeros > ones else '1'

def main():
    with open('input') as f:
        content = [x.strip() for x in f.readlines()]

    content_ox = content
    content_co2 = content
    for idx in range(len(content[0])):
        bit = most_freq_bit(content_ox, idx)
        content_ox = [x for x in content_ox if x[idx] == bit]
        if len(content_ox) == 1:
            ox = content_ox[0]

    for idx in range(len(content[0])):
        bit = '0' if most_freq_bit(content_co2, idx) == '1' else '1'
        content_co2 = [x for x in content_co2 if x[idx] == bit]
        if len(content_co2) == 1:
            co2 = content_co2[0]

    print(co2, ox)

    print(int(co2, 2) * int(ox, 2))
    
if __name__ == '__main__':
    main()