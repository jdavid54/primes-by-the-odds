# primes-by-the-odds
how to get all the primes until a given number


This is inspired by the lecture of 𝐆𝐮𝐢𝐥𝐥𝐚𝐮𝐦𝐞 𝐇𝐚𝐰𝐢𝐧𝐠 : 

Facebook : https://fb.watch/p2PnlYHBWw/

Youtube : https://www.youtube.com/watch?v=cONhad3q10s

Recall : for any k from 0 to infinity, 

1) All primes (except 2) are odd numbers, ie. 2k+1
2) Primes only end with 1, 3, 7, 9, ie. 10*k+11, 10*k+3, 10*k+7, 10*k+9
3) Odd numbers are primes if when ending with :

     a) 1 , are not a product like (10*k+7)(10*k+3) or (10*k+11)(10*k+11) or (10*k+9)(10*k+9)
   
     b) 3 , are not a product like (10*k+3)(10*k+11) or (10*k+7)(10*k+9)
   
     c) 7 , are not a product like (10*k+7)(10*k+11) or (10*k+3)(10*k+9)
   
     d) 9 , are not a product like (10*k+3)(10*k+3) or (10*k+9)(10*k+11) or (10*k+7)(10*k+7)  


So to get primes under a given number (ex : 1 million), we must first sieve out for each number n to be tested :

     - all even numbers (except 2)

     - all odd numbers ending with 5 (except 5)

     - all odd numbers as one of the products above


Then n is divided by each known primes. If n is prime (not a multiple of any known prime), n is then added to the list of primes to be used for the next number n+2.

NB : To optimize the sieve, only search for a prime divisor below the square root of n.
