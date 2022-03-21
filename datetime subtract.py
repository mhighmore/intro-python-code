from datetime import datetime
from typing import List
from datetime import timedelta
from datetime import time



def sum_light(els: List[datetime]) -> int:
    """
        how long the light bulb has been turned on
    """
    total = timedelta()

    for i in range(0,len(els)-1,2):
        start = els[i]
        end = els[i+1]
       # t1 = timedelta(hours=start.hour, minutes=start.minute, seconds=start.second)
       # t2 = timedelta(hours=end.hour, minutes=end.minute, seconds=end.second)
        duration = end - start
        print(start, end, duration)
        total +=duration
    print(total)
    print(total.total_seconds())
    return total.total_seconds()







if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
    ]) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 12, 10 , 10),
    ]) == 4820

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 1),
    ]) == 1

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 13, 11, 0 , 0),
    ]) == 86410

    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")

