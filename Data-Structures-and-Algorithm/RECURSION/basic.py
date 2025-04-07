class Basic:
    def __init__(self):

        pass

    def print_names(self,i,n):
        """Time complexity is O(n) bcs n functions and space is o(n) bcs of stack space"""
        if i > n:
            return
        print("Ray")
        self.print_names(i+1,n)

    def print_1_to_n(self,i,n):
        if i > n:
            return 
        print(i)
        self.print_1_to_n(i+1, n)

    def print_n_to_i(self,i,n):
        if i > n:
            return 
        self.print_n_to_i(i+1, n)
        print(i)

    def backtrack_1n(self, i, n):
        if i < 1:
            return 
        self.backtrack_1n(i-1, n)
        print(i)

    def sum_1_to_n(self, add, i, n):
        if i > n:
            print(add)
            return 
        add +=i
        self.sum_1_to_n(add, i+1, n)

    def func_sum_1_to_n(self, add, i, n):
        if n == 0:
            return 0 
        return n + self.func_sum_1_to_n(add, i, n-1)
        



b = Basic()
# b.backtrack_1n(4,4)
print(b.func_sum_1_to_n(0,1,3))