# Author: Sarthak Singh sxs666@psu.edu
# Collaborator: axa6168@psu.edu Anthony Aguilar
# Collaborator: Justin Maines jtm5948@psu.edu
# Collaborator: Maurizio Hazoury mbh5817@psu.edu


temp = float(input("Enter temperature: "))
unit = (input("Enter unit in F/f or C/c: "))

if unit== "c" or unit=="C":
  fTemp = (temp*(9/5) ) + 32
  print(f"{temp}° in Celsius is equivalent to {fTemp}° Fahrenheit.")

elif unit=="f" or unit=="F":
  cTemp = (temp-32) * (5/9)
  print(f"{temp}° in Fahrenheit is equivalent to {cTemp}° Celsius.")
else:
  print(f"Invalid unit({unit}).")