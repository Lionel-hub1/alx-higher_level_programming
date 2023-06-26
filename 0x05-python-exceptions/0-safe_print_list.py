def safe_print_list(my_list=[], x=0):
  """
  Prints x elements of a list.

  Args:
    my_list: The list to print.
    x: The number of elements to print.

  Returns:
    The real number of elements printed.
  """

  real_len = 0
  try:
    for i in range(x):
      print(my_list[i], end="")
      real_len += 1
  except IndexError:
    pass
  print()
  return real_len
