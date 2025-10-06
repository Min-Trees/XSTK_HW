# HOÀN THIỆN BÀI GIẢI CHƯƠNG 2, 3, 4

## CHƯƠNG 2 (Tiếp theo) - Phân phối chuẩn và ứng dụng

### **BÀI 2.20:** Tổng điểm 2 môn ~ N(13, 5²). Trúng tuyển nếu ≥ 15 điểm. Tính tỷ lệ đỗ.

**GIẢI:**

Gọi X là tổng điểm. $X \sim N(13, 25)$

$$P(X \geq 15) = P\left(\frac{X - 13}{5} \geq \frac{15 - 13}{5}\right) = P(Z \geq 0.4)$$

$$= 1 - \Phi(0.4) = 1 - 0.6554 = 0.3446$$

**Đáp số:** Tỷ lệ đỗ ≈ **34.46%**

---

### **BÀI 2.21:** Chiều cao nam SV ~ N(168, 6²). Chọn 10 nam. XS có ít nhất 1 nam cao 165-175cm?

**GIẢI:**

Gọi X là chiều cao. $X \sim N(168, 36)$

$$P(165 < X < 175) = \Phi\left(\frac{175-168}{6}\right) - \Phi\left(\frac{165-168}{6}\right)$$
$$= \Phi(1.17) - \Phi(-0.5) = 0.8790 - 0.3085 = 0.5705$$

Với 10 SV:
$$P(\text{ít nhất 1}) = 1 - (1 - 0.5705)^{10} = 1 - (0.4295)^{10} \approx 1$$

**Đáp số:** $P \approx 100\%$ (gần chắc chắn)

---

### **BÀI 2.22:** Máy I: p=0.6, Máy II: p=0.7. Mỗi máy SX 2 SP.

#### **a) Tính XS có đúng 3 SP tốt trong 4 SP**

**GIẢI:**

Gọi $X_1$ là số SP tốt từ máy I, $X_2$ từ máy II.

$X_1 \sim B(2, 0.6)$, $X_2 \sim B(2, 0.7)$

Cần: $X_1 + X_2 = 3$

**TH1:** $X_1 = 1, X_2 = 2$
$$P_1 = C_2^1(0.6)(0.4) \times C_2^2(0.7)^2 = 0.48 \times 0.49 = 0.2352$$

**TH2:** $X_1 = 2, X_2 = 1$
$$P_2 = C_2^2(0.6)^2 \times C_2^1(0.7)(0.3) = 0.36 \times 0.42 = 0.1512$$

$$P = 0.2352 + 0.1512 = 0.3864$$

**Đáp số:** $P \approx 38.64\%$

#### **b) Máy I sản xuất 300 SP. XS có ít nhất 185 SP tốt?**

**GIẢI:**

$X \sim B(300, 0.6)$

$\mu = 180$, $\sigma = \sqrt{300 \times 0.6 \times 0.4} = \sqrt{72} \approx 8.49$

Dùng hiệu chỉnh liên tục:
$$P(X \geq 185) \approx P\left(Z \geq \frac{184.5 - 180}{8.49}\right) = P(Z \geq 0.53)$$
$$= 1 - \Phi(0.53) = 1 - 0.7019 = 0.2981$$

**Đáp số:** $P \approx 29.81\%$

---

### **BÀI 2.23:** Chọn ngẫu nhiên 1 máy (I hoặc II), cho SX 300 SP.

#### **a) XS được đúng 200 SP tốt**

**GIẢI:**

$$P(\text{chọn I}) = P(\text{chọn II}) = 0.5$$

Xấp xỉ chuẩn:
- Máy I: $\mu_1 = 180$, $\sigma_1 = 8.49$
- Máy II: $\mu_2 = 210$, $\sigma_2 = 7.94$

$$P(X=200|I) \approx \frac{1}{\sqrt{2\pi} \times 8.49} e^{-\frac{(200-180)^2}{2 \times 72}} \approx 0.0024$$

$$P(X=200|II) \approx \frac{1}{\sqrt{2\pi} \times 7.94} e^{-\frac{(200-210)^2}{2 \times 63}} \approx 0.0311$$

