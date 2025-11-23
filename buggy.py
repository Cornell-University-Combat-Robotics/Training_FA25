def calculate_odd_average(numbers):
    """ Returns the average of the odd numbers in [numbers] """
    total = 0
    total_odd = 0
    for i in range(len(numbers)-1): 
        if (numbers[i] % 2 == 0):   
            total += numbers[i]
        total_odd+=1                
        total += numbers[i]
    avg = total / len(numbers)      
    return avg

