class Calculate_MEX:
    def __init__(self,list):
        self.list=list

    def calculate_value(self) -> list:
        self.list=list(sorted(set(self.list)))
        if len(self.list)==0:
            return 0
        for i in range(0,len(self.list)):
            if self.list[i]==i:
                continue
            else:
                return i
        else:
            return self.list[-1]+1