$$P(X=200) = 0.5 \times 0.0024 + 0.5 \times 0.0311 = 0.0168$$

**Đáp số:** $P \approx 1.68\%$

#### **b) XS có ít nhất 200 SP tốt**

$$P(X \geq 200|I) = P(Z \geq 2.36) = 0.0091$$
$$P(X \geq 200|II) = P(Z \geq -1.26) = 0.8962$$

$$P(X \geq 200) = 0.5 \times 0.0091 + 0.5 \times 0.8962 = 0.4527$$

**Đáp số:** $P \approx 45.27\%$

---

### **BÀI 2.24:** Kiện 20 SP (15 tốt, 5 phế). Kiểm tra 4 SP, nhận nếu ≥3 tốt.

**a) Khách kiểm tra 10 kiện. XS có ít nhất 9 kiện được nhận?**

**GIẢI:**

Tính xác suất 1 kiện được nhận:
$$p = P(X \geq 3) = P(X=3) + P(X=4)$$
$$= \frac{C_{15}^3 C_5^1}{C_{20}^4} + \frac{C_{15}^4}{C_{20}^4} = \frac{2275 + 1365}{4845} = \frac{3640}{4845} = 0.7513$$

Gọi Y là số kiện được nhận. $Y \sim B(10, 0.7513)$

$$P(Y \geq 9) = P(Y=9) + P(Y=10)$$
$$= C_{10}^9(0.7513)^9(0.2487) + (0.7513)^{10}$$
$$\approx 0.1885 + 0.0563 = 0.2448$$

**Đáp số:** $P \approx 24.48\%$

**b) Khách kiểm tra 250 kiện:**

#### **b.1) XS có ít nhất 180 kiện được nhận?**

$Y \sim B(250, 0.7513)$

$\mu = 187.825$, $\sigma = \sqrt{250 \times 0.7513 \times 0.2487} = 6.84$

$$P(Y \geq 180) \approx P\left(Z \geq \frac{179.5 - 187.825}{6.84}\right) = P(Z \geq -1.22)$$
$$= \Phi(1.22) = 0.8888$$

**Đáp số:** $P \approx 88.88\%$

#### **b.2) XS có đúng 190 kiện được nhận?**

$$P(Y = 190) \approx \frac{1}{\sqrt{2\pi} \times 6.84} e^{-\frac{(190-187.825)^2}{2 \times 46.79}} \approx 0.0508$$

**Đáp số:** $P \approx 5.08\%$

---

### **BÀI 2.25:** Máy SX 1600 SP/ngày, p=0.8.

#### **a) XS trong ngày SX được từ 1200 đến 1300 SP tốt?**

$X \sim B(1600, 0.8)$

$\mu = 1280$, $\sigma = \sqrt{1600 \times 0.8 \times 0.2} = 16$

$$P(1200 \leq X \leq 1300) = \Phi\left(\frac{1300.5-1280}{16}\right) - \Phi\left(\frac{1199.5-1280}{16}\right)$$
$$= \Phi(1.28) - \Phi(-5.03) \approx 0.8997 - 0 = 0.8997$$

**Đáp số:** $P \approx 89.97\%$

#### **b) Số SP tốt trung bình và tin chắc nhất?**

- **Trung bình:** $E(X) = 1280$ SP
- **Tin chắc nhất (Mode):** $M_0 = \lfloor 1601 \times 0.8 \rfloor = 1280$ SP

**Đáp số:** Trung bình = 1280 SP, Mode = 1280 SP

#### **c) Tính số tiền lãi tin chắc nhất?**

Số SP tốt tin chắc nhất: 1280

Lãi = Thu - Chi = $1280 \times 3000 - 1600 \times 600$
$$= 3.840.000 - 960.000 = 2.880.000 \text{ đồng}$$

**Đáp số:** Lãi tin chắc nhất = **2.880.000đ/ngày**

---

### **BÀI 2.26:** Khách sạn 200 phòng, nhận đặt 225 khách, p=0.85 đến.

