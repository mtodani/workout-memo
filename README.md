# フィットネストラッカー

このリポジトリには、さまざまな種類のエクササイズと筋肉トレーニングを記録するためのPythonスクリプトが含まれています。


## ファイル一覧

- **main.py**: アプリケーションのメインエントリーポイントです。さまざまなモジュールの実行を調整し、全体のワークフローを管理します。
- **app.py**: アプリケーションの主要な機能を実装しています。ユーザーの入力を処理し、フィットネストラッカーの動作を管理します。
- **cardio_exercise.py**: ランニング、サイクリングなどの有酸素運動に特化した機能を定義しています。
- **exercise_super.py**: 異なる種類のエクササイズに共通する機能を提供するスーパークラスです。他のエクササイズクラスはこのクラスを継承します。
- **file_manager.py**: データファイルの読み書きなどのファイル操作を管理します。
- **strength_exercise.py**: ウエイトリフティングなどの筋力エクササイズに特化した機能を定義しています。