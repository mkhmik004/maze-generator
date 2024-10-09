import random

outerlist = []
walls = ['#', 'o']

def first_row(n):
    inner_list = []
    for row in range(n):
        x = random.choice(walls)
        inner_list.append(x)
    return inner_list

def maze(n, outer):
    locationlist = []
    counter = 0
    top_list = outer[-1]
    # Find the positions of "o" in the previous row
    for location in top_list:
        if location == "o":
            locationlist.append(counter)
        counter += 1
    
    inner_list = ['#'] * n 
    
    for index in locationlist:
        # Choose position for "o" to create path
        position = random.choice([index - 1, index, index + 1])
        # Ensure position is within bounds
        position = max(0, min(position, n - 1))
        inner_list[position] = "o"  # Place the path "o"
    
    outerlist.append(inner_list)

def main():
    size = int(input("Enter length of maze: "))  # Convert input to int
    outerlist.append(first_row(size))
    for _ in range(size - 1):
        maze(size, outerlist)
        
    print(outerlist)

if __name__ == '__main__':
    main()
