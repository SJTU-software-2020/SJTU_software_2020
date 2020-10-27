rm(list = ls())
genePAV <- read.table('GenePAV.matrix.txt',header = T)
rownames(genePAV) <- genePAV[,1]
library(summarytools)
geneCount <- data.frame(rowSums(genePAV[,-1]))
geneCount$Gene <- rownames(geneCount)
geneCount <- merge(geneCount, genePAV, by="Gene")
colnames(geneCount)[2] <- 'Freq'
geneCount$Freq <- round(geneCount$Freq/453,3)
geneCount$Attribute <- factor(ifelse(geneCount$Freq==1, 'core', ifelse(geneCount$Freq > 0.9, 'soft-core', ifelse(geneCount$Freq < 0.05, 'rare','distributed'))))
geneCount_tofile <- geneCount[,c(1,2,ncol(geneCount))] 
write.csv(geneCount_tofile,file='pan-genome.csv', row.names = F)
## visualization
library(ggplot2)
library(ggsci)
df <- data.frame(type=c('core','soft-core','distributed','rare'),count=c(sum(geneCount$Attribute=='core'), sum(geneCount$Attribute=='soft-core'), sum(geneCount$Attribute=='distributed'), sum(geneCount$Attribute=='rare')))
pdf('./distribution.pdf',width = 10, height = 6)
ggplot(df, aes(x=factor(type, levels =c('core','soft-core','distributed','rare')) , y=count, fill = factor(type, levels =c('core','soft-core','distributed','rare'))))+geom_bar(stat = 'identity')+theme(legend.title=element_blank())+scale_fill_aaas()+labs(x='Gene Type')
dev.off()
# resistance gene
resistanceGene <- read.csv('manual_resistance_gene_24.csv', header = F)
colnames(resistanceGene)[2] <- 'Gene'
resistanceGene <- merge(resistanceGene, geneCount, by = 'Gene')
resistanceGene <- resistanceGene[,c(1,2,3,ncol(resistanceGene))]
colnames(resistanceGene)[2] <- 'Description'
write.table(resistanceGene, 'resistance_gene_in_pan-genome.txt',row.names = F, quote = F, col.names = T, sep = '\t')
# get sequence
library(AnnotationHub)
hub <- AnnotationHub()
query(hub,'Oryza_sativa')
rice <- hub[['AH80658']]
library(biomaRt)
mart <- useMart(biomart = "plants_mart", 'osativa_eg_gene', host = "plants.ensembl.org")
features <- getBM(attributes = c("ensembl_gene_id","entrezgene_id","description","chromosome_name","start_position", "end_position"), 
                  filters = c("ensembl_gene_id"), values = resistanceGene$Gene,mart = mart)
mart@biomart <- 'ENSEMBL_MART_ENSEMBL'
dna <- getSequence(id = features$ensembl_gene_id, type = "ensembl_gene_id", seqType = "gene_exon_intron", mart = mart)
write.table(dna,'./sequence.txt', col.names = F, row.names = F, quote = F, sep = '\t')
