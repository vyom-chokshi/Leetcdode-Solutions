class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.prod = [1] * (4 * self.n)
        self.cnt = [[0] * k for _ in range(4 * self.n)]

        self.nums = nums
        self.build(1, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            self.prod[node] = self.nums[l] % self.k
            self.cnt[node][self.prod[node]] = 1
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.merge(node)

    def merge(self, node):
        left = node * 2
        right = node * 2 + 1

        self.prod[node] = (
            self.prod[left] * self.prod[right]
        ) % self.k

       
        for r in range(self.k):
            self.cnt[node][r] += self.cnt[left][r]

       
        for r in range(self.k):
            new_r = (self.prod[left] * r) % self.k

            self.cnt[node][new_r] += self.cnt[right][r]

    def update(self, node, l, r, index, value):
        if l == r:
            self.prod[node] = value % self.k

            self.cnt[node] = [0] * self.k
            self.cnt[node][self.prod[node]] = 1

            return

        mid = (l + r) // 2

        if index <= mid:
            self.update(node * 2, l, mid, index, value)
        else:
            self.update(node * 2 + 1, mid + 1, r, index, value)

        
        self.cnt[node] = [0] * self.k
        self.merge(node)

    def query(self, node, l, r, ql):
        """
        Returns information for nums[ql ... r]
        """

        if r < ql:
            return None

        if l >= ql:
            return self.prod[node], self.cnt[node][:]

        mid = (l + r) // 2

        if ql > mid:
            return self.query(node * 2 + 1, mid + 1, r, ql)

        left_result = self.query(node * 2, l, mid, ql)
        right_result = self.query(node * 2 + 1, mid + 1, r, ql)

        if right_result is None:
            return left_result

        if left_result is None:
            return right_result

        left_prod, left_cnt = left_result
        right_prod, right_cnt = right_result

        result_cnt = [0] * self.k

        for x in range(self.k):
            result_cnt[x] += left_cnt[x]

        
        for x in range(self.k):
            new_x = (left_prod * x) % self.k
            result_cnt[new_x] += right_cnt[x]

        result_prod = (left_prod * right_prod) % self.k

        return result_prod, result_cnt
class Solution:
    def resultArray(self, nums, k, queries):
        seg = SegmentTree(nums, k)

        ans = []

        for index, value, start, x in queries:

            
            seg.update(
                1, 0, len(nums) - 1,
                index, value
            )

    
            _, cnt = seg.query(
                1, 0, len(nums) - 1,
                start
            )

            ans.append(cnt[x])

        return ans