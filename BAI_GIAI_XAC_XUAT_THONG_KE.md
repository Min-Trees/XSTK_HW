# BÀI GIẢI XÁC SUẤT THỐNG KÊ - TỰ LUẬN CHI TIẾT

---

## PHẦN MỞ ĐẦU: BỔ TÚC GIẢI TÍCH TỔ HỢP

### **BÀI 1:** Trong một buổi họp lớp, mỗi bạn bắt tay tất cả các bạn khác 1 lần. Người ta đếm được có tất cả 435 cái bắt tay. Hỏi có bao nhiêu bạn tham dự buổi họp lớp đó?

**GIẢI:**

**Bước 1: Phân tích bài toán**
- Mỗi cái bắt tay là sự kết hợp của 2 bạn
- Gọi n là số bạn tham dự buổi họp
- Số cái bắt tay = số cách chọn 2 bạn từ n bạn

**Bước 2: Lập phương trình**

Số cách chọn 2 bạn từ n bạn là:
$$C_n^2 = \frac{n!}{2!(n-2)!} = \frac{n(n-1)}{2}$$

Theo đề bài:
$$\frac{n(n-1)}{2} = 435$$

**Bước 3: Giải phương trình**

$$n(n-1) = 870$$
$$n^2 - n - 870 = 0$$

Giải phương trình bậc 2:
$$\Delta = 1 + 4 \times 870 = 3481 = 59^2$$

$$n = \frac{1 + 59}{2} = 30$$ (loại nghiệm âm)

**Đáp số:** Có **30 bạn** tham dự buổi họp lớp.

---

### **BÀI 2:** Một hộp gồm 20 bi (6 trắng, 4 đỏ và 10 xanh). Có bao nhiêu cách:

#### **a) Chọn 4 viên bi từ hộp?**

**GIẢI:**

Số cách chọn 4 viên bi từ 20 viên bi là:
$$C_{20}^4 = \frac{20!}{4! \times 16!} = \frac{20 \times 19 \times 18 \times 17}{4 \times 3 \times 2 \times 1} = \frac{116280}{24} = 4845$$

**Đáp số:** **4845 cách**

#### **b) Chọn 4 viên bi từ hộp, trong đó có ít nhất 1 bi đỏ?**

**GIẢI:**

**Cách 1: Tính trực tiếp**
- Có ít nhất 1 bi đỏ nghĩa là: 1 đỏ, 2 đỏ, 3 đỏ hoặc 4 đỏ

+ **1 đỏ, 3 bi khác:** $C_4^1 \times C_{16}^3 = 4 \times 560 = 2240$ cách
+ **2 đỏ, 2 bi khác:** $C_4^2 \times C_{16}^2 = 6 \times 120 = 720$ cách  
+ **3 đỏ, 1 bi khác:** $C_4^3 \times C_{16}^1 = 4 \times 16 = 64$ cách
+ **4 đỏ:** $C_4^4 = 1$ cách

Tổng: $2240 + 720 + 64 + 1 = 3025$ cách

**Cách 2: Phần bù (đơn giản hơn)**

Số cách chọn 4 bi không có bi đỏ nào (chỉ chọn từ 16 bi trắng và xanh):
$$C_{16}^4 = \frac{16 \times 15 \times 14 \times 13}{24} = 1820$$

Số cách chọn có ít nhất 1 bi đỏ:
$$4845 - 1820 = 3025$$

**Đáp số:** **3025 cách**

#### **c) Chọn ra 4 viên bi, trong đó số bi trắng nhiều hơn tổng số bi đỏ và xanh?**

**GIẢI:**

Số bi trắng nhiều hơn tổng số bi đỏ và xanh nghĩa là:
- Số bi trắng > 2 (vì tổng 4 bi)
- Có thể là: 3 trắng - 1 khác, hoặc 4 trắng

**TH1: 3 bi trắng, 1 bi khác (đỏ hoặc xanh)**
$$C_6^3 \times C_{14}^1 = 20 \times 14 = 280$$

**TH2: 4 bi trắng**
$$C_6^4 = 15$$

**Tổng:** $280 + 15 = 295$ cách

**Đáp số:** **295 cách**

---

### **BÀI 3:** Một lớp có 45 sinh viên, trong đó có 20 nam. Có bao nhiêu cách bầu ra ban cán sự lớp gồm 4 sinh viên thỏa mãn:

*Số nữ: 45 - 20 = 25*

#### **a) Có đúng 2 nam**

**GIẢI:**

Chọn 2 nam từ 20 nam và 2 nữ từ 25 nữ:
$$C_{20}^2 \times C_{25}^2 = \frac{20 \times 19}{2} \times \frac{25 \times 24}{2} = 190 \times 300 = 57000$$

**Đáp số:** **57000 cách**

#### **b) Ít nhất một nam**

**GIẢI:**

**Cách 1: Phần bù**

Tổng số cách chọn 4 SV bất kỳ: $C_{45}^4 = 148995$

Số cách chọn 4 SV toàn nữ: $C_{25}^4 = 12650$

Số cách có ít nhất 1 nam: $148995 - 12650 = 136345$

**Đáp số:** **136345 cách**

#### **c) Nhiều nhất 2 nam**

**GIẢI:**

Nhiều nhất 2 nam nghĩa là: 0 nam, 1 nam, hoặc 2 nam

+ **0 nam (4 nữ):** $C_{25}^4 = 12650$
+ **1 nam, 3 nữ:** $C_{20}^1 \times C_{25}^3 = 20 \times 2300 = 46000$
+ **2 nam, 2 nữ:** $C_{20}^2 \times C_{25}^2 = 190 \times 300 = 57000$

**Tổng:** $12650 + 46000 + 57000 = 115650$

**Đáp số:** **115650 cách**

---

### **BÀI 4:** Có 2 hộp. Hộp I đựng 10 bi (8 xanh, 2 đỏ). Hộp II đựng 20 bi (15 xanh, 5 đỏ).

#### **a) Có bao nhiêu cách lấy từ mỗi hộp ra 2 bi?**

**GIẢI:**

Từ hộp I lấy 2 bi: $C_{10}^2 = 45$ cách

Từ hộp II lấy 2 bi: $C_{20}^2 = 190$ cách

Tổng số cách (theo quy tắc nhân): $45 \times 190 = 8550$ cách

**Đáp số:** **8550 cách**

#### **b) Có bao nhiêu cách lấy từ mỗi hộp ra 2 bi sao cho có đúng 1 bi đỏ được lấy ra?**

**GIẢI:**

Đúng 1 bi đỏ có các trường hợp:
- 1 đỏ từ hộp I, 0 đỏ từ hộp II
- 0 đỏ từ hộp I, 1 đỏ từ hộp II

**TH1: 1 đỏ từ I (1 đỏ + 1 xanh), 2 xanh từ II**
$$C_2^1 \times C_8^1 \times C_{15}^2 = 2 \times 8 \times 105 = 1680$$

**TH2: 2 xanh từ I, 1 đỏ từ II (1 đỏ + 1 xanh)**
$$C_8^2 \times C_5^1 \times C_{15}^1 = 28 \times 5 \times 15 = 2100$$

**Tổng:** $1680 + 2100 = 3780$ cách

