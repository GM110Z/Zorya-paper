import sys
from http.client import IncompleteRead
from Bio import SeqIO
import csv
list_of_accession = []
with open (sys.argv[1], 'r', encoding='utf-8-sig') as csvfile:
    efetchin=csv.reader(csvfile, delimiter = ',')
    for row in efetchin:
        list_of_accession.append(str(row[0]))

for record in SeqIO.parse(sys.argv[2], 'fasta'):
    for x in list_of_accession:
        if x in record.id:
            print ('>' + record.id+ '\n' + record.seq, file=open('ZorB2-seqs.txt','a'))


#where sys.argv[1] is a list of protein IDs that you want to extract and sys.argv[2] is the multi fasta file containint all proteins that need to be filtered
