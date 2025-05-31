def main():
    try:
        x= int(input("Enter the number :"))
        print(x)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am inside finally")


main()

# according to python retun means code ended over there
# but here we are using finally that means that finally will anyhow run
# if we don't make that finally, simply write print statement 
# then after retun nothing will run