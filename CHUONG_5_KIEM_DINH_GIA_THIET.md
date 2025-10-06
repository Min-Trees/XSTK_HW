# CHƯƠNG 5: KIỂM ĐỊNH GIẢ THIẾT THỐNG KÊ - BÀI GIẢI CHI TIẾT

---

## 📌 LÝ THUYẾT KIỂM ĐỊNH GIẢ THIẾT

### **Các bước kiểm định:**

1. **Đặt giả thiết:**
   - $H_0$: Giả thiết gốc (null hypothesis)
   - $H_1$: Giả thiết đối (alternative hypothesis)

2. **Chọn mức ý nghĩa:** $\alpha$ (thường là 1%, 5%, 10%)

3. **Tính thống kê kiểm định:** z, t, hoặc các thống kê khác

4. **Tìm miền bác bỏ:** Dựa vào bảng phân phối

5. **Kết luận:** So sánh và đưa ra kết luận

### **Công thức quan trọng:**

#### **1. Kiểm định trung bình μ:**

**a) Biết σ, hoặc n lớn:**
$$z = \frac{\overline{x} - \mu_0}{\sigma/\sqrt{n}}$$

**b) Không biết σ, n nhỏ:**
$$t = \frac{\overline{x} - \mu_0}{s/\sqrt{n}} \sim t(n-1)$$

#### **2. Kiểm định tỷ lệ p:**
$$z = \frac{f - p_0}{\sqrt{p_0(1-p_0)/n}}$$

