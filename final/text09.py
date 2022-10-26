import jieba
text = open("C:\\Users\\周银\Desktop\\期末考试题目-21-学生\\期末考试题目-21-学生\\水浒传.txt",'r',encoding='utf-8')
txt = text.read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) >= 2:
        counts[word] = counts.get(word,0)+1
lis = sorted(counts.items(),key=lambda x:x[1],reverse=True)
print(lis[:10])










