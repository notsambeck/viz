[# viz
visualize code execution


## Pieces of the Problem
1. All code executes as machine code; we are always writing machine code but we rarely know what that code actually is.
1. The VM/stack machine is an imaginary intermediate state: a machine-generated translation of human code. The stack is a valuable abstraction between human code and machine code because:
    1. Writing language->VM and VM->ASM compilers is nicer than writing a single-step compiler
    1. In modern systems, the sharp end of the stack roughly corresponds to cache (i.e. memory is SUPER SLOW!)
    1. Visualizing a CPU machine is much messier than visualizing a stack machine.
1. In a given language, knowing the memory model is a potentially important optimization


## Goal
Create a tool that takes human code as input, and shows how that code actually executes. There are many levels of abstraction at which this could be viewed.

## Components
ref: [The Pthon VM](https://leanpub.com/insidethepythonvirtualmachine/read#:~:text=The%20Python%20virtual%20machine%20is,back%20on%20the%20value%20stack.)

### cPython:
* Input (code)
* Parse tree
* AST
* compiled Python bytecode
* code object
  * creation
  * execution
](https://leanpub.com/insidethepythonvirtualmachine/read#:~:text=The%20Python%20virtual%20machine%20is,back%20on%20the%20value%20stack.)
