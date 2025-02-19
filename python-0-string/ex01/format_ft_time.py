#!/usr/bin/env python3

import time

# Get the current time in seconds since the Unix epoch
epoch_time = time.time()

# Format the time as a readable string
formatted_time = time.strftime("%b %d %Y", time.localtime(epoch_time))

# Print the output with commas separating thousands and scientific notation for seconds
print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:.2e} in scientific notation$")
print(formatted_time)




# {epoch_time:,.4f} the number is formatted with commas separating the thousands
# the time using time.strftime() to match the requested format (%b %d %Y)
