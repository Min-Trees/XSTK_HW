# CHƯƠNG 2, 3, 4 - BÀI GIẢI CHI TIẾT (Tiếp theo)

## CHƯƠNG 2: ĐẠI LƯỢNG NGẪU NHIÊN (Tiếp)

### **BÀI 2.2:** Cho ĐLNN X có hàm phân phối xác suất F(x) = 1/2 + (1/π) arctan x

#### **a) Tính P(0 < X < 1)**

**GIẢI:**

$$P(0 < X < 1) = F(1) - F(0)$$

$$F(1) = \frac{1}{2} + \frac{1}{\pi} \arctan(1) = \frac{1}{2} + \frac{1}{\pi} \times \frac{\pi}{4} = \frac{1}{2} + \frac{1}{4} = \frac{3}{4}$$

$$F(0) = \frac{1}{2} + \frac{1}{\pi} \arctan(0) = \frac{1}{2} + 0 = \frac{1}{2}$$

$$P(0 < X < 1) = \frac{3}{4} - \frac{1}{2} = \frac{1}{4}$$

**Đáp số:** $P = 0.25 = 25\%$

#### **b) Tìm hàm mật độ xác suất của X**

**GIẢI:**

$$f(x) = F'(x) = \frac{d}{dx}\left(\frac{1}{2} + \frac{1}{\pi}\arctan x\right)$$

$$f(x) = \frac{1}{\pi} \times \frac{1}{1+x^2} = \frac{1}{\pi(1+x^2)}$$

**Đáp số:** $f(x) = \frac{1}{\pi(1+x^2)}$ với $x \in \mathbb{R}$ (Phân phối Cauchy)

---

### **BÀI 2.3:** Ba xạ thủ độc lập bắn vào bia, mỗi xạ thủ có một viên đạn. XS để từng xạ thủ bắn trúng bia lần lượt là 0,8; 0,7; 0,6. Gọi X là số viên đạn bắn trúng bia.

#### **a) Lập bảng ppxs và tính các đặc trưng số của X**

**GIẢI:**

X có thể nhận giá trị: 0, 1, 2, 3

**Tính P(X = k):**

$$P(X = 0) = 0.2 \times 0.3 \times 0.4 = 0.024$$

$$P(X = 1) = 0.8 \times 0.3 \times 0.4 + 0.2 \times 0.7 \times 0.4 + 0.2 \times 0.3 \times 0.6$$
$$= 0.096 + 0.056 + 0.036 = 0.188$$

$$P(X = 2) = 0.8 \times 0.7 \times 0.4 + 0.8 \times 0.3 \times 0.6 + 0.2 \times 0.7 \times 0.6$$
$$= 0.224 + 0.144 + 0.084 = 0.452$$

$$P(X = 3) = 0.8 \times 0.7 \times 0.6 = 0.336$$

**Bảng phân phối xác suất:**

| X | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P | 0.024 | 0.188 | 0.452 | 0.336 |

**Kỳ vọng:**
$$E(X) = 0 \times 0.024 + 1 \times 0.188 + 2 \times 0.452 + 3 \times 0.336$$
$$= 0 + 0.188 + 0.904 + 1.008 = 2.1$$

**Kỳ vọng X²:**
$$E(X^2) = 0^2 \times 0.024 + 1^2 \times 0.188 + 2^2 \times 0.452 + 3^2 \times 0.336$$
$$= 0 + 0.188 + 1.808 + 3.024 = 5.02$$

**Phương sai:**
$$Var(X) = E(X^2) - [E(X)]^2 = 5.02 - (2.1)^2 = 5.02 - 4.41 = 0.61$$

**Độ lệch chuẩn:**
$$\sigma(X) = \sqrt{0.61} \approx 0.781$$

**Đáp số:** 
- $E(X) = 2.1$
- $Var(X) = 0.61$
- $\sigma(X) \approx 0.781$

#### **b) Tính P(2 ≤ X ≤ 7)**

**GIẢI:**

Do X chỉ nhận giá trị 0, 1, 2, 3 nên:

$$P(2 \leq X \leq 7) = P(X = 2) + P(X = 3) = 0.452 + 0.336 = 0.788$$

**Đáp số:** $P = 0.788 = 78.8\%$

---

### **BÀI 2.4:** Một hộp có 4 quả cầu trắng và 3 quả cầu đen. Lấy ngẫu nhiên lần lượt từng quả cầu cho đến khi lấy được quả cầu trắng. Tìm hàm phân phối xác suất cho số quả cầu được lấy ra?

