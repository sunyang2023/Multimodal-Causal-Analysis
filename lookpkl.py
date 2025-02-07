import pickle

# 加载 .pkl 文件
file_path = r'C:\Users\孙阳\Downloads\abide.pkl'
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# 查看数据的类型和内容（根据数据结构可能需要不同的方式）
# print(type(data))  # 查看数据类型
print(data)  # 打印数据内容（如果是字典或列表等结构，输出将是较为清晰的）
