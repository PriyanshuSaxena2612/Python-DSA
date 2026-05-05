class Solution:
    def intersectSize(self,a, b):
        # code here
        # first method
        i,j=0,0
        n1,n2=len(a),len(b)
        a.sort()
        b.sort()
        res=[]
        while i<n1 and j<n2:
            if a[i]==b[j]:
                if not res or res[-1]!=a[i]:
                    res.append(a[i])
                i+=1
                j+=1
            elif a[i]<b[j]:
                i+=1
            else: 
                j+=1
        return len(res)
        # second method
        return len(list(set(a)&set(b)))
        # third method
        og_set = set(a)
        seen = set()
        for num in b:
            if num not in seen and num in og_set:
                seen.add(num)
            else:
                continue
        return list(seen)
