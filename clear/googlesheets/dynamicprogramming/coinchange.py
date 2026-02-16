# Learning DP. Almost correct

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort(reverse=True)
        # print(coins)
        first_amount = amount
        set_map = defaultdict(int)
        mini = float('inf')
        sum_ = 0
        total_mini = 0
        j = 0
        if amount:
            while sum_ < first_amount:
                for i, a in enumerate(coins):
                    print("amount", amount)
                    tar = abs(amount - a)
                    total_mini = min(tar, mini)
                    mini = total_mini
                    set_map[tar] = i
                sum_ = sum_ + coins[set_map[total_mini]]
                amount = first_amount - sum_
                print(total_mini, "total_mini")
                print(set_map, "map")
                print(sum_, "sum")
                print(amount, "amount")
                print(j, "IIIIIII")
                j += 1
                set_map = defaultdict(int)

        else:
            return 0
        print(sum_, first_amount)
        if sum_ == first_amount:
            return j
        else:
            return -1
