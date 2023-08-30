## Solutions to the Advanced Exercises

### DPLL I
A=True, B=False, C=True

### DPLL II
All but 	A=False, B=True, C=True, D=False make it satisfiable

### System Statements

The options to consider: 
- Multiuser state (M) or not
- Normal operation (N) or not 
- Kernel functioning (K) or not
- Interrupt mode (I) or not

Have the following statements, now listed in the opposite direction: 
- The system is not in interrupt mode, so ¬I. 
- If the system is not in multiuser state, then it is in interrupt mode, so ¬M ⇒ I. 
- Either the the kernel is not functioning or the system is in interrupt mode, so ¬K ∨ I. 
- If the system is operating normally, the kernel is functioning, so N ⇒ K. 
- The system is in a multiuser state if and only if it is operating normally, so M ⇔ N. 

From statement 1, we have that ¬I. Combined with 2, this entails M, since ¬M would entail I. Now also bringing in 5, M entails N. Now bringing in 4, N entails K. Combining instead 1 and 3, there must be ¬K. Cannot have both K and ¬K, so the statements are **not consistent**. 

### Validity
In short, the statement is **valid**.


[Move back to Medium Logic Exercises](https://github.com/UMdecisionsupport/DecisionSupport2023/blob/main/Logic/Medium.md)