**Đáp số:** **3780 cách**

#### **c) Có bao nhiêu cách lấy từ mỗi hộp ra 2 bi sao cho có đúng 2 bi đỏ được lấy ra?**

**GIẢI:**

Có 3 trường hợp:
- 2 đỏ từ I, 0 đỏ từ II
- 1 đỏ từ I, 1 đỏ từ II  
- 0 đỏ từ I, 2 đỏ từ II

**TH1: 2 đỏ từ I, 2 xanh từ II**
$$C_2^2 \times C_{15}^2 = 1 \times 105 = 105$$

**TH2: 1 đỏ + 1 xanh từ I, 1 đỏ + 1 xanh từ II**
$$C_2^1 \times C_8^1 \times C_5^1 \times C_{15}^1 = 2 \times 8 \times 5 \times 15 = 1200$$

**TH3: 2 xanh từ I, 2 đỏ từ II**
$$C_8^2 \times C_5^2 = 28 \times 10 = 280$$

**Tổng:** $105 + 1200 + 280 = 1585$ cách

**Đáp số:** **1585 cách**

#### **d) Có bao nhiêu cách lấy từ mỗi hộp ra 2 bi sao cho có đúng 3 bi đỏ được lấy ra?**

**GIẢI:**

Có 2 trường hợp:
- 2 đỏ từ I, 1 đỏ từ II
- 1 đỏ từ I, 2 đỏ từ II

**TH1: 2 đỏ từ I, 1 đỏ + 1 xanh từ II**
$$C_2^2 \times C_5^1 \times C_{15}^1 = 1 \times 5 \times 15 = 75$$

**TH2: 1 đỏ + 1 xanh từ I, 2 đỏ từ II**
$$C_2^1 \times C_8^1 \times C_5^2 = 2 \times 8 \times 10 = 160$$

**Tổng:** $75 + 160 = 235$ cách

**Đáp số:** **235 cách**

#### **e) Có bao nhiêu cách lấy từ mỗi hộp ra 2 bi sao cho các bi lấy ra cùng màu?**

**GIẢI:**

Cùng màu có 2 trường hợp: tất cả xanh hoặc tất cả đỏ

**TH1: Tất cả 4 bi đều xanh**
$$C_8^2 \times C_{15}^2 = 28 \times 105 = 2940$$

**TH2: Tất cả 4 bi đều đỏ**
$$C_2^2 \times C_5^2 = 1 \times 10 = 10$$

**Tổng:** $2940 + 10 = 2950$ cách

**Đáp số:** **2950 cách**

---

## CHƯƠNG 1: KHÁI NIỆM CƠ BẢN VÀ CÔNG THỨC XÁC SUẤT

### **BÀI 1.1:** Một lớp có 50 sinh viên. Trong kỳ thi môn XSTK có 6 SV đạt giỏi, 20 SV đạt khá, 5 SV không đạt yêu cầu, các SV còn lại đạt trung bình. Gọi tên ngẫu nhiên 3 SV của lớp. Tìm xác suất gọi được:

*Phân tích: Số SV trung bình = 50 - 6 - 20 - 5 = 19*

#### **a) Ít nhất 1 SV đạt giỏi**

**GIẢI:**

**Bước 1: Xác định không gian mẫu**

Số cách gọi 3 SV từ 50 SV:
$$|\Omega| = C_{50}^3 = \frac{50 \times 49 \times 48}{6} = 19600$$

**Bước 2: Tính xác suất (dùng phần bù)**

Biến cố đối: Không có SV nào đạt giỏi (chọn 3 từ 44 SV còn lại)
$$C_{44}^3 = \frac{44 \times 43 \times 42}{6} = 13244$$

Xác suất không có SV giỏi:
$$P(\overline{A}) = \frac{13244}{19600} = \frac{3311}{4900}$$

Xác suất có ít nhất 1 SV giỏi:
$$P(A) = 1 - \frac{3311}{4900} = \frac{1589}{4900} \approx 0.3243$$

**Đáp số:** $P = \frac{1589}{4900} \approx 32.43\%$

#### **b) 2 SV đạt trung bình và 1 SV đạt khá**

**GIẢI:**

Số cách chọn 2 SV trung bình từ 19: $C_{19}^2 = 171$

Số cách chọn 1 SV khá từ 20: $C_{20}^1 = 20$

Số kết quả thuận lợi: $171 \times 20 = 3420$

Xác suất:
$$P(B) = \frac{3420}{19600} = \frac{171}{980} = \frac{9}{52} \approx 0.1745$$

**Đáp số:** $P = \frac{9}{52} \approx 17.45\%$

#### **c) Không quá 1 SV không đạt yêu cầu**

**GIẢI:**

Không quá 1 nghĩa là: 0 hoặc 1 SV không đạt yêu cầu

**TH1: 0 SV không đạt (chọn 3 từ 45 SV còn lại)**
$$C_{45}^3 = \frac{45 \times 44 \times 43}{6} = 14190$$

**TH2: 1 SV không đạt, 2 SV khác**
$$C_5^1 \times C_{45}^2 = 5 \times 990 = 4950$$

Tổng số kết quả thuận lợi: $14190 + 4950 = 19140$

Xác suất:
$$P(C) = \frac{19140}{19600} = \frac{957}{980} = \frac{159}{163.33...} \approx 0.9765$$

**Đáp số:** $P = \frac{957}{980} \approx 97.65\%$

---

### **BÀI 1.2:** Có hai hộp I và II. Trong đó, hộp I chứa 15 sản phẩm tốt và 5 phế phẩm. Hộp II chứa 8 sản phẩm tốt và 2 phế phẩm. Từ hộp I lấy ra 1 sản phẩm và từ hộp II lấy ra 2 sản phẩm. Tính xác suất để được:

#### **a) Cả 3 sản phẩm tốt**

**GIẢI:**

**Bước 1: Tính xác suất lấy được SP tốt từ hộp I**
$$P(I_{tốt}) = \frac{15}{20} = \frac{3}{4}$$

**Bước 2: Tính xác suất lấy được 2 SP tốt từ hộp II**
$$P(II_{2tốt}) = \frac{C_8^2}{C_{10}^2} = \frac{28}{45}$$

**Bước 3: Tính xác suất cả 3 SP tốt (các biến cố độc lập)**
$$P(A) = \frac{3}{4} \times \frac{28}{45} = \frac{84}{180} = \frac{7}{15} \approx 0.4667$$

**Đáp số:** $P = \frac{7}{15} \approx 46.67\%$

#### **b) Đúng 1 sản phẩm tốt**

**GIẢI:**

Có 2 trường hợp:
- 1 tốt từ I, 0 tốt từ II (2 phế từ II)
- 0 tốt từ I (1 phế từ I), 1 tốt từ II

**TH1: 1 tốt từ I, 2 phế từ II**
$$P_1 = \frac{15}{20} \times \frac{C_2^2}{C_{10}^2} = \frac{3}{4} \times \frac{1}{45} = \frac{1}{60}$$

**TH2: 1 phế từ I, 1 tốt + 1 phế từ II**
$$P_2 = \frac{5}{20} \times \frac{C_8^1 \times C_2^1}{C_{10}^2} = \frac{1}{4} \times \frac{16}{45} = \frac{4}{45}$$

