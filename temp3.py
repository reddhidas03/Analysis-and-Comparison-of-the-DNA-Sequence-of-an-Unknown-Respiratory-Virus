# Comparison & Similarities

comp_1=str(ifz)==str(unk) 
comp_2=str(cov)==str(unk) 
print("\n\nCompare with Influenza(H1N1): ",comp_1)
print("Compare with Covid(SARS-COV2): ",comp_2)

inf_unk = pairwise2.align.globalxx(ifz, unk, one_alignment_only=True, score_only=True) 
print('\n\nInfLuenza/Unknown Similarity (%):', inf_unk / len(Proteins_unknown.seq) * 100)

cov_unk = pairwise2.align.globalxx(cov, unk, one_alignment_only=True, score_only=True)
print('covid/Unknown Similarity (%):', cov_unk / len(seq_recd3.seq) * 100)

i_u= (inf_unk / len(Proteins_unknown.seq) * 100) 
c_u=(cov_unk / len(seq_recd3.seq) * 100)

# Plots & Table	
 
plt.figure(1)
plt.bar(count_nucleotides_ifz.keys(),count_nucleotides_ifz.values (),width=0.2,color=['b','r','y','g']) 
plt.figure(2)
plt.bar(count_nucleotides_cov.keys(),count_nucleotides_cov.values(),width=0.2,color= ['b','r','y','g']) 
plt.figure(3)
plt.bar(count_nucleotides_unk.keys(),count_nucleotides_unk.values(),width=0.2,color= ['b','r','y','g'])

X = ['GC % of Influenza(H1N1)', 'GC % of Covid(SARS-COV2) ', 'GC % of unknown'] 
Y = [GC_of_ifz/ 100 * 100, GC_of_cov/100 * 100, GC_of_unk/100 * 100]
plt.figure(4)
plt.title('GC (%) Comparison')
plt.bar(X,Y,color=(0.6, 0.4, 0.3, 0.5))

A = ['Influenza(H1N1) & Unknown', 'SARS-COV2 & Unknown'] 
B = [i_u, c_u]
plt.figure(5)
plt.title('Similarities (%)')
plt.bar(A,B,color=(0.2, 0.4, 0.6, 0.6))

table=pd.DataFrame(
 {
 'String' :['G','A','T','C','GC%','Amino Acid length','Total Functional Proteins'],
 'Influenza(H1N1)' :[G_of_ifz,A_of_ifz,T_of_ifz,C_of_ifz,GC_of_ifz,len(Amino_Acid_ifz), len(functional_proteins_ifz)], 
 'Covid(SARS-COV2)' : [G_of_cov,A_of_cov,T_of_ifz,C_of_cov,GC_of_cov,len(Amino_Acid_cov),len(functional_proteins_corona)], 
 'Unknown' : [G_of_unk,A_of_ifz,T_of_unk,C_of_unk,GC_of_unk,len(Amino_Acid_unk),len(functional_proteins_unk)]
 }
 )
print("\n\n",table)
