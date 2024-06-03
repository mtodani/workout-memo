from strength_exercise import StrengthExercise
from cardio_exercise import CardioExercise
from file_manager import FileManager


class App:
    """アプリの基本的な操作をまとめたクラス"""

    def __init__(self):
        """筋トレデータと有酸素運動データを格納するリストを空で初期化"""
        self.strength_exercises = []  
        self.cardio_exercises = []

    def add_strength_exercise(self, date, exercise_name, weight, reps, sets, memo):
        """筋トレデータを自分自身に追加するメソッド"""
        kintore_data = StrengthExercise(date, exercise_name, weight, reps, sets, memo) #インスタンス化
        self.strength_exercises.append(kintore_data) #オブジェクトをアペンド


    def add_cardio_exercise(self, date, exercise_name, jikan, memo):
        """有酸素データを自分自身に追加するメソッド"""
        yusanso_undo_data = CardioExercise(date, exercise_name, jikan, memo) #インスタンス化
        self.cardio_exercises.append(yusanso_undo_data) #オブジェクトをアペンド


    def display_all_exercises(self):
        """登録されいてるデータを表示させるメソッド"""
        print("-----------------------------------------")
        
        if not self.strength_exercises and not self.cardio_exercises:   #筋トレリストand有酸素運動リストが空だった場合
            print("登録データがありません")

        elif not self.strength_exercises:    #筋トレリストが空だった場合、有酸素運動のデータだけ表示させる
            print(f"有酸素運動データ:  計{len(self.cardio_exercises)}データ") #len関数でいくつデータがあるか表示
            for yusanso_undo in self.cardio_exercises:
                """特殊メソッド__str__によって、クラスCardioExerciseのインスタンスがprint関数で処理されたら、
                 __str__メソッド内の文字列表現がリターンされて、表示される"""
                print(yusanso_undo) 

        elif not self.cardio_exercises:   #有酸素運動リストが空だった場合、筋トレリストのデータだけ表示させる
            print(f"筋トレデータ:   計{len(self.strength_exercises)}データ") #len関数でいくつデータがあるか表示
            for kintore in self.strength_exercises:
                """特殊メソッド__str__によって、クラスStrengthExerciseのインスタンスがprint関数で処理されたら、
                 __str__メソッド内の文字列表現がリターンされて、表示される"""
                print(kintore)

        else:  #そのほか＝両方ともデータがあった場合、両方を表示
            print(f"筋トレデータ:   計{len(self.strength_exercises)}データ") #len関数でいくつデータがあるか表示
            for kintore in self.strength_exercises:
                """特殊メソッド__str__によって、クラスStrengthExerciseのインスタンスがprint関数で処理されたら、
                 __str__メソッド内の文字列表現がリターンされて、表示される"""
                print(kintore)

            print(f"有酸素運動データ:   計{len(self.cardio_exercises)}データ") #len関数でいくつデータがあるか表示
            for yusanso_undo in self.cardio_exercises:
                """特殊メソッド__str__によって、クラスCardioExerciseのインスタンスがprint関数で処理されたら、
                 __str__メソッド内の文字列表現がリターンされて、表示される"""
                print(yusanso_undo)


    def save_to_txtfile(self):
        """テキストファイルに保存するメソッド"""
        
        strength_data = []  #筋トレデータ用の空のリストを用意
        for kintore_data in self.strength_exercises: #self.strength_exercisesに入っている各オブジェクトを反復処理
            #用意した空のリストにオブジェクトの日付や種目名などをリストでアペンド。何の運動のデータか分かるように、先頭要素の”筋トレ”と追加
            strength_data.append(["筋トレ", kintore_data.date, kintore_data.exercise_name, kintore_data.weight, kintore_data.reps, kintore_data.sets,kintore_data.memo])

        cardio_data = []   #有酸素運動データ用の空のリストを用意
        for yusanso_undo_data in self.cardio_exercises: #self..cardio_exercisesに入っている各オブジェクトを反復処理
            #用意した空のリストにオブジェクトの日付や種目名などをリストでアペンド、何の運動のデータか分かるように、先頭要素の”有酸素”と追加
            cardio_data.append(["有酸素", yusanso_undo_data.date, yusanso_undo_data.exercise_name, yusanso_undo_data.undo_jikan, yusanso_undo_data.memo])
        
        #保存先パスを入力させる
        txt_hozansaki = input("テキストファイル保存先(拡張子.txtも入力)：")

        #保存先と保存するデータを別クラスで定義したメソッドに渡して、具体的な保存の処理を行なわせる
        FileManager.save_to_text(txt_hozansaki, strength_data + cardio_data)


    def save_to_csvfile(self):
        """CSVファイルに保存するメソッド"""

        strength_data = [] #筋トレデータ用の空のリストを用意
        #self.strength_exercisesに入っている各オブジェクトを反復処理
        for kintore_data in self.strength_exercises:
            #用意した空のリストにオブジェクトの日付や種目名などをリストでアペンド。何の運動のデータか分かるように、先頭要素の”筋トレ”と追加
            strength_data.append(["筋トレ", kintore_data.date, kintore_data.exercise_name, kintore_data.weight, kintore_data.reps, kintore_data.sets,kintore_data.memo])
      
        cardio_data = []   #有酸素運動データ用の空のリストを用意
        #self..cardio_exercisesに入っている各オブジェクトを反復処理
        for yusanso_undo_data in self.cardio_exercises:
            #用意した空のリストにオブジェクトの日付や種目名などをリストでアペンド、何の運動のデータか分かるように、先頭要素の”有酸素”と追加
            cardio_data.append(["有酸素", yusanso_undo_data.date, yusanso_undo_data.exercise_name, yusanso_undo_data.undo_jikan, yusanso_undo_data.memo])
        
        #保存先パスを入力させる
        csv_hozansaki = input("csvファイル保存先(拡張子.csvも入力)：")
        #保存先と保存するデータを別クラスで定義したメソッドに渡して、具体的な保存の処理を行なわせる
        FileManager.save_to_csv(csv_hozansaki, strength_data + cardio_data)



    def load_from_txt_file(self):
        """テキストファイルから読み込むメソッド"""
        txt_yomikomisaki = input("テキストファイル読込先：") 
        data = FileManager.load_from_text(txt_yomikomisaki) #指定されたパスのテキストファイルを読み込み、値を返すメソッドを呼び出す
       
        if data: #dataが空ではない場合、
            for youso in data: #data内の各要素を反復処理
                #strip()メソッドを使って、yousoの前後に余分な空白文字を（スペース、改行文字などがあった場合）取り除く、
                # splitメソッドを使ってyouso内をカンマで分け、結果をリスト型として格納。(それぞれの要素の型はこの段階ではstr型)
                lst = youso.strip().split(',')

                if lst[0] == '筋トレ': #lstの０番目が"筋トレ"だったら
                    #それぞれの要素を適した型に変換してから、筋トレデータを追加するメソッドに引数として渡す。
                    self.add_strength_exercise(lst[1], lst[2], float(lst[3]), int(lst[4]), int(lst[5]),lst[6])
                elif lst[0] == '有酸素': #partsの０番目が"有酸素"だったら
                    #それぞれの要素を適した型に変換してから、有酸素運動のデータを追加するメソッドに引数として渡す
                    self.add_cardio_exercise(lst[1], lst[2], float(lst[3]),lst[4])
            print("-----------------------------------------------------------------------------")
            print(f"{txt_yomikomisaki}からテキストファイルを読み込み、データに追加しました。")

        else: 
            print("-----------------------------------------")
            print("指定されたファイルがありません、または空です。")

    
    def load_from_csv_file(self):
        """csvファイルから読み込むメソッド"""
        csv_yomikomisaki = input("CSVファイル読込先：")
        data = FileManager.load_from_csv(csv_yomikomisaki) #指定されたパスのcsvファイルを読み込み、値を返すメソッドを呼び出す

        if data: #dataが空ではない場合、
            for lst in data: #data内の各リストの反復処理
                if lst[0] == '筋トレ': #lstの０番目が"筋トレ"だったら
                    #それぞれの要素を適した型に変換してから、筋トレデータを追加するメソッドに引数として渡す。
                    self.add_strength_exercise(lst[1], lst[2], float(lst[3]), int(lst[4]), int(lst[5]),lst[6])
                elif lst[0] == '有酸素': #partsの０番目が"有酸素"だったら
                    #それぞれの要素を適した型に変換してから、有酸素運動のデータを追加するメソッドに引数として渡す
                    self.add_cardio_exercise(lst[1], lst[2], float(lst[3]),lst[4])
            print("--------------------------------------------------------------------------")
            print(f"{csv_yomikomisaki}からCSVデータを読み込み、データに追加しました。")

        else:
            print("-----------------------------------------")
            print("指定されたファイルがありません、または空です。")
