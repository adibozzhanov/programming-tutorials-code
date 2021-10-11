# GDB quick tips:

## Compile correctly
 Whatever you do wrong to your code C will spit out a single error all the time
 
 That's because once the code is compiled the information about the source code is lost
 
 So the interpreter that is running your C code has no way to identify what the hell is wrong with it.
 
 For that we will need to run our compiler with a special command: `gcc -g source-file.c`
 
 This will leave information about the source code along with the compiled file.
 
 Now that we have our smart compiled file we can play with is using a debugger

## Using GDB

 Your compiled file should be called something like `a.out` or whatever you named it.
 
 Basically run the gdb command on the compiled file.
 
 `gdb a.out`
 
 this will open a propt that will look like this:
 
 ```
 kyouma@nomad ~/D/c/p/c/debugger (main)> gdb a.out 
 GNU gdb (Ubuntu 10.1-2ubuntu2) 10.1.90.20210411-git
 Copyright (C) 2021 Free Software Foundation, Inc.
 License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
 This is free software: you are free to change and redistribute it.
 There is NO WARRANTY, to the extent permitted by law.
 Type "show copying" and "show warranty" for details.
 This GDB was configured as "x86_64-linux-gnu".
 Type "show configuration" for configuration details.
 For bug reporting instructions, please see:
 <https://www.gnu.org/software/gdb/bugs/>.
 Find the GDB manual and other documentation resources online at:
     <http://www.gnu.org/software/gdb/documentation/>.

 For help, type "help".
 Type "apropos word" to search for commands related to "word"...
 Reading symbols from a.out...
 (gdb) 


 ```
 
 This is where we will debug our code.
 
 Use this table to reference useful commands:
 
 | Command  | Explanation  |
 | :-:|---|
 | `quit`  | quit the debugger  |
 | `run`  | run your code  |
 | `break <line_num>`  | set a break point at a specific line number.<br> Once you run, Debugger will stop and prompt for action every single time your code happens to reach that line  |
 | `l`  | Show code that is currently next to where you stopped  |
 | `l <line number>` | Show code that is next to the line number you entered |
 | `p <variable_name>` | print the current value of a variable|
 | `c` | Continue execution until next breakpoint or until the program stops |
 | `s` | Execute 1 next step |
 | `n` | Keep executing untl the code reaches next line |
 | `bt` | Backtrack - show all the nesting of function that happened (print backtrace of all stack frames is the proper way to say it)| 


