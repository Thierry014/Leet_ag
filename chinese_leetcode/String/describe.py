class Solution:
    def desc(self,n):
        s = '1'
        for i in range(n-1):
        # keep update s 
            s = self.res(s)
        print(s)
        return s

    def res(self,string):
        res = ''
        # avoid index out of range
        string += '#'
        # '1121'
        # length of the same num
        count = 1

        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                count += 1
            else:
                res += str(count) + string[i]
                count = 1
        return res


a = Solution()
a.desc(5)