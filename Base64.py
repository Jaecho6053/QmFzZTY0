base64_tb = {
    0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 
    8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 
    16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 
    24:"Y", 25:"Z", 26:"a", 27:"b", 28:"c", 29:"d", 30:"e", 31:"f", 
    32:"g", 33:"h", 34:"i", 35:"j", 36:"k", 37:"l", 38:"m", 39:"n", 
    40:"o", 41:"p", 42:"q", 43:"r", 44:"s", 45:"t", 46:"u", 47:"v", 
    48:"w", 49:"x", 50:"y", 51:"z", 52:"0", 53:"1", 54:"2", 55:"3", 
    56:"4", 57:"5", 58:"6", 59:"7", 60:"8", 61:"9", 62:"+", 63:"/"
}


def main():
    data = int(input("Encode:[0] Decode:[1]\n"))

    if data == 1:
        Decoding_Data()
    elif data == 0:
        Encoding_Data()
    else:
        print("Invalid value")


def Encoding_Data():
    base64_bins = []
    result = ''

    datas = input("Input Datas: ")
    bin_data = ''.join(format(ord(data), "08b") for data in datas)

    if len(bin_data)%6:
        bin_data += "0"*(6-(len(bin_data)%6))

    if len(datas)%3:
        padding = "="*(3-(len(datas)%3))
    else:
        padding = ""

    for cut in range(len(bin_data)//6):
        base64_bins.append(bin_data[cut*6:cut*6+6])

    for base64_bin in base64_bins:
        base64_int = int(base64_bin, 2)
        result += base64_tb.get(base64_int)

    print(result+padding)


def Decoding_Data():
    base64_strs = input("Input encoded Datas: ")

    ascii_bins = []
    base64_bin = ''
    result = ''

    base64_tb_reverse = dict(map(reversed, base64_tb.items()))
    padding_num = base64_strs.count('=')
    base64_strs = base64_strs.replace('='*padding_num, '')

    for base64_str in base64_strs:
        base64_bin += format(base64_tb_reverse.get(base64_str), "06b")

    if padding_num == 1:
        base64_bin = base64_bin[0:-2]
    elif padding_num == 2:
        base64_bin = base64_bin[0:-4]

    for cut in range(len(base64_bin)//8):
        ascii_bins.append(base64_bin[cut*8:cut*8+8])
    
    for ascii_bin in ascii_bins:
        result += chr(int(ascii_bin, 2))
    
    print(result)


if __name__ == "__main__":
    main()