# 動画加工するだけ
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np


def make_movie():
    return


'''
-----使用例------
from models import combine_material,insert_text

input = ["movie/sample.mp4","movie/sample2.mp4","movie/sample.mp4"]
combine_material(input)  #=>output.mp4

font = 'C:\Windows\Fonts\meiryo.ttc'
fontsize = 64
fontcolor = (255, 255, 255, 0)
position = "bottom"
message = [['1text1',1,3,font,fontsize,fontcolor,position],
            ['22text22',3,6,font,80,fontcolor,"center"],
            ['333text333',6,10,font,36,(100,100,100,0),"bottom"],]
input = "movie/sample.mp4"
insert_text(input,message,output="output.mp4")  #=>output.mp4
-----関数の説明------
combine_material(input,output)
 動画結合
 input:
  ファイル名のストリングの配列
  この配列順に結合される
  数に制限はしていない
 output:
  出力ファイル名(default:output.mp4)
insert_text(input,output,message)
 動画内にテキストを入れることができます。
 input:
  入力動画ファイル名
 output:
  出力動画ファイル名(default:output.mp4)
 message:
  ['入力テキスト',開始時間,終了時間,font,fontsize,fontcolor,position]の配列(配列の配列)
 font:パスを設定する
 position:"bottom"or"center"
-----現時点の問題点-----
[全体]
mp4ファイルしか対応していない
[combine_material]
動画1とfps,width,heightが一致していないと読み込めない
[insert_text]
フォントをダウンロードしなきゃいけない(opencvのフォントは日本語未対応)
秒数がかぶっていると先のものが優先される(2つの描画を同時にできない)
position増やす
'''


def combine_material(input, output='tmp/output.mp4'):
    # mp4指定(暫定)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # listの最初の動画から情報の取得しそれを全体の設定とする
    movie = cv2.VideoCapture(input[0])
    fps = movie.get(cv2.CAP_PROP_FPS)
    H = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    W = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
    #print(fps, int(W), int(H))
    # 出力先のファイルを作成
    out = cv2.VideoWriter(output, int(fourcc), fps, (int(W), int(H)))
    for name in input:
        material = cv2.VideoCapture(name)
        #print("reading "+ name)
        # 最初の1フレームを読み込む
        if material.isOpened() == True:
            ret, frame = material.read()
        else:
            ret = False
        # フレームの読み込みに成功している間フレームを書き出し続ける
        while ret:
            # 読み込んだフレームを書き込み
            out.write(frame)
            # 次のフレームを読み込み
            ret, frame = material.read()
    # data[file_infos] =　data[file_infos].append([{'name':'出力名'},{'path':'出力path'}]) とういう状態をコーダイが欲しい
    # views.pyで data[file_infos] = data[file_infos].append(combine_movie(data[file_infos]))で呼び出す
    return {'name': output, 'path': output}


def insert_text(input, message, output='output.mp4'):
    # input動画から情報の取得しそれを全体の設定とする
    movie = cv2.VideoCapture(input)
    Fs = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = movie.get(cv2.CAP_PROP_FPS)
    W = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))
    H = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # mp4指定(暫定)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    step = 1

    # outputファイルの作成
    out = cv2.VideoWriter(output, fourcc, int(fps / step), (W, H))
    ext_index = np.arange(0, Fs, step)

    j = 0  # messageの番号
    section = message[j]
    # section[0]:text:"string"
    # section[1]:start
    # section[2]:end
    # section[3]:font
    # section[4]:fontsize:int
    # section[5]:fontcolor:(255, 255, 255, 0)
    # section[6]:position:"center"or"bottom"
    for i in range(Fs):
        # print(i)
        flag, frame = movie.read()
        check = i == ext_index
        time = i / int(fps/step)
        if flag == True:
            if True in check:
                if section[1] <= time <= section[2]:
                    font_path = section[3]
                    font_size = section[4]
                    font = ImageFont.truetype(font_path, font_size)
                    frame = Image.fromarray(frame)
                    draw = ImageDraw.Draw(frame)
                    w, h = draw.textsize(section[0], font)
                    # position決め打ち(左右は現時点では真ん中のみ)
                    if section[6] == "bottom":
                        position = (int((W - w) / 2),
                                    int(H - (font_size * 1.5)))
                    if section[6] == "center":
                        position = (int((W - w) / 2), int((H - h) / 2))
                    draw.text(position, section[0], font=font, fill=section[5])
                    frame = np.array(frame)
                elif section[1] > time:
                    pass
                else:
                    if j >= len(message) - 1:
                        pass
                    else:
                        j = j + 1
                        section = message[j]
                out.write(frame)
            else:
                pass
        else:
            pass
    return output
