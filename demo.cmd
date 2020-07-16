@echo off
python read_problem.py %1
construction_hurestic.exe
python read_output.py
