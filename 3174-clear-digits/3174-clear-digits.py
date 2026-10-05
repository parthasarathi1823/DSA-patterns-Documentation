class Solution:
    def clearDigits(self, s: str) -> str:
        

        if not s:
            return None

        st = []    

        for i in s:

            if not len(st):
                st.append(i)
                
            else:
                
                if i.isdigit():
                    st.pop()
                else:
                    st.append(i)    

        return "".join(st)                      
