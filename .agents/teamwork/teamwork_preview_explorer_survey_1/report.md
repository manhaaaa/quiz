# Báo Cáo Khảo Sát Chi Tiết Bài Giảng 1 Đến 5 (Lectures 1 - 5)
**Dự án:** C++ & DSA Interactive Quiz Game  
**Thực hiện bởi:** Survey Explorer 1 (`teamwork_preview_explorer_survey_1`)  
**Ngày hoàn thành:** 2026-10-28  
**Thư mục làm việc:** `D:\c++\quiz_game\.agents\teamwork\teamwork_preview_explorer_survey_1`

---

## 1. Đánh Giá Công Cụ & Phương Pháp Trích Xuất Dữ Liệu Slide

### 1.1 Hiện Trạng Tệp Dữ Liệu Slide 1 - 5
Thư mục nguồn `D:\c++\drive-download-20261028T155811Z-1-001` gồm cả hai định dạng:
1. **Lecture 1 - Introduction.ppt** (2.47 MB, định dạng nhị phân OLE2 Compound Document, 41 slide)
2. **Lecture 2 - Basic C++ language.pptx** (677 KB, định dạng nén OpenXML ZIP, 45 slide)
3. **Lecture 3 - class in C++.ppt** (824 KB, định dạng nhị phân OLE2 Compound Document, 43 slide)
4. **Lecture 4 - Analysis algorithms.ppt** (663 KB, định dạng nhị phân OLE2 Compound Document, 33 slide)
5. **Lecture 5 -  Recursive.pptx** (294 KB, định dạng nén OpenXML ZIP, 25 slide)

**Tổng số slide khảo sát:** 41 + 45 + 43 + 33 + 25 = **187 slide**.

### 1.2 Kết Quả Khảo Sát Các Công Cụ Trích Xuất Trên Hệ Thống Windows
Đã kiểm tra trực tiếp các môi trường xử lý có sẵn trên máy:
1. **`python-pptx` (Version 1.0.2 - Đã cài đặt sẵn trong Python 3.11):**
   - Hỗ trợ trực tiếp cực tốt với tệp `.pptx` (Lecture 2 và Lecture 5).
   - Không hỗ trợ đọc trực tiếp tệp `.ppt` nhị phân cổ điển (sẽ báo lỗi `PackageNotFoundError: file is not a zip file`).
2. **`PowerPoint.Application` COM Automation (qua PowerShell hoặc Python `win32com` / `comtypes`):**
   - Hệ thống Windows đã cài đặt Microsoft Office / PowerPoint đầy đủ.
   - Thử nghiệm COM Object `New-Object -ComObject PowerPoint.Application` hoạt động hoàn hảo 100%, không bị giới hạn định dạng, mở và đọc chính xác cả `.ppt` và `.pptx`.
   - Có thể truy xuất toàn bộ text trong từng Shape (`$shape.TextFrame.TextRange.Text`), tiêu đề slide, bảng biểu và ghi chú (Notes).
   - Tốc độ xử lý: Trích xuất toàn bộ 187 slide của 5 bài giảng chỉ mất chưa đầy 6 giây.
3. **Lưu ý Mã Hóa Ký Tự Tiếng Việt (UTF-8 vs CP1252):**
   - Nội dung slide chứa tiếng Việt đầy đủ dấu thanh.
   - Khi xuất từ PowerShell ra JSON cần chỉ định `-Encoding utf8`.
   - Khi đọc bằng Python cần dùng `encoding='utf-8-sig'` hoặc `encoding='utf-8'` và thiết lập `sys.stdout.reconfigure(encoding='utf-8')` để tránh lỗi `charmap UnicodeEncodeError` trên console Windows cp1252.

---

## 2. Phân Tích Nội Dung & Chủ Đề Câu Hỏi Topic 1: Tổng Quan Môn Học & Cấu Trúc Dữ Liệu, Giải Thuật (Lecture 1)

### 2.1 Tóm Tắt Nội Dung Cốt Lõi Từ Slide (41 Slide)
- **Thông tin môn học:** Cấu trúc dữ liệu và giải thuật trong C++ (Data Structures and Algorithms In C++), GV Nguyễn Việt Hưng (hungnv@utc.edu.vn - ĐH Giao thông Vận tải).
- **Mục đích:** Cung cấp nền tảng lưu trữ dữ liệu hiệu quả trong bộ nhớ máy tính, phân tích chi phí thời gian (Time complexity) và không gian bộ nhớ (Space complexity), rèn luyện kỹ năng chọn lựa và cài đặt cấu trúc dữ liệu và giải thuật cho các hệ thống phần mềm lớn.
- **Tài liệu tham khảo tiêu biểu:** Goodrich & Tamassia (DSA in C++), Cormen CLRS (Introduction to Algorithms), Lê Minh Hoàng (ĐH Sư phạm Hà Nội), Đỗ Xuân Lôi, Phạm Văn Ất (OOP & C++).
- **Định nghĩa Dữ liệu (Data):** Là các thông tin cần thiết biểu diễn bài toán trên máy tính, gồm: dữ liệu đầu vào (Input), dữ liệu trung gian, dữ liệu đầu ra (Output).
- **Định nghĩa Cấu trúc dữ liệu (Data Structure):** Cách tổ chức, quản lý và lưu trữ dữ liệu trong bộ nhớ máy tính cho phép truy cập và sửa đổi hiệu quả.
- **3 Đặc điểm cốt lõi của một CTDL:**
  1. *Tính đúng đắn (Correctness):* Thực thi chính xác các thao tác hỗ trợ.
  2. *Độ phức tạp thời gian (Time complexity):* Thời gian xử lý công việc nhỏ nhất có thể.
  3. *Độ phức tạp bộ nhớ (Space complexity):* Lượng bộ nhớ sử dụng càng nhỏ càng tốt.
- **Phân loại CTDL:**
  - *Dữ liệu không có cấu trúc (kiểu đơn lẻ / cơ sở):* `int`, `char`, `float`, `bool`...
  - *Dữ liệu có cấu trúc:* Cấu thành từ các phần tử cơ sở: Mảng (`array` 1 chiều, 2 chiều), Chuỗi (`string`), Bản ghi (`record` / `struct`), Đối tượng (`object`), Danh sách (`collection`).
- **Khái niệm Giải thuật (Algorithm):** Là tập hữu hạn có thứ tự các bước tác động lên dữ liệu để sau một số hữu hạn lần thực hiện sẽ cho ta kết quả. Giải thuật mang tính độc lập với ngôn ngữ lập trình.
- **5 Đặc trưng của một Giải thuật:**
  1. *Đầu vào (Input):* Có 0 hoặc nhiều dữ liệu vào xác định.
  2. *Đầu ra (Output):* Có ít nhất 1 kết quả ra.
  3. *Tính chính xác (Precision):* Các bước thực hiện được mô tả rõ ràng, chính xác.
  4. *Tính hữu hạn (Finiteness):* Phải dừng sau một số hữu hạn bước với mọi đầu vào.
  5. *Tính đơn trị (Uniqueness):* Kết quả trung gian của từng bước được xác định duy nhất, chỉ phụ thuộc đầu vào và các bước trước.
  6. *Tính tổng quát (Generality):* Áp dụng được cho mọi bài toán có dạng đã cho.
