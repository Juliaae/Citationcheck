
# author: zhutongtong time:2020/10/16

@@用途：爬取引用核查文献及文献具体信息，如卷、期、页、出版商等，并将WOS与Scopus引用结果进行初步比较。
@@输出文件解释：
1.output_scopus1.txt
Scopus数据库收录的2018-2019年发表在GENOMICS PROTEOMICS & BIOINFORMATICS上的文章及文献具体信息，列依次为题目、出版商、卷、期、页、出版年份、引用次数。
2.output_scopus2.txt
Scopus数据库引用了2018-2019年发表在GENOMICS PROTEOMICS & BIOINFORMATICS上的文章的文章，列依次为被引用题目，题目、出版商、卷、期、页、出版年份、引用次数。
3.output_wos1.txt
WOS数据库收录的2018-2019年发表在GENOMICS PROTEOMICS & BIOINFORMATICS上的文章及文献具体信息，列依次为题目、出版商、卷、期、页、出版年份、引用次数。
4.output_wos2.txt
WOS数据库引用了2018-2019年发表在GENOMICS PROTEOMICS & BIOINFORMATICS上的文章的文章，列依次为被引用题目，题目、出版商、卷、期、页、出版年份、引用次数。
5.scopus_meiyou.csv
在WOS中被引用但是在Scopus中未被引用的文章，列名同上。
6.wos_meiyou.csv
在Scopus中被引用但是在WOS中未被引用的文章，列名同上。
@@NOTE
1.由于title字母大小写及其它格式错误难以避免会导致数据冗余，请手动删除此类行。只需要与对应的output文件进行比对即可，不需要打开网页逐条查找。
2.输入网址需提前按需求做好筛选，并排好顺序。
3.爬虫使用python，不要关闭命令行打开的浏览器，否则程序终止，也不用点击；矩阵比较时调用R。


