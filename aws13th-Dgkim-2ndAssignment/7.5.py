
def text_statistics(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)
    total_chars = sum(len(line) for line in lines)
    max_line_length = max(len(line) for line in lines)

    print(f"전체 줄 수: {total_lines}")
    print(f"전체 단어 수: {total_words}")
    print(f"전체 문자 수: {total_chars}")
    print(f"가장 긴 줄의 길이: {max_line_length}")

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("전체 줄 수\n")
    f.write("전체 단어 수 (split으로 분리)\n")
    f.write("전체 문자 수 (개행 포함)" + " 가장 긴 줄의 길이")
    f.write("가장 긴 줄의 길이")

file_path = "test.txt"  # 분석할 텍스트 파일 경로
text_statistics(file_path)
