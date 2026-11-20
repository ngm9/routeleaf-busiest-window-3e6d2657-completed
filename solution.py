def busiest_window(deliveries: list[int], k: int) -> int:
    """Return the largest total number of deliveries over any k consecutive days.

    deliveries is a list of daily delivery counts in date order, and k is the
    window length. Bounds: 1 <= k <= len(deliveries) <= 10^5 and
    0 <= deliveries[i] <= 10^4.
    """
    #print("HI")
    print(deliveries)
    res=0
    n=len(deliveries)
    for i in range(n):
        a=deliveries[i:i+k]
        ans=sum(a)
        res=max(ans,res)
    print("res:",res)
    return res

    
# busiest_window([9, 9, 1, 1, 1], 2)
# busiest_window([4, 2, 7, 1, 8, 3], 6)
# busiest_window([4, 2, 7, 1, 8, 3], 1) 
# busiest_window([0, 0, 0], 3)
# busiest_window([5], 1)
# busiest_window([4, 2, 7, 1, 8, 3], 3)
# busiest_window([4, 2, 7, 1, 8, 3], 2)