class Solution:
    def print_n_times(self, name, count, N):
        if count == N:
            return
        print(name, end=" ")
        self.print_n_times(name, count+1, N)

if __name__ == "__main__":
    sol = Solution()
    sol.print_n_times("ABC", 0, 5)