**Tổng xác suất:**
$$P(B) = \frac{1}{60} + \frac{4}{45} = \frac{3}{180} + \frac{16}{180} = \frac{19}{180} \approx 0.1056$$

**Đáp số:** $P = \frac{19}{180} \approx 10.56\%$

#### **c) Ít nhất 2 sản phẩm tốt**

**GIẢI:**

Ít nhất 2 SP tốt nghĩa là: 2 tốt hoặc 3 tốt

**TH1: 3 SP tốt** (đã tính ở câu a)
$$P_{3tốt} = \frac{7}{15}$$

**TH2: Đúng 2 SP tốt**
- 1 tốt từ I, 1 tốt + 1 phế từ II
- 1 phế từ I, 2 tốt từ II

$$P_{2tốt}^{(1)} = \frac{15}{20} \times \frac{C_8^1 \times C_2^1}{C_{10}^2} = \frac{3}{4} \times \frac{16}{45} = \frac{12}{45} = \frac{4}{15}$$

$$P_{2tốt}^{(2)} = \frac{5}{20} \times \frac{C_8^2}{C_{10}^2} = \frac{1}{4} \times \frac{28}{45} = \frac{7}{45}$$

$$P_{2tốt} = \frac{4}{15} + \frac{7}{45} = \frac{12}{45} + \frac{7}{45} = \frac{19}{45}$$

**Tổng:**
$$P(C) = \frac{7}{15} + \frac{19}{45} = \frac{21}{45} + \frac{19}{45} = \frac{40}{45} = \frac{8}{9} \approx 0.8889$$

**Đáp số:** $P = \frac{8}{9} \approx 88.89\%$

---

### **BÀI 1.3:** Trong một hộp có 10 bóng đèn, trong đó có 2 bóng hỏng. Lấy ngẫu nhiên có thứ tự không hoàn lại 3 bóng để dùng. Tìm xác suất để:

#### **a) Lấy được cả 3 bóng đều tốt**

**GIẢI:**

**Bước 1: Số bóng tốt**
Số bóng tốt = 10 - 2 = 8

**Bước 2: Tính xác suất**

Lấy có thứ tự không hoàn lại:
- Bóng 1 tốt: $\frac{8}{10}$
- Bóng 2 tốt (còn 7 tốt trong 9): $\frac{7}{9}$
- Bóng 3 tốt (còn 6 tốt trong 8): $\frac{6}{8}$

$$P(A) = \frac{8}{10} \times \frac{7}{9} \times \frac{6}{8} = \frac{336}{720} = \frac{7}{15} \approx 0.4667$$

**Đáp số:** $P = \frac{7}{15} \approx 46.67\%$

#### **b) Lấy phải 2 bóng hỏng**

**GIẢI:**

Có 3 trường hợp xảy ra (vị trí 2 bóng hỏng):
- Hỏng - Hỏng - Tốt (HHT)
- Hỏng - Tốt - Hỏng (HTH)
- Tốt - Hỏng - Hỏng (THH)

**TH1: HHT**
$$P_1 = \frac{2}{10} \times \frac{1}{9} \times \frac{8}{8} = \frac{16}{720}$$

**TH2: HTH**
$$P_2 = \frac{2}{10} \times \frac{8}{9} \times \frac{1}{8} = \frac{16}{720}$$

**TH3: THH**
$$P_3 = \frac{8}{10} \times \frac{2}{9} \times \frac{1}{8} = \frac{16}{720}$$

**Tổng:**
$$P(B) = \frac{16}{720} + \frac{16}{720} + \frac{16}{720} = \frac{48}{720} = \frac{1}{15} \approx 0.0667$$

**Đáp số:** $P = \frac{1}{15} \approx 6.67\%$

---

### **BÀI 1.4:** Một công nhân đứng 3 máy. XS để trong 1 ca làm việc máy I hỏng là 0,1; máy II hỏng là 0,15 và máy III hỏng là 0,2. Tìm XS để trong ca làm việc:

**Cho:**
- $P(I_{hỏng}) = 0.1 \Rightarrow P(I_{tốt}) = 0.9$
- $P(II_{hỏng}) = 0.15 \Rightarrow P(II_{tốt}) = 0.85$
- $P(III_{hỏng}) = 0.2 \Rightarrow P(III_{tốt}) = 0.8$

#### **a) Cả 3 máy không hỏng**

**GIẢI:**

Các máy hoạt động độc lập:
$$P(A) = P(I_{tốt}) \times P(II_{tốt}) \times P(III_{tốt}) = 0.9 \times 0.85 \times 0.8 = 0.612$$

**Đáp số:** $P = 0.612 = 61.2\%$

#### **b) Có đúng 1 máy hỏng**

**GIẢI:**

Có 3 trường hợp:
- Máy I hỏng, II và III tốt
- Máy II hỏng, I và III tốt
- Máy III hỏng, I và II tốt

$$P_1 = 0.1 \times 0.85 \times 0.8 = 0.068$$
$$P_2 = 0.9 \times 0.15 \times 0.8 = 0.108$$
$$P_3 = 0.9 \times 0.85 \times 0.2 = 0.153$$

$$P(B) = 0.068 + 0.108 + 0.153 = 0.329$$

**Đáp số:** $P = 0.329 = 32.9\%$

#### **c) Có 2 máy không hỏng**

**GIẢI:**

2 máy không hỏng ⇔ 1 máy hỏng (giống câu b)

**Đáp số:** $P = 0.329 = 32.9\%$

#### **d) Ít nhất 1 máy không hỏng**

**GIẢI:**

**Cách 1: Phần bù**

Biến cố đối: Cả 3 máy đều hỏng
$$P(\text{cả 3 hỏng}) = 0.1 \times 0.15 \times 0.2 = 0.003$$

$$P(D) = 1 - 0.003 = 0.997$$

**Đáp số:** $P = 0.997 = 99.7\%$

---

### **BÀI 1.5:** Xác suất vi trùng kháng mỗi loại thuốc A, B, C lần lượt là: 5%, 10%, 15%. Nếu dùng cả 3 loại để diệt vi trùng. Tính xác suất vi trùng bị diệt (giả sử các loại thuốc độc lập nhau).

**GIẢI:**

**Bước 1: Phân tích**
- $P(\text{kháng A}) = 0.05 \Rightarrow P(\text{không kháng A}) = 0.95$
- $P(\text{kháng B}) = 0.10 \Rightarrow P(\text{không kháng B}) = 0.90$
- $P(\text{kháng C}) = 0.15 \Rightarrow P(\text{không kháng C}) = 0.85$

**Bước 2: Vi trùng bị diệt khi KHÔNG kháng ít nhất 1 loại thuốc**

Vi trùng KHÔNG bị diệt ⇔ Vi trùng kháng cả 3 loại:
$$P(\text{kháng cả 3}) = 0.05 \times 0.10 \times 0.15 = 0.00075$$

**Bước 3: Tính xác suất vi trùng bị diệt**
$$P(\text{bị diệt}) = 1 - 0.00075 = 0.99925$$

**Đáp số:** $P = 0.99925 = 99.925\%$

---

