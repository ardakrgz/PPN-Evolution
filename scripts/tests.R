#species <- c("A. besseyi", "A. bicaudatus", "A. fujianensis", "B. xylophilus", "D. destructor", 
#             "D. dipsaci", "G. pallida", "G. rostochiensis", "H. glycines", "H. schachtii", 
#             "M. arenaria", "M. chitwoodi", "M. enterolobii", "M. floridensis", 
#             "M. graminicola", "M. hapla", "M. incognita", "M. javanica")
species <- c( "M. arenaria", "M. enterolobii", "M. incognita", "M. javanica")
#genome_size <- c(46759715, 46428382, 143834322, 74561461, 111138200, 227234012,
#                 123625196, 92682755, 157978452, 179246932, 258067405, 47477280,
#                 240054310, 96673063, 38184958, 53017507, 183531997, 235798407)
genome_size <- c(258067405, 240054310, 183531997, 235798497)
#gene_duplications <- c(1554, 1331, 7771, 4304, 2330, 11231, 4509, 6718, 7549, 
#                       12948, 14849, 1810, 7806, 3615, 1073, 2186, 3988, 13915)
gene_duplications <- c(14849, 7806, 3988, 13915)

shapiro.test(genome_size)

shapiro.test(gene_duplications)

cor.test(genome_size, gene_duplications, method = "spearman")