- **4 Phương pháp biểu diễn giải thuật:**
  1. *Ngôn ngữ tự nhiên:* Đơn giản, dễ hiểu nhưng dài dòng, không có cấu trúc chuẩn, dễ đa nghĩa.
  2. *Lưu đồ (Flowchart):* Trực quan, rõ ràng đường đi logic nhưng cồng kềnh với thuật toán lớn.
  3. *Mã giả (Pseudocode):* Cấu trúc chuẩn hóa, dùng ký hiệu toán học và biến/hàm, súc tích hơn lưu đồ.
  4. *Ngôn ngữ lập trình (Programming language):* Máy tính thực thi trực tiếp được.
- **Phương trình kinh điển Niklaus Wirth:**
  $$\text{Cấu trúc dữ liệu} + \text{Giải thuật} = \text{Chương trình}$$
  *(Data Structures + Algorithms = Programs)*
- **5 Thao tác cơ bản trên CTDL:**
  1. *Search (Tìm kiếm):* Tìm 1 phần tử thỏa mãn điều kiện.
  2. *Sort (Sắp xếp):* Sắp xếp các phần tử theo thứ tự xác định.
  3. *Insert (Chèn):* Bổ sung một phần tử mới vào cấu trúc.
  4. *Update (Cập nhật):* Sửa đổi giá trị của một phần tử.
  5. *Delete (Xóa):* Loại bỏ một phần tử khỏi cấu trúc.

---

### 2.2 15 Chủ Đề Câu Hỏi Ứng Viên (Candidate Question Themes) - Topic 1

1. **Định nghĩa Cấu trúc dữ liệu:** Khái niệm chuẩn về CTDL theo khoa học máy tính (tổ chức, lưu trữ và quản lý dữ liệu trong bộ nhớ để truy cập và sửa đổi hiệu quả).
2. **Ba tiêu chuẩn đánh giá CTDL:** Tính đúng đắn (correctness), chi phí thời gian (time complexity), chi phí không gian/bộ nhớ (space complexity).
3. **Phân biệt kiểu dữ liệu cơ sở và có cấu trúc:** Nhận diện kiểu đơn (int, char, float, bool) so với kiểu có cấu trúc (array, struct, string, class).
4. **Định nghĩa Giải thuật (Algorithm):** Bản chất của thuật toán là tập hữu hạn các bước có thứ tự, độc lập với ngôn ngữ lập trình.
5. **Đặc trưng Tính hữu hạn (Finiteness):** Ý nghĩa của việc giải thuật bắt buộc phải kết thúc sau một số hữu hạn bước tính toán.
6. **Đặc trưng Tính đơn trị (Uniqueness):** Tại mỗi bước của giải thuật, kết quả được xác định rõ ràng, duy nhất từ dữ liệu trước đó, không gây mập mờ.
7. **Đặc trưng Tính tổng quát (Generality):** Thuật toán giải quyết một lớp các bài toán cùng dạng chứ không chỉ áp dụng cho một bộ dữ liệu cụ thể.
8. **Đặc trưng Đầu vào và Đầu ra:** Một giải thuật có thể nhận bao nhiêu đầu vào ($\ge 0$) và tạo ra bao nhiêu đầu ra ($\ge 1$).
9. **So sánh 4 cách biểu diễn giải thuật:** Ưu/nhược điểm giữa ngôn ngữ tự nhiên, lưu đồ khối (flowchart), mã giả (pseudocode), và mã nguồn lập trình.
10. **Ký hiệu chuẩn trong Lưu đồ khối:** Ý nghĩa hình chữ nhật (thao tác/xử lý), hình thoi (điều kiện rẽ nhánh), hình bình hành (nhập/xuất dữ liệu), hình oval/elip (bắt đầu/kết thúc).
11. **Mã giả (Pseudocode) và đặc điểm:** Ngôn ngữ tựa lập trình không phụ thuộc cú pháp cứng nhắc của trình biên dịch cụ thể, giàu cấu trúc hơn ngôn ngữ tự nhiên.
12. **Phương trình Niklaus Wirth:** Công thức nền tảng của khoa học máy tính: Programs = Data Structures + Algorithms.
13. **Năm thao tác cơ bản trên cấu trúc dữ liệu:** Nhận diện và phân biệt vai trò của Search, Sort, Insert, Update, Delete.
14. **Phân loại dữ liệu máy tính trong giải bài toán:** Nhận biết 3 nhóm dữ liệu: đầu vào (input), dữ liệu trung gian, và đầu ra (output).
15. **Mối liên hệ giữa CTDL và Giải thuật:** Cùng một bài toán nhưng chọn cấu trúc dữ liệu khác nhau sẽ dẫn đến các giải thuật và hiệu năng hoàn toàn khác nhau.

---

## 3. Phân Tích Nội Dung & Chủ Đề Câu Hỏi Topic 2: Ngôn Ngữ C++ Cơ Bản (Lecture 2)

### 3.1 Tóm Tắt Nội Dung Cốt Lõi Từ Slide (45 Slide)
- **Lý do chọn C++ cho môn CTDL&GT:** Cung cấp cái nhìn bản chất, hiểu cơ chế cấp phát, truy cập vùng nhớ con trỏ, rèn luyện tư duy logic nền tảng vững chắc.
- **Các tính năng mở rộng của C++ so với C:**
  - Nhập xuất luồng: `cin >>`, `cout <<`, thư viện `<iostream>`, `<iomanip>`, `<bits/stdc++.h>`.
  - Tham chiếu (References `&`): Tạo bí danh (alias) cho ô nhớ.
  - Tham số mặc định của hàm (Default parameters).
  - Nạp chồng hàm (Function overloading).
  - Hàm mẫu (Function templates `template <class T>`).
  - Hướng đối tượng: Kiểu lớp (`class`), đóng gói, kế thừa, đa hình.
- **Biến & Ô nhớ:**
  - Mọi biến đều có 2 thông tin: Giá trị (Value) và Địa chỉ ô nhớ (Address).
  - Toán tử lấy địa chỉ: `&variable`.
- **Con trỏ (Pointers):**
  - Con trỏ là biến chứa địa chỉ ô nhớ của một biến khác.
  - Cú pháp khai báo: `type *pointer_name;` trong đó `type` là kiểu dữ liệu của ô nhớ được trỏ tới, không phải kiểu của bản thân con trỏ.
  - Toán tử giải tham chiếu (Dereference operator `*`): Lấy hoặc ghi giá trị tại địa chỉ ô nhớ mà con trỏ trỏ tới (`*p = 10;`).
  - Cấp phát động: `p = new DataType;`
  - Hủy bộ nhớ động: `delete p;`
  - Con trỏ chưa khởi tạo hoặc giải phóng xong không trỏ tới đâu dễ gây lỗi undefined behavior / dangling pointer.