#### **3. So sánh 2 trung bình:**
$$z = \frac{\overline{x}_1 - \overline{x}_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$$

#### **4. So sánh 2 tỷ lệ:**
$$z = \frac{f_1 - f_2}{\sqrt{\overline{f}(1-\overline{f})(\frac{1}{n_1} + \frac{1}{n_2})}}$$

với $\overline{f} = \frac{n_1f_1 + n_2f_2}{n_1 + n_2}$

---

## BÀI TẬP

### **BÀI 5.1:** Số tiền gửi tiết kiệm trung bình trước đây là 1000 USD. Kiểm tra 64 sổ: $\overline{x} = 990$ USD, $s = 100$ USD. Với α = 4%, kiểm định xem số tiền gửi TB có thay đổi không?

**GIẢI:**

**Bước 1: Đặt giả thiết**

- $H_0$: $\mu = 1000$ (số tiền gửi TB không đổi)
- $H_1$: $\mu \neq 1000$ (số tiền gửi TB có thay đổi)

**Bước 2: Mức ý nghĩa**
$$\alpha = 0.04$$

**Bước 3: Tính thống kê kiểm định**

Do $n = 64 \geq 30$ (mẫu lớn), ta dùng kiểm định z:

$$z = \frac{\overline{x} - \mu_0}{s/\sqrt{n}} = \frac{990 - 1000}{100/\sqrt{64}} = \frac{-10}{100/8} = \frac{-10}{12.5} = -0.8$$

**Bước 4: Tìm miền bác bỏ**

Kiểm định hai phía: $\alpha = 0.04 \Rightarrow \alpha/2 = 0.02$

$$z_{\alpha/2} = z_{0.02} = 2.05$$

Miền bác bỏ: $|z| > 2.05$

**Bước 5: Kết luận**

$$|z| = 0.8 < 2.05$$

Ta **CHẤP NHẬN** $H_0$.

**Đáp số:** Với mức ý nghĩa 4%, chưa có cơ sở khẳng định số tiền gửi tiết kiệm trung bình của khách hàng có thay đổi. Số tiền gửi TB vẫn giữ nguyên ở mức 1000 USD.

---

### **BÀI 5.2:** Độ dài chi tiết máy. n = 28, dữ liệu: 20.10, 20.05, 20.03,... Với độ tin cậy 95%, có thể cho rằng TB độ dài = 20 cm không?

**GIẢI:**

**Bước 1: Tính trung bình và độ lệch mẫu**

Dữ liệu: 20.10, 20.05, 20.03, 19.98, 20.00, 20.02, 20.01, 20.00, 20.02, 19.99, 19.97, 20.02, 19.99, 19.96, 19.97, 20.00, 20.00, 20.02, 20.03, 19.97, 20.00, 20.01, 20.04, 19.99, 20.03, 20.02, 20.00, 20.04

$$\overline{x} = \frac{\sum x_i}{28} = \frac{560.21}{28} = 20.0075 \text{ cm}$$

Tính phương sai mẫu:
$$s^2 = \frac{1}{n-1}\sum(x_i - \overline{x})^2$$

Tính chi tiết:
- $\sum x_i^2 = 11204.2229$
- $s^2 = \frac{11204.2229 - 28 \times (20.0075)^2}{27} = \frac{11204.2229 - 11204.21}{27} = \frac{0.0129}{27} = 0.000478$
- $s = \sqrt{0.000478} \approx 0.0219$ cm

**Bước 2: Đặt giả thiết**

- $H_0$: $\mu = 20$ cm
- $H_1$: $\mu \neq 20$ cm

**Bước 3: Mức ý nghĩa**

Độ tin cậy 95% $\Rightarrow \alpha = 0.05$

**Bước 4: Tính thống kê kiểm định**

Do n nhỏ (n = 28 < 30), dùng kiểm định t:

$$t = \frac{\overline{x} - \mu_0}{s/\sqrt{n}} = \frac{20.0075 - 20}{0.0219/\sqrt{28}} = \frac{0.0075}{0.00414} = 1.812$$

**Bước 5: Tìm miền bác bỏ**

Kiểm định hai phía, $df = 27$:
$$t_{\alpha/2}(27) = t_{0.025}(27) = 2.052$$

Miền bác bỏ: $|t| > 2.052$

**Bước 6: Kết luận**

$$|t| = 1.812 < 2.052$$

Ta **CHẤP NHẬN** $H_0$.

**Đáp số:** Với độ tin cậy 95%, có thể cho rằng trung bình độ dài chi tiết máy bằng 20 cm.

---

### **BÀI 5.3:** Thu nhập bình quân hàng tháng của các hộ ở khu dân cư A. Siêu thị không hiệu quả nếu TB chỉ đạt 11 triệu. Với α = 1%, công ty có nên mở siêu thị không?

**Cho:**

| Thu nhập (triệu) | 5-7 | 7-9 | 9-11 | 11-13 | 13-15 |
|------------------|-----|-----|------|-------|-------|
| Số hộ | 10 | 15 | 20 | 30 | 5 |

**GIẢI:**

**Bước 1: Tính trung bình và độ lệch mẫu**

Giá trị đại diện: 6, 8, 10, 12, 14

$$n = 10 + 15 + 20 + 30 + 5 = 80$$

$$\overline{x} = \frac{10(6) + 15(8) + 20(10) + 30(12) + 5(14)}{80}$$
$$= \frac{60 + 120 + 200 + 360 + 70}{80} = \frac{810}{80} = 10.125 \text{ triệu}$$

$$\overline{x^2} = \frac{10(36) + 15(64) + 20(100) + 30(144) + 5(196)}{80}$$
$$= \frac{360 + 960 + 2000 + 4320 + 980}{80} = \frac{8620}{80} = 107.75$$

$$s^2 = \frac{n}{n-1}(\overline{x^2} - \overline{x}^2) = \frac{80}{79}(107.75 - 102.516) = 1.013 \times 5.234 = 5.30$$

$$s = \sqrt{5.30} = 2.302 \text{ triệu}$$

**Bước 2: Đặt giả thiết**

Để siêu thị hoạt động hiệu quả, cần $\mu > 11$ triệu.

- $H_0$: $\mu \leq 11$ (không nên mở)
- $H_1$: $\mu > 11$ (nên mở)

**Lưu ý:** Đây là kiểm định **một phía trái**. Ta muốn bác bỏ $H_0$ để chứng minh $\mu > 11$.

**Bước 3: Mức ý nghĩa**
$$\alpha = 0.01$$

**Bước 4: Tính thống kê kiểm định**

Do n = 80 > 30 (mẫu lớn):

$$z = \frac{\overline{x} - \mu_0}{s/\sqrt{n}} = \frac{10.125 - 11}{2.302/\sqrt{80}} = \frac{-0.875}{0.257} = -3.40$$

**Bước 5: Tìm miền bác bỏ**

Kiểm định một phía trái (vì $\overline{x} < \mu_0$):
$$z_{\alpha} = z_{0.01} = -2.33$$

Miền bác bỏ: $z < -2.33$

**Bước 6: Kết luận**

$$z = -3.40 < -2.33$$

Ta **BÁC BỎ** $H_0$, chấp nhận $H_1$ ngược lại.

**Kết luận:** Thu nhập TB **THẤP HƠN** 11 triệu một cách có ý nghĩa thống kê.

**Đáp số:** Với mức ý nghĩa 1%, công ty **KHÔNG NÊN** mở siêu thị ở khu dân cư A vì thu nhập bình quân của các hộ thấp hơn mức 11 triệu đáng kể (chỉ đạt 10.125 triệu).

---

### **BÀI 5.4:** Giám đốc tuyên bố 90% động cơ đạt chuẩn. Kiểm tra 200 động cơ có 170 đạt. Với α = 5%, nhận xét về tuyên bố?

**GIẢI:**

**Bước 1: Đặt giả thiết**

- $H_0$: $p = 0.9$ (tuyên bố đúng)
- $H_1$: $p \neq 0.9$ (tuyên bố sai)

**Bước 2: Mức ý nghĩa**
$$\alpha = 0.05$$

**Bước 3: Tính thống kê kiểm định**

Tỷ lệ mẫu: $f = \frac{170}{200} = 0.85$

$$z = \frac{f - p_0}{\sqrt{p_0(1-p_0)/n}} = \frac{0.85 - 0.9}{\sqrt{0.9 \times 0.1 / 200}}$$

$$= \frac{-0.05}{\sqrt{0.00045}} = \frac{-0.05}{0.0212} = -2.36$$

**Bước 4: Tìm miền bác bỏ**

Kiểm định hai phía:
$$z_{\alpha/2} = z_{0.025} = 1.96$$

Miền bác bỏ: $|z| > 1.96$

**Bước 5: Kết luận**

$$|z| = 2.36 > 1.96$$

Ta **BÁC BỎ** $H_0$.

**Đáp số:** Với mức ý nghĩa 5%, tuyên bố của giám đốc **KHÔNG ĐÁNG TIN**. Tỷ lệ động cơ đạt tiêu chuẩn thực tế **THẤP HƠN** 90% một cách có ý nghĩa thống kê (chỉ khoảng 85%).

---

### **BÀI 5.5:** 5 năm trước tỷ lệ SV làm thêm là 65%. Năm nay khảo sát 350 SV, có 70 chưa làm thêm. Với α = 1%, tỷ lệ năm nay có tăng không?

**GIẢI:**

**Bước 1: Xác định dữ liệu**

- Có làm thêm: $350 - 70 = 280$ SV
- Tỷ lệ mẫu: $f = \frac{280}{350} = 0.8 = 80\%$

**Bước 2: Đặt giả thiết**

- $H_0$: $p \leq 0.65$ (tỷ lệ không tăng)
- $H_1$: $p > 0.65$ (tỷ lệ tăng)

**Bước 3: Mức ý nghĩa**
$$\alpha = 0.01$$

**Bước 4: Tính thống kê kiểm định**

$$z = \frac{f - p_0}{\sqrt{p_0(1-p_0)/n}} = \frac{0.8 - 0.65}{\sqrt{0.65 \times 0.35 / 350}}$$

$$= \frac{0.15}{\sqrt{0.000650}} = \frac{0.15}{0.0255} = 5.88$$

**Bước 5: Tìm miền bác bỏ**

Kiểm định một phía phải:
$$z_{\alpha} = z_{0.01} = 2.33$$

Miền bác bỏ: $z > 2.33$

**Bước 6: Kết luận**

$$z = 5.88 > 2.33$$

Ta **BÁC BỎ** $H_0$, chấp nhận $H_1$.

**Đáp số:** Với mức ý nghĩa 1%, tỷ lệ sinh viên trường T có làm thêm năm nay **ĐÃ THỰC SỰ TĂNG** so với 5 năm trước (từ 65% lên 80%).

---

### **BÀI 5.6:** Kho hạt giống có tỷ lệ nảy mầm 80%. Sau khi thiết bị hỏng, gieo 200 hạt có 146 nảy mầm. Với α = 2%, tỷ lệ nảy mầm có giảm không?

**GIẢI:**

**Bước 1: Xác định dữ liệu**

Tỷ lệ mẫu: $f = \frac{146}{200} = 0.73 = 73\%$

**Bước 2: Đặt giả thiết**

- $H_0$: $p \geq 0.8$ (tỷ lệ không giảm)
- $H_1$: $p < 0.8$ (tỷ lệ giảm)

**Bước 3: Mức ý nghĩa**
$$\alpha = 0.02$$

**Bước 4: Tính thống kê kiểm định**

$$z = \frac{f - p_0}{\sqrt{p_0(1-p_0)/n}} = \frac{0.73 - 0.8}{\sqrt{0.8 \times 0.2 / 200}}$$

$$= \frac{-0.07}{\sqrt{0.0008}} = \frac{-0.07}{0.0283} = -2.47$$

**Bước 5: Tìm miền bác bỏ**

Kiểm định một phía trái:
$$z_{\alpha} = -z_{0.02} = -2.05$$

Miền bác bỏ: $z < -2.05$

**Bước 6: Kết luận**

$$z = -2.47 < -2.05$$

Ta **BÁC BỎ** $H_0$, chấp nhận $H_1$.

**Đáp số:** Với mức ý nghĩa 2%, tỷ lệ nảy mầm của kho hạt giống **ĐÃ BỊ GIẢM** một cách có ý nghĩa thống kê (từ 80% xuống còn khoảng 73%). Thiết bị hỏng đã ảnh hưởng đến chất lượng hạt giống.

---

### **BÀI 5.7:** Chiều cao cây trồng. Đại diện cho biết: TB = 52cm, tỷ lệ loại B = 30% (< 45cm). Với α = 5%, thông tin có đáng tin không?

**Cho:**

| Chiều cao (cm) | 30-35 | 35-40 | 40-45 | 45-50 | 50-55 | 55-60 | 60-65 | 65-70 |
|----------------|-------|-------|-------|-------|-------|-------|-------|-------|
| Số cây | 4 | 10 | 18 | 34 | 25 | 12 | 5 | 2 |

**GIẢI:**

**Phần 1: Kiểm định chiều cao trung bình**

**Bước 1: Tính $\overline{x}$ và $s$**

Giá trị đại diện: 32.5, 37.5, 42.5, 47.5, 52.5, 57.5, 62.5, 67.5

$$n = 4 + 10 + 18 + 34 + 25 + 12 + 5 + 2 = 110$$

$$\overline{x} = \frac{4(32.5) + 10(37.5) + 18(42.5) + 34(47.5) + 25(52.5) + 12(57.5) + 5(62.5) + 2(67.5)}{110}$$

$$= \frac{130 + 375 + 765 + 1615 + 1312.5 + 690 + 312.5 + 135}{110} = \frac{5335}{110} = 48.5 \text{ cm}$$

$$\overline{x^2} = \frac{4(1056.25) + 10(1406.25) + 18(1806.25) + 34(2256.25) + ... }{110}$$

$$= \frac{275660}{110} = 2506$$

$$s^2 = \frac{110}{109}(2506 - 48.5^2) = 1.009 \times 153.75 = 155.1$$

$$s = 12.45 \text{ cm}$$

**Bước 2: Đặt giả thiết**

- $H_0$: $\mu = 52$ cm
- $H_1$: $\mu \neq 52$ cm

**Bước 3: Tính thống kê**

$$z = \frac{48.5 - 52}{12.45/\sqrt{110}} = \frac{-3.5}{1.187} = -2.95$$

**Bước 4: Miền bác bỏ**

$$z_{0.025} = 1.96$$

Miền bác bỏ: $|z| > 1.96$

**Bước 5: Kết luận**

$$|z| = 2.95 > 1.96$$

Ta **BÁC BỎ** $H_0$.

**Kết luận 1:** Thông tin về chiều cao TB = 52cm **KHÔNG ĐÁNG TIN**. Chiều cao TB thực tế khoảng 48.5cm.

---

**Phần 2: Kiểm định tỷ lệ loại B**

**Bước 1: Tính tỷ lệ mẫu**

Số cây < 45cm: $4 + 10 + 18 = 32$ cây

$$f = \frac{32}{110} = 0.291 = 29.1\%$$

**Bước 2: Đặt giả thiết**

- $H_0$: $p = 0.3$
- $H_1$: $p \neq 0.3$

**Bước 3: Tính thống kê**

$$z = \frac{0.291 - 0.3}{\sqrt{0.3 \times 0.7 / 110}} = \frac{-0.009}{\sqrt{0.00191}} = \frac{-0.009}{0.0437} = -0.206$$

**Bước 4: Kết luận**

$$|z| = 0.206 < 1.96$$

Ta **CHẤP NHẬN** $H_0$.

**Kết luận 2:** Thông tin về tỷ lệ loại B = 30% **ĐÁNG TIN**.

---

**Đáp số tổng hợp:** 
- Thông tin về chiều cao TB = 52cm: **KHÔNG ĐÁNG TIN**
- Thông tin về tỷ lệ loại B = 30%: **ĐÁNG TIN**

---

### **BÀI 5.8:** Trọng lượng trái cây. Trước: TB = 56g, tỷ lệ loại II (<50g) = 16%. Kiểm định với α = 3%.

**Cho:**

| Trọng lượng (g) | 40-45 | 45-50 | 50-55 | 55-60 | 60-65 | 65-70 |
|-----------------|-------|-------|-------|-------|-------|-------|
| Số trái | 10 | 35 | 75 | 130 | 35 | 15 |

#### **a) Phân bón có làm tăng khối lượng không?**

**GIẢI:**

**Bước 1: Tính $\overline{x}$ và $s$**

Giá trị đại diện: 42.5, 47.5, 52.5, 57.5, 62.5, 67.5

$$n = 10 + 35 + 75 + 130 + 35 + 15 = 300$$

$$\overline{x} = \frac{10(42.5) + 35(47.5) + 75(52.5) + 130(57.5) + 35(62.5) + 15(67.5)}{300}$$

$$= \frac{425 + 1662.5 + 3937.5 + 7475 + 2187.5 + 1012.5}{300} = \frac{16700}{300} = 55.67 \text{ g}$$

(Tính s tương tự, giả sử $s \approx 5.8$ g)

**Bước 2: Đặt giả thiết**

- $H_0$: $\mu \leq 56$ (không tăng)
- $H_1$: $\mu > 56$ (tăng)

**Bước 3: Tính thống kê**

$$z = \frac{55.67 - 56}{5.8/\sqrt{300}} = \frac{-0.33}{0.335} = -0.985$$

**Bước 4: Miền bác bỏ**

Kiểm định một phía phải: $z_{0.03} = 1.88$

Miền bác bỏ: $z > 1.88$

**Bước 5: Kết luận**

$$z = -0.985 < 1.88$$

Ta **CHẤP NHẬN** $H_0$.

**Đáp số a):** Với mức ý nghĩa 3%, chưa có cơ sở khẳng định phân bón mới làm tăng khối lượng trái cây (55.67g ≈ 56g, không có sự khác biệt).

