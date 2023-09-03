# DNA to PROTEIN of Unknown Virus

mRNA=unk.transcribe()
print("\n\nmRNA of Unknown : ",repr(mRNA)) 
print('Size : ',len(mRNA))
print("mRNA Seq: ",repr((mRNA)))

Amino_Acid_unk = mRNA.translate(table=1, cds=False) 
print('Amino Acid of unknown ',repr (Amino_Acid_unk))

print("Length of Amino Acid:",len(Amino_Acid_unk)) 
print("Length of Original mRNA:",len(mRNA))

Proteins_unk = Amino_Acid_unk.split('*')	# * is translated stop codon
df = pd.DataFrame(Proteins_unk)
df.describe()
print('\n\nTotaL proteins in Unknown:', len(df))

def conv(item): 
    return len(item)
def to_str(item): 
    return str(item)

df['sequence_str'] = df[0].apply(to_str)

df['Length'] = df[0].apply(conv)
df.rename(columns={0: "sequence"}, inplace=True)
df.head()# Takes only longer than 20
functional_proteins_unk= df.loc[df['Length'] >= 20]
print('TotaL functional proteins in Unknown:', len(functional_proteins_unk))