- **Số học con trỏ (Pointer Arithmetic):**
  - Chỉ cho phép phép toán cộng (`+`) và trừ (`-`), phép tăng (`++`), giảm (`--`).
  - Khi tăng `p++`, địa chỉ tăng thêm một lượng bằng đúng `sizeof(*p)` bytes (ví dụ: `char*` tăng 1 byte, `short*` tăng 2 bytes, `int*`/`long*` tăng 4 hoặc 8 bytes).
- **Mảng 1 chiều và mối quan hệ với con trỏ:**
  - Tên mảng là một con trỏ hằng (constant pointer) trỏ tới địa chỉ phần tử đầu tiên của mảng (`a == &a[0]`).
  - Công thức truy xuất tương đương: `*(a + i) == a[i]`.
  - Không thể thực hiện phép gán thay đổi địa chỉ của tên mảng (`a = p;` là sai), nhưng con trỏ thông thường thì gán được (`p = a;`).
- **Con trỏ trỏ đến con trỏ (Pointer to Pointer):**
  - Khai báo: `int **ptr_ptr;`
  - Chứa địa chỉ của một biến con trỏ khác. Giải tham chiếu cấp 1 `*q` cho ra địa chỉ của biến thực; cấp 2 `**q` cho ra giá trị biến thực.
- **Cấp phát động mảng 2 chiều:**
  - Bước 1: Cấp phát mảng gồm $m$ con trỏ hàng: `int **a = new int*[m];`
  - Bước 2: Duyệt vòng lặp cấp phát từng hàng gồm $n$ phần tử: `for (int i=0; i<m; i++) a[i] = new int[n];`
  - Giải phóng bộ nhớ mảng 2 chiều: Duyệt từng hàng `delete[] a[i];` rồi mới `delete[] a;`.
- **Hàm và Cơ chế truyền tham số:**
  - *Truyền tham trị (Pass-by-value):* Tạo bản sao, hàm không thể thay đổi giá trị của biến gốc bên ngoài.
  - *Truyền tham chiếu (Pass-by-reference `DataType &arg`):* Hàm dùng trực tiếp ô nhớ của biến gốc. Thay đổi trong hàm tác động trực tiếp ra ngoài (ví dụ hàm `swap(int &a, int &b)`).
  - *Đặc điểm tham chiếu:* Phải được khởi tạo ngay khi khai báo; không thể trỏ sang biến khác sau khi đã gắn; không có khái niệm tham chiếu null.
  - *Truyền tham chiếu trong vòng lặp:* `for (char &z : x) z = toupper(z);`
- **Hàm có đối mặc định (Default Arguments):**
  - Cú pháp: `DataType Func(DataType a, DataType b = val);`
  - Quy tắc: Các đối số có giá trị mặc định phải nằm liên tục ở cuối danh sách tham số.
  - Khi gọi, các đối số không truyền sẽ tự động lấy giá trị mặc định.
- **Nạp chồng hàm (Function Overloading):**
  - Cho phép nhiều hàm trong cùng một phạm vi có cùng tên.
  - Điều kiện: Danh sách tham số phải khác nhau về **số lượng tham số** hoặc **kiểu dữ liệu tham số** (hoặc thứ tự kiểu).
  - *Lưu ý quan trọng:* Chỉ khác nhau về kiểu trả về (return type) thì **không** được coi là nạp chồng hợp lệ và sẽ gây lỗi biên dịch.
- **Hàm mẫu (Function Templates):**
  - Cú pháp: `template <class T>` hoặc `template <typename T>`.
  - Giúp viết hàm tổng quát hoạt động với nhiều kiểu dữ liệu khác nhau (`int`, `float`, `double`, `long long`...).
  - Ví dụ: `template <class T> T GetMax(T a, T b) { return (a > b) ? a : b; }`.
  - Gọi hàm: Có thể để trình biên dịch tự suy luận kiểu `GetMax(5, 6)` hoặc ép kiểu tường minh `binhphuong<long long>(1234567)`.

---

### 3.2 15 Chủ Đề Câu Hỏi Ứng Viên (Candidate Question Themes) - Topic 2

1. **Khái niệm và cú pháp con trỏ trong C++:** Ý nghĩa ký hiệu `*` trong khai báo và toán tử giải tham chiếu `*p`.
2. **Toán tử lấy địa chỉ `&`:** Phân biệt ý nghĩa của `&` khi lấy địa chỉ của biến (`&x`) so với khai báo tham chiếu (`int &r = x;`).
3. **Cấp phát và giải phóng bộ nhớ động:** Cú pháp `new` và `delete` cho biến đơn; `new[]` và `delete[]` cho mảng động. Lỗi rò rỉ bộ nhớ (memory leak).
4. **Quy tắc số học con trỏ (Pointer Arithmetic):** Phép toán `p + k` dịch chuyển địa chỉ bao nhiêu bytes dựa trên `sizeof(*p)`.
5. **Mối quan hệ giữa Mảng và Con trỏ:** Biểu thức tương đương giữa `a[i]` và `*(a + i)`. Bản chất con trỏ hằng của tên mảng.
6. **Con trỏ trỏ đến con trỏ (`Pointer-to-Pointer`):** Cú pháp `int **pp`, cơ chế giải tham chiếu 2 lần để đọc và sửa giá trị đích.
7. **Kỹ thuật cấp phát động mảng 2 chiều:** Thứ tự cấp phát mảng con trỏ `new int*[rows]` và từng hàng `new int[cols]`, cùng thứ tự giải phóng `delete[]`.
8. **Tham số tham chiếu (Pass-by-reference):** Cơ chế chia sẻ ô nhớ của tham số hàm, viết hàm hoán vị `swap(int &a, int &b)`.
9. **Duyệt và biến đổi chuỗi/mảng bằng tham chiếu:** Phân tích đoạn code `for (char &c : str) c = toupper(c);` và so sánh khi không dùng `&`.
10. **Quy tắc đặt tham số mặc định (Default Arguments):** Vị trí bắt buộc của các tham số có giá trị mặc định (phải nằm ở cuối danh sách đối số).
11. **Cách gọi hàm có tham số mặc định:** Kết quả trả về khi gọi hàm bỏ qua một số hoặc toàn bộ các đối mặc định.
12. **Điều kiện nạp chồng hàm (Function Overloading):** Các tiêu chí hợp lệ (khác số lượng hoặc kiểu tham số) và lỗi biên dịch khi chỉ khác kiểu trả về.
13. **Truyền đối số mơ hồ khi nạp chồng (Ambiguous call):** Tình huống biên dịch báo lỗi khi kết hợp nạp chồng hàm với tham số mặc định hoặc chuyển đổi kiểu ngầm định.
14. **Cú pháp và cơ chế Hàm mẫu (Template function):** Cách định nghĩa `template <typename T>` và cách trình biên dịch sinh mã (instantiation) cho từng kiểu dữ liệu.
15. **Gọi hàm mẫu tường minh và ngầm định:** Cú pháp chỉ định kiểu `func<double>(x, y)` so với việc trình biên dịch tự động suy diễn kiểu (type deduction).

