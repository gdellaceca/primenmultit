# primenmultit
Find the first N prime numbers using a sequential or a multiprocess function
---

## Disclaimer
This is a learning project, it will probably contain a whole bunch of errors.\
The learning points are the following:
* Understand how multiprocessing works in Python
* Also applies to multithreading (In a theoretical sense, thanks to GIL)
* Practice some markdown for various purposes (that explains the useless verbosity)
* Apply the above to GPUs, using CUDA with `pycuda`.

## About prime numbers

Prime numbers are famous for a couple of reasons, like the fact that they constitute the fundamental blocks of mathematics or that RSA wouldn't work without them.\
By definition, a prime number's only divisors are 1 and itself. This makes finding an analytical way to compute arbitrary prime numbers quite a daunting task ~(read "a mathematician's wet dream")~. \
The first known attempt to find an order to these numbers traces back to Erathostenes, whose sieve has since been used.

A pseudocode [implementation of the algorithm](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) goes like this:

```
algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.
    
    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
                A[j] := false

    return all i such that A[i] is true.
```
Note the  `for` cycle that goes to the square root of `n`: this saves iterations, as all the multiples of a prime number p before p^2 are already taken care of by the previous prime numbers in the list.\
My implementation uses `numpy`, to ensure speed and general compatibility with other libraries.  
