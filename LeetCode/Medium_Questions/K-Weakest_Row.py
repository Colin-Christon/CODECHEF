import copy

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        li = [0] * len(mat)
        for x in range(len(mat)):
            for y in range(len(mat[x])):
                if mat[x][y] == 1:
                    li[x] += 1
                else:
                    break
        newli = copy.copy(li)
        li.sort()
        result = []
        indices = set() 
        for x in range(k):
            weakest_row = li[x]
            ind = newli.index(weakest_row)
            while ind in indices:
                ind = newli.index(weakest_row, ind + 1)
            indices.add(ind)
            result.append(ind)
        print(indices)
        return result
