"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c


def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temperature_f = temperature_c * (9/5) + 32
    return temperature_f

def convert_c_to_k(temp_c):
    '''Convert Celsius to Kelvin.'''
    return temp_c + 273.15

def convert_f_to_k(temp_f):
    '''Convert Fahrenheit to Kelvin.'''
    return (temp_f - 32) * 5/9 + 273.15

def convert_k_to_c(temp_k):
    '''Convert Kelvin to Celsius'''
    return temp_k - 273.15

def convert_k_to_f(temp_k):
    '''Convert Kelvin to Fahrenheit'''
    return (temp_k - 273.15) * 9/5 + 32

def convert_f(temp_f):
    '''Convert Fahrenheit to Celsius and Kelvin'''
    print('The temperature %s degrees F is:' % temp_f)
    
    temp_c = convert_f_to_c(temp_f)
    temp_k = convert_f_to_k(temp_f)
    print('\t%s degrees Celsius' % temp_c)
    print('\t%s degrees Kelvin' % temp_k)
    