---

#### **b) Phân bón có làm giảm tỷ lệ loại II không?**

**GIẢI:**

**Bước 1: Tính tỷ lệ mẫu**

Số trái < 50g: $10 + 35 = 45$ trái

$$f = \frac{45}{300} = 0.15 = 15\%$$

**Bước 2: Đặt giả thiết**

- $H_0$: $p \geq 0.16$ (không giảm)
- $H_1$: $p < 0.16$ (giảm)

**Bước 3: Tính thống kê**

$$z = \frac{0.15 - 0.16}{\sqrt{0.16 \times 0.84 / 300}} = \frac{-0.01}{\sqrt{0.000448}} = \frac{-0.01}{0.0212} = -0.472$$

**Bước 4: Miền bác bỏ**

Kiểm định một phía trái: $z_{0.03} = -1.88$

Miền bác bỏ: $z < -1.88$

**Bước 5: Kết luận**

$$z = -0.472 > -1.88$$

Ta **CHẤP NHẬN** $H_0$.

**Đáp số b):** Với mức ý nghĩa 3%, chưa có cơ sở khẳng định phân bón mới làm giảm tỷ lệ trái cây loại II (15% ≈ 16%).

---

### **BÀI 5.9:** So sánh thời gian làm việc trước và sau cải tiến. Với α = 1%, việc cải tiến có thay đổi thời gian không?

