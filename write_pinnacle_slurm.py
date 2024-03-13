#! /usr/bin/env python3

job_name = input('Job name:')
partition = input('Partition needed:')
nodes = input('Nodes needed:')
node_type = input('Node type:')
time_needed = input('Time needed: (HH:MM:SS)')

print('#!/bin/bash')
print('#SBATCH --job-name=' + job_name)
print('#SBATCH --partition', partition)
print('#SBATCH --nodes=' + nodes)
print('#SBATCH --qos', node_type)
print('#SBATCH --tasks-per-node=32')
print('#SBATCH --time=' + time_needed)
print('#SBATCH -o ' + job_name + '%j.out')
print('#SBATCH -e ' + job_name + '%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=matayad@uark.edu')
print()
print('module purge')
print()
print("#job command here")
