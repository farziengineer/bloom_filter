import mmh3
from bitarray import bitarray
import csv

size=30
inc_by=1

bit_array = bitarray(size)
bit_array.setall(0)


# This is used to map a url to a hashcode
def mapper(url):
	global inc_by
	bit_1 = mmh3.hash(url, 21)%size
	bit_array[bit_1*inc_by]=1

	bit_2 = mmh3.hash(url, 22)%size
	bit_array[bit_2*inc_by]=1

	bit_3 = mmh3.hash(url, 23)%size
	bit_array[bit_3*inc_by]=1

	bit_4 = mmh3.hash(url, 24)%size
	bit_array[bit_4*inc_by]=1

	bit_5 = mmh3.hash(url, 25)%size
	bit_array[bit_5*inc_by]=1

	bit_6 = mmh3.hash(url, 26)%size
	bit_array[bit_6*inc_by]=1

	bit_7 = mmh3.hash(url, 27)%size
	bit_array[bit_7*inc_by]=1

	print bit_1, bit_2, bit_3, bit_4, bit_5, bit_6,  bit_7


# This function is used to double the size of the bitarray
# This is used for making the amortized complexity of insertion
# approximately O(n)

def extender(cur_size):
	global bit_array, inc_by
	extra = bit_array[:]
	bit_array=bitarray(cur_size*2)
	bit_array.setall(0)

	inc_by =inc_by*2
	for idx, bits in enumerate(extra):
		bit_array[2*idx] = extra[idx]



def checker(url):
	global inc_by

	bit_1 = mmh3.hash(url, 21)%size
	# bit_array[bit_1]=1

	bit_2 = mmh3.hash(url, 22)%size
	# bit_array[bit_2]=1

	bit_3 = mmh3.hash(url, 23)%size
	# bit_array[bit_3]=1

	bit_4 = mmh3.hash(url, 24)%size
	# bit_array[bit_4]=1

	bit_5 = mmh3.hash(url, 25)%size
	# bit_array[bit_5]=1

	bit_6 = mmh3.hash(url, 26)%size
	# bit_array[bit_6]=1

	bit_7 = mmh3.hash(url, 27)%size
	# bit_array[bit_7]=1
	print bit_1*inc_by, bit_2*inc_by, bit_3*inc_by, bit_4*inc_by, bit_5*inc_by, bit_6*inc_by, bit_7*inc_by

	# print bit_array[bit_1*inc_by], bit_array[bit_2*inc_by], bit_array[bit_3*inc_by], bit_array[bit_4*inc_by]

	if bit_array[bit_1*inc_by] and bit_array[bit_2*inc_by] \
	 and bit_array[bit_3*inc_by] and bit_array[bit_4*inc_by] \
	  and bit_array[bit_5*inc_by] and bit_array[bit_6*inc_by] \
	   and bit_array[bit_7*inc_by]:

	   return "maybe present"
	return "defenitely not present" 



def reader_and_writer():
	global bit_array
	r = csv.reader(open("test1.csv"));
	for row in r:
		url=row[1]
		mapper(url);
	# print "done"

	with open("bloom_filter.txt","wb") as fh:
		bit_array.tofile(fh)


	# f=open("bloom_filter.txt","wb")
	# f.write(str(bit_array))
	# f.close()


reader_and_writer()


while(1):
	n=int(raw_input())
	if(n==1):
		print bit_array
		s = raw_input()
		print checker(s)
	else:
		extender(bit_array.length())
		print bit_array