---

## 4. Phân Tích Nội Dung & Chủ Đề Câu Hỏi Topic 3: Lớp và Hướng Đối Tượng Trong C++ (Lecture 3)

### 4.1 Tóm Tắt Nội Dung Cốt Lõi Từ Slide (43 Slide)
- **So sánh Lập trình Hướng thủ tục (POP) vs Hướng đối tượng (OOP):**
  - Cả hai đều áp dụng phương pháp tinh chỉnh từng bước (stepwise refinement).
  - *POP:* Tập trung vào hàm (functions), phân rã chức năng. Cấu trúc dữ liệu cụ thể phải định nghĩa sớm, khó thay đổi khi yêu cầu mở rộng.
  - *OOP:* Tập trung vào các đối tượng trừu tượng (abstract objects). Dữ liệu và hành vi được đóng gói trong một thực thể. Dễ tái sử dụng và bảo trì.
- **Khái niệm Lớp (Class) và Đối tượng (Object):**
  - Lớp là sự mở rộng của cấu trúc dữ liệu (`struct`), bao gồm các thuộc tính (data members) và phương thức (member functions/methods).
  - Lớp đóng vai trò là một kiểu dữ liệu do người dùng định nghĩa; Đối tượng là một thể hiện cụ thể (instance / biến) của lớp đó.
- **Đặc tả truy nhập (Access Specifiers):**
  - `private`: Chỉ các phương thức trong cùng lớp (hoặc hàm bạn `friend`) mới được truy cập trực tiếp. Mặc định trong `class` là `private`.
  - `public`: Có thể truy cập từ bất kỳ đâu bên ngoài lớp thông qua đối tượng.
  - `protected`: Cho phép truy cập trong nội bộ lớp và các lớp con kế thừa.
- **Cài đặt phương thức:**
  - *Cài đặt bên trong lớp:* Tự động xem là hàm nội tuyến (`inline`). Không nên chứa các vòng lặp phức tạp.
  - *Cài đặt bên ngoài lớp:* Dùng toán tử định phạm vi (scope resolution operator `::`):
    `Return_Type ClassName::MethodName(ArgumentList) { ... }`
- **Truy cập thành phần lớp:**
  - Biến đối tượng trên Stack: Dùng dấu chấm `.` (ví dụ: `rect.area()`).
  - Con trỏ đối tượng trên Heap: Dùng dấu mũi tên `->` (ví dụ: `rect->area()`). Cần cấp phát qua `new` trước khi dùng và giải phóng qua `delete`.
- **Hàm khởi tạo (Constructor - Cấu tử):**
  - Hàm đặc biệt cùng tên với lớp, không có kiểu trả về (kể cả `void`).
  - Tự động gọi khi một đối tượng được tạo ra. Dùng để khởi tạo giá trị thuộc tính và cấp phát bộ nhớ.
  - Nạp chồng cấu tử: Cấu tử không đối (Default Constructor), cấu tử có tham số (Parameterized Constructor).
- **Hàm hủy (Destructor - Hủy tử):**
  - Tên trùng với lớp nhưng có dấu ngã phía trước `~ClassName()`.
  - Không có kiểu trả về, không nhận bất kỳ tham số nào $\rightarrow$ Trong một lớp chỉ có duy nhất 1 hàm hủy (không thể nạp chồng).
  - Tự động gọi khi đối tượng bị hủy (ra khỏi block scope hoặc bị gọi lệnh `delete`).
  - Bắt buộc phải giải phóng các vùng nhớ động mà lớp sở hữu (ví dụ `delete[] element;`).
- **Con trỏ `this`:**
  - Mọi phương thức không tĩnh (non-static member function) đều có một tham số ẩn là con trỏ `this`.
  - `this` trỏ trực tiếp đến địa chỉ của đối tượng đang gọi phương thức.
  - Cú pháp truy xuất: `this->propertyName` hoặc trực tiếp `propertyName`. Thường dùng để phân biệt khi tên tham số trùng tên thuộc tính, hoặc trả về đối tượng hiện tại `return *this;`.
- **Lớp mẫu (Template Class):**
  - Định nghĩa lớp tổng quát cho kiểu dữ liệu chưa xác định trước: `template <class T, class Y> class CPair`.
  - Cú pháp khai báo đối tượng: `CPair<int, float> myObj(100, 75.5);`.
  - Cài đặt phương thức bên ngoài: `template <class T, class Y> T CPair<T, Y>::getmax() { ... }`.
- **Quá tải toán tử (Operator Overloading):**
  - Cho phép tái định nghĩa hành vi của các toán tử chuẩn C++ cho kiểu lớp do người dùng định nghĩa.
  - Các nhóm toán tử:
    1. *Toán tử một ngôi (Unary):* `++`, `--`, `-` (đổi dấu). Cú pháp: `DataType operator sign();`.
    2. *Toán tử hai ngôi (Binary):* `+`, `-`, `*`, `/`. Cú pháp: `DataType operator sign(ClassType arg);`. Toán hạng trái chính là `*this`.
    3. *Toán tử so sánh:* `==`, `>`, `<`, `!=`... Trả về `bool` hoặc `int`.
    4. *Toán tử nhập xuất luồng (`>>`, `<<`):* Không thể cài đặt dưới dạng phương thức thường vì toán hạng bên trái là đối tượng của luồng (`istream`, `ostream`). Bắt buộc cài đặt bằng **hàm bạn (`friend`)**:
       - `friend istream& operator>>(istream &is, ClassName &obj);`
       - `friend ostream& operator<<(ostream &os, ClassName obj);`
  - Các ví dụ điển hình trong slide: Lớp hình chữ nhật `CRectangle`, lớp ma trận động `CMatrix`, lớp phân số `PS`, lớp điểm mặt phẳng `Point`, đoạn thẳng `Segment`.

---

### 4.2 15 Chủ Đề Câu Hỏi Ứng Viên (Candidate Question Themes) - Topic 3