**GIẢI:**

Gọi X là số quả cầu được lấy ra. X có thể nhận giá trị: 1, 2, 3, 4

$$P(X = 1) = \frac{4}{7}$$ (Lấy ngay quả trắng)

$$P(X = 2) = \frac{3}{7} \times \frac{4}{6} = \frac{12}{42} = \frac{2}{7}$$ (Đen, rồi Trắng)

$$P(X = 3) = \frac{3}{7} \times \frac{2}{6} \times \frac{4}{5} = \frac{24}{210} = \frac{4}{35}$$ (Đen, Đen, Trắng)

$$P(X = 4) = \frac{3}{7} \times \frac{2}{6} \times \frac{1}{5} \times \frac{4}{4} = \frac{24}{840} = \frac{1}{35}$$ (Đen, Đen, Đen, Trắng)

**Hàm phân phối xác suất:**

$$F(x) = P(X \leq x) = \begin{cases}
0 & \text{nếu } x < 1 \\
\frac{4}{7} & \text{nếu } 1 \leq x < 2 \\
\frac{4}{7} + \frac{2}{7} = \frac{6}{7} & \text{nếu } 2 \leq x < 3 \\
\frac{6}{7} + \frac{4}{35} = \frac{34}{35} & \text{nếu } 3 \leq x < 4 \\
1 & \text{nếu } x \geq 4
\end{cases}$$

---

### **BÀI 2.5:** Tỷ lệ xe máy bị tai nạn trong năm là 0,0055. Công ty bảo hiểm bán với giá 60.000đ/xe, bồi thường 3 triệu/vụ. Chi phí quản lý 30% giá bán. Tính lợi nhuận kỳ vọng cho mỗi hợp đồng?

**GIẢI:**

**Phân tích:**
- Thu từ bán BH: 60.000đ
- Chi phí quản lý: 60.000 × 0.3 = 18.000đ
- Xác suất tai nạn: p = 0.0055
- Bồi thường nếu tai nạn: 3.000.000đ

Gọi X là lợi nhuận (đơn vị: nghìn đồng)

- Nếu không tai nạn (p = 0.9945): $X = 60 - 18 = 42$
- Nếu có tai nạn (p = 0.0055): $X = 60 - 18 - 3000 = -2958$

**Kỳ vọng lợi nhuận:**
$$E(X) = 42 \times 0.9945 + (-2958) \times 0.0055$$
$$= 41.769 - 16.269 = 25.5 \text{ nghìn đồng}$$

**Đáp số:** Lợi nhuận kỳ vọng = **25.500đ/hợp đồng**

---

### **BÀI 2.6:** Khảo sát số khách trên xe buýt. Chi phí 200 ngàn/chuyến. Tìm giá vé để lời bình quân 100 ngàn/chuyến.

| Số khách | 25 | 30 | 35 | 40 | 45 |
|----------|----|----|----|----|-----|
| Tần suất | 0.15 | 0.2 | 0.3 | 0.25 | 0.1 |

**GIẢI:**

Gọi X là số khách trên một chuyến, a là giá vé (nghìn đồng)

**Kỳ vọng số khách:**
$$E(X) = 25 \times 0.15 + 30 \times 0.2 + 35 \times 0.3 + 40 \times 0.25 + 45 \times 0.1$$
$$= 3.75 + 6 + 10.5 + 10 + 4.5 = 34.75 \text{ khách}$$

**Thu nhập trung bình:** $34.75 \times a$ nghìn đồng

**Lợi nhuận trung bình = Thu nhập - Chi phí:**
$$34.75a - 200 = 100$$
$$34.75a = 300$$
$$a = \frac{300}{34.75} \approx 8.633 \text{ nghìn đồng}$$

**Đáp số:** Giá vé cần là khoảng **8.600đ - 8.700đ**

---

### **BÀI 2.7:** Hộp I: 10 SP (7 tốt, 3 phế). Hộp II: 15 SP (11 tốt, 4 phế). Lấy 1 từ I, 2 từ II. Lập bảng ppxs số SP tốt.

**GIẢI:**

Gọi X là số SP tốt. X nhận giá trị: 0, 1, 2, 3

**Tính P(X = k):**

$$P(X = 0) = \frac{3}{10} \times \frac{C_4^2}{C_{15}^2} = \frac{3}{10} \times \frac{6}{105} = \frac{18}{1050} = \frac{3}{175}$$

