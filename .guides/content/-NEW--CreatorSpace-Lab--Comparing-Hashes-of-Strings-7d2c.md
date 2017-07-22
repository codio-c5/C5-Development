
Let's examine th behavior of several common hash algorithms: MD5, SHA1, SHA256, and SHA512.

In the terminal on the left, run the following command with the sample text string as input (include the parentheses).

```python hashes.py "take me out to the ballgame"```

Notice that it returns different hashes for each hash function. Why is the length of each output different?

Now, make a small change to the input.

```python hashes.py "take me out to the ballgamE"```

You'll see how each function produces different output. How much different is the result for each different after changing one letter?

Instructor's note: You can erase - clear - the terminal screen at any time by entering the command ```clear```.