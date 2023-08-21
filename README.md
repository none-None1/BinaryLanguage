# BinaryLanguage
 A Turing complete esoteric language based on binary operations

## Memory Model

BinaryLanguage uses three registers (initially zero): <code>A</code>, <code>B</code> and <code>C</code>. They can contain unsigned integers of ''any'' size (or up to at least 2<sup>10000</sup>).
## Commands
It has these commands:
| Command | Meaning |
| ---- | ---- |
| + | Increments <code>A</code> |
| - | Decrements <code>A</code> |
| & | Bitwise **and** <code>A</code> and <code>B</code>, stores the result in <code>A</code> |
| &#124; | Bitwise **or** <code>A</code> and <code>B</code>, stores the result in <code>A</code> |
| ^ | Bitwise **xor** <code>A</code> and <code>B</code>, stores the result in <code>A</code> |
| < | Bitwise left shift <code>A</code> by <code>B</code> bits, stores the result in <code>A</code> |
| > | Bitwise right shift <code>A</code> by <code>B</code> bits, stores the result in <code>A</code> |
| ~ | Swaps <code>A</code> and <code>B</code> |
| * | Performs a right circular shift to the three registers |
| ( | If <code>A=0</code>, jump to the matching <code>)</code> |
| ) | If <code>A!=0</code>, jump to the matching <code>(</code> |
| , | Reads a character from user input and stores its ASCII value to <code>A</code> |
| . | Output the character with its ASCII value the same as <code>A</code> |