1. **Sự khác biệt cốt lõi giữa POP và OOP:** Tập trung vào hàm/thuật toán (POP) so với đóng gói dữ liệu và phương thức vào đối tượng (OOP).
2. **Khái niệm Lớp (Class) và Đối tượng (Object):** Mối quan hệ giữa khuôn mẫu (kiểu dữ liệu) và thể hiện cụ thể trong bộ nhớ (biến).
3. **Các từ khóa đặc tả truy xuất trong C++:** Phạm vi và ý nghĩa bảo mật của `private`, `public`, `protected`. Tính chất mặc định là `private` của `class`.
4. **Phân biệt `struct` và `class` trong C++:** Điểm khác biệt duy nhất về quyền truy cập mặc định (`public` trong struct vs `private` trong class).
5. **Toán tử định phạm vi (Scope Resolution Operator `::`):** Cú pháp cài đặt phương thức ngoài định nghĩa lớp và cơ chế liên kết với tên lớp.
6. **Phương thức nội tuyến (Inline methods):** Tác động khi định nghĩa phương thức ngay trong thân lớp và điều kiện không nên dùng (chứa vòng lặp lớn).
7. **Truy cập thành viên qua biến và con trỏ đối tượng:** Phân biệt toán tử dấu chấm `.` cho biến đối tượng và toán tử mũi tên `->` cho con trỏ đối tượng.
8. **Bản chất của Hàm khởi tạo (Constructor):** Tên hàm, đặc điểm không có kiểu trả về, thời điểm tự động kích hoạt và nạp chồng constructor.
9. **Bản chất của Hàm hủy (Destructor):** Ký hiệu `~`, đặc điểm không tham số, tính duy nhất (không nạp chồng) và vai trò thu hồi bộ nhớ động.
10. **Hậu quả khi thiếu hàm hủy trong lớp có con trỏ động:** Nguy cơ rò rỉ bộ nhớ (memory leak) khi đối tượng bị giải phóng nhưng vùng nhớ `new` chưa giải phóng.
11. **Vai trò và kiểu của con trỏ `this`:** Bản chất tham số ngầm định trỏ tới đối tượng hiện tại, cách dùng `this->property` giải quyết xung đột tên.
12. **Cú pháp và cơ chế của Lớp mẫu (Template Class):** Khai báo `template <class T>`, cách truyền tham số kiểu khi khởi tạo đối tượng `CMatrix<float>`.
13. **Quá tải toán tử hai ngôi số học (`+`, `-`, `*`, `/`):** Cách thức nhận tham số, vai trò của toán hạng bên trái (`*this`) và trả về đối tượng mới.
14. **Quá tải toán tử một ngôi tiền tố (`++`, `--`):** Khai báo và cơ chế sửa đổi trạng thái của đối tượng đang gọi.
15. **Quá tải toán tử nhập xuất (`cin >>`, `cout <<`) bằng hàm bạn `friend`:** Giải thích tại sao bắt buộc dùng hàm `friend` và cơ chế trả về tham chiếu luồng `istream&` / `ostream&` để cho phép ghép nối toán tử (`cin >> a >> b`).

---

## 5. Phân Tích Nội Dung & Chủ Đề Câu Hỏi Topic 4: Phân Tích Thuật Toán & Ký Hiệu Big-O (Lecture 4)

### 5.1 Tóm Tắt Nội Dung Cốt Lõi Từ Slide (33 Slide)
- **Khái niệm và Mục tiêu phân tích thuật toán:**
  - Thuật toán là quy trình từng bước giải quyết vấn đề trong thời gian hữu hạn.
  - Hai tài nguyên cần đánh giá:
    1. *Bộ nhớ (Space Complexity):* Dung lượng RAM cần để lưu dữ liệu đầu vào, biến trung gian và đầu ra.
    2. *Thời gian chạy (Running Time Complexity):* Thời gian cần thiết để thuật toán thực thi xong như một hàm phụ thuộc vào kích thước dữ liệu vào $n$.
- **Ba trường hợp phân tích thời gian chạy:**
  - *Trường hợp xấu nhất (Worst-case):* Thời gian lớn nhất trên mọi bộ dữ liệu vào kích thước $n$. Thường được chọn vì dễ xác định và cung cấp cận trên đảm bảo cho hệ thống.
  - *Trường hợp trung bình (Average-case):* Thời gian kỳ vọng trên phân phối dữ liệu vào; thường rất khó tính toán do phải xác định phân phối xác suất.
  - *Trường hợp tốt nhất (Best-case):* Thời gian nhỏ nhất; ít có ý nghĩa thực tế khi đánh giá hiệu năng an toàn.
- **Hai phương pháp đánh giá thuật toán:**
  - *Phương pháp thực nghiệm (Experimental):*
    - Cài đặt chương trình, chạy với các kích thước đầu vào khác nhau, dùng đồng hồ đo thời gian, vẽ đồ thị.
    - *Hạn chế:* Phải code hoàn chỉnh; kết quả phụ thuộc cấu hình phần cứng, hệ điều hành, trình biên dịch; chỉ đánh giá được trên một số bộ dữ liệu hữu hạn đã thử nghiệm.
  - *Phương pháp phân tích lý thuyết (Theoretical):*
    - Dùng mã giả (Pseudocode) ở mức trừu tượng cao; không phụ thuộc phần cứng hay ngôn ngữ lập trình.
    - Đánh giá thời gian dưới dạng hàm số $T(n)$ phụ thuộc vào kích thước dữ liệu vào $n$, bao quát mọi trường hợp đầu vào.
- **Mô hình máy tính RAM (Random Access Machine Model):**
  - Gồm 1 CPU và bộ nhớ ô nhớ không giới hạn.
  - Mỗi ô nhớ lưu trữ một số nguyên hoặc một ký tự.
  - Truy nhập vào bất kỳ ô nhớ nào đều tiêu tốn một đơn vị thời gian cố định ($O(1)$).
- **Phép toán cơ sở (Primitive Operations):**
  - Các phép toán cơ bản: Định giá biểu thức, phép gán biến, truy xuất phần tử mảng, so sánh, gọi hàm, lệnh `return`.
  - Mỗi phép toán cơ sở được giả định thực hiện trong một khoảng thời gian hằng số cố định $[a, b]$.
- **Bảy hàm quan trọng xếp theo tốc độ tăng trưởng:**
  1. Hằng số: $O(1)$
  2. Logarit: $O(\log n)$
  3. Tuyến tính: $O(n)$
  4. N-log-N: $O(n \log n)$
  5. Bậc hai (Quadratic): $O(n^2)$
  6. Bậc ba (Cubic): $O(n^3)$
  7. Hàm mũ: $O(2^n)$
  *(Trên biểu đồ log-log, độ dốc của đường thẳng phản ánh cấp bậc tăng trưởng của thuật toán).*
