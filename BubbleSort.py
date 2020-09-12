numbers = [1,4,5,3,6,2,100,23,34,563,24] #Numbers to sort.
length = len(numbers) # Calculates length of list.
indexCount  = length - 1 #Takes length and converts to index count form for indexing.
for x in range(0, indexCount): #first loop / main loop
    for i in range(0, indexCount): #worker loop
        if i+1 == indexCount: 
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                break
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp 

print(numbers) #prints bubble sorted list
