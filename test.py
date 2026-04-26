def nextGreaterElement(nums):
    stack = [] # Stores indices or values
    result = [-1] * len(nums)

    for i in range(len(nums)):
        # While stack is not empty and current element is greater than the top
        
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        
        stack.append(i)
    return result

print(nextGreaterElement([1,2,4,3]))