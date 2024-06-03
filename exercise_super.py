from abc import ABC, abstractmethod

class Exercise(ABC):
    """運動データの親クラス"""
    def __init__(self, date, exercise_name,memo): #子クラスで共通している属性を親クラスで初期化
        self.date = date
        self.exercise_name = exercise_name
        self.memo = memo

    @abstractmethod #__str__メソッドを抽象メソッドとする。子クラスに対してこのメソッドの実装を強制
    def __str__(self):
        pass