- **Định nghĩa toán học của Ký hiệu Ô-lớn (Big-Oh Notation):**
  - Cho hai hàm $f(n)$ và $g(n)$, ta nói $f(n)$ là $O(g(n))$ nếu tồn tại hằng số thực dương $c > 0$ và số nguyên $n_0 \ge 1$ sao cho:
    $$f(n) \le c \cdot g(n), \quad \forall n \ge n_0$$
  - Big-Oh thể hiện **cận trên tiệm cận (asymptotic upper bound)** của tốc độ phát triển hàm.
  - Ví dụ: $2n + 10$ là $O(n)$ (chọn $c = 3, n_0 = 10$). Ngược lại, $n^2$ không thể là $O(n)$ vì không tồn tại hằng số $c$ cố định để $n \le c$ với mọi $n$ lớn tùy ý.
- **Quy tắc xác định Big-Oh:**
  - Nếu $f(n)$ là đa thức bậc $d$: $f(n) = a_d n^d + \dots + a_1 n + a_0$ thì $f(n)$ là $O(n^d)$.
  - *Bỏ qua các hệ số hằng:* $100n$ vẫn là $O(n)$.
  - *Bỏ qua các số hạng bậc thấp:* $3n^3 + 20n^2 + 5$ là $O(n^3)$.
  - Luôn chọn lớp hàm đơn giản nhất và nhỏ nhất (chặt nhất): Nói $2n$ là $O(n)$ thay vì $O(n^2)$.
- **Ví dụ điển hình phân tích thuật toán: Prefix Averages (Trung bình cộng tiền tố):**
  - Bài toán: Cho mảng $X$ có $n$ phần tử, tính mảng $A$ với $A[i] = \frac{1}{i+1} \sum_{j=0}^{i} X[j]$.
  - *Thuật toán 1 (Bậc hai):* Duyệt $i$ từ $0 \dots n-1$, với mỗi $i$ lại dùng vòng lặp $j$ từ $1 \dots i$ để cộng dồn.
    - Tổng phép tính: $T(n) = 2n^2 + 8n + 4$.
    - Độ phức tạp thời gian: $O(n^2)$.
  - *Thuật toán 2 (Tuyến tính):* Duyệt $i$ từ $0 \dots n-1$, duy trì một biến tích lũy $s = s + X[i]$.
    - Tổng phép tính: $T(n) = 9n + 5$.
    - Độ phức tạp thời gian: $O(n)$.
    - Kết luận: Cải tiến giải thuật giảm thời gian từ bậc hai xuống tuyến tính, tạo chênh lệch tốc độ khổng lồ khi $n$ lớn.
- **Quy tắc kết hợp khi phân tích đoạn mã:**
  - *Quy tắc cộng (Đoạn mã tuần tự $P_1, P_2$):*
    $$T(n) = O(\max(g(n), f(n)))$$
  - *Quy tắc nhân (Vòng lặp lồng nhau $P_2$ nằm trong $P_1$):*
    $$T(n) = O(g(n) \times f(n))$$

---

### 5.2 15 Chủ Đề Câu Hỏi Ứng Viên (Candidate Question Themes) - Topic 4

1. **Hai khía cạnh tài nguyên của phân tích thuật toán:** Phân biệt độ phức tạp thời gian (Running time) và độ phức tạp không gian (Space complexity).
2. **Ba trường hợp phân tích thời gian (Worst, Average, Best case):** Khái niệm và lý do khoa học máy tính luôn ưu tiên phân tích Worst-case.
3. **So sánh phương pháp thực nghiệm và phương pháp lý thuyết:** Nhược điểm phụ thuộc phần cứng của đo đạc thực nghiệm so với tính độc lập của phân tích lý thuyết.
4. **Mô hình máy tính trừu tượng RAM (Random Access Machine):** Khái niệm CPU đơn, ô nhớ không giới hạn và thời gian truy cập ô nhớ là hằng số $O(1)$.
5. **Nhận diện phép toán cơ sở (Primitive Operations):** Xác định các thao tác tốn thời gian hằng số (gán, so sánh, số học, đánh chỉ số mảng).
6. **Xếp hạng 7 hàm tăng trưởng thông dụng:** Thứ tự tăng dần tốc độ phát triển: $1 < \log n < n < n \log n < n^2 < n^3 < 2^n$.
7. **Định nghĩa hình thức toán học của Big-Oh:** Ý nghĩa của cặp hằng số $(c, n_0)$ trong bất đẳng thức $f(n) \le c \cdot g(n)$ với mọi $n \ge n_0$.
8. **Chứng minh một hàm thuộc lớp Big-Oh:** Tìm cặp giá trị hợp lệ $(c, n_0)$ cho các hàm tuyến tính hoặc đa thức đơn giản (ví dụ: $2n + 10$ là $O(n)$).
9. **Giải thích vì sao hàm bậc cao không thuộc Big-Oh hàm bậc thấp:** Chứng minh toán học vì sao $n^2$ không thể là $O(n)$.
10. **Quy tắc lược bỏ hệ số hằng số:** Tại sao hằng số nhân không làm thay đổi lớp hàm tiệm cận (ví dụ: $10^6 n$ vẫn là $O(n)$).
11. **Quy tắc lược bỏ số hạng bậc thấp trong đa thức:** Xác định bậc cao nhất quyết định độ phức tạp (ví dụ: $5n^3 + 100n^2 + 2000$ là $O(n^3)$).
12. **Áp dụng Quy tắc cộng cho các khối lệnh tuần tự:** Tính độ phức tạp của chuỗi các khối lệnh độc lập bằng hàm cực đại $\max(O_1, O_2)$.
13. **Áp dụng Quy tắc nhân cho các vòng lặp lồng nhau:** Phân tích độ phức tạp khi một vòng lặp $O(n)$ lồng trong một vòng lặp $O(n)$ khác thành $O(n^2)$.
14. **Phân tích ca điển hình Prefix Average 1 vs Prefix Average 2:** So sánh chi phí giữa cách tiếp cận hai vòng lặp $O(n^2)$ và dùng biến cộng dồn $O(n)$.
15. **Xác định cận trên chặt nhất (Tightest upper bound):** Hiểu nguyên tắc chọn lớp hàm đại diện nhỏ nhất và đơn giản nhất khi phát biểu độ phức tạp thuật toán.

---

## 6. Phân Tích Nội Dung & Chủ Đề Câu Hỏi Topic 5: Đệ Quy (Recursion) (Lecture 5)

### 6.1 Tóm Tắt Nội Dung Cốt Lõi Từ Slide (25 Slide)
- **Khái niệm Đệ quy (Recursion):**
  - Xảy ra khi một hàm tự gọi lại chính nó (trực tiếp hoặc gián tiếp thông qua hàm khác).
  - Bản chất: Chia bài toán kích thước $n$ thành một hoặc nhiều bài toán con cùng dạng nhưng có kích thước nhỏ hơn ($n-1$, $n/2$...).
  - Ví dụ đời sống & khoa học máy tính: Hệ thống thư mục tệp tin lồng nhau của hệ điều hành, ngữ pháp hình thức của ngôn ngữ lập trình, đồ họa máy tính phân dạng (fractals), cấu trúc phân nhánh trong tự nhiên.
