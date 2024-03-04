import re
def print_matches(text,pattern):
        text=text.replace('\n',' ')
        try:
            pattern=re.compile(pattern)
            matches=pattern.finditer(text)
            groups=pattern.groups
            ans=[]
            for i,match in enumerate(matches):
                flag=1
                for j in range(groups+1):
                    if j==0:
                        ans.append('Match {} {}-{} {}'.format(i+1,match.span()[0],match.span()[1], match.group(j)))
                    elif match.group(j)!=None:
                        if flag==1: 
                            si=match.span()[0]
                            flag=0
                        ei=len(match.group(j))+si
                        ans.append('Group {} {}-{} {}'.format(j,si,ei, match.group(j)))
                        si=ei
            return True,ans
        except re.error as e:
            return False,ans

def validate_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Using re.match() to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False