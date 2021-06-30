    def t2Sum(self,B):

        ans = [0]
        h={}

        def in_order(A, B):
            if A == None:
                return

            in_order(A.left, B)

            if A.data in h:
                ans[0] += 1
            else:
                h[B - A.data] = A.data

            in_order(A.right, B)

            return

        in_order(self, B)
        return ans[0]
