from exercise_super import Exercise

class StrengthExercise(Exercise):
    """筋トレデータのクラス、Exerciseクラスを継承"""
    def __init__(self, date, exercise_name, weight, reps, sets, memo): #属性を初期化
        super().__init__(date, exercise_name,memo) # 親クラスのコンストラクタを呼び出す
        self.weight = weight
        self.reps = reps
        self.sets = sets

    def __str__(self):  #このクラスのオブジェクトがprint()で呼び出されたら以下の文字列表現を返す
        return f"日付: {self.date}\n種目: {self.exercise_name}\n重量: {self.weight} kg\nレップ数: {self.reps}\nセット数: {self.sets}\n備考(メモ)：{self.memo}\n"
