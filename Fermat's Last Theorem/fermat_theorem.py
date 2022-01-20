# The function checks if fermat's last theorem holds true according to the given input parameters
def verify_fermat(a, b, c, n):
    if n > 2 and (pow(a,n) + pow(b, n) == pow(c, n)):
        print("Fermat's last theorem is debunked!")
    else:
        print("Fermat's last theorem is verified")

verify_fermat(5, 3, 7, 1)
