from app import App


app = App() #クラスAppからappをインスタンス化


while True:
    print("----------MENU---------")
    print("1. 筋トレデータを追加")
    print("2. 有酸素運動データを追加")
    print("3. すべてのデータを表示")
    print("4. テキストファイルに保存")
    print("5. テキストファイルからデータを読み込んで追加する")
    print("6. CSVファイルに保存")
    print("7. CSVファイルからデータを読み込んで追加する")
    print("8. 終了")
    print("--------------------------------")

    
    choice = input("選択してください: ")


    if choice == "1":
        date = input("実施日を入力してください（YYYY-MM-DD）: ")
        exercise_name = input("種目を入力してください: ")
        while True:
            try:
                weight = float(input("重量を入力してください（kg）: "))
                reps = int(input("レップ数を入力してください: "))
                sets = int(input("セット数を入力してください: "))
                break  # 正しい数値が入力された場合、ループを抜ける
            except ValueError: #ValueErrorを除き
                print("-----------------------------------------------------------")
                print("再度正しい値（整数）で入力してください。")
                print("-----------------------------------------------------------")

        memo = input("備考(メモ)を入力してください: ")

        #筋トレデータを自分自身に追加するメソッドに入力したものを渡す
        app.add_strength_exercise(date, exercise_name, weight, reps, sets, memo)

        print("-----------------------------------------")
        print(f"{exercise_name}のデータが登録されました")


    elif choice == "2":
        date = input("実施年月日を入力してください（YYYY-MM-DD）: ")
        exercise_name = input("種目を入力してください: ")
        while True:
            try:
                undo_jikan = float(input("運動時間を入力してください（時間）: "))
                break
            except ValueError:
                print("数値で入力してください。")

        memo = input("備考(メモ)を入力してください: ")

        #有酸素データを自分自身に追加するメソッドに入力したものを渡す
        app.add_cardio_exercise(date, exercise_name, undo_jikan, memo)

        print("-----------------------------------------")
        print(f"{exercise_name}のデータが登録されました")

    elif choice == "3":
        #すべてのデータを表示
        app.display_all_exercises()

    elif choice == "4":
        #テキストファイルに保存
        app.save_to_txtfile()
        
    elif choice == "5":
        #テキストファイルからデータを読み込んで追加する
        app.load_from_txt_file() 

    elif choice == "6":
        #CSVファイルに保存
        app.save_to_csvfile()

    elif choice == "7":
        # CSVファイルからデータを読み込んで追加する
        app.load_from_csv_file()

    elif choice == "8":
        print("プログラムを終了します。")
        break #ループを抜ける

    else:
        print("-----------------------------------------")
        print("無効な選択です。再度選択をしてください。")

