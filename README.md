# ConsoleInput
    Small python class to get console input
    supports adding new commands and will
    take any number of arguments. 

```python
    from ConsoleInput import *

    def testFunc(*arguments):
        print len(arguments),"Arguments"
        print "First",arguments[0]
        print "Last",arguments[:-1]

    console = ConsoleInput(">")
    console.addCommand("test",testFunc)
    console.input()
```
# Example Output

    Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
    [GCC 5.4.0 20160609] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from ConsoleInput import *
    >>> console = ConsoleInput(">")
    >>> console.input()
    >test
    Unknown Command test
    >help 56
    Invalid Format help
    >help
    Console Input Help
    Avaliable Commands
    quit
    prompt
    help
    >sklfjskldfjkl
    Unknown Command sklfjskldfjkl
    >quit
    Jon@Machine:~/Projects/ConsoleInput$
    >>> 



