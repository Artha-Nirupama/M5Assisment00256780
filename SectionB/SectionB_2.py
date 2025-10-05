def main():
    x=1
    while x <= 20:
        if x % 5 == 0:
            x+=1
            continue
        if x > 15:
            break
        print(x)
        x+=1
    
if __name__ == "__main__":
    main()