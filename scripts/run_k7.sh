#!/bin/bash
cd "$(dirname "$0")"
for p in 61 73; do
 for c in 1,-1,1,-1,1,-1 1,2,5,3,4,6 1,-1,1,-1,2,3 2,3,1,-1,1,-1 1,-1,2,-2,1,-1 1,-1,3,-3,1,-1; do
  for m in 3 5 4; do python3 halves_general.py $p ell 7 $m $c; done
 done
done
echo K7DONE