$$P(X = 1) = \frac{3}{10} \times \frac{C_{11}^1 \times C_4^1}{C_{15}^2} + \frac{7}{10} \times \frac{C_4^2}{C_{15}^2}$$
$$= \frac{3}{10} \times \frac{44}{105} + \frac{7}{10} \times \frac{6}{105} = \frac{132 + 42}{1050} = \frac{174}{1050} = \frac{29}{175}$$

$$P(X = 2) = \frac{3}{10} \times \frac{C_{11}^2}{C_{15}^2} + \frac{7}{10} \times \frac{C_{11}^1 \times C_4^1}{C_{15}^2}$$
$$= \frac{3}{10} \times \frac{55}{105} + \frac{7}{10} \times \frac{44}{105} = \frac{165 + 308}{1050} = \frac{473}{1050}$$

$$P(X = 3) = \frac{7}{10} \times \frac{C_{11}^2}{C_{15}^2} = \frac{7}{10} \times \frac{55}{105} = \frac{385}{1050} = \frac{11}{30}$$

**Bảng phân phối:**

| X | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P | 3/175 | 29/175 | 473/1050 | 11/30 |

**Kỳ vọng:**
$$E(X) = \frac{7}{10} \times 1 + \frac{11}{15} \times 2 = 0.7 + 1.467 = 2.167$$

**Đáp số:** Kỳ vọng số SP tốt ≈ 2.17

---

### **BÀI 2.8:** Bán máy lạnh lời 800k, bảo hành lỗ 1tr. XS bảo hành 10%. Tính mức lời TB?

**GIẢI:**

Gọi X là lợi nhuận (nghìn đồng)

- Không bảo hành (p = 0.9): X = 800
- Phải bảo hành (p = 0.1): X = -1000

$$E(X) = 800 \times 0.9 + (-1000) \times 0.1 = 720 - 100 = 620 \text{ nghìn đồng}$$

**Đáp số:** Mức lời trung bình = **620.000đ/máy**

---

### **BÀI 2.9:** 10 hộp (4 loại I, 6 loại II). Loại I: 15 tốt/5 phế. Loại II: 13 tốt/7 phế. Chọn 1 hộp, lấy 3 SP.

**GIẢI:**

Gọi X là số SP tốt. 

$$P(H_1) = \frac{4}{10} = 0.4, \quad P(H_2) = \frac{6}{10} = 0.6$$

**Tính P(X = k):**

$$P(X = 0) = 0.4 \times \frac{C_5^3}{C_{20}^3} + 0.6 \times \frac{C_7^3}{C_{20}^3}$$
$$= 0.4 \times \frac{10}{1140} + 0.6 \times \frac{35}{1140} = \frac{4 + 21}{1140} = \frac{25}{1140}$$

$$P(X = 1) = 0.4 \times \frac{C_{15}^1 \times C_5^2}{C_{20}^3} + 0.6 \times \frac{C_{13}^1 \times C_7^2}{C_{20}^3}$$
$$= 0.4 \times \frac{150}{1140} + 0.6 \times \frac{273}{1140} = \frac{60 + 163.8}{1140} = \frac{223.8}{1140}$$

(Tương tự cho X = 2, 3)

**Kỳ vọng:** 
$$E(X) = 0.4 \times \frac{15}{20} \times 3 + 0.6 \times \frac{13}{20} \times 3 = 0.9 + 1.17 = 2.07$$

**Đáp số:** $E(X) \approx 2.07$ SP tốt

---

### **BÀI 2.10:** Thùng 24 chai (5 quá hạn). Chọn 6 chai.

#### **a) X là số chai quá hạn. Tính E(X), Var(X)**

**GIẢI:**

X tuân theo phân phối siêu bội: $X \sim H(6, 5, 24)$

$$P(X = k) = \frac{C_5^k \times C_{19}^{6-k}}{C_{24}^6}$$

**Kỳ vọng:**
$$E(X) = n \times \frac{K}{N} = 6 \times \frac{5}{24} = \frac{30}{24} = 1.25$$

**Phương sai:**
$$Var(X) = n \times \frac{K}{N} \times \frac{N-K}{N} \times \frac{N-n}{N-1}$$
$$= 6 \times \frac{5}{24} \times \frac{19}{24} \times \frac{18}{23} = 1.25 \times 0.7917 \times 0.7826 \approx 0.775$$

**Đáp số:** $E(X) = 1.25$, $Var(X) \approx 0.775$

#### **b) Y là số chai còn hạn. Tính E(Y), Var(Y)**

**GIẢI:**

