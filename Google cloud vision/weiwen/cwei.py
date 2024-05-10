from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file(file_path):
    """读取文件并返回内容"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_similarity(text1, text2):
    """计算并返回两段文本的余弦相似度"""
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

# 读取文件
text1 = read_file('cdwei.txt')
text2 = read_file('dwei.txt ')

# 计算相似度
similarity = calculate_similarity(text1, text2)
print(f"文本相似度为: {similarity:.2f}")

def read_file(file_path):
    """读取文件并返回内容"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_similarity(text1, text2):
    """计算并返回两段文本的余弦相似度"""
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

# 读取文件
text1 = read_file('cswei.txt')
text2 = read_file('swei.txt ')

# 计算相似度
similarity = calculate_similarity(text1, text2)
print(f"文本相似度为: {similarity:.2f}")