### **BÀI 1.6:** Có 2 hộp giống hệt nhau, mỗi hộp chứa 20 bi. Trong đó, hộp I gồm 15 bi đỏ và 5 bi trắng; hộp II gồm 12 bi đỏ và 8 bi trắng. Lấy ngẫu nhiên 1 hộp rồi từ hộp đó lấy ngẫu nhiên 4 bi.

#### **a) Tính xác suất lấy được 2 bi đỏ và 2 bi trắng**

**GIẢI:**

**Bước 1: Áp dụng công thức xác suất đầy đủ**

Gọi:
- $H_1$: chọn hộp I, $P(H_1) = \frac{1}{2}$
- $H_2$: chọn hộp II, $P(H_2) = \frac{1}{2}$
- A: lấy được 2 đỏ và 2 trắng

**Bước 2: Tính xác suất có điều kiện**

Nếu chọn hộp I:
$$P(A|H_1) = \frac{C_{15}^2 \times C_5^2}{C_{20}^4} = \frac{105 \times 10}{4845} = \frac{1050}{4845} = \frac{70}{323}$$

Nếu chọn hộp II:
$$P(A|H_2) = \frac{C_{12}^2 \times C_8^2}{C_{20}^4} = \frac{66 \times 28}{4845} = \frac{1848}{4845} = \frac{616}{1615}$$

**Bước 3: Áp dụng công thức xác suất đầy đủ**
$$P(A) = P(H_1) \times P(A|H_1) + P(H_2) \times P(A|H_2)$$
$$P(A) = \frac{1}{2} \times \frac{70}{323} + \frac{1}{2} \times \frac{616}{1615}$$
$$P(A) = \frac{1}{2} \times \frac{350}{1615} + \frac{1}{2} \times \frac{616}{1615} = \frac{1}{2} \times \frac{966}{1615} = \frac{483}{1615}$$

**Đáp số:** $P = \frac{483}{1615} \approx 0.2991 = 29.91\%$

#### **b) Giả sử đã được 2 bi đỏ và 2 bi trắng. Hỏi khả năng chọn được hộp nào cao hơn?**

**GIẢI:**

Áp dụng công thức Bayes:

$$P(H_1|A) = \frac{P(H_1) \times P(A|H_1)}{P(A)} = \frac{\frac{1}{2} \times \frac{70}{323}}{\frac{483}{1615}} = \frac{\frac{35}{323}}{\frac{483}{1615}}$$

$$P(H_1|A) = \frac{35}{323} \times \frac{1615}{483} = \frac{35 \times 5}{483} = \frac{175}{483} \approx 0.3623$$

$$P(H_2|A) = 1 - P(H_1|A) = 1 - \frac{175}{483} = \frac{308}{483} \approx 0.6377$$

**Kết luận:** Khả năng chọn được **hộp II cao hơn** (63.77% so với 36.23%)

**Đáp số:** Hộp II có khả năng cao hơn với $P(H_2|A) = \frac{308}{483} \approx 63.77\%$

---

### **BÀI 1.7:** Có 3 cửa hàng I, II, III cùng kinh doanh một loại sản phẩm. Tỷ lệ sản phẩm tốt trong 3 cửa hàng lần lượt là 80%, 85% và 75%. Một khách chọn ngẫu nhiên một cửa hàng và từ đó mua 1 sản phẩm.

#### **a) Tính xác suất để khách mua phải phế phẩm**

**GIẢI:**

**Bước 1: Xác định giả thuyết**
- $H_1$: Chọn CH I, $P(H_1) = \frac{1}{3}$, $P(\text{phế}|H_1) = 0.2$
- $H_2$: Chọn CH II, $P(H_2) = \frac{1}{3}$, $P(\text{phế}|H_2) = 0.15$
- $H_3$: Chọn CH III, $P(H_3) = \frac{1}{3}$, $P(\text{phế}|H_3) = 0.25$

**Bước 2: Công thức xác suất đầy đủ**
$$P(\text{phế}) = \sum_{i=1}^{3} P(H_i) \times P(\text{phế}|H_i)$$
$$P(\text{phế}) = \frac{1}{3}(0.2 + 0.15 + 0.25) = \frac{1}{3} \times 0.6 = 0.2$$

**Đáp số:** $P = 0.2 = 20\%$

#### **b) Giả sử khách mua phải 1 phế phẩm. Tính xác suất khách mua sản phẩm đó từ cửa hàng II**

**GIẢI:**

Áp dụng công thức Bayes:
$$P(H_2|\text{phế}) = \frac{P(H_2) \times P(\text{phế}|H_2)}{P(\text{phế})} = \frac{\frac{1}{3} \times 0.15}{0.2} = \frac{0.05}{0.2} = 0.25$$

**Đáp số:** $P = 0.25 = 25\%$

---

### **BÀI 1.8:** Có 2 hộp đựng cùng một loại thuốc. Hộp I gồm 8 lọ thuốc (có 3 lọ kém phẩm chất). Hộp II gồm 10 lọ thuốc (có 4 lọ kém phẩm chất). Từ hộp I lấy ngẫu nhiên 1 lọ bỏ sang hộp II, sau đó từ hộp II lấy ngẫu nhiên 2 lọ. Giả sử đã lấy được 1 lọ tốt và 1 lọ kém phẩm chất từ hộp II. Tính xác suất đã lấy được lọ thuốc tốt ở hộp I.

**GIẢI:**

**Bước 1: Xác định giả thuyết**
- $H_1$: Lấy lọ tốt từ I sang II (5 lọ tốt, 3 lọ kém)
  - $P(H_1) = \frac{5}{8}$
  - Hộp II lúc này: 7 tốt, 4 kém
  
- $H_2$: Lấy lọ kém từ I sang II  
  - $P(H_2) = \frac{3}{8}$
  - Hộp II lúc này: 6 tốt, 5 kém

**Bước 2: Tính xác suất có điều kiện**

Gọi A: Lấy được 1 tốt + 1 kém từ hộp II

$$P(A|H_1) = \frac{C_7^1 \times C_4^1}{C_{11}^2} = \frac{7 \times 4}{55} = \frac{28}{55}$$

$$P(A|H_2) = \frac{C_6^1 \times C_5^1}{C_{11}^2} = \frac{6 \times 5}{55} = \frac{30}{55}$$

**Bước 3: Tính P(A)**
$$P(A) = \frac{5}{8} \times \frac{28}{55} + \frac{3}{8} \times \frac{30}{55} = \frac{140 + 90}{440} = \frac{230}{440} = \frac{23}{44}$$

**Bước 4: Áp dụng công thức Bayes**
$$P(H_1|A) = \frac{P(H_1) \times P(A|H_1)}{P(A)} = \frac{\frac{5}{8} \times \frac{28}{55}}{\frac{23}{44}} = \frac{\frac{140}{440}}{\frac{230}{440}} = \frac{140}{230} = \frac{14}{23}$$

**Đáp số:** $P = \frac{14}{23} \approx 0.6087 = 60.87\%$

---

