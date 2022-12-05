a=[1,2,3,4,5,6]
def extract():
    for i in range(len(a)):
        if i%2==0:
            print(a[i])
        else:
            print("no")
