
Before we start, click the clean up button to clear out any previous work.

{CLEAN UP}(sh rsa/cleanup.sh lab-part1)

## Generate Your Keys

To get started, you will generate a key pair; your partner will do the same. A key pair consists of a private key and a public key.

 - If you are Alice, click the Generate Alice's keys button.

{Generate Alice's keys}(sh rsa/keygen.sh alice)

 - If you are Bob, click the Generate Bob's keys button.

{Generate Bob's keys}(sh rsa/keygen.sh bob)

The file tree on the left shows the keys, along with other files, that you just generated. One is ```private.key``` and the other is ```alice-public.key``` or ```bob-public.key```.

## Download The Public Key

 - Alice and Bob download their public key file to their respective computers. To download, right click on the public key file name in the tree on the left and select "Download". 

## Email Public Key

 - Alice emails the renamed public key file to Bob and vice versa.

 - Click on the private key in the file tree, on the left, and a tab opens in this space showing its contents. (You can move between the tabs by clicking on them.)
 
 - Copy and paste the private key into the box below. 
 {Submit Answer!|assessment}(free-text-3445674952)

 - Open up the public key file that has been created.
 - Copy and paste the public key into the box below. 
 {Submit Answer!|assessment}(free-text-648952340)
