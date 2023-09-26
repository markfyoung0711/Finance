def rate_of_return(interest, term, frequency):
        return (1 + (interest/frequency)) ** (term*frequency)

        
def future_value(principle, interest, term, frequency=1):
    return principle * rate_of_return(interest, term, frequency)

def present_value(future_value, interest, term, frequency=1):
    return future_value * (1/rate_of_return(interest, term, frequency))