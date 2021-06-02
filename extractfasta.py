#提取指定基因序列
from Bio import SeqIO
record_dict = SeqIO.index("2-12_ATTCCT_L006_R2_001.fasta","fasta")
seqfile = open("2-12_R2.fasta","w")
with open("readslist6.txt") as seqlist:
    #首行不能为空
    for seqname in seqlist.readlines():
        seqname = seqname.strip('\n')
        #去除\n
        target_seq = record_dict.get_raw(seqname).decode()
        seqfile.write(target_seq)

seqfile.close()
seqlist.close()
