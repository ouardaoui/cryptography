ct = b"abcdefghvxyz"
chunks = (ct[:3], ct[3:3*2] , ct[3*2: 3*3] , ct[3*3: 3*4])


def combinations_two(chunks) : 
    output = []
    for i in range(len(chunks)) : 
        for j  in range(i+ 1, len(chunks)) :
            k = (chunks[i], chunks[j])
            output.append(k) 
    return output

com = combinations_two(chunks)
print(com)