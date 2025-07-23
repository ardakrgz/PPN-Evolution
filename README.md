# Genomic Structures and Phylogenetic Relationships of Plant-Parasitic Nematodes

## Project Summary

This project investigates genomic features and evolutionary relationships of plant-parasitic nematodes (PPNs), focusing on genome size, gene duplications, and parasitism mechanisms.

## Contents
- `Research_Project_Karagoz.pdf`: Full project report
- `scripts/`: Bash, R, and Python scripts for quality check, filtering, phylogenetic analysis, and statistical plots
- `data/`: Includes PPN protein FASTA files used in OrthoFinder for phylogenetic construction and the result file which was used in FigTree.
- `results/`: Output figures and an Excel file on thorough assembly information for each species.

## Databases
- NCBI genome database
- Euuropean Nucleotide Archive (EBI-ENA)
- UniProt

## Dependencies
- BUSCO v5.8.0
- OMAmer
- OMArk
- OrthoFinder v3.0.1b1
- R (>= 4.4.1)
- Python 3.12 with libraries `matplotlib`, `seaborn`, `pandas`
- MAFFT, DIAMOND (used by OrthoFinder)

## How to Reproduce
1. Run BUSCO and OMAmer/OMArk scripts on downloaded data.
2. Filter species with high-quality data using `filtering_species.R`.
3. Run OrthoFinder with protein sequences.
4. Use `correlation_plot.py` to generate genome size vs. gene duplication plot.

## Author
Arda Burak Karagoz - arda.karagoz@metu.edu.tr