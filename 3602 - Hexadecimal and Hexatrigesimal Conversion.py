class Solution:
    def concatHex36(self, n: int) -> str:
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n_2 = n * n
        n_3 = n_2 * n
        
        result_2 = []
        while n_2 > 0:
            div, mod = divmod(n_2, 16)
            result_2.append(alphabet[mod])
            n_2 = div
        result_2 = result_2[::-1]

        result_3 = []
        while n_3 > 0:
            div, mod = divmod(n_3, 36)
            result_3.append(alphabet[mod])
            n_3 = div

        result_3 = result_3[::-1]

        result = result_2 + result_3
        
        return "".join(result)