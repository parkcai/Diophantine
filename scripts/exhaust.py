def main():
    
    a = int(input()); b = int(input()); c = int(input())
    solutions = []
    
    A = a; x = 1; C = c; y = 1
    
    search_threshold = int(f"1{'0'*100}")
    
    while A < search_threshold or C < search_threshold:
        
        if A + b == C:
            solutions.append((x, y))
            A *= a; x += 1
            
        elif A + b > C:
            C *= c; y += 1
            
        else:
            A *= a; x += 1
    
    print(solutions)


if __name__ == "__main__":
    
    main()