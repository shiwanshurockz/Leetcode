class Solution:
    def isNumber(self, s: str) -> bool:
        #+-
        # 8.9e 9.e .6E-57
        # 67824e789432
        # ^ - Start of string
        # $ - end of string
        # ? - 0 or 1
        # + - 1 or more
        # * - 0 or more
        exp = "^[+-]?(((\\d+\\.\\d*)|(\\.\\d+))|\\d+)([eE][+-]?\\d+)?$"
        if re.search(exp,s):
            return True
        return False        
