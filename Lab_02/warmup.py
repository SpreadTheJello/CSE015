from logic import TruthTable

print("a ∧ ¬b\n")
firstTable = TruthTable(['a', 'b'], ['-b', 'a and -b'])
firstTable.display()
print("\n\n")
print("(a ∧ b) ∨ ¬c\n")
secondTable = TruthTable(['a', 'b', 'c'], ['(a and b)', '-c', '(a and b) or -c'])
secondTable.display()