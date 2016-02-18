# Atx-8

This is just a symetric encryption algorithm I made back when I was 17, had one year of experience with basic Python and was a dank Anonymous h@cker shit

I also made an asymetric version of it ( just like PGP except it doesn't protect shit )

###Here is pretty much how it works:

Let's suppose we want to send the message 'Hello' with the key 'password'

**We'll use false values for comprehension and because I'm lazy af**

So let's say H equals to 32 in our alphabet, we save that number ( 32 ) and scramble the alphabet using our functions applied to the key 'password'

**3 functions are used in the algorithm**
* The first function shifts all characters of the alphabet *n* position to the right
* The second function creates groups of *n* characters and invert the position of the characters inside
* The third function creates groups of *n* characters and swaps them 2 by 2

It then executes them many times in a particular order using the key's letters, so it looks like this:

First_function('p')

Second_function('a')

Third_function('s')

Second_function('s')

First_function('w')

Third-function('o')

Second_function('r')

First_function('d')

**As it executes functions for a total of 8 times, the key must be 8 characters minimum**

We now have a scrambled alphabet, so we just take the 32nd one ( because the 'H' we wanted to crypt was the 32nd one in then ormal alphabet )

We now have crypted a character, so we shift the key by one position before crypting the second one ( the key now becomes 'dpassword', then it will become 'rdpasswo' for the 3rd character and so on... )

With this ~~secret~~ technique we can avoid having the same key for all the characters and it makes it harder to decrypt without knowing the key
