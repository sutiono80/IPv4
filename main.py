# URL
# https://networkengineering.stackexchange.com/questions/7106/how-do-you-calculate-the.prefix-network-subnet-and-host-numbers

from PYsutiono import IPv4, Table, Cell


# Main Concept
tbl = Table('table.yml')
print (tbl.stitle())
print (tbl.dline())
print (tbl.columns())
print (tbl.dline())

subnets = open("subnets.yml")

idx = 1
for subnet in subnets:
	dest = IPv4(subnet)
	cel = list()
	cel.append(Cell(tbl.schema['fields'][0], idx))
	cel.append(Cell(tbl.schema['fields'][1], "{}/{}".format(dest.network(), dest.cidr)))
	cel.append(Cell(tbl.schema['fields'][2], "{} - {}".format(dest.netrange()[0], dest.netrange()[1])))
	cel.append(Cell(tbl.schema['fields'][3], dest.broadcast()))
	print (tbl.rows(cel))
	idx = idx + 1
# print (dest.network())
# print (dest.broadcast())
# print ("{} - {}".format(dest.netrange()[0], dest.netrange()[1]))

print (tbl.sline())
