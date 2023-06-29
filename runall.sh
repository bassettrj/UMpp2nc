#!/bin/bash

for f in ./myjob*
    do echo "Submitting $f job."
    sbatch $f
done