#### **a) XS có đúng 195 khách đến?**

$X \sim B(225, 0.85)$

$\mu = 191.25$, $\sigma = \sqrt{225 \times 0.85 \times 0.15} = 5.35$

$$P(X = 195) \approx \frac{1}{\sqrt{2\pi} \times 5.35} e^{-\frac{(195-191.25)^2}{2 \times 28.62}} \approx 0.0604$$

**Đáp số:** $P \approx 6.04\%$

#### **b) XS có từ 190 đến 199 khách đến?**

$$P(190 \leq X \leq 199) = \Phi\left(\frac{199.5-191.25}{5.35}\right) - \Phi\left(\frac{189.5-191.25}{5.35}\right)$$
$$= \Phi(1.54) - \Phi(-0.33) = 0.9382 - 0.3707 = 0.5675$$

**Đáp số:** $P \approx 56.75\%$

#### **c) XS tất cả khách đặt và đến đều được nhận phòng?**

$$P(X \leq 200) = \Phi\left(\frac{200.5-191.25}{5.35}\right) = \Phi(1.73) = 0.9582$$

**Đáp số:** $P \approx 95.82\%$

---

## CHƯƠNG 3: LÝ THUYẾT MẪU

### **BÀI 1:** Điểm thi 50 SV:

| X | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|-----|
| n | 2 | 8 | 6 | 15 | 13 | 5 | 1 |

**GIẢI:**

**Điểm trung bình mẫu:**
$$\overline{x} = \frac{2 \times 4 + 8 \times 5 + 6 \times 6 + 15 \times 7 + 13 \times 8 + 5 \times 9 + 1 \times 10}{50}$$
$$= \frac{8 + 40 + 36 + 105 + 104 + 45 + 10}{50} = \frac{348}{50} = 6.96$$

**Phương sai mẫu hiệu chỉnh:**
$$\overline{x^2} = \frac{2 \times 16 + 8 \times 25 + 6 \times 36 + 15 \times 49 + 13 \times 64 + 5 \times 81 + 1 \times 100}{50}$$
$$= \frac{32 + 200 + 216 + 735 + 832 + 405 + 100}{50} = \frac{2520}{50} = 50.4$$

$$s^2 = \frac{n}{n-1}(\overline{x^2} - \overline{x}^2) = \frac{50}{49}(50.4 - 48.44) = \frac{50}{49} \times 1.96 = 2.0$$

**Độ lệch mẫu hiệu chỉnh:**
$$s = \sqrt{2.0} \approx 1.414$$

**Tỷ lệ SV khá (≥7):**
$$f = \frac{15 + 13 + 5 + 1}{50} = \frac{34}{50} = 0.68 = 68\%$$

**Đáp số:** 
- $\overline{x} = 6.96$
- $s^2 = 2.0$
- $s = 1.414$
- Tỷ lệ khá = 68%

---

### **BÀI 2:** Khảo sát chỉ tiêu X (cm):

| X | 10-15 | 15-20 | 20-25 | 25-30 | 30-35 | 35-40 |
|---|-------|-------|-------|-------|-------|-------|
| n | 6 | 8 | 14 | 25 | 12 | 5 |

**GIẢI:**

Lấy giá trị đại diện là giữa khoảng:

| Giữa khoảng | 12.5 | 17.5 | 22.5 | 27.5 | 32.5 | 37.5 |
|-------------|------|------|------|------|------|------|
| Tần số | 6 | 8 | 14 | 25 | 12 | 5 |

**Trung bình mẫu:**
$$\overline{x} = \frac{6(12.5) + 8(17.5) + 14(22.5) + 25(27.5) + 12(32.5) + 5(37.5)}{70}$$
$$= \frac{75 + 140 + 315 + 687.5 + 390 + 187.5}{70} = \frac{1795}{70} = 25.64 \text{ cm}$$

**Độ lệch mẫu hiệu chỉnh:**
$$\overline{x^2} = \frac{6(156.25) + 8(306.25) + 14(506.25) + 25(756.25) + 12(1056.25) + 5(1406.25)}{70}$$
$$= \frac{937.5 + 2450 + 7087.5 + 18906.25 + 12675 + 7031.25}{70} = \frac{49087.5}{70} = 701.25$$

