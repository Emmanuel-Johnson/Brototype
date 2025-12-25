The nonlocal keyword in Python is used to modify a variable that is not local to the current function, but exists in an enclosing (outer) function, and is not global. In simple words, nonlocal allows an inner function to update a variable from its outer function’s scope.

To understand why nonlocal is needed, we first need to understand Python’s scope rules. Python follows the LEGB rule: Local, Enclosing, Global, and Built-in. When a variable is assigned inside a function, Python treats it as local by default. So if an inner function tries to change a variable defined in the outer function, Python creates a new local variable instead of modifying the outer one — unless we explicitly say otherwise.

This is where nonlocal comes in. By declaring a variable as nonlocal, we tell Python: “This variable is not local to this function — it belongs to the nearest enclosing function, and I want to modify that one.”

For example, imagine an outer function that defines a variable called count, and an inner function that increments count. Without nonlocal, Python throws an error because it thinks count is a local variable that’s being used before assignment. When we add nonlocal count, Python correctly links the variable to the outer function and allows the update.

So conceptually:

Without nonlocal → inner function creates a new local variable

With nonlocal → inner function modifies the outer function’s variable

It’s important to understand how nonlocal is different from global.
The global keyword refers to variables defined at the module level, accessible everywhere.
The nonlocal keyword refers to variables defined in the nearest enclosing function, not the global scope.

That means:

global → works with module-level variables

nonlocal → works with function-level outer variables

Another key point is that nonlocal only works with nested functions. If there is no enclosing function, using nonlocal will result in an error. Also, the variable must already exist in the enclosing scope — you cannot create a new variable using nonlocal.

In real-world usage, nonlocal is commonly seen in closures, decorators, and stateful functions, where an inner function needs to remember or update some state across multiple calls without using global variables. This helps keep code clean, modular, and safer.

To summarize for interviews:
The nonlocal keyword allows an inner function to modify a variable from its enclosing function’s scope. It solves scope conflicts in nested functions, supports closures, and avoids unnecessary use of global variables. Knowing when to use nonlocal shows a strong understanding of Python’s scope and function behavior.