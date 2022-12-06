## Exception Handling

When a python program is executed, there may be two types of errors that we face. During `compilation (syntax)` and `execution (exceptions / runtime)`. Sometimes, even when there is no error the output might be wrong, such an error is known as `logical error`.

The process of responding to the raised exception is known as exception handling. The super class is Exception in python.

The basic blocks we use to handle exception are as follows:

1. `try` - it is used to keep the code segment under check

2. `except` - it is used to handle the exception

3. `else` - it is a segment that executes if there are no exceptions

4. `finally` - it is used to execute code regardless of excpetions occuring

5. `raise` - it is used to raise a system / user-defined exception


Some nuances of `try - except`:

1. A try block can be nested inside another try block. 

2. A single try block can have multiple except blocks. However, only one will be excecuted.

3. Multiple exceptions can be given in one except block as a tuple.