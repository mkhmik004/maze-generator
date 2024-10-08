import random
outerlist =[]
walls = ['#', 'o']

def first_row(n):
    inner_list = []
    for row in range (n):
        x = random.choice(walls)
        inner_list.append (x)
    return inner_list

def maze(n,outer):
    locationlist = []
    counter = 0
    top_list = outer[-1]
    for location in top_list:
        if location == "o":
            locationlist.append (counter)
            counter += 1
        else:
            counter += 1 
            continue
    inner_list = []
    index = 0 
    for i in range (n-1):
        if index in locationlist:
            position = random.choice([index -1, index, index+ 1])
            while 0 <= position <= n-1:
                 position = random.choice([index -1, index, index+ 1])
            inner_list[position] = "o"
            index+=1
        else:
            inner_list.append ('#')
            index+=1
    print(inner_list)
    outerlist.append(inner_list)
    
def main():
    size = input ("Enter length of maze: ")
    outerlist.append(first_row(int(size)))
    print (outerlist)
    maze(int(size),outerlist)
    print(outerlist)

if  __name__ == '__main__':
  main()