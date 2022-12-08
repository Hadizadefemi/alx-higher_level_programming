#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        efx = 0
        ef = 0
        for i in range(len(my_list)):
            for j in range(len(my_list[i])):
                efx += my_list[i][j] * my_list[i][j+1]
                ef += my_list[i][j+1]
                break
    return (efx / ef)