### **BÀI 1.9:** Có 2 hộp đựng bi, mỗi hộp chứa 10 bi. Trong đó, hộp I gồm 8 bi đỏ và 2 bi trắng; hộp II gồm 7 bi đỏ và 3 bi trắng. Lấy ngẫu nhiên từ hộp I 2 bi bỏ sang hộp II, sau đó, từ hộp II lấy ngẫu nhiên ra 4 bi. Tính xác suất để lấy được:

#### **a) 2 bi đỏ và 2 bi trắng từ hộp II**

**GIẢI:**

**Bước 1: Phân tích các trường hợp chuyển từ I sang II**

- $H_1$: Chuyển 2 đỏ từ I sang II
  - $P(H_1) = \frac{C_8^2}{C_{10}^2} = \frac{28}{45}$
  - Hộp II có: 9 đỏ, 3 trắng
  
- $H_2$: Chuyển 1 đỏ + 1 trắng từ I sang II
  - $P(H_2) = \frac{C_8^1 \times C_2^1}{C_{10}^2} = \frac{16}{45}$
  - Hộp II có: 8 đỏ, 4 trắng
  
- $H_3$: Chuyển 2 trắng từ I sang II
  - $P(H_3) = \frac{C_2^2}{C_{10}^2} = \frac{1}{45}$
  - Hộp II có: 7 đỏ, 5 trắng

**Bước 2: Tính xác suất có điều kiện**

Gọi A: Lấy 2 đỏ + 2 trắng từ hộp II

$$P(A|H_1) = \frac{C_9^2 \times C_3^2}{C_{12}^4} = \frac{36 \times 3}{495} = \frac{108}{495}$$

$$P(A|H_2) = \frac{C_8^2 \times C_4^2}{C_{12}^4} = \frac{28 \times 6}{495} = \frac{168}{495}$$

$$P(A|H_3) = \frac{C_7^2 \times C_5^2}{C_{12}^4} = \frac{21 \times 10}{495} = \frac{210}{495}$$

**Bước 3: Công thức xác suất đầy đủ**
$$P(A) = \frac{28}{45} \times \frac{108}{495} + \frac{16}{45} \times \frac{168}{495} + \frac{1}{45} \times \frac{210}{495}$$
$$P(A) = \frac{1}{22275}(28 \times 108 + 16 \times 168 + 1 \times 210)$$
$$P(A) = \frac{3024 + 2688 + 210}{22275} = \frac{5922}{22275} = \frac{1974}{7425} = \frac{658}{2475}$$

**Đáp số:** $P = \frac{658}{2475} \approx 0.2659 = 26.59\%$

#### **b) 1 bi đỏ và 3 bi trắng từ hộp II**

**GIẢI:**

Gọi B: Lấy 1 đỏ + 3 trắng từ hộp II

$$P(B|H_1) = \frac{C_9^1 \times C_3^3}{C_{12}^4} = \frac{9 \times 1}{495} = \frac{9}{495}$$

$$P(B|H_2) = \frac{C_8^1 \times C_4^3}{C_{12}^4} = \frac{8 \times 4}{495} = \frac{32}{495}$$

$$P(B|H_3) = \frac{C_7^1 \times C_5^3}{C_{12}^4} = \frac{7 \times 10}{495} = \frac{70}{495}$$

**Công thức xác suất đầy đủ:**
$$P(B) = \frac{28}{45} \times \frac{9}{495} + \frac{16}{45} \times \frac{32}{495} + \frac{1}{45} \times \frac{70}{495}$$
$$P(B) = \frac{1}{22275}(28 \times 9 + 16 \times 32 + 1 \times 70)$$
$$P(B) = \frac{252 + 512 + 70}{22275} = \frac{834}{22275} = \frac{278}{7425}$$

**Đáp số:** $P = \frac{278}{7425} \approx 0.0374 = 3.74\%$

#### **c) Lấy được 1 bi đỏ và 1 bi trắng từ hộp I, biết đã lấy được 2 bi đỏ và 2 bi trắng từ hộp II**

**GIẢI:**

Cần tìm $P(H_2|A)$ với A: lấy 2 đỏ + 2 trắng từ II

Áp dụng công thức Bayes:
$$P(H_2|A) = \frac{P(H_2) \times P(A|H_2)}{P(A)}$$

Từ câu a, ta có $P(A) = \frac{658}{2475}$

$$P(H_2|A) = \frac{\frac{16}{45} \times \frac{168}{495}}{\frac{658}{2475}} = \frac{\frac{2688}{22275}}{\frac{658}{2475}}$$

$$P(H_2|A) = \frac{2688}{22275} \times \frac{2475}{658} = \frac{2688}{22275} \times \frac{2475}{658} = \frac{2688 \times 2475}{22275 \times 658}$$

$$P(H_2|A) = \frac{2688}{658 \times 9} = \frac{2688}{5922} = \frac{448}{987}$$

**Đáp số:** $P = \frac{448}{987} \approx 0.4539 = 45.39\%$

---

### **BÀI 1.10:** Có 3 sinh viên làm bài thi một cách độc lập. Xác suất làm được bài của sinh viên I là 0,8; của sinh viên II là 0,7; và của sinh viên III là 0,5. Biết có ít nhất một sinh viên làm được bài, tính xác suất sinh viên III làm được bài.

**GIẢI:**

**Bước 1: Ký hiệu**
- $A_1$: SV I làm được, $P(A_1) = 0.8$
- $A_2$: SV II làm được, $P(A_2) = 0.7$
- $A_3$: SV III làm được, $P(A_3) = 0.5$
- B: Có ít nhất 1 SV làm được

**Bước 2: Tính P(B)**

$$P(\overline{B}) = P(\text{cả 3 đều không làm được}) = 0.2 \times 0.3 \times 0.5 = 0.03$$
$$P(B) = 1 - 0.03 = 0.97$$

**Bước 3: Tính $P(A_3 \cap B)$**

$A_3 \cap B$ nghĩa là SV III làm được và có ít nhất 1 SV làm được.

Vì SV III đã làm được rồi thì điều kiện "ít nhất 1 SV làm được" tự động thỏa mãn.

Do đó: $P(A_3 \cap B) = P(A_3) = 0.5$

**Bước 4: Tính xác suất có điều kiện**
$$P(A_3|B) = \frac{P(A_3 \cap B)}{P(B)} = \frac{0.5}{0.97} = \frac{50}{97} \approx 0.5155$$

**Đáp số:** $P = \frac{50}{97} \approx 51.55\%$

---

### **BÀI 1.11:** Có 10 hộp đựng các sản phẩm cùng loại, mỗi hộp chứa 20 sản phẩm. Trong đó, có 3 hộp loại I (mỗi hộp đựng 18 sản phẩm tốt và 2 phế phẩm); 5 hộp loại II (mỗi hộp đựng 16 sản phẩm tốt và 4 phế phẩm); và 2 hộp loại III (mỗi hộp đựng 14 sản phẩm tốt và 6 phế phẩm). Lấy ngẫu nhiên một hộp và từ hộp đó lấy ngẫu nhiên 4 sản phẩm.

#### **a) Tính xác suất lấy được cả 4 sản phẩm tốt**

**GIẢI:**

**Bước 1: Xác định giả thuyết**
- $H_1$: Chọn hộp loại I, $P(H_1) = \frac{3}{10}$
- $H_2$: Chọn hộp loại II, $P(H_2) = \frac{5}{10}$
- $H_3$: Chọn hộp loại III, $P(H_3) = \frac{2}{10}$

