import time


def add_one_unit(add_unit):
    #print('add_one_unit')
    #print(add_unit[0])
    sum=0
    for val in add_unit[0]:
        sum = sum + val
    add_unit = (add_unit[0],sum)
    time.sleep(3)
    return add_unit

def add_all_units(addition_units):
    #print('add_all_units')
    result_units = []
    for add_unit in addition_units:
        add_result =  add_one_unit(add_unit)
        result_units.append(add_result)
    return result_units

def build_addition_units(size):
    addition_units = []

    for index in range(size):
        addends = []
        addends.append(index)
        addends.append(index+1)
        addends.append(index+2)
        addition_units.append((addends,0))
    #print(addition_units)
    return addition_units

if __name__ == "__main__":
    #build add units
    size=5
    start_time = time.time()
    addition_units = build_addition_units(size)
    duration = time.time() - start_time
    print(f"Built {size} units in {duration} seconds")

    #For each add the addends and store in result
    start_time = time.time()
    result_units = add_all_units(addition_units)
    print(result_units)
    duration = time.time() - start_time
    print(f"After adding {size} units in {duration} seconds")