- **Hai thành phần cốt lõi bắt buộc của một hàm đệ quy:**
  1. *Trường hợp cơ sở (Base case / Anchor case):* Điều kiện dừng đệ quy. Tại đây bài toán có lời giải trực tiếp mà không cần gọi thêm đệ quy nữa. Bắt buộc phải có ít nhất một trường hợp cơ sở.
  2. *Bước đệ quy (Recursive step):* Lời gọi lại chính hàm đó nhưng với đối số được thu hẹp quy mô, bắt buộc phải dẫn tiến trình tính toán tiến dần về trường hợp cơ sở.
  - *Hậu quả khi thiếu hoặc sai Base case:* Đệ quy vô tận (infinite recursion) dẫn đến cạn kiệt bộ nhớ ngăn xếp cuộc gọi $\rightarrow$ Lỗi tràn ngăn xếp (**Stack Overflow Error**).
- **Phân loại các dạng đệ quy:**
  - **1. Đệ quy tuyến tính (Linear Recursion - Đệ quy 1 lần):**
    - Trong mỗi lần thực thi hàm, chỉ có **duy nhất một lời gọi đệ quy** được kích hoạt.
    - *Ví dụ 1: Tính giai thừa $n!$*
      ```cpp
      int recursiveFactorial(int n) {
          if (n == 0) return 1; // Base case
          else return n * recursiveFactorial(n - 1); // Linear call
      }
      ```
    - *Ví dụ 2: Tính tổng các phần tử trong mảng `LinearSum(A, n)`*
      - Nếu $n = 1$: trả về $A[0]$.
      - Ngược lại: trả về $\text{LinearSum}(A, n - 1) + A[n - 1]$. Thời gian chạy $O(n)$.
    - *Ví dụ 3: Đảo ngược mảng `ReverseArray(A, i, j)`*
      - Đổi chỗ $A[i]$ và $A[j]$, sau đó gọi đệ quy `ReverseArray(A, i + 1, j - 1)`.
      - *Kỹ thuật thiết kế tham số đệ quy:* Việc bổ sung các tham số chỉ số phạm vi ($i, j$) giúp việc biểu diễn bài toán đệ quy trên mảng trở nên tự nhiên và hiệu quả hơn rất nhiều so với chỉ truyền tên mảng.
  - **2. Đệ quy bậc hai / Chia để trị (Repeated Squaring / Divide-and-Conquer Power):**
    - Bài toán tính lũy thừa $p(x, n) = x^n$.
    - *Cách đệ quy tuyến tính ngây thơ:* $x^n = x \times x^{n-1} \rightarrow$ Gọi đệ quy $n$ lần, thời gian $O(n)$.
    - *Cách đệ quy chia đôi số mũ (Repeated Squaring):*
      - Nếu $n = 0$: trả về 1.
      - Nếu $n$ lẻ: $y = \text{Power}(x, (n-1)/2) \rightarrow$ trả về $x \cdot y \cdot y$.
      - Nếu $n$ chẵn: $y = \text{Power}(x, n/2) \rightarrow$ trả về $y \cdot y$.
      - *Điểm mấu chốt tối ưu:* Tính và lưu kết quả vào biến tạm $y$ một lần duy nhất, tránh việc gọi hàm đệ quy 2 lần riêng biệt!
      - Số bước đệ quy giảm từ $n$ xuống $\log_2 n \rightarrow$ Độ phức tạp thời gian đạt **$O(\log n)$**.
      - Ý nghĩa số học logarit: Đổi cơ số log chỉ sai khác một hằng số nhân ($\log_{10} n = \log_2 10 \cdot \log_2 n$), do đó độ phức tạp vẫn là $O(\log n)$.
  - **3. Đệ quy nhị phân (Binary Recursion - Đệ quy 2 lần):**
    - Hàm mà trong thân của nó thực hiện **hai lời gọi đệ quy** độc lập.
    - *Ví dụ 1: Vẽ thước đo inch (English Ruler)*
      - Hàm `drawticks(ticklength)` gọi đệ quy `drawticks(ticklength - 1)` hai lần, xen giữa là một lần gọi `drawonetick(ticklength)`.
    - *Ví dụ 2: Tính tổng mảng bằng chia đôi `BinarySum(A, i, n)`*
      - Chia mảng thành 2 nửa: $\text{BinarySum}(A, i, n/2) + \text{BinarySum}(A, i + n/2, n/2)$.
    - *Ví dụ 3: Tính số Fibonacci ngây thơ (`BinaryFib(k)`)*
      - Định nghĩa: $F_0 = 1, F_1 = 1, F_i = F_{i-1} + F_{i-2}$.
      - Mã giả: nếu $k \le 1$ return 1; ngược lại return $\text{BinaryFib}(k-1) + \text{BinaryFib}(k-2)$.
      - *Phân tích chi phí:* Cây đệ quy bùng nổ, số lời gọi đệ quy $n_k > 2^{k/2} \rightarrow$ Độ phức tạp thời gian là **hàm mũ $O(2^k)$**! Rất nhiều bài toán con bị tính đi tính lại trùng lặp.
      - *Thuật toán cải tiến `LinearFibonacci(k)`:* Dùng đệ quy tuyến tính trả về cặp $(F_k, F_{k-1})$. Thời gian chạy giảm ngoạn mục xuống **tuyến tính $O(k)$**.

---

### 6.2 15 Chủ Đề Câu Hỏi Ứng Viên (Candidate Question Themes) - Topic 5

