class Solution:
        def makeGood(self,s):

            if not s:
                return None

            st = []    

            for i in s:

                if not len(st):
                    st.append(i)
                    
                else:
                    if i.islower():
                        if i.upper()==st[-1]:
                            st.pop()
                        else:
                            st.append(i)    
                    else:
                        if i.lower()==st[-1]:
                            st.pop()
                        else:
                            st.append(i)    

            return "".join(st)                      