**Bước 2: Tính xác suất có điều kiện**

Gọi A: Lấy được 4 SP tốt

$$P(A|H_1) = \frac{C_{18}^4}{C_{20}^4} = \frac{3060}{4845} = \frac{68}{107}$$

$$P(A|H_2) = \frac{C_{16}^4}{C_{20}^4} = \frac{1820}{4845} = \frac{364}{969}$$

$$P(A|H_3) = \frac{C_{14}^4}{C_{20}^4} = \frac{1001}{4845} = \frac{143}{693}$$

**Bước 3: Công thức xác suất đầy đủ**
$$P(A) = \frac{3}{10} \times \frac{3060}{4845} + \frac{5}{10} \times \frac{1820}{4845} + \frac{2}{10} \times \frac{1001}{4845}$$

$$P(A) = \frac{1}{48450}(3 \times 3060 + 5 \times 1820 + 2 \times 1001)$$

$$P(A) = \frac{9180 + 9100 + 2002}{48450} = \frac{20282}{48450} = \frac{10141}{24225} \approx 0.4186$$

**Đáp số:** $P \approx 0.4186 = 41.86\%$

#### **b) Tính xác suất để được số sản phẩm tốt nhiều hơn số phế phẩm**

**GIẢI:**

Số SP tốt > số phế phẩm nghĩa là: 3 tốt + 1 phế, hoặc 4 tốt

**TH1: 4 tốt** (đã tính ở câu a)

**TH2: 3 tốt + 1 phế**

$$P(B|H_1) = \frac{C_{18}^3 \times C_2^1}{C_{20}^4} = \frac{816 \times 2}{4845} = \frac{1632}{4845}$$

$$P(B|H_2) = \frac{C_{16}^3 \times C_4^1}{C_{20}^4} = \frac{560 \times 4}{4845} = \frac{2240}{4845}$$

$$P(B|H_3) = \frac{C_{14}^3 \times C_6^1}{C_{20}^4} = \frac{364 \times 6}{4845} = \frac{2184}{4845}$$

$$P(B) = \frac{3}{10} \times \frac{1632}{4845} + \frac{5}{10} \times \frac{2240}{4845} + \frac{2}{10} \times \frac{2184}{4845}$$

$$P(B) = \frac{1}{48450}(3 \times 1632 + 5 \times 2240 + 2 \times 2184) = \frac{4896 + 11200 + 4368}{48450} = \frac{20464}{48450}$$

**Tổng xác suất (4 tốt hoặc 3 tốt):**
$$P(\text{tốt > phế}) = P(A) + P(B) = \frac{20282 + 20464}{48450} = \frac{40746}{48450} = \frac{20373}{24225} \approx 0.8410$$

**Đáp số:** $P \approx 0.8410 = 84.10\%$

#### **c) Giả sử trong 4 sản phẩm lấy ra có 3 sản phẩm tốt. Tính xác suất đã lấy được hộp loại III**

**GIẢI:**

Gọi C: Lấy được 3 tốt + 1 phế

Từ câu b, ta có các xác suất có điều kiện.

Tính P(C) theo công thức xác suất đầy đủ:
$$P(C) = \frac{20464}{48450}$$

Áp dụng công thức Bayes:
$$P(H_3|C) = \frac{P(H_3) \times P(C|H_3)}{P(C)} = \frac{\frac{2}{10} \times \frac{2184}{4845}}{\frac{20464}{48450}}$$

$$P(H_3|C) = \frac{\frac{4368}{48450}}{\frac{20464}{48450}} = \frac{4368}{20464} = \frac{273}{1279} \approx 0.2134$$

**Đáp số:** $P = \frac{273}{1279} \approx 21.34\%$

---

### **BÀI 1.12:** Có 10 hộp đựng sản phẩm cùng loại, mỗi hộp chứa rất nhiều sản phẩm. Trong đó, có 7 hộp của nhà máy M sản xuất, 2 hộp của nhà máy N sản xuất và 1 hộp của nhà máy P sản xuất. Tỷ lệ sản phẩm tốt của các nhà máy M, N, P lần lượt là 60%, 80% và 95%.

#### **a) Lấy ngẫu nhiên một hộp và từ hộp đó lấy ngẫu nhiên 1 sản phẩm. Tính xác suất lấy được sản phẩm tốt**

**GIẢI:**

**Bước 1: Xác định giả thuyết**
- $H_M$: Chọn hộp M, $P(H_M) = \frac{7}{10}$, $P(\text{tốt}|H_M) = 0.6$
- $H_N$: Chọn hộp N, $P(H_N) = \frac{2}{10}$, $P(\text{tốt}|H_N) = 0.8$
- $H_P$: Chọn hộp P, $P(H_P) = \frac{1}{10}$, $P(\text{tốt}|H_P) = 0.95$

**Bước 2: Công thức xác suất đầy đủ**
$$P(\text{tốt}) = \frac{7}{10} \times 0.6 + \frac{2}{10} \times 0.8 + \frac{1}{10} \times 0.95$$
$$P(\text{tốt}) = 0.42 + 0.16 + 0.095 = 0.675$$

**Đáp số:** $P = 0.675 = 67.5\%$

#### **b) Lấy ngẫu nhiên một hộp và từ hộp đó lấy ngẫu nhiên 5 sản phẩm. Tính xác suất lấy được 4 sản phẩm tốt**

**GIẢI:**

Vì mỗi hộp chứa rất nhiều SP nên các lần lấy độc lập, áp dụng phân phối nhị thức.

$$P(4\text{ tốt}|H_M) = C_5^4 \times (0.6)^4 \times (0.4)^1 = 5 \times 0.1296 \times 0.4 = 0.2592$$

$$P(4\text{ tốt}|H_N) = C_5^4 \times (0.8)^4 \times (0.2)^1 = 5 \times 0.4096 \times 0.2 = 0.4096$$

$$P(4\text{ tốt}|H_P) = C_5^4 \times (0.95)^4 \times (0.05)^1 = 5 \times 0.8145 \times 0.05 = 0.2036$$

**Công thức xác suất đầy đủ:**
$$P(4\text{ tốt}) = \frac{7}{10} \times 0.2592 + \frac{2}{10} \times 0.4096 + \frac{1}{10} \times 0.2036$$
$$P(4\text{ tốt}) = 0.1814 + 0.0819 + 0.0204 = 0.2837$$

**Đáp số:** $P = 0.2837 = 28.37\%$

---

### **BÀI 1.13:** Một nhà máy gồm 3 phân xưởng I, II, III. Trong đó, phân xưởng I sản xuất ra 45% số lượng sản phẩm, phân xưởng II sản xuất ra 30% số lượng sản phẩm, phân xưởng III sản xuất ra 25% số lượng sản phẩm. Tỷ lệ sản phẩm tốt của các phân xưởng I, II, III lần lượt là 70%, 75% và 80%.

#### **a) Tính tỷ lệ sản phẩm tốt nói chung do nhà máy sản xuất**

**GIẢI:**

