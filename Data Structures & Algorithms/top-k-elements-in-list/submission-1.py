class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #We are solving this using a dictionary
        counter = {}
        for i in nums:
            if i not in  counter:
                counter[i] = 1
            else:
                counter[i] += 1
        

     #Get the maximum value in the dictionary
        sorted_keys = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)

        return sorted_keys[:k]