def merge_strings(str1,str2):
    combined_parts = []
    i = 0 #index pointer to iterate through both strings
    
    while i < len(str1) and i < len(str2):
        combined_parts.append(str1[i])
        combined_parts.append(str2[i])
        i += 1
        
        # i is currently at an arbitrary index, which is the index of the last character of the shortest string
        
        combined_parts.append(str1[i:]) # append the remaining characters of str1
        combined_parts.append(str2[i:]) # append the remaining characters of str2
        #for the shortest string , the above slices an empty string
        
        return "".join(combined_parts)