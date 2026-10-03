from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        st.append('_')
        for s_c in s:
            if st[-1] + s_c in ['[]', '()','{}']:
                st.pop()
            else:
                st.append(s_c)
        
        return True if st[-1] == '_' else False


        