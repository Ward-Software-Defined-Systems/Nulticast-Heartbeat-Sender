# Multicast Heartbeat Sender #

While working on deploying and validating multicast configurations I found the need for a simple 
utility that could join a multicast group and send messages. I couldn't find anything basic
that fit, so I started looking into creating my own utility using Python.

I found a few standard code patterns that was what I was looking for at the core, so I decided 
to repurpose them into this Multicast Heartbeat Sender script/app.

### Summary: ###

* Version 1
* Used to send multicast heartbeats to a group/channel specified via command line.

### Run: ###
multicast-sender.py is designed to work with my multicast-receiver.py script/app but it can be used
to send multicast messages in general:

* ./multicast-sender.py [MULTICAST GROUP] [PORT] [TTL]
* ./multicast-sender.py 239.0.1.2 5004 3
* python3 multicast-sender.py 239.0.1.2 5004 3
