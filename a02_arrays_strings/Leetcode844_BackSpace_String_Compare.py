import itertools
import functools

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        my_list = []
        for x, y in itertools.zip_longest(F(s), F(t)):
            print(x, '-', y)
            my_list.append((x, y))
        print(my_list)
        return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))

    def backspaceCompare2(self,s:str, t:str) -> bool:
        def back(res, c):
            if c!='#':
                res.append(c)
            elif res:
                res.pop()
            return res
        return functools.reduce(back, s, []) == functools.reduce(back, t, [])



if __name__ == '__main__':
    a = 'ab##c'
    b = 'ad#c'

    solution = Solution()
    res = solution.backspaceCompare(a, b)
    print(res)

    res2 = solution.backspaceCompare2(a, b)
    print(res2)
