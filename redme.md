# keromin
## オタマミンをMIDIファイルで演奏します。
明和電機さんの光操作テルミン[OTAMAMIN](https://www.maywadenki.com/news/otamamin/)をMIDIファイルで自動演奏します。<BR>
![動いているところ](https://user-images.githubusercontent.com/111331376/209469582-38ec4a31-d50f-46d0-b875-d93cf964b1ad.png)<BR>
MIDIのNote番号をLEDの明度に変換しNeoPixel(WS2812)を光らせて、その光でオタマミンを演奏しています。<BR>
明度を調整すると音をチューニングすることができます。<BR>
[チューニングしていないサンプル](https://twitter.com/layer812/status/1606994241691213826)はこんな感じです。<br>
## つなぎ方
![つなぎ方](https://user-images.githubusercontent.com/111331376/209469383-a9894deb-25db-4bc3-97f0-7f5101352df0.png)<BR>
NeoPixelのGNDをPicoのGNDに、5VをVBUSに、dinをGP28につなぎます。<BR>
## 設定のしかた
1.Picoに[Circuit Python](https://circuitpython.org/board/raspberry_pi_pico/) をいれます。私は7.3.3を使いました。<BR>
2.[NeoPixelのライブラリ](https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel)をPicoのlibフォルダ以下に配置します。<BR>
  画面中段の青いアイコン「Download project bundle」より圧縮ファイルをダウンロードし、下位フォルダのlib以下のmpyを使います。<BR>
3.[Adafruit Midiのライブラリ](https://learn.adafruit.com/grand-central-usb-midi-controller-in-circuitpython/code-usb-midi-in-circuitpython)をPicoのlibフォルダ以下に配置します。<BR>
  画面中段の青いアイコン「Download project bundle」より圧縮ファイルをダウンロードし、下位フォルダの「adafruit_midi」フォルダをフォルダごと使います。<BR>
4.code.pyを修正し、Picoに保存します。<BR>
  接続するPico側のPinに合わせて、pixel_pin = board.GP28の「GP28」部分を変更します。<BR>
  お使いになるNeoPixelのLED数に合わせてnum_pixels = 28の「28」部分を修正します。20個より少ないLED数のNeoPixelで動かす場合は改造が必要です。<BR>
## 使い方
設定を行ったPicoをUSBでPC(Windows)に接続すると、USB MIDIデバイスとして「Circuit Python Audio」が現れます。<BR>
![デバイスの見え方](https://user-images.githubusercontent.com/111331376/209470443-88edd61b-821b-4d68-b8c4-f85fc5867476.png)<BR>
お好きなMIDIプレイヤーでMIDIファイルを演奏してください。私は[mid radio](https://download.music-eclub.com/)を使っています。(デバイスが表示されないときは管理者モードで起動します。)<BR>
点灯するNeoPixelの上にオタマミンを並べてください。歌います。<BR>
## 制限
 - すべてのMIDIファイルには対応していません。
 - LEDを点灯させるMIDIのChは1～4チャネルです。変更したい場合はin_channel=(0,1,2,3)を修正してください。
 - 本記事内容及びプログラムを使用したことにより発生する、いかなる損害も補償しません。

## Thanks to
 - [明和電機](https://www.maywadenki.com/news/otamamin/) インスピレーションの宝石箱。
 - [楽しくやろう。](https://blog.boochow.com/) やりたいことを検索するといつも最初にヒットします！
 - [YAMAHAさん](https://download.music-eclub.com/)MID RADIO使いやすい、ありがとう。

## ライセンス
 [Apache License v2.0](http://www.apache.org/licenses/LICENSE-2.0)に基づいてご利用ください。ご連絡は[layer8](https://twitter.com/layer812)までお願いします。
