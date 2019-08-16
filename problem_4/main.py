'''
    Given an array of integers, find the first missing positive integer in linear time and constant
        space. In other words, find the lowest positive integer that does not exist in the array.
        The array can contain duplicates and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.
'''
SAMPLE_1 = [3, 4, -1, 1]
ANSWER_1 = 2

SAMPLE_2 = [1, 2, 0]
ANSWER_2 = 3

def main(data):
    '''
    Find the lowest missing integer.

    data is a list of integers
    '''
    data.sort(reverse=True)
    for index, datum in enumerate(data):
        if index == 0:
            continue
        if datum < 0:
            continue

        # Since we are reverse sorted, check that the last number is only one larger than us.
        if datum < data[index-1]-1:
            return datum+1

    return data[0]+1

if __name__ == "__main__":
    assert main(SAMPLE_1) == ANSWER_1
    assert main(SAMPLE_2) == ANSWER_2
