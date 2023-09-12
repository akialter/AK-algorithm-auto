# HƯỚNG DẪN CÁCH CHẠY AUTO ARKNIGHTS CHẾ ĐỘ RECLAMATION ALGORITHM

Video hướng dẫn nhanh: [link](https://www.youtube.com/watch?v=Vp98zE-LzTY)

## Chạy file exe luôn
Mình có úp link file exe ở đây: [link](https://drive.google.com/drive/folders/1bkYlfIhkb0Bj5QTXKXtDRTPUsXQD5L8W?usp=drive_link)

Anh em chỉ việc tải về và chạy (lưu ý phải hoàn thành các bước dưới trước).

## Git clone về rồi tự chạy (nếu không chạy exe ở trên)
Nếu anh em có python trên máy (hoặc không tin tưởng file exe của mình), thì clone repo này:

```https://github.com/akialter/AK-algorithm-auto.git```

Xong rồi cái hết các requirements:

```pip install -r requirements.txt```

Rồi chạy main.py thôi:

```python main.py```

## Giao diện

![image](https://github.com/akialter/AK-algorithm-auto/assets/117612624/e88e00ea-3b09-4865-8784-fd5d4be306e7)


**Thời gian click chuột:** thời gian giữa những lần click, để 1s là ok nhất.

**Thời gian đợi chuyển screen:** kiểu mấy animation lúc đổi qua các màn, mình để 7s thì code chạy ổn. Anh em máy yếu thì có thể để cao hơn.

**Thời gian đợi load game:** sau khi bắt đầu/kết thúc 1 màn thì nó sẽ load game hơi lâu, mình để 16s nhưng anh em có thể để cao hơn.

Thời gian mình để mặc định là khá ổn rồi, anh em ***không nên để thấp hơn*** mà chỉ nên để cao hơn nếu auto fail khi chạy trên máy anh em.

**Lặp lại bao nhiều lần:** mỗi lần chạy được 54 badges, mình cần 6000 badges thì khoảng 110 lần chạy, nhưng chạy hết sẽ rất lâu. Mình khuyên để 30-40 lần (tầm 4 tiếng chạy) tùy vào thời gian anh em treo máy.

## Setup phím trên giả lập
Auto này chỉ hoạt động trên LDPlayer vs Bluestack (mình đã test), mấy cái khác mình không chắc. Phím layout như sau:

![image](https://github.com/akialter/AK-algorithm-auto/assets/117612624/9ae22c9c-d550-4af8-b939-6886bea9341e)

Mình sẽ úp clip hướng dẫn, nhưng cách import key layout như sau:

- LDPlayer: Anh em chỉ việc nhập code ```leidian3944f422a25a``` là xong.
- Bluestack: mình có để file ```AKautoBluestack.cfg``` trong repo, anh em tải về rồi import vô Bluestack.


## Hướng dẫn
Bước 1: Chơi qua màn tutorial. Bấm thủ công ít nhất 1 lần để hiểu thao tác với lại load trước map (lần sau auto map load nhanh hơn). Link hướng dẫn của Arckhive nếu anh em chưa biết làm: [link](https://www.youtube.com/watch?v=V1HaBXQkh24)

Bước 2: Import keymap layout (ở trên) vô giả lập của anh em (LDPlayer hoặc Bluestack). Anh em có thể lên mạng coi hướng dẫn.

Bước 3: Mở app lên, vào màn hình như sau. Lần đầu cứ để thông số như mặc định. Lưu ý để game full màn hình:

![image](https://github.com/akialter/AK-algorithm-auto/assets/117612624/66104bdf-2d9b-4a5a-aa68-427eff2ee16d)

Bước 4: Bấm Run để chạy, ráng ngồi theo dõi nó chạy xem có bị lỗi gì không. Kiên nhẫn 1 chút. Nếu sau 1 thời gian cảm giác auto bị kẹt thì có thể nó bị hỏng. Tăng thời gian load game lên (theo mình thì đây thường là nguyên nhân chính).

Bước 5: Cứ để nó chạy thôi :). Rồi đi ngủ. Lưu ý giờ server reset đừng để auto chạy.

## Mẹo

- Nhớ để full màn hình!
- Chỉ nên chỉnh thời gian load, mấy cái kia nên giữ nguyên
- Auto được test ở độ phân giải 1600x900 trở lên, nếu thấp quá có thể auto không hoạt động.


