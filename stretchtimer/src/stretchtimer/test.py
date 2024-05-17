import time


def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        seconds -= 1

    print("\nTimer complete!")

# Example: Set the timer for 5 minutes (300 seconds)
countdown_timer(10)



# input("Press Enter to start")
# start_time = time.time()
#
# input("Press Enter to stop")
# end_time = time.time()
#
# time_lapsed = end_time - start_time
# time_converter(time_lapsed)


