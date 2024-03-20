#TIME COMPLEXITY - O(nlogn)
#SPACE COMPLEXITY - O(N)
class Solution:
    def countSmaller(self, nums):
        n=len(nums)
        self.count=[0 for i in range(n)]
        temp=[0 for i in range(n)]
        idx_arr=[i for i in range(n)]
        self.divide(0,nums,temp,idx_arr,n-1)
        return self.count
    def divide(self,low,nums,temp,idx_arr,high):
        if low<high:
            mid=(low+high)//2
            self.divide(low,nums,temp,idx_arr,mid)
            self.divide(mid+1,nums,temp,idx_arr,high)
            self.merge(low,mid,high,nums,idx_arr,temp)
        return
    def merge(self,low,mid,high,nums,idx_arr,temp):
        i,j,k=low,mid+1,low
        while i<=mid and j<=high:
            if nums[idx_arr[i]]<=nums[idx_arr[j]]:
                self.count[idx_arr[i]]+=j-mid-1
                temp[k]=idx_arr[i]
                k,i=k+1,i+1
            else:
                temp[k]=idx_arr[j]
                k,j=k+1,j+1
        while i<=mid:
            temp[k]=idx_arr[i]
            self.count[idx_arr[i]]+=j-mid-1
            k,i=k+1,i+1
        while j<=high:
            temp[k]=idx_arr[j]
            k,j=k+1,j+1
        for t in range(low,high+1):
            idx_arr[t]=temp[t]
        return 