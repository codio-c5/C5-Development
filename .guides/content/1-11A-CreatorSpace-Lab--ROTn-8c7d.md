The ROTate by 13 places cipher (ROT13) is variation of the Caesar cipher. It shifts each character 13 places, or mid-way through the Latin (i.e., English) alphabet. This is not an arbitrary choice because the ROT13 cipher will encrypt a plaintext message the first time it's applied and decrypt the ciphertext the 2nd time it's applied. It's like moving the hour hand of a clock ahead 6 hours and then forward again by 6 hours and ending up where you started.

As we've learned shift ciphers provide little or no encryption. However, the ROT13 cipher is still a useful tool. It's used to hide information like plot spoilers from on-line from a casual glance. It's also good for teaching introductory cryptography!

The interactive ROTn on the left hand side is an cryptanalyst tool that lets you experiment with decoding ciphertext. It applies all 26 possible keys to the ciphertext.

Enter some ciphertext, for instance like  "WDNH PH RXW WR WKH EDOO JDPH", in the main text area and then press **Show ROTn**.

The application applies all 26 possible keys - rotations - to the ciphertext. Examine the results and see if something stands out.

Hint: look towards the bottom.

Indeed, the plaintext is revealed from a previous example of the Caesar cipher. You just used the Brute Force cryptanalysis technique by trying every possible key. That process revealed the original plaintext.