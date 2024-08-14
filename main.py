import re
import math
from js import document

def setup_calculator():
    def display(value):
        document.getElementById('display').innerText = value

    def append(value):
        display_value = document.getElementById('display').innerText
        
        # Remove the initial "0" if it exists and the new value is not an operator or parenthesis
        if display_value == '0' and value not in ('+', '-', '*', '/', ')'):
            display(value)
        else:
            display(display_value + value)
        
        update_equals_button()

    def clear():
        display('0')
        update_equals_button()

    def calculate(equation):
        # Convert '^' to '**' for exponentiation
        equation = equation.replace('^', '**')
        
        # Handle 'sqrt' by replacing it with 'math.sqrt'
        equation = re.sub(r'sqrt\(([^)]+)\)', r'math.sqrt(\1)', equation)
        
        try:
            # Evaluate the equation
            result = eval(equation, {"math": math})
            # Round the result to avoid floating-point precision issues
            result = round(result, 10)
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"

    def calculate_result(event):
        equation = document.getElementById('display').innerText
        if equation == '0':
            return
        result = calculate(equation)
        display(result)

    def update_equals_button():
        equation = document.getElementById('display').innerText
        # Enable the "=" button only if there's at least one operator
        has_operator = any(op in equation for op in ('+', '-', '*', '/'))
        equals_button = document.getElementById('buttonEquals')
        equals_button.disabled = not has_operator

    # Bind functions to buttons
    def bind_buttons():
        document.getElementById('button1').onclick = lambda e: append('1')
        document.getElementById('button2').onclick = lambda e: append('2')
        document.getElementById('button3').onclick = lambda e: append('3')
        document.getElementById('buttonPlus').onclick = lambda e: append('+')
        document.getElementById('button4').onclick = lambda e: append('4')
        document.getElementById('button5').onclick = lambda e: append('5')
        document.getElementById('button6').onclick = lambda e: append('6')
        document.getElementById('buttonMinus').onclick = lambda e: append('-')
        document.getElementById('button7').onclick = lambda e: append('7')
        document.getElementById('button8').onclick = lambda e: append('8')
        document.getElementById('button9').onclick = lambda e: append('9')
        document.getElementById('buttonMultiply').onclick = lambda e: append('*')
        document.getElementById('button0').onclick = lambda e: append('0')
        document.getElementById('buttonDot').onclick = lambda e: append('.')
        document.getElementById('buttonDivide').onclick = lambda e: append('/')
        document.getElementById('buttonPow').onclick = lambda e: append('^')
        document.getElementById('buttonSqrt').onclick = lambda e: append('sqrt(')
        document.getElementById('buttonOpenParen').onclick = lambda e: append('(')
        document.getElementById('buttonCloseParen').onclick = lambda e: append(')')
        document.getElementById('buttonClear').onclick = lambda e: clear()
        document.getElementById('buttonEquals').onclick = calculate_result

    bind_buttons()

    # Initial update of the equals button state
    update_equals_button()

# Run the setup function when PyScript is ready
setup_calculator()
