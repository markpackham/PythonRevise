# Import entire module called "greet.py"
import greet

greet.sayHello('Tim')

# Import a specific element from greet.py
from greet import sayGoodbye

sayGoodbye('Tom')