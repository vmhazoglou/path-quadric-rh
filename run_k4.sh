#!/bin/bash
# k=3 (theory known) and k=4 (open) sequences; plain vs generic coefficients
for fam in x2p1 ell; do
  python3 k4_sequences.py $fam 3 5 5 1,1
  python3 k4_sequences.py $fam 3 5 5 1,2
  python3 k4_sequences.py $fam 4 5 5 1,1,1
  python3 k4_sequences.py $fam 4 5 5 1,2,3
  python3 k4_sequences.py $fam 4 7 4 1,1,1
  python3 k4_sequences.py $fam 4 7 4 1,2,3
done
echo ALLDONE
