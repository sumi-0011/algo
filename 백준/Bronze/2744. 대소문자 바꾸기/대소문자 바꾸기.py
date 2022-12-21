import sys

 
if __name__ == "__main__":

    s = sys.stdin.readline()
    arr = list(s)
    res = ''
    for x in arr:
        if x.isupper():
            res += x.lower()
        else:
            res += x.upper()
    print(res)
