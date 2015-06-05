# Download every 25th BAM file from Swift, convert them into SAM format,
# and store them in HDFS.

BAMFILES=$(swift list GenomeData | grep -v .bam. | awk 'NR % 25 == 0')
for BAMFILE in $BAMFILES; do
  SAMFILE=$(echo $BAMFILE | sed 's/.bam/.sam/g')
  swift download GenomeData $BAMFILE --output - | samtools view - | hdfs dfs -put - /seqdata/$SAMFILE
done
