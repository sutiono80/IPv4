# URL
# https://networkengineering.stackexchange.com/questions/7106/how-do-you-calculate-the.prefix-network-subnet-and-host-numbers

from PYsutiono import IPv4, Table, Field, Cell


# Main Concept
dest = IPv4("192.168.0.149/22")
print (dest.network())
print (dest.broadcast())
print ("{} - {}".format(dest.netrange()[0], dest.netrange()[1]))
