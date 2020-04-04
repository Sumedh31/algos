def countCountries(ans,n):
    i=0
    total_countries=0
    while(i<n):
        current=ans[i]
        num=ans[i]
        while(num>0):
            if(ans[i]!=current):
                print("invalid answer")
                return
            else:
                num=num-1
            i=i+1
        total_countries=total_countries+1
    print("There are {} total conutries".format(total_countries))
    

ans = [ 1, 1, 2, 2, 4, 4, 4, 4 ]
n = len(ans)
countCountries(ans, n)