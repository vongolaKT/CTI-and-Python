# function that prints a letter grade based on a grade input
# 11/30/2020
# CTI-110 P3HW1 - Debugging
# Kevin Griffin

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # doesn't check if a number is above 100, which while impossible for school can be input in error
    # Will still return an A though
    
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    
    elif score >= B_score and score < A_score:
        print('Your grade is: B')
    elif score >= C_score and score < B_score:
        print('Your grade is: C')
    elif score >= D_score and score < C_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')







# program start
main()
