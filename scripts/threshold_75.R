table <- read_excel("~/Desktop/wormbase_parasite/species_Nematoda.xlsx")

#BUSCO protein completeness scores more than 75%
busco_protein_c <- as.numeric(gsub('"', '', as.character(unlist(table[, 10]))))

busco_more_75 <- busco_protein_c[!is.na(busco_protein_c) & busco_protein_c > 75]

#omark protein completeness scores more than 75%
omark <- as.numeric(gsub('"', '', as.character(unlist(table[, 21]))))

omark_more_75 <- omark[!is.na(omark) & omark > 75]

busco_table <- table[!is.na(busco_protein_c) & busco_protein_c > 75,]

#final table containing species with both BUSCO and omark values more than 75%
filtered_table <- table[!is.na(busco_protein_c) & busco_protein_c > 75 & !is.na(omark) & omark > 75, ]
