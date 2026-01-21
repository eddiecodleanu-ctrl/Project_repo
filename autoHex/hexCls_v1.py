class Autohex:
    def __init__(self,

            hexa:str=False,
            binary:str=False,
            denary:str=False,

        ):

        """
        Subclass made for the sole purpose of automatic conversion between hexadecimal, binary and denery interchangeably

        :param hexa: hexadecimal, str val, base 16 language
        :param binary: binary, str val, base 2 language
        :param denary:  denery, str val, base 10 language
        """

        self.hexa = hexa
        self.binary = binary
        self.denary = denary

        self.hex_dict = {
            "0000":"0",
            "0001":"1",
            "0010":"2",
            "0011":"3",
            "0100":"4",
            "0101":"5",
            "0110":"6",
            "0111":"7",
            "1000":"8",
            "1001":"9",
            "1010":"A",
            "1011":"B",
            "1100":"C",
            "1101":"D",
            "1110":"E",
            "1111":"F",
        }

    def auto_nibble(self):
        den = int(self.denary)
        counter = 1

        while den >= 2 ** (4 * counter):
            counter += 1

        return counter

    #==========================#
    #          DENARY          #
    #==========================#

    def den_to_bin(self, manual:int=None):
        den = int(self.denary) if manual is None else manual

        if den <= 0:
            return "0"

        nibble = self.auto_nibble()
        total_bits = 4 * nibble

        current_bit_val = 2 ** (total_bits - 1)
        bin_str = ""

        for _ in range(total_bits):
            if den >= current_bit_val:
                bin_str += "1"
                den -= current_bit_val
            else:
                bin_str += "0"

            current_bit_val //= 2


        return bin_str

    def den_to_hex(self):
        bin_str = self.den_to_bin()

        nibble_num = len(bin_str) // 4
        hex_str = ""

        hex_map = self.hex_dict

        for i in range(nibble_num):
            nibble = bin_str[i * 4:(i * 4) + 4]
            hex_str += hex_map[nibble]

        return hex_str

    # ==========================#
    #           BINARY          #
    # ==========================#

    def bin_to_den(self, manual:str=None):
        bin_str = self.binary if manual is None else manual

        current_n = 0

        current_bit_val = 1
        for i in range(0, len(bin_str)):
            current_bit_val *= 2

        for i in bin_str:
            if i == "1":
                current_n += current_bit_val
                current_bit_val /= 2
            elif i == "0":
                current_bit_val /= 2

        return current_n // 2

    def bin_to_hex(self):
        bin_str = self.binary
        hex_str = ""

        hex_map = self.hex_dict

        nibble_num = len(bin_str) // 4

        for i in range(nibble_num):
            nibble = bin_str[i * 4:(i * 4) + 4]
            hex_str += hex_map[nibble]

        return hex_str

    # ==========================#
    #           HEX             #
    # ==========================#

    def hex_to_bin(self):
        hex_str = self.hexa.upper()
        bin_str = ""

        # reverse the map: hex -> binary
        rev_map = {v: k for k, v in self.hex_dict.items()}

        for char in hex_str:
            if char not in rev_map:
                raise ValueError(f"Invalid hex digit: {char}")
            bin_str += rev_map[char]

        return bin_str

    def hex_to_den(self):
        bin_str = self.hex_to_bin()
        den_str = self.bin_to_den(bin_str)

        return den_str






# ONLY FILL ONE SPACE

denary = "" # INPUT DENARY HERE

binary = "" # INPUT BINARY HERE

hexa = "" # INPUT HEXADECIMAL HERE


hex_cls = Autohex(denary=denary, binary=binary, hexa=hexa)

if denary:
    bina = hex_cls.den_to_bin()
    hexdecimal = hex_cls.den_to_hex()

    print(f"\nDENARY: {denary}")
    print(f"BINARY: {bina}")
    print(f"HEX: {hexdecimal}")

elif binary:
    den = hex_cls.bin_to_den()
    hexdecimal = hex_cls.bin_to_hex()
    print(f"\nBINARY: {binary}")
    print(f"DENARY: {den:.0f}")
    print(f"HEX: {hexdecimal}")

elif hexa:
    bina = hex_cls.hex_to_bin()
    den = hex_cls.hex_to_den()
    print(f"\nHEX: {hexa}")
    print(f"BINARY: {bina}")
    print(f"DENARY: {den:.0f}")



