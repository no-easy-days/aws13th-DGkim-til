# 1
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

file_path = "test.txt"
text_statistics(file_path)

# 2
import os
from datetime import datetime

class Diary:
    def __init__(self,base_dir):
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def write_today_diary(self):
        today = datetime.today().strftime("%Y-%m-%d")
        filename = f"diary_{today}.txt"
        filepath = os.path.join(self.base_dir, filename)

        content = input("오늘의 일기를 입력하세요:\n")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"오늘 일기가 저장되었습니다: {filename}")

    def read_diary(self, date_str):
        filename = f"diary_{date_str}.txt"
        filepath = os.path.join(self.base_dir, filename)

        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                print(f"\n[{filename}] 내용:")
                print(f.read())
        else:
            print(f"{date_str} 날짜의 일기가 존재하지 않습니다.")

    def list_all_diaries(self):
        files = os.listdir(self.base_dir)
        diaries = [f for f in files if f.startswith("diary_") and f.endswith(".txt")]

        if diaries:
            print("\n 저장된 모든 일기 목록:")
            for d in sorted(diaries):
                print("-", d)
        else:
            print("아직 작성된 일기가 없습니다.")

my_diary = Diary("dairy")
while True:
        print("\n=== 간단한 일기장 ===")
        print("1. 오늘 일기 쓰기")
        print("2. 특정 날짜 일기 읽기")
        print("3. 모든 일기 목록 보기")
        print("4. 종료")

        choice = input("메뉴 선택: ")

        if choice == "1":
            my_diary.write_today_diary()
        elif choice == "2":
            date_str = input("읽을 날짜 입력 (YYYY-MM-DD): ")
            my_diary.read_diary(date_str)
        elif choice == "3":
            my_diary.list_all_diaries()
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

# 3
import os

def copy_file(source,destination):
    try:
        with open(source, 'rb') as f_s:
            with open(destination, 'wb') as f_d:
                while True:
                    chunk = f_s.read(4096)
                    if not chunk:
                        break
                    f_d.write(chunk)

        src_size = os.path.getsize(source)
        dest_size = os.path.getsize(destination)

        print(f"복사 완료: {source} → {destination}")
        print(f"원본 파일 크기: {src_size} bytes")
        print(f"복사본 파일 크기: {dest_size} bytes")

        if src_size == dest_size:
            print("파일 크기가 동일합니다. 복사 성공")
        else:
            print("파일 크기가 다릅니다. 복사 오류.")

    except Exception as e:
        print(f"복사 중 에러 발생: {e}")
        return False

with open('original.txt', 'w', encoding='utf-8') as f:
    f.write("테스트 파일입니다.\n" * 100)
    copy_file('original.txt', 'copied.txt')