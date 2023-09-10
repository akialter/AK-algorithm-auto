# HƯỚNG DẪN CÁCH CHẠY AUTO ARKNIGHTS CHẾ ĐỘ RECLAMATION ALGORITHM

## Chạy file exe luôn
Mình có úp link file exe ở đây: [link](https://drive.google.com/file/d/1oO76KwlxTtKdUEyVETvJPCggK3EAMOQU/view?usp=sharing)


Anh em chỉ việc tải về và chạy (lưu ý phải hoàn thành các bước dưới trước).

## Git clone về rồi tự chạy
Nếu anh em có python trên máy (hoặc không tin tưởng file exe của mình), thì clone repo này:

```https://github.com/akialter/AK-algorithm-auto.git```

Xong rồi cái hết các requirements:

```pip install -r requirements.txt```

Rồi chạy main.py thôi:

```python main.py```

## Giao diện

![image](https://github.com/akialter/AK-algorithm-auto/assets/117612624/ffc62f54-881c-4226-b99b-e10cbcd8d2f1)

**Thời gian click chuột:** thời gian giữa những lần click, để 1s là ok nhất.

**Thời gian đợi chuyển screen:** kiểu mấy animation lúc đổi qua các màn, mình để 7s thì code chạy ổn. Anh em máy yếu thì có thể để cao hơn.

**Thời gian đợi load game:** sau khi bắt đầu/kết thúc 1 màn thì nó sẽ load game hơi lâu, mình để 12s nhưng anh em có thể để cao hơn.

Thời gian mình để mặc định là khá ổn rồi, anh em ***không nên để thấp hơn*** mà chỉ nên để cao hơn nếu auto fail khi chạy trên máy anh em.

**Lặp lại bao nhiều lần:** mỗi lần chạy được 54 badges, mình cần 6000 badges thì khoảng 110 lần chạy, nhưng chạy hết sẽ rất lâu. Mình khuyên để 30-40 lần (tầm 4 tiếng chạy) tùy vào thời gian anh em treo máy.

## Setup phím trên giả lập
Auto này chỉ hoạt động trên LDPlayer vs Bluestack (mình đã test), mấy cái khác mình không chắc. Phím layout như sau:

![image](https://github.com/akialter/AK-algorithm-auto/assets/117612624/5cb7dc1d-e73a-40a6-a679-2dc3d4078053)

Mình sẽ úp clip hướng dẫn, nhưng cách import key layout như sau:

- LDPlayer: Anh em chỉ việc nhập code ```leidian0eca0285c5c5``` là xong.
- Bluestack: mình có để file ```AKautoBluestack.cfg``` trong repo, anh em tải về rồi import vô Bluestack.

