# Praze-Cipher
Python implementation of the praze cipher by Praise James


**PRAZE CIPHER ALGORITHM**
decided to look back at my recent math algorithm and made a cypher out of it
My algorithm for encryption, the praze cipher
'How do you tell  someone you know 
a secret without saying the secret?'
mathematically, let's say, given 3*7 = 21, you can 
easily get back 3 if it was missing i.e x*7 = 21,
 x = 21/7 = 3. But how about something you can multiply
 but not get back to.
So here's the algorithm:

let's say (x, y)(a, b) = (f, g), if you don't know (x, y)
you can't get it, like this

let's say x = 2, y = 3, a = 6, b = 1

(2, 3)(6, 1) = (f, g)
let's say
(2(6, 1)), (3(6, 1))
(12, 2), (18, 3)
216, 36, 36, 6
 Note: following the algorithm, there will always be 2 alike
numbers, regardless of the numbers being used
the next part of the algorithm eliminates the 2 alike numbers
thus

(2, 3)*(6, 1) = (216, 6)
 where (2, 3) is the secret, (6, 1) is the key and (216, 6) is the encrypted data
if you're to look for (x, y) i.e:
(x, y)*(6, 1) = (216, 6)
x, y, cannot be found!

Unless you are given the value of B where B = [y*a, y*b], the value of
the alike number, the value of the encrypted data and the value of a

which is what is needed to decrypt the data, this would be the algorithm to 
decrypt it (written in python):

_x_ = 216/B[0]
_y_ = 6/B[1]
out = (_x_, _y_)
final = [_x_/a, B[0]/a]

this would result the initial secret
final = (2, 3)

here is the source code to a python implementation of the algorithm>>>
https://github.com/Trojan-Cipher/Praze-Cipher

the source code (and perhaps the algorithm) would be upgraded from time to time. feel free to test the cipher, try hacking the cipher or use it in your cryptographic projects :) ,
a detailed and better explanation would be pondered on my whitepaper which you should expect
soon! :D
i'll love your feedbacks