1. **Khái niệm cơ bản về Hàm đệ quy:** Định nghĩa hàm tự gọi lại chính nó và cơ chế phân rã bài toán lớn thành các bài toán con tương tự.
2. **Hai thành phần cốt lõi của giải thuật đệ quy:** Vai trò bắt buộc của Trường hợp cơ sở (Base case) và Bước đệ quy (Recursive step).
3. **Hiện tượng Tràn ngăn xếp (Stack Overflow):** Nguyên nhân dẫn đến tràn bộ nhớ Call Stack khi gọi đệ quy vô hạn hoặc thiếu trường hợp cơ sở.
4. **Cơ chế hoạt động của Call Stack trong đệ quy:** Cách hệ thống lưu trữ khung ngăn xếp (Stack Frame) chứa biến cục bộ và địa chỉ trả về qua từng lần gọi hàm.
5. **Khái niệm Đệ quy tuyến tính (Linear Recursion):** Đặc trưng mỗi lần gọi hàm chỉ kích hoạt tối đa một lời gọi đệ quy (ví dụ tính giai thừa $n!$).
6. **Kỹ thuật thiết kế tham số đệ quy:** Lý do bổ sung các tham số chỉ số mảng ($i, j$) trong bài toán đảo ngược mảng `ReverseArray(A, i, j)`.
7. **Phân tích thuật toán tính tổng mảng `LinearSum`:** Lần vết đệ quy (trace) và xác định độ phức tạp thời gian $O(n)$ cùng không gian bộ nhớ ngăn xếp $O(n)$.
8. **Thuật toán tính lũy thừa ngây thơ vs Lũy thừa nhanh:** So sánh cách tính $O(n)$ bằng nhân liên tiếp và cách chia đôi số mũ $O(\log n)$.
9. **Kỹ thuật lưu biến tạm trong lũy thừa nhanh:** Tầm quan trọng của việc gán $y = \text{Power}(x, n/2)$ để tránh gọi hàm trùng lặp làm bùng nổ độ phức tạp.
10. **Bản chất thời gian chạy $O(\log n)$ trong đệ quy:** Giải thích vì sao kích thước bài toán giảm một nửa qua mỗi bước đệ quy dẫn đến số bước là $\log_2 n$.
11. **Khái niệm Đệ quy nhị phân (Binary Recursion):** Đặc điểm hàm chứa hai lời gọi đệ quy riêng biệt và cấu trúc cây phân nhánh đệ quy.
12. **Thuật toán vẽ thước kẻ (English Ruler):** Giải thích quy luật đối xứng và cách vẽ vạch thước qua hàm đệ quy nhị phân `drawticks`.
13. **Thuật toán tính tổng mảng đệ quy nhị phân `BinarySum`:** Cách chia đôi mảng và tổng hợp kết quả của hai nhánh con.
14. **Phân tích nhược điểm đệ quy Fibonacci ngây thơ:** Tại sao hàm Fibonacci gọi đệ quy 2 lần có độ phức tạp hàm mũ $O(2^n)$ và gây lặp phép tính.
15. **Tối ưu hóa Fibonacci bằng đệ quy tuyến tính:** Kỹ thuật trả về cặp số $(F_k, F_{k-1})$ giúp giảm thời gian chạy từ $O(2^k)$ xuống còn $O(k)$.

---

## 7. Bảng Tổng Hợp 75 Chủ Đề Câu Hỏi & Khung Thiết Kế Ngân Hàng Dữ Liệu (Topics 1 - 5)

| Topic ID | Tên Chủ Đề (Topic Name) | Số Slide | Trọng Tâm Kiến Thức | Số Chủ Đề Câu Hỏi |
| :---: | :--- | :---: | :--- | :---: |
| **topic_01** | Tổng quan CTDL & Giải thuật | 41 | Khái niệm CTDL, 5 đặc trưng thuật toán, lưu đồ, mã giả, công thức Wirth, 5 thao tác cơ bản | 15 themes |
| **topic_02** | Ngôn ngữ C++ cơ bản | 45 | Con trỏ, địa chỉ `&`, số học con trỏ, mảng & con trỏ hằng, cấp phát động `new`/`delete`, mảng 2D động, tham chiếu `&`, tham số mặc định, nạp chồng hàm, hàm mẫu `template` | 15 themes |
| **topic_03** | Lớp & Lập trình HĐT C++ | 43 | POP vs OOP, khai báo class, specifiers, inline vs `::`, constructor, destructor, con trỏ `this`, template class, nạp chồng toán tử 1 ngôi, 2 ngôi, toán tử nhập xuất stream với hàm bạn `friend` | 15 themes |
| **topic_04** | Phân tích thuật toán & Big-O | 33 | Thời gian & bộ nhớ, 3 trường hợp, thực nghiệm vs lý thuyết, mô hình RAM, phép toán cơ sở, 7 hàm tăng trưởng, định nghĩa Big-O, quy tắc cộng/nhân, Prefix Average | 15 themes |
| **topic_05** | Đệ quy (Recursion) | 25 | Bản chất đệ quy, Base case & Recursive step, Stack Overflow, Call Stack, đệ quy tuyến tính, luỹ thừa nhanh $O(\log n)$, đệ quy nhị phân, vẽ thước, tối ưu hóa Fibonacci | 15 themes |
| **TỔNG** | **5 Chuyên Đề Đầu Tiên** | **187** | **Nền tảng C++ & Tư duy phân tích thuật toán** | **75 themes** |

---

## 8. Hướng Dẫn Kỹ Thuật Cho Các Tác Nhân Tiếp Theo (Downstream Agents)

### 8.1 Chuẩn Ngôn Ngữ & Thuật Ngữ Kỹ Thuật (Vietnamese + Technical Terms)
- Câu hỏi và giải thích hoàn toàn bằng tiếng Việt tự nhiên, chuẩn mực sư phạm.
- Giữ nguyên các từ khóa C++ và thuật ngữ khoa học máy tính chuẩn quốc tế:
  - *Keywords:* `class`, `struct`, `public`, `private`, `protected`, `new`, `delete`, `delete[]`, `template`, `friend`, `operator`, `this`, `inline`, `cin`, `cout`, `istream`, `ostream`.
  - *CS Terms:* Pointer, Reference, Dereference, Array, Dynamic Allocation, Constructor, Destructor, Memory Leak, Function Overloading, Scope Resolution (`::`), Primitive Operations, RAM Model, Big-Oh ($O$), Worst-case, Average-case, Best-case, Asymptotic Analysis, Recursion, Base Case, Recursive Step, Call Stack, Stack Frame, Stack Overflow, Repeated Squaring, Binary Recursion.

### 8.2 Định Dạng Schema Cho `questions.json`
Mỗi câu hỏi cần tuân thủ cấu trúc chặt chẽ:
```json
{
  "id": "q001",
  "topicId": 1,
  "topicName": "Tổng quan CTDL & Giải thuật",
  "question": "Nội dung câu hỏi ngắn gọn, rõ ràng, có thể kèm đoạn mã C++...",
  "options": [
    "Phương án A",
    "Phương án B",
    "Phương án C",
    "Phương án D"
  ],
  "answer": "Phương án đúng (khớp chính xác 1 trong 4 chuỗi trong options)",
  "explanation": "Giải thích chi tiết tại sao đúng, chỉ ra quy tắc ngôn ngữ hoặc công thức tính toán liên quan."
}
```

### 8.3 Khuyến Nghị Triển Khai Bộ Tạo Câu Hỏi (Question Generation Pipeline)
1. **Trích xuất slide:** Tận dụng file JSON đã trích xuất đầy đủ tại `C:\Users\manha\AppData\Local\Temp\lecture_*_extracted.json` hoặc sử dụng mã PowerShell COM đã kiểm chứng.
2. **Đảm bảo tính đa dạng:** Mỗi chủ đề có đủ câu hỏi lý thuyết, câu hỏi phân tích mã nguồn C++ (code trace), câu hỏi tính toán độ phức tạp, và câu hỏi nhận diện lỗi biên dịch/runtime.
3. **Tránh lỗi phổ biến:** Đảm bảo 4 lựa chọn không trùng lặp, câu trả lời đúng phải khớp chính xác tuyệt đối với 1 phần tử trong mảng `options`.
