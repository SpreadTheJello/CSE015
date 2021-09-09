from logic import TruthTable

# Declare all turth tables
modusPonens = TruthTable(['p', 'q'], ['(p -> q)', '(p -> q) and p', '((p -> q) and p) -> q'])
modusTollens = TruthTable(['p', 'q'], ['-q', 'p -> q', '-q and (p -> q)', '-p', '(-q and (p -> q)) -> -p'])
hypoSyllogism = TruthTable(['p', 'q', 'r'], ['(p -> q)', '(q -> r)', '((p -> q) and (q -> r))', '(p -> r)', '((p -> q) and (q -> r)) -> (p -> r)'])
disSyllogism = TruthTable(['p', 'q'], ['(p or q)', '-p', '(p or q) and -p', '((p or q) and -p) -> q'])
addition = TruthTable(['p', 'q'], ['(p or q)', 'p -> (p or q)'])
simplification = TruthTable(['p', 'q'], ['(p -> q)', '(p -> q) and p', '((p -> q) and p) -> q'])
conjunction = TruthTable(['p', 'q'], ['((p) and (q))', '(p and q)', '((p) and (q)) -> (p and q)'])
resolution = TruthTable(['p', 'q', 'r'], ['(p or q)', '-p', '(-p or q)', '((p or q) and (-p or q))', '(q or r)', '((p or q) and (-p or q)) -> (q or r)'])

# Ask for rule of inference
table = input("Enter the name of the rule of inference, ex: Modus Ponens. \n To display all, type: \"ALL\" \n")
table = table.upper()

# return users rule of inference requested
if table == "MODUS PONENS":
    print("\nModus Ponens")
    print("((p → q) ∧ p) → q\n")
    modusPonens.display()

elif table == "MODUS TOLLENS":
    print("\nModus Tollens")
    print("(¬q ∧ (p → q)) → ¬p\n")
    modusTollens.display()

elif table == "HYPOTHETICAL SYLLOGISM":
    print("\nHypothetical Syllogism")
    print("((p → q) ∧ (q → r)) → (p → r)\n")
    hypoSyllogism.display()

elif table == "DISJUNCTIVE SYLLOGISM":
    print("\nDisjunctive Syllogism")
    print("((p ∨ q) ∧ ¬p) → q)\n")
    disSyllogism.display()

elif table == "ADDITION":
    print("\nAddition")
    print("(p → (p ∨ q)\n") 
    addition.display()

elif table == "SIMPLIFICATION":
    print("\nSimplification")
    print("((p → q) ∧ p) → q\n")
    simplification.display()

elif table == "CONJUNCTION":
    print("\nConjunction")
    print("((p) ∧ (q)) → (p ∧ q) → q\n")
    conjunction.display()

elif table == "RESOLUTION":
    print("\nResolution")
    print("((p ∨ q) ∧ (¬p ∨ r)) → (q ∨ r)\n")
    resolution.display()

elif table == "ALL":
    print("\nModus Ponens")
    print("((p → q) ∧ p) → q\n")
    modusPonens.display()
    print("\nModus Tollens")
    print("(¬q ∧ (p → q)) → ¬p\n")
    modusTollens.display()
    print("\nHypothetical Syllogism")
    print("((p → q) ∧ (q → r)) → (p → r)\n")
    hypoSyllogism.display()
    print("\nDisjunctive Syllogism")
    print("((p ∨ q) ∧ ¬p) → q)\n")
    disSyllogism.display()
    print("\nAddition")
    print("(p → (p ∨ q)\n") 
    addition.display()
    print("\nSimplification")
    print("((p → q) ∧ p) → q\n")
    simplification.display()
    print("\nConjunction")
    print("((p) ∧ (q)) → (p ∧ q) → q\n")
    conjunction.display()
    print("\nResolution")
    print("((p ∨ q) ∧ (¬p ∨ r)) → (q ∨ r)\n")
    resolution.display()

else:
    print("Invalid rule of inference input.")