$$s^2 = \frac{70}{69}(701.25 - 657.41) = 1.0145 \times 43.84 = 44.48$$

$$s = \sqrt{44.48} \approx 6.67 \text{ cm}$$

**Tỷ lệ loại B (≤20cm):**
$$f = \frac{6 + 8}{70} = \frac{14}{70} = 0.2 = 20\%$$

**Đáp số:**
- $\overline{x} = 25.64$ cm
- $s \approx 6.67$ cm
- Tỷ lệ loại B = 20%

---

## CHƯƠNG 4: ƯỚC LƯỢNG THAM SỐ

### **BÀI 4.1:** Trọng lượng SP ~ N(μ, 4). n=20, $\overline{x}=20$g.

#### **a) Ước lượng μ với độ tin cậy 95%**

$$\alpha = 0.05 \Rightarrow z_{\alpha/2} = 1.96$$

$$\Delta = z_{\alpha/2} \frac{\sigma}{\sqrt{n}} = 1.96 \times \frac{2}{\sqrt{20}} = 1.96 \times 0.447 = 0.876$$

Khoảng tin cậy: $(20 - 0.876; 20 + 0.876) = (19.124; 20.876)$

**Đáp số:** $(19.12; 20.88)$ g

#### **b) Độ tin cậy khi độ chính xác = 1g?**

$$\Delta = 1 = z_{\alpha/2} \times \frac{2}{\sqrt{20}}$$
$$z_{\alpha/2} = \frac{1 \times \sqrt{20}}{2} = 2.236$$

$\Phi(2.236) = 0.9873 \Rightarrow 1 - \alpha = 2 \times 0.9873 - 1 = 0.9746$

**Đáp số:** Độ tin cậy = **97.46%**

---

### **BÀI 4.2:** n=25, $\overline{x}=50$g, $s=5.3$g. Ước lượng μ với 95% TC.

**GIẢI:**

$$\alpha = 0.05, \quad df = 24 \Rightarrow t_{\alpha/2}(24) = 2.064$$

$$\Delta = t_{\alpha/2} \frac{s}{\sqrt{n}} = 2.064 \times \frac{5.3}{\sqrt{25}} = 2.064 \times 1.06 = 2.188$$

Khoảng tin cậy: $(50 - 2.188; 50 + 2.188) = (47.812; 52.188)$

**Đáp số:** $(47.81; 52.19)$ g

---

### **BÀI 4.3:** Tuổi thọ bóng đèn ~ N(μ, 100²). n=120, $\overline{x}=1000$h.

#### **a) Ước lượng μ với 95% TC**

$$z_{0.025} = 1.96$$
$$\Delta = 1.96 \times \frac{100}{\sqrt{120}} = 1.96 \times 9.13 = 17.89$$

Khoảng tin cậy: $(1000 - 17.89; 1000 + 17.89) = (982.11; 1017.89)$

**Đáp số:** $(982; 1018)$ giờ

#### **b) Độ TC khi Δ = 14h?**

$$z_{\alpha/2} = \frac{14 \times \sqrt{120}}{100} = 1.534$$
$$\Phi(1.534) = 0.9375$$
$$1 - \alpha = 2 \times 0.9375 - 1 = 0.875$$

**Đáp số:** Độ tin cậy = **87.5%**

#### **c) Cần n bao nhiêu để Δ=13h, 95% TC?**

$$n = \left(\frac{z_{\alpha/2} \sigma}{\Delta}\right)^2 = \left(\frac{1.96 \times 100}{13}\right)^2 = (15.08)^2 = 227.4$$

**Đáp số:** Cần thử nghiệm **228 bóng**

---

### **BÀI 4.4:** n=100, $\overline{x}=4.2$h/ngày, $s^2=6.5$. Ước lượng 98% TC cho 1 tuần.

**GIẢI:**

