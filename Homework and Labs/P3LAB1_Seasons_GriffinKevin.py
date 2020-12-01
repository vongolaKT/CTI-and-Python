def main():
    input_month = input()
    input_day = int(input())
    
    
    if input_month.lower() == 'january':
        print('Winter')
    elif input_day > 31:
        print ('Invalid')
    elif input_day < 1:
        print('Invalid')
    elif input_month.lower() == 'february' and input_day <= 28:
        print('Winter')
    elif input_month.lower() == 'february' and input_day > 28:
        print('Invalid')
    elif input_month.lower() == 'march' and input_day <= 19:
        print('Winter')
    elif input_month.lower() == 'march' and input_day >= 20:
        print('Spring')
    elif input_month.lower() == 'april' and input_day > 30:
        print('Invalid')
    elif input_month.lower() == 'april':
        print('Spring')
    elif input_month.lower() == 'may':
        print('Spring')
    elif input_month.lower() == 'june' and input_day <= 20:
        print('Spring')
    elif input_month.lower() == 'june' and input_day > 30:
        print('Invalid')
    elif input_month.lower() == 'june' and input_day > 20:
        print('Summer')
    elif input_month.lower() == 'july':
        print('Summer')
    elif input_month.lower() == 'august':
        print('Summer')
    elif input_month.lower() == 'september' and input_day <= 21:
        print('Summer')
    elif input_month.lower() == 'september' and input_day > 30:
        print('Invalid')
    elif input_month.lower() == 'september' and input_day > 21:
        print('Autumn')
    elif input_month.lower() == 'october':
        print('Autumn')
    elif input_month.lower() == 'november' and input_day > 30:
        print('Invalid')
    elif input_month.lower() == 'november':
        print('Autumn')
    elif input_month.lower() == 'december' and input_day <= 21:
        print('Autumn')
    elif input_month.lower() == 'december' and input_day > 21:
        print('Winter')
    else:
        print('Invalid')


main()