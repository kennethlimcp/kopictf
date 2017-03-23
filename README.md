#### General information
1. 1-2 hour challenge
2. Byte flipping + CBC padding oracle attack? (Yes)
3. Unique plaintext and ciphertext for each query during byte flipping
4. Morse code plaintext for flag (maybe)
5. byte flipping will lead to receiving the encrypted file for next part of the challenge
6. Twist so that direct operation of the goggled solution doesn't work

#### Task
- CBC encryption and decryption functions
- Server design and the response
  - tcp service for decryption verification
  - http UI?
- Story line (2-3 sentences)
- step by step documentation on how to solve the challenge
  - hints provided to guide them to the solution

#### Resources
- [Padding oracle attack](http://robertheaton.com/2013/07/29/padding-oracle-attack/)
- [Byte flipping](http://resources.infosecinstitute.com/cbc-byte-flipping-attack-101-approach/#gref)