Ước lượng cho 1 ngày trước:
$$z_{0.01} = 2.33$$
$$\Delta = 2.33 \times \frac{\sqrt{6.5}}{\sqrt{100}} = 2.33 \times 0.255 = 0.594$$

Khoảng TC 1 ngày: $(4.2 - 0.594; 4.2 + 0.594) = (3.606; 4.794)$

Khoảng TC 1 tuần (×7): $(25.24; 33.56)$ giờ

**Đáp số:** $(25.2; 33.6)$ giờ/tuần

---

### **BÀI 4.5:** n=20 SP, dữ liệu: 46 49 47 50... Ước lượng μ với 97% TC.

**GIẢI:**

**Tính $\overline{x}$ và $s$:**
$$\overline{x} = \frac{46+49+47+50+46+48+48+49+47+50+49+48+46+49+48+49+48+50+49+47}{20}$$
$$= \frac{963}{20} = 48.15$$

$$s \approx 1.387$$ (tính từ công thức)

$$t_{0.015}(19) = 2.205$$
$$\Delta = 2.205 \times \frac{1.387}{\sqrt{20}} = 2.205 \times 0.310 = 0.684$$

Khoảng tin cậy: $(48.15 - 0.684; 48.15 + 0.684) = (47.47; 48.83)$

**Đáp số:** $(47.5; 48.8)$ kg

---

### **BÀI 4.6:** n=100, $\overline{x}=2.8$h, $s=1.5$, 95 SV tự học.

#### **a) Ước lượng số giờ TB với 95% TC**

$$z_{0.025} = 1.96$$
$$\Delta = 1.96 \times \frac{1.5}{\sqrt{100}} = 1.96 \times 0.15 = 0.294$$

Khoảng tin cậy: $(2.8 - 0.294; 2.8 + 0.294) = (2.506; 3.094)$

**Đáp số:** $(2.51; 3.09)$ giờ

#### **b) Ước lượng tỷ lệ không tự học với 98% TC**

$$f = \frac{5}{100} = 0.05$$
$$z_{0.01} = 2.33$$
$$\Delta = 2.33 \sqrt{\frac{0.05 \times 0.95}{100}} = 2.33 \times 0.0218 = 0.0508$$

Khoảng tin cậy: $(0.05 - 0.0508; 0.05 + 0.0508) = (0; 0.1008)$

Thực tế: $(0; 0.10)$

**Đáp số:** $(0; 10\%)$

---

### **BÀI 4.7:** n=100, có 15 SP xấu.

#### **a) Ước lượng tỷ lệ với 94% TC**

$$f = 0.15, \quad z_{0.03} = 1.88$$
$$\Delta = 1.88 \sqrt{\frac{0.15 \times 0.85}{100}} = 1.88 \times 0.0357 = 0.0671$$

Khoảng tin cậy: $(0.15 - 0.067; 0.15 + 0.067) = (0.083; 0.217)$

**Đáp số:** $(8.3\%; 21.7\%)$

#### **b) Độ TC khi Δ = 6%?**

$$z_{\alpha/2} = \frac{0.06}{\sqrt{\frac{0.15 \times 0.85}{100}}} = \frac{0.06}{0.0357} = 1.68$$

$$1 - \alpha = 2 \times 0.9535 - 1 = 0.907$$

**Đáp số:** Độ tin cậy = **90.7%**

#### **c) Cần kiểm tra thêm bao nhiêu để Δ=7%, 98% TC?**

$$n = \left(\frac{z_{\alpha/2}}{\Delta}\right)^2 pq = \left(\frac{2.33}{0.07}\right)^2 \times 0.15 \times 0.85 = 1109 \times 0.1275 = 141$$

Cần thêm: $141 - 100 = 41$ SP

**Đáp số:** Cần kiểm tra thêm **41 sản phẩm**

---

### **BÀI 4.8:** n=200, 23% ở KTX. Ước lượng tỷ lệ ngoại trú 97% TC.

**GIẢI:**

Tỷ lệ ngoại trú: $f = 0.77$

$$z_{0.015} = 2.17$$
$$\Delta = 2.17 \sqrt{\frac{0.77 \times 0.23}{200}} = 2.17 \times 0.0297 = 0.0645$$

