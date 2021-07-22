class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ret=[]
        dic={}
        not_arr=[]
        for i in arr1:
            if i not in arr2:
                not_arr.append(i)
            else:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
        for i in arr2:
            ret+=[i]*dic[i]
        return ret+sorted(not_arr)