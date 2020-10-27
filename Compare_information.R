#比较wos和Scopus中的信息
wos2<-read.table("D:/output_wos2.txt",sep = "\t",quote = "\"\'",fill = T)
scopus2<-read.table("D:/output_scopus2.txt",sep = "\t",quote = "\"\'",fill = T,fileEncoding = "UTF-8")

#转化为小写
wos2v2<-apply(matrix(wos2$V2,ncol = 1), 1, function(x) tolower(x))
scopus2v2<-apply(matrix(scopus2$V2,ncol = 1), 1, function(x) tolower(x))
#在WOS里有但是Scopus里没有
index1<-!(wos2v2 %in% scopus2v2)
res1<-wos2[index1,]
#在Scopus里有但是WOS里没有
index2<-!(scopus2v2 %in% wos2v2)
res2<-scopus2[index2,]
score1<-c()
score2<-c()
#匹配影响因子IF
ifscore<-read.csv("JournalHomeGrid.txt","sep = "\t")
score<-paste("[",ifscore$2,"]",sep="")

for(i in 1:dim(res1)[1]){
index11<-which(res1$V3[i]==score)
if(length(index11)!=0){
score1<-c(score1,score[index11])
}else{
score1<-c(score1,"")
}
}

for(i in 1:dim(res2)[1]){
index22<-which(res2$V3[i]==score)
if(length(index22)!=0){
score2<-c(score2,score[index22])
}else{
score2<-c(score2,"")
}
}
res1<-cbind(res1,score1)
res1<-cbind(res2,score2)
write.csv(res1,"D:/scopus_meiyou.csv")
write.csv(res2,"D:/wos_meiyou.csv")
