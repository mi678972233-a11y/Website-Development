numberLargest = int(input("Enter Largest Number :"))
numberSmallest = int(input("Enter Smallest Number :"))
while(numberSmallest):
    numberStore = numberSmallest
    numberLargest = numberStore
    numberSmallest = numberLargest % numberSmallest
    print("HCF is : ",numberLargest)