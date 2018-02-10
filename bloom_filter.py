import mmh3
from bitarray import bitarray


size=5000
inc_by=2

bit_array = bitarray(size)
bit_array.setall(0)


# This is used to map a url to a hashcode
def mapper(url):
	bit_1 = mmh3.hash(url, 21)%size
	bit_array[bit_1]=1

	bit_2 = mmh3.hash(url, 22)%size
	bit_array[bit_2]=1

	bit_3 = mmh3.hash(url, 23)%size
	bit_array[bit_3]=1

	bit_4 = mmh3.hash(url, 24)%size
	bit_array[bit_4]=1

	bit_5 = mmh3.hash(url, 25)%size
	bit_array[bit_5]=1

	bit_6 = mmh3.hash(url, 26)%size
	bit_array[bit_6]=1

	bit_7 = mmh3.hash(url, 27)%size
	bit_array[bit_7]=1


# This function is used to double the size of the bitarray
# This is used for making the amortized complexity of insertion
# approximately O(n)

