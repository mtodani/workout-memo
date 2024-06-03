import os
import csv


class FileManager:
    """ファイルを読み書きする処理を静的メソッドにしてまとめたクラス
       静的メソッドを使うことで、インスタンスを作成せずにクラスから直接呼び出せるようにしてある
    """
    @staticmethod
    def save_to_text(file_path, data):
        """テキストファイルに書き込む"""
        try:
            with open(file_path, 'w') as file:
                for list in data: #dataに入ってる、各リストを反復処理
                    # リストの各要素を、map関数を使ってstr型に変換し、joinメソッドによってカンマで区切り、文字列として書き込む。改行。
                    file.write(','.join(map(str, list)) + '\n')

            print("---------------------------------------------------")
            print(f"{file_path}にテキストファイルを保存しました。")
        except FileNotFoundError: #ファイル、ディレクトリがなかったときを除き
            print("----------------------------------")
            print("無効なパスです。")
            print("もう一度メニュに戻ります")



    @staticmethod
    def save_to_csv(file_path, data):
        """csvファイルに書き込む"""
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data) #dataに入っている各リストを１行１行書き込む

            print("---------------------------------------------------")
            print(f"{file_path}にcsvファイルを保存しました。")
        except FileNotFoundError: #ファイル、ディレクトリがなかった場合を除き
            print("----------------------------------")
            print("無効なパスです。")
            print("もう一度メニュに戻ります")


    @staticmethod
    def load_from_text(file_path):
        """指定されたパスのテキストファイルを読み込み、返すメソッド"""
        if os.path.exists(file_path): #os.path モジュールを使用して、指定されたファイルが指定ディレクトリに存在するかどうかをチェック
            with open(file_path, 'r') as file:
                data = file.readlines() #readlinesメソッドを使って、ファイルの各行をリストの要素として読み込み、リスト型としてdataに格納。
            return data
        else: #指定されたファイルが指定ディレクトリに存在しない場合
            return None #None=何もないを返す
            

    @staticmethod
    def load_from_csv(file_path):
        """指定されたパスのcsvファイルを読み込み、返すメソッド"""

        if os.path.exists(file_path): #os.path モジュールを使用して、指定されたファイルが指定ディレクトリに存在するかどうかをチェック
            with open(file_path, 'r') as file:
                reader = csv.reader(file) # csv.readerオブジェクトを作成
                data = [gyo for gyo in reader]  #各行はリストとして、dataリストに格納
            return data
        else: #指定されたファイルが指定ディレクトリに存在しない場合
            return None #None=何もないを返す
           