$Y = 6 - X$

$$E(Y) = 6 - E(X) = 6 - 1.25 = 4.75$$

$$Var(Y) = Var(6 - X) = Var(X) = 0.775$$

**Đáp số:** $E(Y) = 4.75$, $Var(Y) = 0.775$

---

### **BÀI 2.11:** Theo dõi 12 máy. XS cần điều chỉnh = 0.2/máy.

#### **a) Tính XS có ít nhất 1 máy cần điều chỉnh trong 1 giờ**

**GIẢI:**

Gọi X là số máy cần điều chỉnh. $X \sim B(12, 0.2)$

$$P(X \geq 1) = 1 - P(X = 0) = 1 - C_{12}^0 (0.2)^0 (0.8)^{12}$$
$$= 1 - (0.8)^{12} = 1 - 0.0687 = 0.9313$$

**Đáp số:** $P \approx 0.9313 = 93.13\%$

#### **b) Cần theo dõi bao nhiêu máy để trung bình gặp 3 máy cần điều chỉnh?**

**GIẢI:**

Gọi n là số máy. $E(X) = np = n \times 0.2 = 3$

$$n = \frac{3}{0.2} = 15 \text{ máy}$$

**Đáp số:** Cần theo dõi **15 máy**

---

### **BÀI 2.12:** 30 con gà, XS đẻ = 0.6/con.

#### **a) Không có con nào đẻ**

$$P(X = 0) = C_{30}^0 (0.6)^0 (0.4)^{30} = (0.4)^{30} \approx 1.15 \times 10^{-12}$$

**Đáp số:** $P \approx 0$ (gần như không thể)

#### **b) Có đúng 15 con đẻ**

$$P(X = 15) = C_{30}^{15} (0.6)^{15} (0.4)^{15} \approx 0.0654$$

**Đáp số:** $P \approx 6.54\%$

#### **c) Có ít nhất 1 con đẻ**

$$P(X \geq 1) = 1 - P(X = 0) \approx 1$$

**Đáp số:** $P \approx 100\%$

#### **d) Có ít nhất 2 con đẻ**

$$P(X \geq 2) = 1 - P(X = 0) - P(X = 1)$$
$$P(X = 1) = C_{30}^1 (0.6)^1 (0.4)^{29} \approx 0$$
$$P(X \geq 2) \approx 1$$

**Đáp số:** $P \approx 100\%$

**Số con đẻ có khả năng nhất (Mode):**
$$M_0 = \lfloor (n+1)p \rfloor = \lfloor 31 \times 0.6 \rfloor = 18 \text{ con}$$

**Để có TB 100 trứng/ngày:** $n \times 0.6 = 100 \Rightarrow n = \frac{100}{0.6} \approx 167$ con

**Đáp số:** Nhiều khả năng nhất 18 con đẻ; cần nuôi 167 con để có 100 trứng/ngày

---

### **BÀI 2.13:** Tỷ lệ sốt rét = 0.05

#### **a) Khám 3 người, XS có ít nhất 1 mắc bệnh**

$$P(X \geq 1) = 1 - (0.95)^3 = 1 - 0.8574 = 0.1426$$

**Đáp số:** $P \approx 14.26\%$

#### **b) Cần khám bao nhiêu người để P(ít nhất 1 mắc) ≥ 0.9?**

$$1 - (0.95)^n \geq 0.9$$
$$(0.95)^n \leq 0.1$$
$$n \ln(0.95) \leq \ln(0.1)$$
$$n \geq \frac{\ln(0.1)}{\ln(0.95)} = \frac{-2.303}{-0.0513} \approx 44.9$$

**Đáp số:** Cần khám ít nhất **45 người**

---

### **BÀI 2.14:** Nuôi n gà, p = 0.7 đẻ/ngày. Chắc chắn nhất có 100 con đẻ?

**GIẢI:**

"Chắc chắn nhất" nghĩa là mode $M_0 = 100$

$$M_0 = \lfloor (n+1)p \rfloor = 100$$

$$(n+1) \times 0.7 = 100$$
$$n + 1 = \frac{100}{0.7} = 142.86$$
$$n = 142$$

**Đáp số:** Cần nuôi ít nhất **142 con gà**

---

### **BÀI 2.15:** Thi trắc nghiệm 50 câu, 4 đáp án, mỗi câu đúng = 0.2 điểm

#### **a) A trả lời ngẫu nhiên, tính XS được 5 điểm**

5 điểm = 25 câu đúng

$X \sim B(50, 0.25)$

