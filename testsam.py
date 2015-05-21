import pysam

samfile = pysam.AlignmentFile('HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam', 'rb')
iter = samfile.fetch()

for obj in iter:
	print obj
