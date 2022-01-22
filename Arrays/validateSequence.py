'''
arr=[1,5,6,9,11,14,8,2]
subsq = [1,5,11,14]
'''

def validateSeq(arr,seq):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(arr) and seqIdx<len(seq):
        if arr[arrIdx] == seq[seqIdx]:
            seqIdx+=1
        arrIdx+=1
    return seqIdx== len(seq)

a1= int(input)
s1= int(input)
print("is a valid subsequenc: ", validateSeq(a1,s1))
        