Gọi:
- $H_1$: SP từ phân xưởng I, $P(H_1) = 0.45$
- $H_2$: SP từ phân xưởng II, $P(H_2) = 0.30$
- $H_3$: SP từ phân xưởng III, $P(H_3) = 0.25$

Công thức xác suất đầy đủ:
$$P(\text{tốt}) = 0.45 \times 0.7 + 0.30 \times 0.75 + 0.25 \times 0.8$$
$$P(\text{tốt}) = 0.315 + 0.225 + 0.2 = 0.74$$

**Đáp số:** Tỷ lệ SP tốt = **74%**

#### **b) Mua ngẫu nhiên 10 sản phẩm (trong số rất nhiều sản phẩm) do nhà máy sản xuất. Tính xác suất để mua được ít nhất 9 sản phẩm tốt**

**GIẢI:**

Vì số SP rất nhiều nên các lần mua độc lập.

Gọi X là số SP tốt trong 10 SP, X ~ B(10, 0.74)

$$P(X \geq 9) = P(X = 9) + P(X = 10)$$

$$P(X = 9) = C_{10}^9 \times (0.74)^9 \times (0.26)^1 = 10 \times 0.0596 \times 0.26 \approx 0.1550$$

$$P(X = 10) = C_{10}^{10} \times (0.74)^{10} = 0.0441$$

$$P(X \geq 9) = 0.1550 + 0.0441 = 0.1991$$

**Đáp số:** $P \approx 0.1991 = 19.91\%$

---

### **BÀI 1.14:** Có hai lô hàng đựng các sản phẩm cùng loại, mỗi lô chứa 70% sản phẩm tốt, trong đó lô I chứa 30 sản phẩm, lô II chứa rất nhiều sản phẩm. Từ mỗi lô lấy ngẫu nhiên 5 sản phẩm. Tính xác suất để trong 10 sản phẩm thu được có đúng 8 sản phẩm tốt.

**GIẢI:**

**Phân tích:**
- Lô I: 30 SP (21 tốt, 9 phế) - lấy không hoàn lại
- Lô II: Rất nhiều SP (70% tốt) - lấy có hoàn lại (các lần độc lập)

Gọi $X_1$ là số SP tốt từ lô I, $X_2$ là số SP tốt từ lô II.

Cần: $X_1 + X_2 = 8$

**Các trường hợp:**
- $X_1 = 3, X_2 = 5$
- $X_1 = 4, X_2 = 4$
- $X_1 = 5, X_2 = 3$

**TH1:** $P(X_1 = 3, X_2 = 5)$
$$P(X_1 = 3) = \frac{C_{21}^3 \times C_9^2}{C_{30}^5} = \frac{1330 \times 36}{142506} = \frac{47880}{142506}$$
$$P(X_2 = 5) = C_5^5 \times (0.7)^5 = 0.16807$$
$$P_1 = \frac{47880}{142506} \times 0.16807 \approx 0.0565$$

**TH2:** $P(X_1 = 4, X_2 = 4)$
$$P(X_1 = 4) = \frac{C_{21}^4 \times C_9^1}{C_{30}^5} = \frac{5985 \times 9}{142506} = \frac{53865}{142506}$$
$$P(X_2 = 4) = C_5^4 \times (0.7)^4 \times (0.3)^1 = 5 \times 0.2401 \times 0.3 = 0.36015$$
$$P_2 = \frac{53865}{142506} \times 0.36015 \approx 0.1361$$

**TH3:** $P(X_1 = 5, X_2 = 3)$
$$P(X_1 = 5) = \frac{C_{21}^5}{C_{30}^5} = \frac{20349}{142506}$$
$$P(X_2 = 3) = C_5^3 \times (0.7)^3 \times (0.3)^2 = 10 \times 0.343 \times 0.09 = 0.3087$$
$$P_3 = \frac{20349}{142506} \times 0.3087 \approx 0.0441$$

**Tổng:**
$$P = P_1 + P_2 + P_3 \approx 0.0565 + 0.1361 + 0.0441 = 0.2367$$

**Đáp số:** $P \approx 0.2367 = 23.67\%$

---

### **BÀI 1.15:** Có hai lô hàng đựng các sản phẩm cùng loại, mỗi lô chứa 70% sản phẩm tốt, trong đó lô I chứa 30 sản phẩm, lô II chứa rất nhiều sản phẩm. Lấy ngẫu nhiên từ lô II 1 sản phẩm bỏ sang lô I, sau đó từ lô I lấy ngẫu nhiên 5 sản phẩm. Tính xác suất được 4 sản phẩm tốt.

**GIẢI:**

**Bước 1: Phân tích giả thuyết**

Lô I ban đầu: 21 tốt, 9 phế

- $H_1$: Bỏ SP tốt từ II sang I
  - $P(H_1) = 0.7$
  - Lô I lúc này: 22 tốt, 9 phế (tổng 31)
  
- $H_2$: Bỏ SP phế từ II sang I
  - $P(H_2) = 0.3$
  - Lô I lúc này: 21 tốt, 10 phế (tổng 31)

**Bước 2: Tính xác suất có điều kiện**

Gọi A: Lấy được 4 SP tốt từ lô I

$$P(A|H_1) = \frac{C_{22}^4 \times C_9^1}{C_{31}^5} = \frac{7315 \times 9}{169911} = \frac{65835}{169911}$$

$$P(A|H_2) = \frac{C_{21}^4 \times C_{10}^1}{C_{31}^5} = \frac{5985 \times 10}{169911} = \frac{59850}{169911}$$

**Bước 3: Công thức xác suất đầy đủ**
$$P(A) = 0.7 \times \frac{65835}{169911} + 0.3 \times \frac{59850}{169911}$$
$$P(A) = \frac{46084.5 + 17955}{169911} = \frac{64039.5}{169911} \approx 0.3769$$

**Đáp số:** $P \approx 0.3769 = 37.69\%$

---

### **BÀI 1.16:** Một máy sản xuất sản phẩm với tỷ lệ sản phẩm tốt là 70%. Một lô hàng chứa 20 sản phẩm (14 tốt, 6 phế phẩm). Cho máy sản xuất 2 sp và từ lô hàng lấy ra 1 sp. Tính xs được ít nhất 2 sp tốt.

**GIẢI:**

**Phân tích:**
- Máy sản xuất 2 SP: Gọi X là số SP tốt, $X \sim B(2, 0.7)$
- Lô hàng lấy 1 SP: Xác suất lấy được SP tốt = $\frac{14}{20} = 0.7$

Tổng có 3 SP. Ít nhất 2 tốt nghĩa là: 2 tốt hoặc 3 tốt

**TH1: 3 tốt** (máy sản xuất 2 tốt, lô cho 1 tốt)
$$P_1 = (0.7)^2 \times 0.7 = 0.49 \times 0.7 = 0.343$$

**TH2: Đúng 2 tốt**
- Máy: 2 tốt, Lô: 1 phế: $P = 0.49 \times 0.3 = 0.147$
- Máy: 1 tốt + 1 phế, Lô: 1 tốt: $P = C_2^1 \times 0.7 \times 0.3 \times 0.7 = 2 \times 0.21 \times 0.7 = 0.294$
- Máy: 0 tốt (2 phế), Lô: 1 tốt: Không đủ 2 tốt - loại

