"""CompositeFunction"""
def main():
    """CompositeFunction"""
    var_x = int(input())
    def funf(var_x):
        """functionf"""
        funf = var_x*2
        return funf
    def fung(var_x):
        """functiong"""
        fung = (var_x/2) + 1
        return fung
    ans1 = funf(fung(var_x))
    ans2 = fung(funf(var_x))
    print("%.2f"%ans1)
    print("%.2f"%ans2)
main()
