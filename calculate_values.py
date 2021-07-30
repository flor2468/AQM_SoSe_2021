
def calculate_mean(array):

    sum = 0

    for i in range(len(array)):
        sum += int(array[i])

    mean = round(sum / len(array), 3)

    return mean