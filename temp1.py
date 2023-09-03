# DNA Sequencing of the Unknown Virus

for Proteins_unknown in SeqI0.parse('E:/Thesis Documents/Fasta files/Hepatitis C.fasta', "fasta"): 
 print("\n\nUnknown ID:",Proteins_unknown.id)
 print("Seq: ",Proteins_unknown.seq)
 print("Length: ",len(Proteins_unknown))

count_nucleotides_unk={
 'G of unk':unk.count("G"), 
 'A of unk':unk.count("A"),
 'T of unk':unk.count("T"), 
 'C of unk':unk.count("C")
}
G_of_unk = unk.count("G") 
A_of_unk = unk.count("A") 
T_of_unk = unk.count("T") 
C_of_unk = unk.count("C") 
GC_of_unk = (100*float(unk.count("G")+unk.count("C"))/len(unk))
