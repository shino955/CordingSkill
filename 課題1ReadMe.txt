課題1 当たり判定


行10～
自機判定入力
課題PDFの入力例に倣い
「左上 x座標」「左上 y座標」「幅」 「高さ」
として入力
スペースを入れて1回で入力するが .split()によって分割されて
Mcoliというリストに格納

その後、計算しやすくする為
「幅」 「高さ」の代わりに「右下 x座標」「右下 y座標」
を後半に入れたMRectというリストを作成


行23～
敵機数を入力
Enemyに格納


行27～
敵機判定を入力
自機判定入力と同じように入力
スペースを入れて1回で入力するが .split()によって分割されて
Ecoliというリストに格納
これをEnemyの回数分だけ繰り返す為 Ecoli.append()によって分割、追加する

その後も自機と同じように計算しやすくする為に
「右下 x座標」「右下 y座標」
を後半に入れたERectというリストを作成
Enemyの分だけ二次元配列として格納
これによってERectの中にEnemyの数だけそれぞれの敵機の判定を入れられる


行44～
接触判定



