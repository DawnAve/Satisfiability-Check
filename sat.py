#!/usr/bin/python3
import itertools
import sys

def is_satisfiable(clauses, assignment):
    for clause in clauses:
        if not any(assignment.get(literal.strip('~'), False) != literal.startswith('~') for literal in clause):
            return False
    return True

def solve_sat(clauses):
    atoms = sorted(set(lit.strip('~') for clause in clauses for lit in clause))

    for assignment in itertools.product([True, False], repeat=len(atoms)):
        assignment_dict = dict(zip(atoms, assignment))
        if is_satisfiable(clauses, assignment_dict):
            return 'satisfiable', ' '.join(f'{atom}={"T" if assignment_dict[atom] else "F"}' for atom in atoms)
    return 'unsatisfiable', ''

def main():
    clauses = [line.strip().split(',') for line in sys.stdin]
    result, solution = solve_sat(clauses)
    print(result, solution)

if __name__ == "__main__":
    main()
