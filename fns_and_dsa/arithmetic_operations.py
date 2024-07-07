def perform_operation(num1, num2, operation):
  """
  Performs basic arithmetic operations based on the provided parameters.

  Args:
      num1: First number (float).
      num2: Second number (float).
      operation: String representing the desired operation ('add', 'subtract', 'multiply', or 'divide').

  Returns:
      The result of the arithmetic operation or a message for division by zero.
  """
  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    if num2 == 0:
      return "Error: Cannot divide by zero"
    else:
      return num1 / num2
  else:
    return "Invalid operation"

# Example usage (uncomment for testing)
# result = perform_operation(5, 6, 'add')
# print(result)
