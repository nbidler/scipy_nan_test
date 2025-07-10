import numpy as np

from scipy import special

def is_result_nan(lower, upper):
    result = special.softmax([lower, lower, upper])
    print(result)
    return np.isnan(result).any()

def binary_search_nan_bound(lower_bound, upper_bound):
    # between a lower and upper bound number
    # find the point at which the array result becomes NAN
    # can probably be a binary search
    # if finding the boundary where the break happens, can't just binary search
    # must find where prev_result & cur_result are FALSE-TRUE or TRUE-FALSE
    # but also prev_num & cur_num are only 1 number apart

    lo_num = lower_bound
    hi_num = upper_bound
    mid = (hi_num) / 2

    while (mid <= hi_num):
        print(lo_num, mid, hi_num)
        input("Press Enter to continue...")
        
        low_bound = mid
        low_result = is_result_nan(lo_num, mid)

        high_bound = hi_num
        high_result = is_result_nan(lo_num, hi_num)
        
        if (low_bound == high_bound - 1) and (low_bound != np.inf) and (high_bound != np.inf):
            if (low_result == False and high_result ==  True):
                #found numbers that go from real result to NAN
                return (lo_num, hi_num, True)
            else: 
                #met in middle but did not find discontinuity
                return (lo_num, hi_num, False)
        
        # result not found, move targets
        if (low_result == True) and (high_result ==  True):
            # low and high result both NAN, too high
            hi_num = mid
            mid = (lo_num + mid) / 2
        elif (low_result == False) and (high_result ==  False):
            # low and high result both number, too low
            mid = (mid + hi_num) / 2
            # hi_num = hi_num, no change
        # else low_result and high_result are either True/False or False/True
        # True/False means "on the right track but no precise answer"
        # False/True means something bad has happened
    return (lo_num, hi_num)
    #mid = (lo_num + hi_num) / 2
        



if __name__ == "__main__":
    np.set_printoptions(precision=5)

    x = np.array([[1, 0.5, 0.2, 3],
                [1,  -1,   7, 3],
                [2,  12,  13, 3]])

    print(x)

    m = special.softmax(x)

    print(m)

    print(m.sum())

    # print("World Hello")

    #big_number = np.finfo(np.float64).max
    #np.float64 max not big enough for NAN

    #big_number = np.iinfo(np.uintp).max
    #uintp max not big enough for NAN

    # big_number = np.finfo(np.float128).max
    #np.longdouble max not big enough for NAN

    print( binary_search_nan_bound(1, 1e500) )