$$P(X = 25) = C_{50}^{25} (0.25)^{25} (0.75)^{25}$$

Dùng xấp xỉ chuẩn: $E(X) = 12.5$, $\sigma = \sqrt{50 \times 0.25 \times 0.75} = 3.06$

$$P(X = 25) \approx 0$$ (rất nhỏ, không khả thi)

**Đáp số:** $P \approx 0$ (gần như không thể)

#### **b) B chắc 8 câu, các câu còn lại ngẫu nhiên. XS được 5 điểm?**

B cần thêm 17 câu đúng trong 42 câu còn lại.

$Y \sim B(42, 0.25)$

$$P(Y = 17) = C_{42}^{17} (0.25)^{17} (0.75)^{25}$$

$E(Y) = 10.5$, $\sigma_Y = 2.81$

Xấp xỉ chuẩn: $P(Y = 17) \approx 0.01$

**Đáp số:** $P \approx 1\%$

---

### **BÀI 2.16:** 10000 cây lan (2000 trắng). Chọn 50 cây, tính XS chọn được 10 cây trắng.

**GIẢI:**

Do N rất lớn, dùng xấp xỉ nhị thức: $X \sim B(50, 0.2)$

$$P(X = 10) = C_{50}^{10} (0.2)^{10} (0.8)^{40}$$

$E(X) = 10$, $\sigma = \sqrt{50 \times 0.2 \times 0.8} = 2.83$

$$P(X = 10) \approx \frac{1}{\sqrt{2\pi} \times 2.83} \approx 0.1413$$

**Đáp số:** $P \approx 14.13\%$

---

### **BÀI 2.17:** Bến xe: TB 90 xe/giờ

#### **a) XS có ít nhất 1 xe xuất bến trong 2 phút**

$\lambda = 90 \text{ xe/h} = 3 \text{ xe/2 phút}$

$X \sim Poisson(3)$

$$P(X \geq 1) = 1 - P(X = 0) = 1 - e^{-3} = 1 - 0.0498 = 0.9502$$

**Đáp số:** $P \approx 95.02\%$

#### **b) Trong 5 phút có 8 xe xuất bến**

$\lambda = 90 \times \frac{5}{60} = 7.5$ xe/5 phút

$$P(X = 8) = \frac{7.5^8 e^{-7.5}}{8!} \approx 0.1321$$

**Đáp số:** $P \approx 13.21\%$

---

### **BÀI 2.18:** TB 5 phút có 15 khách. Tính XS có nhiều hơn 1 khách trong 20 giây.

**GIẢI:**

$\lambda = 15 \text{ khách/5 phút} = 1$ khách/20 giây

$$P(X > 1) = 1 - P(X \leq 1) = 1 - [P(X=0) + P(X=1)]$$
$$= 1 - [e^{-1} + 1 \cdot e^{-1}] = 1 - 2e^{-1} = 1 - 0.7358 = 0.2642$$

**Đáp số:** $P \approx 26.42\%$

---

### **BÀI 2.19:** Xe chở 1000 bia SG (p=0.001) và 2000 Coca (p=0.0015).

#### **a) XS ≤ 1 chai bia SG bể**

$X_1 \sim Poisson(1)$

$$P(X_1 \leq 1) = e^{-1} + 1 \cdot e^{-1} = 2e^{-1} \approx 0.7358$$

**Đáp số:** $P \approx 73.58\%$

#### **b) XS ≤ 2 chai Coca bể**

$X_2 \sim Poisson(3)$

$$P(X_2 \leq 2) = e^{-3}(1 + 3 + \frac{9}{2}) = e^{-3} \times 8.5 \approx 0.4232$$

**Đáp số:** $P \approx 42.32\%$

#### **c) XS lái xe được thưởng (≤ 1 chai tổng bể)**

$X = X_1 + X_2 \sim Poisson(4)$

$$P(X \leq 1) = e^{-4}(1 + 4) = 5e^{-4} \approx 0.0916$$

**Đáp số:** $P \approx 9.16\%$

#### **d) Cần chở bao nhiêu chuyến để P(ít nhất 1 chuyến thưởng) ≥ 0.95?**

$$1 - (1 - 0.0916)^n \geq 0.95$$
$$(0.9084)^n \leq 0.05$$
$$n \geq \frac{\ln(0.05)}{\ln(0.9084)} \approx 31.2$$

**Đáp số:** Cần chở ít nhất **32 chuyến**

---

*Tiếp tục với các bài còn lại...*


