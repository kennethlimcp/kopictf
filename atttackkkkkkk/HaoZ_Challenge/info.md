You work for a secret intelligence agency.
One of your undercover agent managed to steal an important intel from “Enemy of the State Corporation”. Y
ou know that they use a new encryption scheme with Shift CPB Cipher (contains md5).
Unfortunately, the specification of the cipher was incomplete because he didn’t have top level clearance.
The director wants you to crack the encrypted PDF file and get the intel.

Hint: think about the input and output length

A full range Ascii shift (0 to 127) is used.

Secret key: 3 char long alphabetical string

The Cipher Feedback (CFB) mode

(hint is MD5 of HAOZ)
IV: 09bf1e72affb6a192448a572e11e4620

Block size: 128bit (128/8 = 16 bytes)

Input: 0x41 0x42
Key:   0x01 0x02
Ouput: 0x42 0x44


### Resources
- https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Feedback_.28CFB.29
