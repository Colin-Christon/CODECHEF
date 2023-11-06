class SeatManager:

    def __init__(self, n: int):
        self.li=[]
        self.i=0

    def reserve(self) -> int:
        if self.li==[]:
            self.i+=1
            return self.i
        else:
            self.li.sort()
            a=self.li.pop(0)
            print(a)
            return a
        

    def unreserve(self, seatNumber: int) -> None:
        self.li.append(seatNumber)
        # print(self.li)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
