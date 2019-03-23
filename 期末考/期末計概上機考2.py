import numpy as np

arrayA = np.random.rand(7,5)

print(arrayA)
print(np.shape(arrayA))
print(np.ndim(arrayA))

arrayB= arrayA.reshape(35)
print(arrayB)
print(np.shape(arrayB))
print(np.ndim(arrayB))

np.random.shuffle(arrayB)
print(arrayB)
print(np.max(arrayB))
print(np.min(arrayB))
print(np.sum(arrayB))
print(np.average(arrayB))

listA = [0,0,0,0]
listA[0] = np.max(arrayB)
listA[1] = np.min(arrayB)
listA[2] = np.sum(arrayB)
listA[3] = np.average(arrayB)

np.random.shuffle(arrayB)
arrayB.shape=(7,5)

listB = [0,0,0,0]
listB[0] = np.max(arrayB)
listB[1] = np.min(arrayB)
listB[2] = np.sum(arrayB)
listB[3] = np.average(arrayB)

listC = [0,0,0,0]
for i in range(len(listA)):
    listC[i] = listA[i] + listB[i]
    
print(sum(listC)/4)




