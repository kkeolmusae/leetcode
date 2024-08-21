# 풀이
- LeetCode 75, Easy
- Array / String
- Time: ?
- 두 문자 길이의 최대공약수(gcd)를 구한 다음에 그 숫자만큼 잘라주면 됨. 대신 str1 이랑 str2랑 뒤집에서 붙여봤을때 같아야함. 

## 내 풀이​
```py
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_num = gcd(len(str1), len(str2))
        return str1[:gcd_num]
```