class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 < x < 2**31 - 1:
            a = x
            new = str(a)
            st = ""

            for i in range(len(new) - 1, -1, -1):
                st += new[i]

            if a < 0:
                st = "-" + st
                st = st[0:len(st)-1]

            reversed_x = int(st)

            if -2**31 <= reversed_x <= 2**31 - 1:
                return reversed_x
            else:
                return 0
        else:
            return 0
