#####
# This is a custom 'getting started' script, made with care for tfontaine@troyfontaine.com.
# If you have any questions, please email us! support@initialstate.com
#####

# Import the ISStreamer module
from ISStreamer.Streamer import Streamer
# Import time for delays
import time

# Streamer constructor, this will create a bucket called Python Stream Example
# you'll be able to see this name in your list of logs on initialstate.com
# your access_key is a secret and is specific to you, don't share it!
streamer = Streamer(bucket_name="CTL-R2002", bucket_key="default_configv1", access_key="lMHiNF8EX06ef9VYoBdZgHJG7BdPPtP0")

# example data logging
streamer.log("My Messages", "Stream Starting")
for num in range(1, 20):
	time.sleep(0.1)
	streamer.log("My Numbers", num)
	if num%2 == 0:
		streamer.log("My Booleans", False)
	else: 
		streamer.log("My Booleans", True)
	if num%3 == 0:
		streamer.log("My Events", "pop")
	if num%10 == 0:
		streamer.log("My Messages", "Stream Half Done")
streamer.log("My Messages", "Stream Done")

# Once you're finished, close the stream to properly dispose
streamer.close()