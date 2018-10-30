import yaml

# https://networkengineering.stackexchange.com/questions/7106/how-do-you-calculate-the.prefix-network-subnet-and-host-numbers
class IPv4:
	def __init__(self, address):
		# construct.cidr & octets within network subnet
		subnet = address.split("/")[0]
		self.cidr = int(address.split("/")[1])
		self.octets = tuple(subnet.split("."))

	def netmask(self, files):
		netmask_data = open(files, 'r')
		octets = (yaml.load(netmask_data)[self.cidr]).split(".")
		return octets

	@staticmethod
	def flip_bits(bits):
		# working
		temp_bits = []
		for b in bits:
			if b == "1":
				temp_bits.append("0")
			else:
				temp_bits.append("1")
		return temp_bits

	@staticmethod
	def bit_format(decstr):
		return "{:0>8}".format(bin(int(decstr)).lstrip("0b"))

	def inbits(self, octets):
		print "{}.{}.{}.{}".format(self.bit_format(octets[0]),
		                           self.bit_format(octets[1]),
		                           self.bit_format(octets[2]),
		                           self.bit_format(octets[3]))

	def host_bit_mask(self):
		octets = self.netmask("netmask.yml")
		hb_mask = []
		for o in octets:
			bits = self.bit_format(o)  # padding to prevent 0 become ""
			temp_bits = ""
			for b in bits:
				if b == "0":
					temp_bits = temp_bits + "1"
				else:
					temp_bits = temp_bits + "0"
			hb_mask.append(str(int(temp_bits, 2)))
		return hb_mask

	def network(self):
		# version 2
		netw_octets = []
		nmsk_bits = self.netmask("netmask.yml")
		for idx in range(4):
			netw_octets.append(int(nmsk_bits[idx]) & int(self.octets[idx]))  # Logical AND operation
		return netw_octets

	def broadcast(self):
		bcst_octets = []
		for idx in range(4):
			bcst_octets.append(int(self.octets[idx]) | int(self.host_bit_mask()[idx]))  # Logical OR Operation
		return bcst_octets

	def netrange(self):
		first = self.network()
		first.pop(3)
		first.append(self.network()[3] + 1)
		last = self.broadcast()
		last.pop(3)
		last.append(self.broadcast()[3] - 1)
		return first, last
