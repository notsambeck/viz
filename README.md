# viz

visualize code execution

## Mission

Build a graphical simulation of computer execution.

It should be:
* Pretty to look at
* Informative about how some programs "look" in execution
* Able to visualize the execution of meaningful code

## Pieces of the Problem

1. All code executes as machine code; we are always producing machine instructions, but we rarely see them.
    1. Even if we saw the machine instructions, they are so low-level that they aren't easily understood in context.
2. The VM/stack machine is an imaginary intermediate state: a machine-generated translation of human code.
   The stack is a valuable abstraction between human code and machine code because:
    1. Writing language->VM and VM->ASM compilers is nicer than writing a single-step compiler
    2. In modern systems, the sharp end of the stack roughly corresponds to cache (i.e. memory is SUPER SLOW!)
    3. Visualizing a CPU machine is much messier than visualizing a stack machine.

## Goal

Create a tool that takes human code as input, and shows how that code executes.
There are many levels of abstraction at which this could be viewed.

## Components

ref: [The Python VM](https://leanpub.com/insidethepythonvirtualmachine/read#:~:text=The%20Python%20virtual%20machine%20is,back%20on%20the%20value%20stack.)

### cPython:

* Input (code)
* Parse tree
* AST
* compiled Python bytecode
* code object
    * creation
    * execution
* ASM
* machine code


### C

* input code
* AST
* machine instructions
* execution model
  * (virtual) memory space
  * CPU instruction set
  * data buses


### Assembly
See: shenzhen I/O


### Hack
This largely exists already:

[VM emulator: live view of memory, PC, etc. from stack machine POV](https://www.nand2tetris.org/software?lightbox=dataItem-j9d33lz0)

[CPU simulator: instructions, symbolic memory, and bit-level binary memory viewer i.e. a screen](https://www.nand2tetris.org/software?lightbox=dataItem-j9cwy0cn)
