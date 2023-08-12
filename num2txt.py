class Convert():
    def __init__(self, num):
        self.num = num
        self.listed = list(str(num))
        while len(self.listed) != 3:
            self.listed.insert(0, "0")
    hundred_map = {
        "0": "*",
        "1": "!",
        "2": "#"
    }
    hunded_swaped = {value: key for key, value in hundred_map.items()}

    ten_map = {
        "0": "z",
        "1": "a",
        "2": "b",
        "3": "c",
        "4": "d",
        "5": "e",
        "6": "f",
        "7": "g",
        "8": "h",
        "9": "i",
    }
    ten_swaped = {value: key for key, value in ten_map.items()}

    one_map = {
        "0": "Z",
        "1": "j",
        "2": "k",
        "3": "l",
        "4": "m",
        "5": "n",
        "6": "o",
        "7": "p",
        "8": "q",
        "9": "r",
    }
    one_swaped = {value: key for key, value in one_map.items()}

    def inttotxt(self) -> str:
        ret = self.listed
        ret[0] = self.hundred_map[self.listed[0]]
        ret[1] = self.ten_map[self.listed[1]]
        ret[2] = self.one_map[self.listed[2]]
        self.txt = ''.join(ret)
    
    def fromtxt(self) -> int:
        listed = self.listed
        listed[0] = self.hunded_swaped[self.listed[0]]
        listed[1] = self.ten_swaped[self.listed[1]]
        listed[2] = self.one_swaped[self.listed[2]]

        string = ''.join(listed)
        self.num = int(string) 
        

if __name__ == '__main__':
    my_ascii_converter = Convert(0)
    my_ascii_converter.inttotxt()
    print(my_ascii_converter.txt)