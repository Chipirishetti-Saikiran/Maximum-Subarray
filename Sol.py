def max1(arr):
    final_max=0 
    initial_max=0 
    for i in arr:
        initial_max=initial_max+int(i)
        initial_max=max(initial_max,0)
        final_max=max(final_max,initial_max)
    return final_max 
    
arr=[-2,1,-3,4,-1,2,1,-5,4]
print(max1(arr))
