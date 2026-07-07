def revstr(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return revstr(s,left+1,right-1)
s="leve"
print(revstr(s,0,len(s)-1))


