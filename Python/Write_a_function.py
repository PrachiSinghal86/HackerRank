def is_leap(year):
    if year%4==0:
        if year%100==0 and year%400==0:
            return True
        elif year%100!=0:
            return True
        else:
            return False
    else:
        return False
    
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))