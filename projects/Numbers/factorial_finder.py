
def recursive(n):
    if n == 1:
        return n
    else:
        return n*recursive(n-1)

def loop(n):
    if n == 0 or n == 1:
        return n
    else:
        i = n - 1
        while i > 1:
            n = n * i
            i -= 1
            
        return n

def main():
    n = int(input())
    print(loop(n))

if __name__ == "__main__":
    main()