'''
'''
import sys

INPUT_LIST = [1, 2, 3, 4, 5]

def main(list_of_numbers):
    '''
    list_of_numbers is an array of integers
    
    print the output array as designed.
    '''
    product = 1
    for value in list_of_numbers:
        product = product * value
        
    result_list = []
    print("Testing list: {}".format(list_of_numbers))
    for value in list_of_numbers:
        result_list.append(int(product/value))
    
    print("Calculated list: {}".format(result_list))

    return 0

def follow_up(list_of_numbers):
    '''
    list_of_numbers is an array of integers
    
    print the output array as designed.
    '''
    def calculate(position):
        '''
        Calculate product of the array exempting the current position.
        '''
        result = 1
        for index, value in enumerate(list_of_numbers):
            if position == index:
                continue
                
            result = result * value
            
        return result 
        
    result_list = []
    print("Testing list: {}".format(list_of_numbers))
    for index, value in enumerate(list_of_numbers):
        result_list.append(calculate(index))
    
    print("Calculated list: {}".format(result_list))

    return 0

if __name__ == "__main__":
    main(INPUT_LIST)
    follow_up(INPUT_LIST)
    sys.exit()
