"""
A pharmaceutical company wants to know whether an experimental drug affects systolic blood pressure.
Fifteen randomly selected subjects were given the drug and, after sufficient time for the drug to have an impact,
their systolic blood pressures were recorded.
The data appears in a python list.

THE FOLLOWING POINTS MUST BE DONE USING SOME FUNCTIONS OF SOME MODULE, AND WITH ANOTHER FUNCTION THAT YOU BUILT,
THAT IS, IMITATE THE BEHAVIOUR OF THAT FUNCTION

1. Calculate the value of 'x bar' (sample mean) and the value of s (the sample standard deviation)

"""
import statistics
data = [172, 140, 123, 130, 115, 148, 108, 129, 137, 161, 123, 152, 133, 128, 142]

def media(list):
    # suma = 0
    # tam = len(list)
    # for _ in list:
    #     suma += _
    media = sum(list)/len(list)
    return media


def dtdev(list):
    n = len(list)
    suma=0
    for _ in list:
        suma += pow(_-media(list),2)
    dtdev = pow((suma/(n-1)),0.5)
    return dtdev


print(media(data))
print(dtdev(data))