class Solution(object):
 
    def rev(self, num1):
        rev = 0
       
        while (num1 > 0):
            rev = rev*10 + num1%10
            num1 = num1 // 10
       
        return rev

    def minMirrorPairDistance(self, nums):

        d = defaultdict(int)
        ret = -1

        for i in range( len(nums)-1, -1, -1):
            no = self.rev(nums[i])
            # print(no , d)
            if no in d:
                if (ret == -1 or ret > d[no] - i ):
                    ret = d[no] - i 
                    if ret == 1:
                        return 1

            d[nums[i]] = i
    
        return ret
        