"""Run Length Encoding"""
def main():
    """Run Length Encoding"""
    text = input()
    ans = text[0]
    var = ''
    newtext = ''
    while text != '':
        for i in text:
            word = i
            if word != ans:
                break
            var += i
            ans = word
        many = var.count(ans)
        rans = str(many) + str(ans)
        text = text.replace(var, '', 1)
        var = ''
        if text != '':
            ans = text[0]
        newtext += rans
    print(newtext)
main()
