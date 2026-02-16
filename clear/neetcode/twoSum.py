class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = []
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t in numbers and t != numbers[i]:
                f.append(i + 1)
        return f

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = defaultdict(int)  # Stores and the value and the index of it, {value: index}
        for i in range(len(numbers)):
            t = target - numbers[i]
            if f[t]:
                return [f[t], i + 1]
            f[numbers[i]] = i + 1
            print(f)
        return f
