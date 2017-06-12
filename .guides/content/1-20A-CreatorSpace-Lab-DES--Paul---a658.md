Here's a complex graphic describing DES. You can see from this that it is rather more rigorous in its approach than the shift and substjavascript:void(0)itution algorithms we have seen so far.

![](.guides/img/DES.png)

DES is a block cipher, meaning that rather than working on a stream of data - bit-by-bit - it works on one block at a time. One block consists of 64-bits.

Computing power has increased dramatically at less cost since the 1970s. The original DES used a key of 56 bits and given increased compute power it is not considered secure. One reasonable solution is Triple DES (3DES) that simply applies DES three time on each data block.

http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm