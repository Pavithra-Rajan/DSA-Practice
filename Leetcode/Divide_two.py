lass Solution:
    def divide(self, dividend: int, divisor: int) -> int:
  
        flag=0
        if dividend<0:
            flag=1
            dividend*=(-1)
        if divisor<0:
            if flag==1:
                flag=0
            else:
                flag=1
            divisor*=(-1)
            
        count=0 
        
        while dividend>=divisor:
            temp=divisor
            i=1
            while dividend>=temp:
                dividend-=temp
                temp<<=4
                count+=i
                i<<=4
        if flag==1:
            count*=(-1)
        
        if count>pow(2,31)-1:
            return pow(2,31)-1
        
        return count
        
      
          
            