### The flowchart on the left is a representation of the Caesar Cipher algorithm.
It describes the cipher algorithm, or recipe, that shifts characters by the specified key. If you were to write the algorithm in plain English, it would look a lot like a recipe. At the end, you'll have a ciphertext instead of chocolate chip cookies.

1. Get the file
2. Get the number of characters to shift
3. Get the first character from the file
4. Skip to the next character if it's not a letter (i.e., if it's a number or special character like #)
5. Shift the character specified number
6. Check if the shift goes past the end of the alphabet and, if so, go back to the beginning of the alphabet
7. Check if the shifted character is the last character in the file and exit if true
8. Get the next character and start at 4th step