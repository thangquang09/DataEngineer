text1 = """Hãy đóng vai một kỹ sư dữ liệu lớn (Big Data Engineering) có kinh nghiệm 5 năm về Data Engineer và kiến thức sâu rộng về Generative AI và đưa ra cho tôi bài giảng chi tiết, chính xác, dễ hiểu, nhiều ví dụ trực quan. Tôi sẽ cung cấp cho bạn transcript tiếng anh và bạn dùng nó làm ra bài giảng tiếng Việt đầy đủ và chi tiết. Đây là script:\n"""
text2 = """\nTôi sẽ rất vui nếu có các ví dụ thực tế trong bài giảng của bạn, đảm bảo các tiêu đề sẽ bắt đầu ở dạng subtitle ## và có đánh số từ 1"""

with open('transcript.txt', 'r') as f:
    transcript = f.read()

with open('transcript.txt', 'w') as f:
    final = text1+transcript+text2
    f.write(final)
