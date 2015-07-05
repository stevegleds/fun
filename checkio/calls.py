__author__ = 'Steve'
# consider calculating cost of call before updating summary to fix final problem
def calculate_total_cost(summary):
    total = 0
    for date in range(len(summary)):        
        total += daily_cost(summary[date])
        print("total is ", total)
    return total


def total_cost(calls):
    print(calls)
    cost = 0
    summary = []
    first_colon = calls[0].find(":") # used to find the data in the list elements
    current_month = int(calls[0][first_colon - 5:first_colon - 3]) # identifies the date from the list element
        
    for day in range(365): # need a value for each day in the month
        summary.append(0)
    for call in range(len(calls)):
        print("call number: ", call)
        date = int(calls[call][first_colon - 5:first_colon - 3]) # identifies the date from the list element
        month = int(calls[call][first_colon - 8:first_colon - 6]) # identifies the date from the list element
        if month != current_month:
            date += 31
        print("date: ", date)
        duration_seconds = int(calls[call][first_colon + 6:]) # number of seconds of the call
        duration_minutes = int(round((duration_seconds / 60) + 0.49, 0))  # add 0.49 to ensure we round up
        print("minutes: ", duration_minutes)
        summary[date] += duration_minutes
        print("summary after call ",call, " is ", summary)
        print("duration for call ", call + 1, "is ", duration_minutes)
        # cost += daily_cost(duration_minutes)
        # print("Cost after day ", call + 1, " is ", cost)
        print(summary)
    return calculate_total_cost(summary)

def daily_cost(duration):
    if duration <= 100:
        return duration
    else:
        return 100 + ((duration - 100) * 2)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"