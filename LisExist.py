    def lengthOfLastWord(self, s) -> int:
         
        
        str_list = s.split(' ')
        
        # if the last element in the list is '' we should remove it beacuse it's not word 
        while str_list:
            if str_list[-1] == '':
                str_list = str_list[0:-1]
            else:
                break
        
        # when given a empty list 
        if not len(str_list):
            return 0
        
        print(str_list)
        return len(str_list[-1])



        # 判断list是否存在
        # 1. len(list) == 0  2.not list  3. not len(list)