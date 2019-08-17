'''
'''
import sys

LIST_OF_NUMBERS = [10, 15, 3, 7, 14]
SUMMATION = 17
EXHAUSTIVE_SEARCH = True

def main(list_to_test, sum_value, complete_search):
    '''
    list_to_test is a list of integers
    sum_value is an integers

    return 0 if any 2 elements in the list sum to sum_value
    '''
    result = 1
    print("Testing for instances of {} as the sum of any two elements in {}.".format(
        sum_value,
        list_to_test))
    for first_index, first_value in enumerate(list_to_test):
        for second_index, second_value in enumerate(list_to_test):
            # don't test adding yourself together
            if first_index == second_index:
                continue

            # record and report if we have a winner.
            if first_value+second_value == sum_value:
                print("{} + {} = {}".format(first_value, second_value, sum_value))
                result = 0
                if not complete_search:
                    return result

    if result == 1:
        print("No matches found.")
        
    return result

if __name__ == "__main__":
    sys.exit(main(LIST_OF_NUMBERS, SUMMATION, EXHAUSTIVE_SEARCH))
