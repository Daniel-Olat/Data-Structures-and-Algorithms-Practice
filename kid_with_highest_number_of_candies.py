
def kid_with_highest_number_ofcandies (candies, extracandies):
    result = []
    for candy in candies:
        if candy + extracandies >= max(candies):
            result.append(True)
        else: 
            result.append(False)
            
    return result