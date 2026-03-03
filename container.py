def container(height):
    l=0
    r=len(height)-1
    res=0

    while l<r:
        width=r-l
        area=min(height[l],height[r])*width

        if height[l]<height[r]:
            l+=1
        else:
            r-=1
        res=max(res,area)
    return res

height=[1,2,5,6,3,14,5,8,9,10]
print(container(height))