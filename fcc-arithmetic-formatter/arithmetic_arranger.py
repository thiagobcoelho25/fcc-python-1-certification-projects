def arithmetic_arranger(arg1,arg2 = False):
  topRow = ""
  bottomRow = ""
  lineRow = ""
  sumRow = ""

  #Error for too many problems
  if len(arg1) > 5:
    return "Error: Too many problems."

  for problem in arg1:
    sep = problem.split(" ")
    num = sep[0]
    den = sep[2]
    operator = sep[1]

    if not num.isnumeric() or not den.isnumeric():
      return "Error: Numbers must only contain digits."
    if len(num) > 4 or len(den) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    length = max(len(num),len(den))
    
    if operator == "+" or operator == "-":
      topRow = topRow + 2*" " + " "*(length - len(num))+ num + 4*" "
      bottomRow = bottomRow + operator + " " + " "*(length - len(den)) + den + 4*" "
      lineRow = lineRow + 2*"-" + "-"*length + 4*" "
    else:
      return "Error: Operator must be '+' or '-'."
    
    if arg2 == True:
      result = 0
      if operator == "+":
        result = int(num) + int(den)
      else:
        result = int(num) - int(den)
      sumRow = sumRow  +" "*((length + 2) - len(str(result))) + str(result) + "    "
  
  return topRow.rstrip() + "\n" + bottomRow.rstrip() + "\n" + lineRow.rstrip() if not arg2 == True else topRow.rstrip() + "\n" + bottomRow.rstrip() + "\n" + lineRow.rstrip() + "\n" + sumRow.rstrip()
