"""TheFunctionWithin"""
def main():
    """https://www.youtube.com/watch?v=0iww5vMh4J8"""
    var_a = float(input())
    var_b = float(input())
    var_c = float(input())
    var_d = float(input())
    def funf(var_a):
        """funf"""
        funf = 2*var_a
        return funf
    def fung(var_a):
        """fung"""
        fung = (3*(var_a**4))-(var_a**3)+(2*(var_a**2))+10
        return fung
    def funh(var_x, var_y, var_z):
        """Funh"""
        funh = (var_z+var_x)**2 - var_x*var_y + var_y**2
        return funh
    def funi(var_a, var_b, var_c, var_d):
        """funi"""
        funi = ((var_a**2)+(var_b**2)-(var_c**2))/((var_d**2)-(2*var_a*var_d)+(2*var_a))
        return funi
    ans1 = funf(funf(var_a))
    ans2 = fung(funf(var_a - var_b))
    ans3 = funh(funf(var_a+var_b), funf(var_a+var_c), fung(funf(var_d**2)))
    ans4 = funi(funh(funf(var_a+var_b), funf(var_a-var_c), fung(funf(var_d**2))), \
fung(funf(var_a-var_b)), funf(funf(funf(funf(funf(var_c))))), var_d**8)
    print(ans1)
    print(ans2)
    print(ans3)
    print(ans4)
main()
