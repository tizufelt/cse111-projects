def main():
    colors = ['red', 'yellow', 'blue', 'yellow', 'green']
    colors.append("brown")
    colors.insert(6, 'gray')
    length = len(colors)
    print(f"number of elements: {length}")
    print(colors[2])
    colors[3] = 'purple'

    print(colors)
    
if __name__ == "__main__":
    main()








