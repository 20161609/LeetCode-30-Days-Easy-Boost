"""
Problem: Binary Watch
Link: https://leetcode.com/problems/binary-watch/
Topic: Backtracking/Enumeration
Difficulty: Easy

Note: Replace this file with your accepted solution.
"""
from collections import defaultdict

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:        
        def backtrack(i, cnt, _sum, _list, box, max_value):
            if _sum > max_value:
                return
            if i == len(_list) or cnt == turnedOn:
                box[cnt].add(_sum)
                return
            backtrack(i+1, cnt, _sum, _list, box, max_value)
            backtrack(i+1, cnt+1, _sum+_list[i], _list, box, max_value)

        H, M = [1,2,4,8], [1,2,4,8,16,32]
        h_box, m_box = defaultdict(set), defaultdict(set)
        backtrack(0, 0, 0, H, h_box, 11), backtrack(0, 0, 0, M, m_box, 59)

        answer = []
        for i in range(turnedOn+1):
            j = turnedOn - i
            for h in h_box[i]:
                for m in m_box[j]:
                    answer.append(f"{h}:"+f"{100+m}"[1::])
        return answer