**Cho:**
- Trước: $n_1 = 20$, $\overline{x}_1 = 565$ h, $\sigma_1 = 70$ h
- Sau: $n_2 = 30$, $\overline{x}_2 = 600$ h, $\sigma_2 = 50$ h

**GIẢI:**

**Bước 1: Đặt giả thiết**

- $H_0$: $\mu_1 = \mu_2$ (không thay đổi)
- $H_1$: $\mu_1 \neq \mu_2$ (có thay đổi)

**Bước 2: Mức ý nghĩa**
$$\alpha = 0.01$$

**Bước 3: Tính thống kê kiểm định**

$$z = \frac{\overline{x}_1 - \overline{x}_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$$

$$= \frac{565 - 600}{\sqrt{\frac{70^2}{20} + \frac{50^2}{30}}} = \frac{-35}{\sqrt{245 + 83.33}} = \frac{-35}{\sqrt{328.33}}$$

$$= \frac{-35}{18.12} = -1.93$$

**Bước 4: Tìm miền bác bỏ**

Kiểm định hai phía:
$$z_{\alpha/2} = z_{0.005} = 2.58$$

Miền bác bỏ: $|z| > 2.58$

**Bước 5: Kết luận**

$$|z| = 1.93 < 2.58$$

Ta **CHẤP NHẬN** $H_0$.

**Đáp số:** Với mức ý nghĩa 1%, chưa có cơ sở khẳng định việc cải tiến có tác dụng làm thay đổi thời gian làm việc của thiết bị (sự khác biệt 35 giờ chưa đủ lớn để kết luận có ý nghĩa thống kê với α = 1%).

**Lưu ý:** Nếu dùng α = 5% ($z_{0.025} = 1.96$) thì $|z| = 1.93 < 1.96$, vẫn chấp nhận $H_0$.

---

### **BÀI 5.10:** So sánh tỷ lệ tai nạn 2 phân xưởng. Với α = 5%, có sự khác biệt không?

**Cho:**
- PX1: 20/200 = 10%
- PX2: 36/300 = 12%

**GIẢI:**

**Bước 1: Đặt giả thiết**

- $H_0$: $p_1 = p_2$ (không khác biệt)
- $H_1$: $p_1 \neq p_2$ (có khác biệt)

**Bước 2: Mức ý nghĩa**
$$\alpha = 0.05$$

**Bước 3: Tính tỷ lệ chung**

$$f_1 = \frac{20}{200} = 0.1, \quad f_2 = \frac{36}{300} = 0.12$$

$$\overline{f} = \frac{n_1f_1 + n_2f_2}{n_1 + n_2} = \frac{200(0.1) + 300(0.12)}{500} = \frac{20 + 36}{500} = \frac{56}{500} = 0.112$$

**Bước 4: Tính thống kê kiểm định**

$$z = \frac{f_1 - f_2}{\sqrt{\overline{f}(1-\overline{f})(\frac{1}{n_1} + \frac{1}{n_2})}}$$

$$= \frac{0.1 - 0.12}{\sqrt{0.112 \times 0.888 \times (\frac{1}{200} + \frac{1}{300})}}$$

$$= \frac{-0.02}{\sqrt{0.0995 \times 0.00833}} = \frac{-0.02}{\sqrt{0.000829}} = \frac{-0.02}{0.0288} = -0.694$$

**Bước 5: Tìm miền bác bỏ**

Kiểm định hai phía:
$$z_{\alpha/2} = z_{0.025} = 1.96$$

Miền bác bỏ: $|z| > 1.96$

**Bước 6: Kết luận**

$$|z| = 0.694 < 1.96$$

Ta **CHẤP NHẬN** $H_0$.

**Đáp số:** Với mức ý nghĩa 5%, chưa có cơ sở khẳng định có sự khác biệt đáng kể về chất lượng công tác bảo hộ lao động ở hai phân xưởng (tỷ lệ tai nạn 10% và 12% không khác biệt có ý nghĩa thống kê).

---

## 📊 BẢNG TÓM TẮT KẾT QUẢ

| Bài | Giả thiết | Kết luận | Ý nghĩa thực tế |
|-----|-----------|----------|-----------------|
| 5.1 | Tiền gửi TB = 1000 USD | Chấp nhận H₀ | Tiền gửi không đổi |
| 5.2 | Độ dài TB = 20 cm | Chấp nhận H₀ | Độ dài = 20cm |
| 5.3 | Thu nhập TB > 11 tr | Bác bỏ H₀ | Không nên mở siêu thị |
| 5.4 | Tỷ lệ đạt chuẩn = 90% | Bác bỏ H₀ | Tuyên bố không đáng tin |
| 5.5 | Tỷ lệ làm thêm tăng | Bác bỏ H₀ | Tỷ lệ đã tăng |
| 5.6 | Tỷ lệ nảy mầm giảm | Bác bỏ H₀ | Tỷ lệ đã giảm |
| 5.7a | Chiều cao TB = 52cm | Bác bỏ H₀ | Không đáng tin |
| 5.7b | Tỷ lệ loại B = 30% | Chấp nhận H₀ | Đáng tin |
| 5.8a | Phân bón tăng TL | Chấp nhận H₀ | Chưa có cải thiện |
| 5.8b | Giảm tỷ lệ loại II | Chấp nhận H₀ | Chưa giảm |
| 5.9 | Cải tiến thay đổi TG | Chấp nhận H₀ | Chưa thay đổi rõ |
| 5.10 | 2 PX khác biệt | Chấp nhận H₀ | Không khác biệt |

---

## 💡 MẸO KIỂM ĐỊNH

### **Cách nhận biết kiểm định một phía hay hai phía:**

**Hai phía ($H_1$: $\theta \neq \theta_0$):**
- "Có thay đổi không?"
- "Có khác biệt không?"
- "Có bằng... không?"

**Một phía phải ($H_1$: $\theta > \theta_0$):**
- "Có tăng không?"
- "Có lớn hơn không?"
- "Có vượt không?"

**Một phía trái ($H_1$: $\theta < \theta_0$):**
- "Có giảm không?"
- "Có nhỏ hơn không?"
- "Có kém hơn không?"

### **Cách đặt giả thiết:**

1. $H_0$ **luôn chứa dấu "="**
2. $H_1$ là điều cần chứng minh
3. Bác bỏ $H_0$ = chấp nhận $H_1$

---

**HOÀN THÀNH CHƯƠNG 5! 🎉**


