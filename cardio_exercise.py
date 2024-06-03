from exercise_super import Exercise


class CardioExercise(Exercise):
    """有酸素運動データのクラス、Exerciseクラスを継承"""

    def __init__(self, date, exercise_name, undo_jikan, memo): #属性を初期化
        super().__init__(date, exercise_name,memo) # 親クラスのコンストラクタを呼び出す
        self.undo_jikan = undo_jikan

    def __str__(self): #このクラスのオブジェクトがprint()で呼び出されたら以下の文字列表現を返す
        return f"日付: {self.date}\n種目: {self.exercise_name}\n運動時間: {self.undo_jikan} 時間\n備考(メモ)：{self.memo}\n"
