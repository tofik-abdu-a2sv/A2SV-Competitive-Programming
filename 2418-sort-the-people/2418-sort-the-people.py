class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # return sorted(names , key= lambda x: heights.index)
        for i in range(len(heights)):
            for  j in range(len(heights)-1):
                if heights[j] > heights[j+1]:
                    
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
        
        names.reverse()
        return names
        