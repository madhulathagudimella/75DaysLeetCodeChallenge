from bisect import bisect_left, insort

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.seg = [0] * (4 * n)

    def update(self, idx, val, node, l, r):
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(idx, val, node * 2, l, mid)
        else:
            self.update(idx, val, node * 2 + 1, mid + 1, r)

        self.seg[node] = max(self.seg[node * 2], self.seg[node * 2 + 1])

    def query(self, ql, qr, node, l, r):
        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2

        return max(
            self.query(ql, qr, node * 2, l, mid),
            self.query(ql, qr, node * 2 + 1, mid + 1, r)
        )


class Solution:
    def getResults(self, queries):
        MAXX = 50000

        st = SegmentTree(MAXX + 1)

        obs = [0]

        ans = []

        for q in queries:

            if q[0] == 1:
                x = q[1]

                i = bisect_left(obs, x)

                prev = obs[i - 1]

                nxt = MAXX if i == len(obs) else obs[i]

                st.update(x, x - prev, 1, 0, MAXX)

                if nxt != MAXX:
                    st.update(nxt, nxt - x, 1, 0, MAXX)

                insort(obs, x)

            else:
                x, sz = q[1], q[2]

                i = bisect_left(obs, x + 1)

                prev = obs[i - 1]

                best = st.query(0, x, 1, 0, MAXX)

                ans.append(max(best, x - prev) >= sz)

        return ans