from collections import Counter

arr= [1,1,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,3,3]

def migratoryBirds(arr):
    # Create a dictionary to store the frequency of each bird type

    
    bird_freq = Counter(arr)
    max_freq = max(bird_freq.values())
    return min(k for k, v in bird_freq.items() if v == max_freq)


    
       
        
            # Write your code here

    
    

print(migratoryBirds(arr))