import random
import string

all = (
    string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
)


def newgen():
    plen = int(input("Enter the length: "))
    password = "".join(random.sample(all, plen))
    print(password)
    x = input("Do you want to continue? : ")
    if x == "y":
        newgen()
    else:
        exit()


newgen()
