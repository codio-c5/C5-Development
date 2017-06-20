IBM created the Data Encryption Standard (DES) encryption algorithm in 1970's. Following Kerckhoffs’s Principle, they submitted it to the National Bureau of Standards (NBS). That, plus a version modified and endorsed by the NSA, led to its worldwide use for protecting non-classified, sensitive data.

|||
The NBS is now the National Institute of Standards and Technology (NIST)
|||

Here's a complex graphic describing DES. You can see from this that it is rather more rigorous in its approach than the shift and substjavascript:void(0)itution algorithms we have seen so far.

![](.guides/img/DES.png)
Source: https://en.wikipedia.org/wiki/Data_Encryption_Standard

DES is a block cipher, meaning that rather than working on a stream of data - bit-by-bit - it works on one block at a time. One block consists of 64 bits.

Computing power has increased dramatically at less cost since the 1970s. The original DES used a key of 56 bits and given increased compute power it is not considered secure. One reasonable solution is Triple DES (3DES) that simply applies DES three times on each data block.

|||guidance
**Instructor'sNote:** Students can explore DES further here: http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
|||
