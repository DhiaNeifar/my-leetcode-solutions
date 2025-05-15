class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        if num == 100:
            return 'One Hundred'
        if num == 1000:
            return 'One Thousand'
        if num == 1000000:
            return 'One Million'
        if num == 1000000000:
            return 'One Billion'
        d = {
            "0": "",
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
        }

        d1 = {
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen",
        }

        d2 = {
            "0": "",
            "1": "Ten",
            "2": "Twenty",
            "3": "Thirty",
            "4": "Forty",
            "5": "Fifty",
            "6": "Sixty",
            "7": "Seventy",
            "8": "Eighty",
            "9": "Ninety",
        }

        d3 = {
            0: "",
            1: "Thousand",
            2: "Million",
            3: "Billion",
        }

        string = str(num)[::-1]

        length = len(string)
        if length % 3:
            x = length // 3
        else:
            x = length // 3 - 1

        l = []
        i = 0

        while i < x:
            
            sub_string = string[3 * i: 3 * i + 3]
            if sub_string != '000':
                l.append(d3[i])
            if sub_string[1] == "1":
                l.append(d1[sub_string[1:: -1]])
            else:
                l.append(d[sub_string[0]])
                l.append(d2[sub_string[1]])
            if sub_string[2] != '0':
                l.append("Hundred")
                l.append(d[sub_string[2]])

            i += 1

        l.append(d3[i])
        last = length - 3 * i
        sub_string = string[3 * i: 3 * i + 3]
        if last == 1:
            l.append(d[sub_string[0]])
            return " ".join([x for x in l[::-1] if x])
        else:
            if sub_string[1] == "1" and sub_string[0] != "0":
                l.append(d1[sub_string[1:: -1]])
            else:
                l.append(d[sub_string[0]])
                l.append(d2[sub_string[1]])
            if last == 3:
                l.append("Hundred")
                l.append(d[sub_string[2]])
            return " ".join([x for x in l[::-1] if x])