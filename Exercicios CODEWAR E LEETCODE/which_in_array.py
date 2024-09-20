def in_array(array1, array2):
    comparison = []
    for i in array1:
        for j in array2:
            if i in j:
                if i in comparison:
                    pass
                else:
                    comparison.append(i)
                    break
    return sorted(comparison)

#return substrings from array2 that in array1