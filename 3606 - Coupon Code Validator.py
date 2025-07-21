from collections import defaultdict

class Solution:
    def validateCoupons(self, codes: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        our_dict = defaultdict(list)
        electronics, grocery, pharmacy, restaurant = [], [], [], []
        for index, code in enumerate(codes):
            if code != "" and check_code(code) and isActive[index]:
                our_dict[businessLine[index]].append(code)

        for businessline in our_dict:
            our_dict[businessline].sort()

        return our_dict["electronics"] + our_dict["grocery"] + our_dict["pharmacy"] + our_dict["restaurant"]


def check_code(code):
    alphanumerics = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    for char in code:
        if char not in alphanumerics:
            return False
    return True