import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

species = ["A. besseyi", "A. bicaudatus", "A. fujianensis", "B. xylophilus", "D. destructor", 
             "D. dipsaci", "G. pallida", "G. rostochiensis", "H. glycines", "H. schachtii", 
             "M. arenaria", "M. chitwoodi", "M. enterolobii", "M. floridensis", 
             "M. graminicola", "M. hapla", "M. incognita", "M. javanica"]
genome_size = [46759715, 46428382, 143834322, 74561461, 111138200, 227234012,
               123625196, 92682755, 157978452, 179246932, 258067405, 47477280,
               240054310, 96673063, 38184958, 53017507, 183531997, 235798407]
gene_duplications = [1554, 1331, 7771, 4304, 2330, 11231, 4509, 6718, 7549, 
                     12948, 14849, 1810, 7806, 3615, 1073, 2186, 3988, 13915]
categories = ["Diploid"] * 10 + ["Polyploid", "Diploid", "Polyploid", "Diploid", 
                                 "Diploid", "Diploid", "Polyploid", "Polyploid"]

genome_size_mbp = [i / 1e6 for i in genome_size]

data = pd.DataFrame({
    'GenomeSizeMbp': genome_size_mbp,
    'GeneDuplications': gene_duplications,
    'Species': species,
    'Ploidy': categories
})

plt.figure(figsize=(10, 8))
sns.scatterplot(
    x='GenomeSizeMbp', 
    y='GeneDuplications', 
    hue='Ploidy', 
    data=data, 
    palette={'Diploid': 'blue', 'Polyploid': 'orange'}, 
    s=50,
    edgecolor='black'
)

sns.regplot(
    x='GenomeSizeMbp', 
    y='GeneDuplications', 
    data=data, 
    scatter=False, 
    line_kws={'color': 'brown'}
)

for i in range(len(data)):
    plt.text(
        x=data['GenomeSizeMbp'][i] + 1.5,
        y=data['GeneDuplications'][i], 
        s=data['Species'][i], 
        fontsize=10,
        color='black'
    )

plt.grid(True)
plt.ylim(bottom=0, top=16000)
plt.title('Genome Size vs. Gene Duplications', fontsize=14)
plt.xlabel('Genome Size (Mbp)', fontsize=12)
plt.ylabel('Number of Gene Duplications', fontsize=12)
plt.legend(title='Ploidy', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()