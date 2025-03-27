#https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735

class Solution:
    def getSecondLargest(self, arr):
        
        arr1 = set(arr)
        arr = [i for i in arr1]
        #Approach 1 - TLE
        
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
        if len(arr)>=2:
            return(arr[-2])
        else:
            return -1
        
        
        #2Approach 
        
        if len(arr)>=2:
            return(sorted(arr)[-2])
        else:
            return -1

        # Approach 3
        a = 0
        b = 0
        if len(arr)>=2:
            for i in range(len(arr)):
                
                if arr[i] > a:
                    b = a
                    a = arr[i]
                elif arr[i] > b:
                    b = arr[i]
        
        else:
            return -1
        return b