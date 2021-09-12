"""Rectangle"""

def main():
    """Rectangle"""
    high = int(input())
    wide = int(input())
    def area(wide, high):
        """หาพื้นที่"""
        area = wide*high
        return area
    def perimeter(wide, high):
        """หาเส้รรอบรูป"""
        perimeter = (wide*2)+(high*2)
        return perimeter
    area = area(wide, high)
    perimeter = perimeter(wide, high)
    print(area)
    print(perimeter)
main()
