Just a simple tool to check if some HMM profiles are present in a bunch of fasta files.

# usuage

```
usage: hmmvis [-h] [--hmm HMM] [--fasta_dir FASTA] [--output_dir OUT]
              [--use_query] [--colorful] [--version]

optional arguments:
  -h, --help         show this help message and exit
  --hmm HMM          path to hmm file
  --fasta_dir FASTA  path to folder where .fasta files are located
  --output_dir OUT   path to output folder
  --use_query        use query id insead of accession
  --colorful         use colors for heatmap
  --version          show program's version number and exit
```

e.g. ` hmmvis/hmmvis --hmm example/example.hmm --fasta_dir example/faa/ --use_query --colorful`

# output
![alt text](heatmap.png "example heatmap")

# installation

```
git clone https://github.com/philippmuench/hmmvis.git
cd hmmvis
python setup.py install
```

you also need dependencies: `prodigal` and `hmmer` and want to use `virtualenv`

# licence
GNU General Public License, version 3 (GPL-3.0)


# cite
this script is part of the PlasmidMiner toolkit. If you use this script please cite:

```
Muench et al., A method for the in silico detection of plasmid fragments in environmental samples
```
