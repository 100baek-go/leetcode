class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        result = ""
        for i in range(7,-1,-1):
            four_bit_hex_value = (num >> i*4) & 0xf
            if four_bit_hex_value == 0 and not result:
                continue
            if four_bit_hex_value >= 10:
                result += chr(ord('a') + four_bit_hex_value - 10)
            else:
                result += str(four_bit_hex_value)
        return result