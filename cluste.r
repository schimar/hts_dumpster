library(bla)

#############
directory <- "/home/mschilling/Desktop/boechera/vsearch/run/centroids/subc/"

files <- list.files(directory, pattern= "vsearch_ri*")

runinf <- list()
for (i in files){
    name <- paste("runinf", i, sep= "_")
    assign(name, read.


    runinf[i] <- readLines(i)


     
for(i in 1:6) { #-- Create objects  'r.1', 'r.2', ... 'r.6' --
    nam <- paste("r", i, sep = ".")
    assign(nam, 1:i)
}
     ls(pattern = "^r..$")






#############
# in ../lasio/vsearch/run/centroids/subc/

consNclust <- read.table("l105cons_nClust.txt", sep= ' ', header= T)

##
hist(consNclust$nClust, ylim= c(0, 500))

plot(consNclust$id, consNclust$nClust, type= 'l', pch= '+', xlab= "consensus id", ylab= "N clusters", cex= 1.4)

#hist(clust$V3, ylim= c(0, 500))

mrgd <- merge(clust, clust_cons, by="V1") 
table(mrgd$V2.x == mrgd$V2.y) # just checking if the two counts are actually the same

