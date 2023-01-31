

def main():
    locations = list_locations("provinces.txt")
    print(locations)
    locations.pop(0)
    locations.pop()
    
    for x in range(len(locations)):
        if locations[x] =="AB":
            locations[x] == "Alberta"
            
    count = locations.count("Alberta")
    
    print(f"Alberta occurs {count} times in the modified list. ")
    
    
    
    
def list_locations(file):
    list = []
    
    with open(file, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            list.append(clean_line)    
    
    return list




if __name__ == "__main__":
    main()
        