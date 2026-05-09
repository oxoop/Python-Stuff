def main(m, n):
    for i in range(m):
        for x in n:
            print(x * (i + 1))
        for y in n:
            print(y * (i + 2))    
main(5, "*")