

def mergeSort(list):
    
    if len(list)>1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
       
        i=0
        j=0
        k=0
        length = lefthalf
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1

        if i==length:
                list[k]=lefthalf[i]
                i=i+1
                k=k+1

        else :
                list[k]=righthalf[j]
                j=j+1
                k=k+1
   

list = [4,5,3,2,0]
mergeSort(list)
print(list)