$$P_2 = 0.147 + 0.294 = 0.441$$

**Tổng:**
$$P = 0.343 + 0.441 = 0.784$$

**Đáp số:** $P = 0.784 = 78.4\%$

---

### **BÀI 1.17:** Có hai lô hàng I và II. Lô I chứa 10 sản phẩm (có 8 sản phẩm tốt). Lô II chứa 15 sản phẩm (có 12 sản phẩm tốt). Lấy ngẫu nhiên từ mỗi lô 2 sản phẩm. Sau đó, trong 4 sản phẩm thu được lấy ngẫu nhiên 2 sản phẩm. Tính XS để được 2 sản phẩm tốt sau cùng.

**GIẢI:**

**Bước 1: Phân tích các trường hợp**

Gọi $X$ là số SP tốt trong 4 SP lấy từ 2 lô.

$X$ có thể nhận các giá trị: 0, 1, 2, 3, 4

**Bước 2: Tính phân phối của X**

$$P(X = 0) = \frac{C_2^2}{C_{10}^2} \times \frac{C_3^2}{C_{15}^2} = \frac{1}{45} \times \frac{3}{105} = \frac{3}{4725} = \frac{1}{1575}$$

$$P(X = 1) = \frac{C_8^1 \times C_2^1}{C_{10}^2} \times \frac{C_3^2}{C_{15}^2} + \frac{C_2^2}{C_{10}^2} \times \frac{C_{12}^1 \times C_3^1}{C_{15}^2}$$
$$= \frac{16}{45} \times \frac{3}{105} + \frac{1}{45} \times \frac{36}{105} = \frac{48}{4725} + \frac{36}{4725} = \frac{84}{4725} = \frac{4}{225}$$

$$P(X = 2) = \frac{C_8^2}{C_{10}^2} \times \frac{C_3^2}{C_{15}^2} + \frac{C_8^1 \times C_2^1}{C_{10}^2} \times \frac{C_{12}^1 \times C_3^1}{C_{15}^2} + \frac{C_2^2}{C_{10}^2} \times \frac{C_{12}^2}{C_{15}^2}$$
$$= \frac{28}{45} \times \frac{3}{105} + \frac{16}{45} \times \frac{36}{105} + \frac{1}{45} \times \frac{66}{105}$$
$$= \frac{84 + 576 + 66}{4725} = \frac{726}{4725} = \frac{242}{1575}$$

$$P(X = 3) = \frac{C_8^2}{C_{10}^2} \times \frac{C_{12}^1 \times C_3^1}{C_{15}^2} + \frac{C_8^1 \times C_2^1}{C_{10}^2} \times \frac{C_{12}^2}{C_{15}^2}$$
$$= \frac{28}{45} \times \frac{36}{105} + \frac{16}{45} \times \frac{66}{105} = \frac{1008 + 1056}{4725} = \frac{2064}{4725} = \frac{688}{1575}$$

$$P(X = 4) = \frac{C_8^2}{C_{10}^2} \times \frac{C_{12}^2}{C_{15}^2} = \frac{28}{45} \times \frac{66}{105} = \frac{1848}{4725} = \frac{88}{225}$$

**Bước 3: Tính xác suất lấy được 2 tốt trong 4 SP**

Gọi B: Lấy được 2 tốt trong 4 SP

$$P(B) = \sum_{k=2}^{4} P(X = k) \times P(\text{lấy 2 tốt} | X = k)$$

$$P(\text{lấy 2 tốt} | X = k) = \frac{C_k^2}{C_4^2}$$

$$P(B) = P(X=2) \times \frac{C_2^2}{C_4^2} + P(X=3) \times \frac{C_3^2}{C_4^2} + P(X=4) \times \frac{C_4^2}{C_4^2}$$

$$P(B) = \frac{242}{1575} \times \frac{1}{6} + \frac{688}{1575} \times \frac{3}{6} + \frac{88}{225} \times 1$$

$$P(B) = \frac{242}{9450} + \frac{2064}{9450} + \frac{3696}{9450} = \frac{6002}{9450} = \frac{3001}{4725} \approx 0.6351$$

**Đáp số:** $P = \frac{3001}{4725} \approx 63.51\%$

---

## CHƯƠNG 2: ĐẠI LƯỢNG NGẪU NHIÊN VÀ LUẬT PHÂN PHỐI XS

### **BÀI 2.1:** Cho ĐLNN X liên tục có hàm mật độ xác suất f(x) = c(3x - x²) nếu x ∈ [0,3]; 0 nếu x ∉ [0,3].

#### **a) Xác định hằng số c**

**GIẢI:**

Điều kiện chuẩn hóa:
$$\int_{-\infty}^{+\infty} f(x)dx = 1$$

$$\int_0^3 c(3x - x^2)dx = 1$$

$$c \left[\frac{3x^2}{2} - \frac{x^3}{3}\right]_0^3 = 1$$

$$c \left(\frac{3 \times 9}{2} - \frac{27}{3}\right) = 1$$

$$c \left(\frac{27}{2} - 9\right) = c \times \frac{9}{2} = 1$$

$$c = \frac{2}{9}$$

**Đáp số:** $c = \frac{2}{9}$

#### **b) Tính P(1 < X < 5)**

**GIẢI:**

Do $f(x) = 0$ khi $x > 3$, nên:

$$P(1 < X < 5) = P(1 < X \leq 3) = \int_1^3 \frac{2}{9}(3x - x^2)dx$$

$$= \frac{2}{9} \left[\frac{3x^2}{2} - \frac{x^3}{3}\right]_1^3$$

$$= \frac{2}{9} \left[\left(\frac{27}{2} - 9\right) - \left(\frac{3}{2} - \frac{1}{3}\right)\right]$$

$$= \frac{2}{9} \left[\frac{9}{2} - \frac{7}{6}\right] = \frac{2}{9} \times \frac{27 - 7}{6} = \frac{2}{9} \times \frac{20}{6} = \frac{40}{54} = \frac{20}{27}$$

**Đáp số:** $P(1 < X < 5) = \frac{20}{27} \approx 0.7407 = 74.07\%$

#### **c) Tìm hàm phân phối xác suất của X**

**GIẢI:**

Hàm phân phối: $F(x) = P(X \leq x) = \int_{-\infty}^x f(t)dt$

**Với $x < 0$:** $F(x) = 0$

**Với $0 \leq x \leq 3$:**
$$F(x) = \int_0^x \frac{2}{9}(3t - t^2)dt = \frac{2}{9}\left[\frac{3t^2}{2} - \frac{t^3}{3}\right]_0^x$$

$$F(x) = \frac{2}{9}\left(\frac{3x^2}{2} - \frac{x^3}{3}\right) = \frac{x^2}{3} - \frac{2x^3}{27}$$

**Với $x > 3$:** $F(x) = 1$

**Đáp số:**
$$F(x) = \begin{cases}
0 & \text{nếu } x < 0 \\
\frac{x^2}{3} - \frac{2x^3}{27} & \text{nếu } 0 \leq x \leq 3 \\
1 & \text{nếu } x > 3
\end{cases}$$

---

*Tiếp tục phần 3 với các bài còn lại...*


