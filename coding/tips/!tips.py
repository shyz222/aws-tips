# 実行時間の目安
# 制限時間が1sの場合、
# 10**6　余裕を持って間に合う
# 10**7　おそらく間に合う
# 10**8　非常にシンプルな処理でない限り厳しい

# 浮動小数点の出力
# https://code-graffiti.com/print-format-with-string-in-python/#toc2
print('浮動小数点数の表示: %.2f' %(3.141592))
print('浮動小数点数の表示: %.5f' %(3.141592))
print('浮動小数点数の表示: %1.2f' %(3.141592))
print('浮動小数点数の表示: %1.0f' %(3.141592))
print('浮動小数点数の表示: %1.5f' %(3.141592))
print('浮動小数点数の表示: %10.2f' %(3.141592))
print('浮動小数点数の表示: %20.2f' %(3.141592))
# 浮動小数点数の表示: 3.14
# 浮動小数点数の表示: 3.14159
# 浮動小数点数の表示: 3.14
# 浮動小数点数の表示: 3
# 浮動小数点数の表示: 3.14159
# 浮動小数点数の表示:       3.14
# 浮動小数点数の表示:                 3.14

# in演算子の計算量
# https://takeg.hatenadiary.jp/entry/2019/06/02/172831
# リスト list O(n)
# タプル tuple O(n)
# 集合 set O(1)
# 辞書 dict O(1)

# list/dequeの計算量
# https://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb
# list.insert() O(n)
# deque.appendleft() O(n)