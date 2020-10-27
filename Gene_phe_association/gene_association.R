# 1. Read the origin data
# 1) genePAV table
data <- read.table("D:\\SJTU\\igem\\3Krice-pav\\GenePAV.matrix.txt",
                     header = TRUE, check.names = FALSE)
# 2) phenotype
pheno <- read.table("D:\\SJTU\\igem\\phe\\phe\\rice_453_flag_leaf_angle.phe")
pheno <- read.table("D:\\SJTU\\igem\\phe\\phe\\rice_453_grain_length.phe")
pheno <- read.table("D:\\SJTU\\igem\\phe\\phe\\rice_453_grain_weight.phe")
pheno <- read.table("D:\\SJTU\\igem\\phe\\phe\\rice_453_grain_width.phe")
pheno <- read.table("D:\\SJTU\\igem\\phe\\phe\\rice_453_height.phe")
pheno <- read.table("D:\\SJTU\\igem\\phe\\phe\\rice_453_leaf_angle.phe")
pheno <- read.table("D:\\SJTU\\igem\\phe\\phe\\rice_453_leaf_length.phe")
pheno <- read.table("D:\\SJTU\\igem\\phe\\phe\\rice_453_leaf_width.phe")
pheno <- na.omit(pheno)
# 3) intersection
rowname <- as.character(pheno$V1)
colname <- colnames(data)
new <- data[,which(colname %in% c(rowname,"Gene"))]

# 2. Sequential matching
new_pheno <- pheno[order(pheno$V1),]
y <- as.matrix(new_pheno$V3)

# 3. output
mynew <- data.frame(t(new),stringsAsFactors = F)

write.table(mynew,"D:\\SJTU\\igem\\3Krice-pav\\geneTable_flag_leaf_angle.txt",quote=FALSE,row.names = FALSE,col.names = FALSE)
write.table(y,"D:\\SJTU\\igem\\3Krice-pav\\label_flag_leaf_angle.txt",quote = FALSE,row.names = FALSE, col.names = FALSE)

write.table(mynew,"D:\\SJTU\\igem\\3Krice-pav\\geneTable_grain_length.txt",quote=FALSE,row.names = FALSE,col.names = FALSE)
write.table(y,"D:\\SJTU\\igem\\3Krice-pav\\label_grain_length.txt",quote = FALSE,row.names = FALSE, col.names = FALSE)

write.table(mynew,"D:\\SJTU\\igem\\3Krice-pav\\geneTable_grain_weight.txt",quote=FALSE,row.names = FALSE,col.names = FALSE)
write.table(y,"D:\\SJTU\\igem\\3Krice-pav\\label_grain_weight.txt",quote = FALSE,row.names = FALSE, col.names = FALSE)

write.table(mynew,"D:\\SJTU\\igem\\3Krice-pav\\geneTable_grain_width.txt",quote=FALSE,row.names = FALSE,col.names = FALSE)
write.table(y,"D:\\SJTU\\igem\\3Krice-pav\\label_grain_width.txt",quote = FALSE,row.names = FALSE, col.names = FALSE)

write.table(mynew,"D:\\SJTU\\igem\\3Krice-pav\\geneTable_height.txt",quote=FALSE,row.names = FALSE,col.names = FALSE)
write.table(y,"D:\\SJTU\\igem\\3Krice-pav\\label_height.txt",quote = FALSE,row.names = FALSE, col.names = FALSE)

write.table(mynew,"D:\\SJTU\\igem\\3Krice-pav\\geneTable_leaf_angle.txt",quote=FALSE,row.names = FALSE,col.names = FALSE)
write.table(y,"D:\\SJTU\\igem\\3Krice-pav\\label_leaf_angle.txt",quote = FALSE,row.names = FALSE, col.names = FALSE)

write.table(mynew,"D:\\SJTU\\igem\\3Krice-pav\\geneTable_leaf_length.txt",quote=FALSE,row.names = FALSE,col.names = FALSE)
write.table(y,"D:\\SJTU\\igem\\3Krice-pav\\label_leaf_length.txt",quote = FALSE,row.names = FALSE, col.names = FALSE)

write.table(mynew,"D:\\SJTU\\igem\\3Krice-pav\\geneTable_leaf_width.txt",quote=FALSE,row.names = FALSE,col.names = FALSE)
write.table(y,"D:\\SJTU\\igem\\3Krice-pav\\label_leaf_width.txt",quote = FALSE,row.names = FALSE, col.names = FALSE)
