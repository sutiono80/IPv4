# URL
# https://networkengineering.stackexchange.com/questions/7106/how-do-you-calculate-the-prefix-network-subnet-and-host-numbers

import yaml
import math


class IPv4:

	def __init__(self, address):
		# construct prefix & octets within network subnet
		subnet = address.split("/")[0]
		self.prefix = int(address.split("/")[1])
		self.octets = tuple(subnet.split("."))

	def netmask(self, files):
		netmask_data = open(files, 'r')
		octets = (yaml.load(netmask_data)[self.prefix]).split(".")
		return octets

	@staticmethod
	def flip_bits(start, end, val):
		mask = (math.pow(2, end+1) - 1 - (math.pow(2, start) - 1))
		final_num = val ^ int (mask)
		return final_num

	def broadcast(self):
		# working on how to invert the bits
		# clarify again, especially for [1:9]
		octet_bits = self.netmask("netmask.yml")
		binary = bin(int(octet_bits[3])).lstrip("0b")
		inverted = bin(self.flip_bits(0,8, 128)).lstrip("0b")[1:9]
		print ("binary  {}".format(binary))
		print inverted


	def network(self):
		# version 2
		netmask_octets = []
		octet_bits = self.netmask("netmask.yml")
		for idx in range(4):
			netmask_octets.append(int(octet_bits[idx]) & int(self.octets[idx]))

		return "{}.{}.{}.{}/{}".format(netmask_octets[0],
										netmask_octets[1],
										netmask_octets[2],
										netmask_octets[3],
										self.prefix)

#	def network(self):
#       # Version 1
#		once = False
#		full_bit = 255
#		net_bits = []
#		netmask_octets = []
#		host_bits_idx = self.prefix % 8                         # to determine host bits
#		num_net_bits = self.prefix / 8                          # to determine number of full wildcard bits (255)
#		mask_data = open('bits.yml', 'r')                       # open the file contains host bits index
#		host_mask_bit = yaml.load(mask_data)[host_bits_idx]     # to determine host bits
#
#		# reassignment for network bits value, either 255 or other values for each octet to determine netmask
#		for oct_idx in range(4):
#			if oct_idx+1 <= num_net_bits:
#				net_bits.append(full_bit)
#			else:
#				if not once:
#					net_bits.append(host_mask_bit)
#					once = True
#				else:
#					net_bits.append(0)
#
#		# to determine network address value for each octets
#		for idx in range(4):
#			netmask_octets.append(net_bits[idx] & int(self.octets[idx]))
#
#		# final
#		return "{}.{}.{}.{}/{}".format(netmask_octets[0],
#										netmask_octets[1],
#										netmask_octets[2],
#										netmask_octets[3],
#										self.prefix)


# Main Concept
dest = IPv4("192.168.1.0/25")
# print (dest.network())
# print (dest.netmask("netmask.yml"))
print (dest.broadcast())
# print (dest.reverse())