def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    fruit_list.reverse()
    print("reversed: ", fruit_list)
    
    print()
    fruit_list.append("orange")
    print("append orange:", fruit_list)
    
    print()
    fruit_list.insert(1, "cherry")
    print("add cherry at index 2: ", fruit_list)
    
    print()
    fruit_list.remove("banana")
    print("remove banana :", fruit_list)
    
    print()
    fruit_list.pop()
    print("removed last item.pop:", fruit_list)
    
    print()
    fruit_list.sort()
    print("sorted list:", fruit_list)
    
    print()
    fruit_list.clear()
    print("cleared list:", fruit_list)
    

# Call main to start this program.
if __name__ == "__main__":
    main()
