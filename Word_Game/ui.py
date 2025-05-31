import tkinter as tk #tkinter toolkit interface, UI: user interface
from logic import get_question, check_answer #문제출제, 정답확인 불러오기

#Game app을 구성하는 클래스입니다.
class WordGameApp:
    def __init__(self,root):
        self.level = "easy" #초기 난이도 설정
        self.word,self.meaning = get_question(self.level) # 단어퀴즈를 하나 가져옵니다.
        #####나머지 구성은 다음시간에.


     #실제로 앱을 실행하는 함수입니다.
def run_app():
        root = tk.Tk() #Tkinter의 루트 윈도우를 생성합니다.
        root.title("AI 단어 학습게임") #윈도우 제목을 설정합니다.    
        app = WordGameApp(root) #WordGameApp 클래스의 인스턴스를 생성합니다.
        root.mainloop() #Tkinter 이벤트 루프를 시작합니다.
     