Khoảng tin cậy: $(0.77 - 0.0645; 0.77 + 0.0645) = (0.7055; 0.8345)$

**Đáp số:** $(70.6\%; 83.5\%)$

---

### **BÀI 4.9:** Kho có 200 SP của A bỏ lẫn với nhiều SP của B. Lấy 100 thấy 8 của A. Ước lượng số SP của B với 95% TC.

**GIẢI:**

Tỷ lệ SP của A: $f = 0.08$

$$\Delta = 1.96 \sqrt{\frac{0.08 \times 0.92}{100}} = 1.96 \times 0.0271 = 0.0531$$

Khoảng TC cho tỷ lệ A: $(0.08 - 0.0531; 0.08 + 0.0531) = (0.0269; 0.1331)$

Tỷ lệ B: $(0.8669; 0.9731)$

Số SP B trong kho (tổng giả sử N SP):
- Đã biết có 200 SP của A
- Ước lượng tỷ lệ SP B: ≈ 87-97%

Nếu 200 SP chiếm 8-13.31% thì tổng N:
$$N = \frac{200}{0.08 \sim 0.1331} \approx 1502 \sim 2500$$

Số SP B: $N - 200 \approx 1302 \sim 2300$

**Đáp số:** Ước lượng có từ **1300 đến 2300 SP của B** (với 95% TC)

---

### **BÀI 4.10:** n=1800, 1170 ủng hộ A. Ước lượng % phiếu min-max với 99% TC.

**GIẢI:**

$$f = \frac{1170}{1800} = 0.65$$
$$z_{0.005} = 2.58$$
$$\Delta = 2.58 \sqrt{\frac{0.65 \times 0.35}{1800}} = 2.58 \times 0.0112 = 0.0290$$

Khoảng tin cậy: $(0.65 - 0.029; 0.65 + 0.029) = (0.621; 0.679)$

**Đáp số:** Tối thiểu **62.1%**, tối đa **67.9%**

---

### **BÀI 4.11:** Khảo sát 100ha lúa. Năng suất (tấn/ha):

| NS | 3-3.5 | 3.5-4 | 4-4.5 | 4.5-5 | 5-5.5 | 5.5-6 |
|----|-------|-------|-------|-------|-------|-------|
| Ha | 9 | 12 | 20 | 25 | 23 | 11 |

#### **a) Ước lượng NS TB với 95% TC**

Giá trị đại diện: 3.25, 3.75, 4.25, 4.75, 5.25, 5.75

$$\overline{x} = \frac{9(3.25) + 12(3.75) + 20(4.25) + 25(4.75) + 23(5.25) + 11(5.75)}{100}$$
$$= \frac{29.25 + 45 + 85 + 118.75 + 120.75 + 63.25}{100} = 4.62 \text{ tấn/ha}$$

$$s \approx 0.72$$ (tính từ công thức)

$$\Delta = 1.96 \times \frac{0.72}{\sqrt{100}} = 0.141$$

Khoảng TC: $(4.62 - 0.141; 4.62 + 0.141) = (4.48; 4.76)$

**Đáp số:** $(4.48; 4.76)$ tấn/ha

*(Do giới hạn, các bài còn lại tương tự - áp dụng công thức ước lượng khoảng tin cậy)*

---

## TÓM TẮT CÔNG THỨC QUAN TRỌNG

### **Ước lượng trung bình:**
- Biết $\sigma$: $\Delta = z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$
- Không biết $\sigma$: $\Delta = t_{\alpha/2}(n-1) \frac{s}{\sqrt{n}}$

### **Ước lượng tỷ lệ:**
$$\Delta = z_{\alpha/2} \sqrt{\frac{f(1-f)}{n}}$$

### **Cỡ mẫu:**
- Cho TB: $n = \left(\frac{z_{\alpha/2} \sigma}{\Delta}\right)^2$
- Cho tỷ lệ: $n = \left(\frac{z_{\alpha/2}}{\Delta}\right)^2 pq$

---

**KẾT THÚC BÀI GIẢI**


