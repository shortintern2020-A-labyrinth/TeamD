# 動画加工するだけ
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np

'''
-----使用例------
from models import combine_material
input = ["movie/sample.mp4","movie/sample2.mp4","movie/sample.mp4"]
combine_material(input)  #=>output.mp4
-----説明---------
combine_material(input,output)
 動画結合
 input:
  ファイル名のストリングの配列
  この配列順に結合される
  数に制限はしていない
 output:
  出力ファイル名(default:output.mp4)
-----現時点の問題点-----
mp4ファイルしか対応していない
動画1とfps,width,heightが一致していないと読み込めない
'''
def combine_material(input,output='output.mp4'):
    # mp4指定(暫定)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # listの最初の動画から情報の取得しそれを全体の設定とする
    movie = cv2.VideoCapture(input[0])
    fps = movie.get(cv2.CAP_PROP_FPS)
    H = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    W  = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
    #print(fps, int(W), int(H))
    # 出力先のファイルを作成
    out = cv2.VideoWriter(output, int(fourcc), fps, (int(W), int(H)))
    for name in input:
        material = cv2.VideoCapture(name)
        #print("reading "+ name)
        # 最初の1フレームを読み込む
        if material.isOpened() == True:
            ret,frame = material.read()
        else:
            ret = False
        # フレームの読み込みに成功している間フレームを書き出し続ける
        while ret:
            # 読み込んだフレームを書き込み
            out.write(frame)
            # 次のフレームを読み込み
            ret,frame = material.read()
    return
