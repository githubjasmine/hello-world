# LeetCode 66 - Plus One: https://leetcode.com/problems/plus-one/
"""
Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that the most
significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits)-1

        # initialize the result
        res = []

        # carry to contain mid-result &| sum greater than 10
        carry

        while i >= 0:
            carry += digits[i]
            i -= 1
            # add till the and of the digits
            # not only adding for the last digits: 9999

            res.append(carry%10)
            carry = carry//10

        # 9999: after the above code, res = [0,0,0,0], carry = 1,
        # should put 1 to the start of the digits
        if carry > 0:
            res.append(1)

        return res[::-1]


# LeetCode 67 - Add Binary: https://leetcode.com/problems/add-binary/

"""
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i,j = len(a)-1, len(b)-1

        res = ""
        carry = 0

        while i >= 0 or j >= 0:
            # use or, since we want to loop till the end of both str
            # if and, would stop when the shorter reaches its append

            if i >= 0:
                carry += int(a[i])
                i -=1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            res += str(carry%2)
            carry = carry//2

        if carry > 0:
            res += str(carry)

        return res[::-1]


# LeetCode 415 - Add Strings: https://leetcode.com/problems/add-strings/
"""
Given two non-negative integers num1 and num2 represented as string,
return the sum of num1 and num2.
"""
def addStrings(num1, num2):

    i,j = len(num1)-1, len(nums2)-1

    res = ""
    carry = 0

    while i >= 0 or j >= 0:
        # use or, since we want to loop till the end of both str
        # if and, would stop when the shorter reaches its append

        if i >= 0:
            carry += int(num1[i])
            i -=1
        if j >= 0:
            carry += int(num2[j])
            j -= 1

        res += str(carry%2)
        carry = carry//2

    if carry > 0:
        res += str(carry)

    return res[::-1]

# LeetCode 989 - Add to Array-Form of Integer:
# https://leetcode.com/problems/add-to-array-form-of-integer/
"""
For a non-negative integer X,
the array-form of X is an array of its digits in left to right order.
For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X,
return the array-form of the integer X+K.

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
"""

def addToArrayForm(A: List[int], K: int):

    i = len(A) - 1

    res = []
    carry = 0

    while i >= 0 or K > 0:
        # K>0 instead of >=0: else the while loop never ends

        if i >= 0:
            carry += A[i]
            i -= 1
        if K > 0:
            carry += K%10
            K = K//10

        res.append(carry%10)
        carry = carry//10

    if carry > 0:
        res.append(1)

    return res[::-1]
