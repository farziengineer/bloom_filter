# bloom_filter 
Bloom Filter with naive scalability. 
Bloom filter is a widely used probabilistic data structure, that is used to answer whether an element is present in a set or not. If the bloom filter answers **"NO"**, it means the element is **definitely** not present, but if the filter answers **"YES"**, then there is a chance that the element is present in the set, or not. Bloom filter is basically a space-time trade off with accuracy.


In case you are thinking of use case of Bloom Filter, read this briliant answer on [Stack Overflow](https://stackoverflow.com/questions/4282375/what-is-the-advantage-to-using-bloom-filters), which explains how this is used by Chrome Web Browser for detection of malicious url when the user types the address into the address bar.Databases such as Cassandra use bloom filters to see if it should do a large query or not. 

Read [this](http://www.maxburstein.com/blog/creating-a-simple-bloom-filter/) article to find out how a simple bloom filter is implemented.
