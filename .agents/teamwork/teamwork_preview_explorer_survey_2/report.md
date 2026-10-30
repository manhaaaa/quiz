# Báo Cáo Khảo Sát Chi Tiết Bài Giảng 6 Đến 10 (Lectures 6-10 Content & Concept Survey)

**Dự án:** Web-based C++ and Data Structures & Algorithms Quiz Review Game  
**Thực hiện bởi:** Survey Explorer 2 (`teamwork_preview_explorer_survey_2`)  
**Ngày thực hiện:** 2026-10-28  
**Thư mục làm việc:** `D:\c++\quiz_game\.agents\teamwork\teamwork_preview_explorer_survey_2`  
**Tập tài liệu khảo sát:** `D:\c++\drive-download-20261028T155811Z-1-001`

---

## 1. Tổng Quan Khảo Sát & Danh Mục Tài Liệu Nguồn

Khảo sát toàn diện 5 bài giảng từ Bài 6 đến Bài 10 phục vụ xây dựng ngân hàng câu hỏi trắc nghiệm (200+ câu, ~15 câu/chủ đề) chuẩn kỹ thuật C++ và Cấu trúc dữ liệu & Giải thuật.

| Bài | Tên tệp tin gốc | Định dạng | Số slide/trang | Trọng tâm nội dung chính |
| :--- | :--- | :--- | :--- | :--- |
| **Lecture 6** | `Lecture 6 - Vector 2026.pptx` | PPTX | 21 slides | Kiểu dữ liệu trừu tượng Vector ADT, Dynamic Array, thư viện STL `std::vector`, Modifiers, Iterators, Capacity, Element Access, chiến lược cấp phát lại bộ nhớ, bài tập code mẫu. |
| **Lecture 7** | `Lecture 7  Linked List.pptx` | PPTX | 31 slides | List ADT, Singly Linked List (DSLK đơn), Doubly Linked List (DSLK kép), cấu trúc Node, các nút canh gác (`header`, `trailer`), thuật toán `insertAfter`, `remove`, so sánh Mảng vs DSLK, `std::list`. |
| **Lecture 8** | `Lecture 8 - Stack.ppt` | PPT (OLE binary) | 34 slides | Ngăn xếp Stack ADT, nguyên lý LIFO, cài đặt mảng tĩnh & mảng động, phân tích chiến lược tăng dần ($+c$) vs gấp đôi ($\times 2$), bài toán Computing Spans $O(n)$, Ký pháp Ba Lan (Infix, Postfix, Prefix), Shunting-Yard, kiểm tra ngoặc. |
| **Lecture 9** | `Lecture 9 - queues.ppt` | PPT (OLE binary) | 13 slides | Hàng đợi Queue ADT, nguyên lý FIFO, cài đặt mảng vòng tròn (Circular Array) với phép toán modulo `% N`, con trỏ $F$ và $L$, biến đếm $num$, cài đặt bằng DSLK, ứng dụng thực tế. |
| **Lecture 10** | `Lectures 10 From GT Ch6 Trees new.ppt` & `.pdf` | PPT & PDF | 43 slides / 40 trang | Cấu trúc dữ liệu Cây phi tuyến (Trees), General Tree ADT, Binary Tree, Proper/Full Binary Tree, các định lý toán học ($e = i + 1, n = 2e - 1$), duyệt cây (Preorder, Inorder, Postorder), cây biểu thức toán học, mở rộng BST và AVL. |

---

## 2. Đánh Giá Công Cụ Trích Xuất & Phương Pháp Kiểm Tra

Hệ thống Windows của dự án được cấu hình và kiểm chứng khả năng trích xuất dữ liệu đa phương thức:
1. **`python-pptx` (v1.0.2):** Trích xuất tự động và hoàn hảo 100% cấu trúc, văn bản, bảng biểu từ các file `.pptx` chuẩn OpenXML (`Lecture 6` và `Lecture 7`).
2. **`win32com.client` (PowerPoint COM Automation 16.0):** Xử lý trực tiếp các file định dạng nhị phân cổ điển `.ppt` (`Lecture 8`, `Lecture 9`, `Lecture 10`) không qua convert trung gian, trích xuất nguyên vẹn văn bản tiếng Việt UTF-8 và danh sách các shape, code snippet.
3. **`pymupdf` (v2.0):** Kiểm chứng đối chiếu tài liệu `Lectures 10 From GT Ch6 Trees new.pdf`, bảo đảm không sót bất kỳ sơ đồ giải thuật hay công thức toán học nào.

---

## 3. Phân Tích Chi Tiết Từng Chủ Đề (Topics 6 - 10)

### 3.1. Topic 6: Vector & Dynamic Arrays (Lecture 6)

#### 3.1.1. Khái niệm cốt lõi & Cơ chế hoạt động
- **Vector ADT:** Là kiểu dữ liệu trừu tượng mở rộng khái niệm mảng tĩnh. Vector quản lý một dãy đối tượng liên tiếp trong bộ nhớ với khả năng tự động co giãn kích thước linh hoạt khi thêm hoặc bớt phần tử.
- **Truy cập ngẫu nhiên (Random Access):** Truy cập phần tử bất kỳ tại chỉ số $i$ với độ phức tạp $O(1)$ nhờ tính chất lưu trữ trên một vùng nhớ liên tục (contiguous memory).
- **So sánh với Mảng tĩnh C/C++:**
  - Mảng tĩnh cố định kích thước khi biên dịch, không thể mở rộng, không tự giải phóng hoặc quản lý số lượng phần tử thực tế.
  - Vector tự động quản lý cấp phát động (`heap`), tự giải phóng bộ nhớ khi ra khỏi phạm vi (`RAII`), cung cấp các phương thức phong phú kiểm tra kích thước và xử lý ngoại lệ.

#### 3.1.2. Nhóm phương thức chuẩn trong STL `std::vector<T>`
1. **Modifiers (Thêm, sửa, xóa):**
   - `push_back(val)`: Chèn phần tử vào cuối vector. Chi phí trung bình khấu hao (amortized) là $O(1)$.
   - `pop_back()`: Xóa phần tử cuối cùng của vector ($O(1)$).
   - `insert(iterator pos, val)`: Chèn phần tử vào vị trí bộ lặp `pos`. Chi phí $O(n)$ do phải dịch chuyển các phần tử phía sau sang phải.
   - `erase(iterator pos)`: Xóa phần tử tại vị trí bộ lặp `pos`. Chi phí $O(n)$ do phải dịch chuyển các phần tử phía sau sang trái.
   - `assign(unsigned n, T val)`: Gán $n$ phần tử với giá trị mới `val`.
   - `swap(vector& x)`: Hoán đổi nội dung của hai vector ($O(1)$ thông qua hoán đổi con trỏ buffer nội bộ).
   - `clear()`: Xóa sạch toàn bộ phần tử trong vector (`size` về 0, nhưng `capacity` giữ nguyên).
2. **Element Access (Truy cập phần tử):**
   - `operator[] (unsigned i)`: Truy cập phần tử tại chỉ số $i$, không kiểm tra biên (no bounds checking), tốc độ tối đa nhưng có thể gây lỗi Undefined Behavior nếu truy cập ngoài phạm vi.
   - `at(unsigned i)`: Truy cập có kiểm tra biên; ném ra ngoại lệ `std::out_of_range` nếu $i \ge size$.
   - `front()`: Trả về tham chiếu đến phần tử đầu tiên (`v[0]`).
   - `back()`: Trả về tham chiếu đến phần tử cuối cùng (`v[v.size() - 1]`).
3. **Iterators (Bộ duyệt):**
   - `begin()`: Trả về iterator trỏ tới phần tử đầu tiên.
   - `end()`: Trả về iterator trỏ tới vị trí ngay sau phần tử cuối cùng (past-the-end).
   - `rbegin()`, `rend()`: Reverse iterator duyệt ngược từ cuối về đầu.
   - Hiện tượng mất hiệu lực iterator (Iterator Invalidation): Khi `push_back` hoặc `insert` kích hoạt việc tái cấp phát bộ nhớ (reallocation), toàn bộ iterator trỏ vào vector trước đó đều bị vô hiệu hóa.
4. **Capacity (Quản lý dung lượng):**
   - `size()`: Số lượng phần tử hiện tại có trong vector.
   - `capacity()`: Dung lượng bộ nhớ đã được cấp phát (sức chứa tối đa trước khi phải cấp phát lại). Quy tắc: `capacity >= size`.
   - `empty()`: Trả về `true` nếu `size == 0`, ngược lại trả về `false`.
   - `reserve(n)`: Đặt trước dung lượng bộ nhớ tối thiểu chứa được $n$ phần tử để tránh việc cấp phát lại liên tục.
   - `resize(n, val)`: Thay đổi kích thước `size()` thành $n$. Nếu mở rộng, các phần tử mới được khởi tạo bằng `val` hoặc mặc định.

#### 3.1.3. 15 Chủ đề câu hỏi trắc nghiệm ứng viên cho Topic 6
1. **Khái niệm Vector ADT:** Định nghĩa kiểu dữ liệu trừu tượng vector và sự khác biệt căn bản với mảng tĩnh.
2. **Phân biệt `size()` và `capacity()`:** Ý nghĩa khác nhau giữa số phần tử hiện tại và dung lượng bộ nhớ thực tế đã cấp phát.
3. **Cơ chế `reserve()` vs `resize()`:** Phân biệt hàm chỉ thay đổi `capacity` và hàm thực sự thay đổi `size` cùng các phần tử.
4. **Kiểm tra biên: `operator[]` vs `at()`:** Hành vi khi truy cập chỉ số ngoài giới hạn và ngoại lệ `std::out_of_range`.
5. **Độ phức tạp các thao tác sửa đổi:** Phân tích độ phức tạp thời gian của `push_back` (amortized $O(1)$) so với `insert`/`erase` ($O(n)$).
6. **Truy cập đầu và cuối:** Cú pháp và cách sử dụng an toàn của `front()` và `back()`.
7. **Bản chất iterator `begin()` và `end()`:** Ý nghĩa vị trí phần tử mà `end()` trỏ tới (one-past-the-last element).
8. **Bộ lặp ngược (Reverse Iterators):** Cách hoạt động của `rbegin()` và `rend()`.
9. **Thao tác `erase()` trên iterator:** Giá trị trả về của `erase()` và cách duyệt xóa phần tử đúng cách mà không bị lỗi con trỏ.
10. **Hành vi của `clear()`:** Tác động của `clear()` lên `size()` (về 0) và `capacity()` (không tự động giải phóng dung lượng).
11. **Tối ưu hóa với `swap()`:** Độ phức tạp $O(1)$ của việc hoán đổi 2 vector và kỹ thuật "shrink-to-fit" trong C++98/03.
12. **Hiện tượng vô hiệu hóa bộ lặp (Iterator Invalidation):** Điều kiện khiến các iterator, con trỏ và tham chiếu tới phần tử vector bị vô hiệu hóa khi chèn/xóa/realloc.
13. **Chiến lược nhân đôi bộ nhớ (Doubling Strategy):** Tại sao vector nhân đôi dung lượng khi đầy thay vì cộng thêm một hằng số cố định.
14. **Phân tích output code mẫu:** Truy vết kết quả xuất ra màn hình của đoạn code sử dụng vòng lặp `while(!v.empty()) { sum += v.back(); v.pop_back(); }`.
15. **Vector lưu trữ đối tượng tự định nghĩa:** Xây dựng `vector<SinhVien>` hoặc `vector<Diem>`, sắp xếp và tìm kiếm theo thuộc tính.

---

### 3.2. Topic 7: Linked List (Lecture 7)

#### 3.2.1. Khái niệm cốt lõi & Cấu trúc Node
- **List ADT:** Dãy các nút phân tán trong bộ nhớ, thiết lập quan hệ tuyến tính trước/sau (predecessor/successor) thông qua các liên kết con trỏ.
- **Node trong Danh sách liên kết đơn (Singly Linked List):**
  - Thuộc tính: `Element elem; Node *next;`
  - Các hàm thành viên: `getNext()`, `setNext(Node*)`, `getElem()`, `setElem(Element)`.
- **Node trong Danh sách liên kết kép (Doubly Linked List):**
  - Thuộc tính: `Element elem; Node *prev; Node *next;`
  - Các nút đặc biệt: Nút đầu canh gác (`header`) và nút cuối canh gác (`trailer`) giúp triệt tiêu các trường hợp biên đặc biệt khi danh sách rỗng hoặc thao tác ở 2 đầu.

#### 3.2.2. Các thao tác và giải thuật trên DSLK
1. **Danh sách liên kết đơn:**
   - `push_front(e)`: Tạo nút mới $q$, $q \to next = head$, $head = q$ ($O(1)$).
   - `pop_front()`: Nút tạm $p = head$, $head = head \to next$, `delete p` ($O(1)$).
   - `push_back(e)`: Nếu có con trỏ `tail`, gắn $tail \to next = q$, $tail = q$ ($O(1)$). Nếu không có `tail`, phải duyệt từ `head` ($O(n)$).
   - `pop_back()`: Luôn mất $O(n)$ trong DSLK đơn vì cần duyệt tìm nút ngay trước `tail` để ngắt kết nối và cập nhật `tail` mới.
2. **Danh sách liên kết kép:**
   - `insertAfter(Node* p, Element e)`:
     ```cpp
     Node *q = new Node(e);
     q->setNext(p->getNext());
     p->getNext()->setPrev(q);
     q->setPrev(p);
     p->setNext(q);
     return q;
     ```
   - `remove(Node* p)`:
     ```cpp
     p->getPrev()->setNext(p->getNext());
     p->getNext()->setPrev(p->getPrev());
     p->setPrev(NULL);
     p->setNext(NULL);
     delete p;
     ```
     Đạt chi phí $O(1)$ khi đã có con trỏ tới nút cần xóa.
3. **Danh sách liên kết vòng (Circular Linked List):**
   - Nút cuối cùng trỏ ngược lại nút đầu tiên thay vì trỏ tới `NULL`.
   - Ứng dụng trong lập lịch xoay vòng (Round-Robin), danh sách phát nhạc lặp lại.

#### 3.2.3. Bảng So Sánh Toàn Diện: Mảng vs Danh Sách Liên Kết (Slide 28)

| Đặc trưng | Mảng (Array / Vector) | Danh sách liên kết (Linked List) |
| :--- | :--- | :--- |
| **Cơ chế cấp phát bộ nhớ** | Vùng nhớ liên tục (Contiguous). Phụ thuộc vào kích thước mảng cấp phát trước. | Cấp phát động từng nút riêng lẻ trên Heap theo nhu cầu thực tế. |
| **Chi phí bộ nhớ phụ trội** | Không có (hoặc chỉ một số biến quản trị `size`, `capacity`). | Tốn thêm bộ nhớ cho các con trỏ liên kết (`next`, `prev`) tại mỗi nút. |
| **Truy cập phần tử theo chỉ số** | $O(1)$ (Direct Random Access qua chỉ số $i$). | $O(n)$ (Phải duyệt tuần tự từ đầu danh sách). |
| **Chèn/Xóa tại vị trí đã biết** | $O(n)$ (Do phải dồn dịch các phần tử xung quanh). | $O(1)$ (Chỉ cập nhật lại các con trỏ liên kết). |
| **Cache Locality** | Rất cao (Tận dụng bộ nhớ đệm CPU cache tuyệt vời). | Thấp (Các nút nằm rải rác trong bộ nhớ dẫn đến Cache Miss). |
| **Tìm kiếm tuần tự** | $O(n)$ (Nếu chưa sắp xếp), $O(\log n)$ (nếu đã sắp xếp qua Binary Search). | $O(n)$ (Không thể áp dụng Binary Search hiệu quả do không có $O(1)$ random access). |

#### 3.2.4. Thư viện STL `std::list` trong C++
- Bản chất là Doubly Linked List.
- Cung cấp Bidirectional Iterator (chỉ hỗ trợ `++` và `--`, không hỗ trợ `+ n` hoặc `operator[]`).
- Các hàm thành viên: `push_front()`, `pop_front()`, `push_back()`, `pop_back()`, `insert()`, `erase()`, `front()`, `back()`.

#### 3.2.5. 15 Chủ đề câu hỏi trắc nghiệm ứng viên cho Topic 7
1. **Cấu trúc nút DSLK đơn:** Khái niệm trường dữ liệu `elem` và con trỏ `next`.
2. **Cấu trúc nút DSLK kép:** Vai trò của 2 con trỏ `prev` và `next`.
3. **Thao tác thêm vào đầu (`push_front`):** Độ phức tạp $O(1)$ và các bước gán con trỏ đúng thứ tự.
4. **Nghịch lý `pop_back` trong DSLK đơn:** Tại sao `pop_back` trong DSLK đơn mất $O(n)$ ngay cả khi có con trỏ `tail`.
5. **Ưu điểm của DSLK kép so với DSLK đơn:** Khả năng duyệt 2 chiều và xóa nút bất kỳ trong $O(1)$ khi biết trước con trỏ nút đó.
6. **Nút canh gác (Dummy/Sentinel Nodes):** Vai trò của `header` và `trailer` trong việc đơn giản hóa mã nguồn và tránh kiểm tra `NULL`.
7. **Thuật toán `insertAfter(p, e)` trong DSLK kép:** Thứ tự thực hiện 4 phép gán con trỏ để không làm đứt gãy danh sách.
8. **Thuật toán `remove(p)` trong DSLK kép:** Các bước nối vòng qua nút bị xóa và giải phóng bộ nhớ `delete p`.
9. **Đặc trưng của DSLK vòng (Circular List):** Điều kiện kết thúc vòng lặp duyệt và ứng dụng thực tiễn.
10. **So sánh Mảng và DSLK về chi phí bộ nhớ:** Phân tích overhead của con trỏ và hiện tượng phân mảnh bộ nhớ heap.
11. **So sánh về chi phí truy cập và tìm kiếm:** Đánh giá $O(1)$ vs $O(n)$ khi truy cập ngẫu nhiên.
12. **Phân tích Cache Locality:** Tại sao mảng duyệt tuần tự nhanh hơn danh sách liên kết trên kiến trúc phần cứng hiện đại.
13. **Thư viện `std::list` trong C++:** Đặc tính iterator hai chiều (Bidirectional Iterator) và lý do không có `operator[]`.
14. **Truy vết mã nguồn C++:** Đoạn mã tính toán `mylist.front() -= mylist.back();` và kết quả in ra.
15. **Quản lý bộ nhớ và Memory Leak:** Tầm quan trọng của việc giải phóng từng node trong Destructor của lớp List.

---

### 3.3. Topic 8: Stack (Lecture 8)

#### 3.3.1. Khái niệm cốt lõi & Cơ chế hoạt động
- **Stack ADT:** Cấu trúc dữ liệu trừu tượng tuyến tính hoạt động nghiêm ngặt theo cơ chế **LIFO** (Last In, First Out - Vào sau ra trước).
- Mọi thao tác bổ sung và lấy ra đều chỉ được thực hiện tại một đầu duy nhất gọi là **Đỉnh ngăn xếp (Top)**.
- **Các phép toán chính:**
  - `push(Object o)`: Đưa phần tử $o$ vào đỉnh ngăn xếp ($O(1)$).
  - `pop()`: Loại bỏ phần tử ở đỉnh ngăn xếp ($O(1)$).
- **Các phép toán bổ trợ:**
  - `top()`: Trả về giá trị/tham chiếu phần tử ở đỉnh mà không xóa ($O(1)$).
  - `size()`: Trả về số phần tử hiện thời ($O(1)$).
  - `empty()` / `isEmpty()`: Kiểm tra ngăn xếp rỗng ($O(1)$).
- **Các trường hợp ngoại lệ:**
  - `StackEmptyException` (Underflow): Xảy ra khi gọi `pop()` hoặc `top()` trên ngăn xếp rỗng.
  - `StackFullException` (Overflow): Xảy ra khi gọi `push()` trên ngăn xếp mảng cố định đã đầy dung lượng.

#### 3.3.2. Cài đặt Stack & Phân tích chiến lược cấp phát bộ nhớ
1. **Cài đặt bằng mảng tĩnh (`ArrayStack`):**
   - Khởi tạo chỉ số đỉnh `t = -1`.
   - `push(o)`: `S[++t] = o`.
   - `pop()`: `return S[t--]`.
   - Dung lượng bị cố định từ đầu, gây lãng phí bộ nhớ hoặc tràn ngăn xếp.
2. **Chiến lược mở rộng mảng động (Amortized Analysis - Slide 27-30):**
   - **Chiến lược gia tăng (Incremental Strategy - $+c$):**
     - Mỗi khi đầy mảng, tăng thêm $c$ ô nhớ. Cần thay thế mảng $k = n / c$ lần.
     - Tổng thời gian copy chuỗi $n$ phần tử:
       $$T(n) = n + c(1 + 2 + \dots + k) = n + c \frac{k(k+1)}{2} = O(n + k^2) = O(n^2)$$
     - Thời gian trung bình mỗi thao tác push là $O(n)$ $\rightarrow$ Kém hiệu quả!
   - **Chiến lược gấp đôi (Doubling Strategy - $\times 2$):**
     - Mỗi khi đầy mảng, nhân đôi kích thước mảng. Cần thay thế mảng $k = \log_2 n$ lần.
     - Tổng thời gian copy chuỗi $n$ phần tử:
       $$T(n) = n + 1 + 2 + 4 + \dots + 2^k = n + 2^{k+1} - 1 \approx 2n - 1 = O(n)$$
     - Thời gian trung bình khấu hao (Amortized Time) cho mỗi thao tác push là $T(n)/n = O(1)$ $\rightarrow$ Tối ưu tuyệt đối!
3. **Cài đặt bằng Danh sách liên kết đơn:**
   - Đỉnh ngăn xếp (Top) luôn tương ứng với đầu danh sách (`head`).
   - `push` $\equiv$ `push_front()` ($O(1)$); `pop` $\equiv$ `pop_front()` ($O(1)$). Không lo bị giới hạn dung lượng.

#### 3.3.3. Các thuật toán & Ứng dụng kinh điển của Stack trong bài giảng
1. **Quản lý thực thi chương trình trong C++ (Call Stack / Runtime Stack - Slide 8):**
   - Khi gọi một hàm, hệ thống đẩy một Activation Frame (chứa biến cục bộ, tham số, địa chỉ trả về) vào Call Stack.
   - Khi hàm kết thúc, Frame được pop ra và CPU quay lại địa chỉ lệnh tiếp theo.
2. **Kiểm tra ngoặc hợp lệ (Balanced Parentheses - Slide 34):**
   - Duyệt chuỗi: gặp ngoặc mở `(` thì `push` vào stack; gặp ngoặc đóng `)` thì kiểm tra nếu stack rỗng $\rightarrow$ sai, ngược lại `pop`. Kết thúc chuỗi, stack rỗng $\rightarrow$ hợp lệ.
3. **Bài toán Tính toán liên tiếp (Computing Spans / Stock Span Problem - Slide 18-21):**
   - Cho mảng $X$, span $S[i]$ là số lượng lớn nhất các phần tử liền kề trước $X[i]$ có giá trị $\le X[i]$.
   - Thuật toán vét cạn (Brute-force): 2 vòng lặp lồng nhau mất $O(n^2)$.
   - Thuật toán tuyến tính dùng Stack (Monotonic Stack): Lưu các chỉ số. Pop các chỉ số $j$ mà $X[j] \le X[i]$. Khi dừng lại, $S[i] = i - \text{top}$. Push $i$ vào stack.
   - Mỗi phần tử được push đúng 1 lần và pop tối đa 1 lần $\rightarrow$ Chi phí toàn bộ là $O(n)$!
4. **Ký pháp Ba Lan & Thuật toán Shunting-Yard (Slide 22-25):**
   - **Trung tố (Infix):** $a \times (b + c) - (d \times a)$
   - **Tiền tố (Prefix):** $- \times a + b c \times d a$
   - **Hậu tố (Postfix / Reverse Polish Notation):** $a b c + \times d a \times -$
   - **Chuyển Infix sang Postfix:** Dùng Stack lưu toán tử theo thứ tự ưu tiên `/, *` > `-, +` > `)`.
   - **Tính giá trị biểu thức Hậu tố:** Dùng Stack lưu toán hạng; gặp toán tử thì pop 2 toán hạng, tính toán và push kết quả trở lại.

#### 3.3.4. 15 Chủ đề câu hỏi trắc nghiệm ứng viên cho Topic 8
1. **Định nghĩa Stack ADT & Nguyên lý LIFO:** Khái niệm vào sau ra trước và điểm truy cập duy nhất tại đỉnh.
2. **Các phép toán cơ bản:** Cú pháp, ngữ nghĩa và trạng thái thay đổi khi gọi `push()`, `pop()`, `top()`.
3. **Xử lý ngoại lệ trong Stack:** Hiện tượng Underflow khi pop stack rỗng và Overflow khi đầy mảng.
4. **Cài đặt Stack bằng mảng:** Cách hoạt động của biến chỉ số `t` (khởi tạo `-1`, quy tắc `++t` và `t--`).
5. **Phân tích chiến lược mở rộng gia tăng ($+c$):** Tại sao tổng thời gian lại là $O(n^2)$ và chi phí push trung bình là $O(n)$.
6. **Phân tích chiến lược gấp đôi ($\times 2$):** Chứng minh chi phí khấu hao (amortized time) của thao tác push đạt $O(1)$.
7. **Cài đặt Stack bằng DSLK:** Tại sao thao tác ở đầu danh sách (`head`) là lựa chọn tối ưu cho Stack.
8. **Call Stack trong C++:** Cơ chế lưu trữ Activation Record (biến cục bộ, địa chỉ hồi quy) khi gọi hàm đệ quy/lồng nhau.
9. **Thuật toán kiểm tra ngoặc đúng:** Trạng thái của stack khi chuỗi ngoặc bị thiếu mở ngoặc hoặc thiếu đóng ngoặc.
10. **Khái niệm Ký pháp Ba Lan:** Phân biệt biểu thức Trung tố (Infix), Tiền tố (Prefix) và Hậu tố (Postfix).
11. **Ưu điểm của Ký pháp Hậu tố (RPN):** Không cần dùng dấu ngoặc và thứ tự tính toán hoàn toàn đơn trị từ trái sang phải.
12. **Thuật toán chuyển đổi Infix sang Postfix:** Xử lý độ ưu tiên toán tử và vai trò của các dấu mở/đóng ngoặc trong stack.
13. **Thuật toán tính giá trị biểu thức Postfix:** Thứ tự lấy 2 toán hạng $op2$ và $op1$ khi thực hiện phép tính $op1 \text{ operator } op2$.
14. **Bài toán Computing Spans:** Sự vượt trội của giải thuật Monotonic Stack đạt $O(n)$ so với vét cạn $O(n^2)$.
15. **Ứng dụng đổi cơ số (Decimal to Binary/Hex):** Thuật toán chia lấy dư và đẩy vào stack để in ra kết quả đảo ngược.

---

### 3.4. Topic 9: Queue (Lecture 9)

#### 3.4.1. Khái niệm cốt lõi & Cơ chế hoạt động
- **Queue ADT:** Cấu trúc dữ liệu trừu tượng tuyến tính tổ chức theo cơ chế **FIFO** (First In, First Out - Vào trước ra trước).
- Các đối tượng được đưa vào ở một đầu gọi là **Cuối hàng (Rear / Back)** và được lấy ra ở đầu kia gọi là **Đầu hàng (Front)**.
- **Các phép toán chính:**
  - `push(Object o)` / `enqueue(o)`: Thêm một phần tử vào cuối hàng đợi ($O(1)$).
  - `pop()` / `dequeue()`: Loại bỏ phần tử ở đầu hàng đợi ($O(1)$).
- **Các phép toán bổ trợ:**
  - `front()`: Lấy giá trị phần tử ở đầu hàng mà không xóa ($O(1)$).
  - `back()`: Lấy giá trị phần tử ở cuối hàng mà không xóa ($O(1)$).
  - `size()`: Số lượng phần tử hiện đang lưu trữ ($O(1)$).
  - `isEmpty()`: Kiểm tra hàng đợi có rỗng hay không ($O(1)$).

#### 3.4.2. Cài đặt Queue & Giải pháp Mảng Vòng (Circular Array)
1. **Hạn chế của Mảng Tuyến Tính Đơn Thuần:**
   - Nếu mỗi lần `pop()` ta dịch toàn bộ các phần tử về bên trái, chi phí sẽ là $O(n)$ cho mỗi thao tác lấy ra.
   - Nếu dịch chuyển con trỏ `front` sang phải để đạt $O(1)$, các ô nhớ phía trước sẽ bị bỏ trống, con trỏ `rear` nhanh chóng chạm giới hạn mảng trong khi dung lượng thực tế vẫn còn dư thừa (Hiện tượng trôi mảng - Array Drifting / False Overflow).
2. **Cấu trúc Mảng Vòng Tròn (Circular Array - Slide 6, 8, 9, 11):**
   - Mảng kích thước $N$.
   - Con trỏ $F$ (Front): Lưu chỉ số phần tử đầu tiên hiện tại.
   - Con trỏ $L$ (Last / Rear): Lưu chỉ số ô nhớ tiếp theo sẽ nhận phần tử mới.
   - Biến đếm $num$: Lưu số lượng phần tử hiện có trong Queue ($0 \le num \le N$).
   - **Công thức Modulo giải quyết quay vòng:**
     - Thêm phần tử `push(o)`:
       ```
       if (num == N) reserve(N * 2 + 2);
       Q[L] = o;
       L = (L + 1) mod N;
       num++;
       ```
     - Xóa phần tử `pop()`:
       ```
       F = (F + 1) mod N;
       num--;
       ```
     - Lấy phần tử đầu: `front() = Q[F];`
     - Lấy phần tử cuối: `back() = Q[(L - 1 + N) mod N];`
   - Đảm bảo toàn bộ các thao tác đạt độ phức tạp thời gian tuyệt đối $O(1)$ mà không tốn công dịch chuyển phần tử.
3. **Cài đặt bằng Danh sách liên kết:**
   - Dùng DSLK đơn với 2 con trỏ `head` (tương ứng `front`) và `tail` (tương ứng `rear`).
   - `push`: thêm vào cuối (`tail->next = q; tail = q;`) $\rightarrow O(1)$.
   - `pop`: xóa ở đầu (`head = head->next;`) $\rightarrow O(1)$.
   - Không bị giới hạn kích thước dung lượng.

#### 3.4.3. Ứng dụng thực tế của Hàng Đợi (Slide 5, 12)
- **Ứng dụng trực tiếp:**
  - Hàng đợi in ấn (Printer Spooler) trong mạng LAN.
  - Lập lịch đa nhiệm CPU (Multi-programming / Round-Robin Scheduling).
  - Đệm truyền gói tin mạng (Packet Buffering trong Router/Switch).
  - Xử lý các yêu cầu dịch vụ theo thứ tự đến trước phục vụ trước.
- **Ứng dụng gián tiếp & Giải thuật:**
  - Cấu trúc hỗ trợ cho thuật toán duyệt đồ thị và cây theo chiều rộng (BFS - Breadth-First Search).
  - Giải thuật mô phỏng sự kiện rời rạc (Discrete Event Simulation).
  - Bài toán lồng cốc (Nested Cups Problem - Slide 12).

#### 3.4.4. 15 Chủ đề câu hỏi trắc nghiệm ứng viên cho Topic 9
1. **Định nghĩa Queue ADT & Nguyên lý FIFO:** Bản chất vào trước ra trước và hai đầu vào/ra độc lập.
2. **So sánh cơ chế Stack vs Queue:** Đối chiếu nguyên lý LIFO (vào sau ra trước) vs FIFO (vào trước ra trước).
3. **Các thao tác cơ bản của Queue:** Vai trò và tác động của `push()`, `pop()`, `front()`, `back()`.
4. **Vấn đề trôi mảng (Array Drifting):** Nguyên nhân mảng tuyến tính thông thường không phù hợp để cài đặt queue hiệu quả.
5. **Cơ chế Mảng Vòng (Circular Array):** Vai trò của phép toán modulo `% N` trong việc kết nối ô cuối về ô đầu.
6. **Điều kiện nhận biết Queue đầy và rỗng:** Sử dụng biến đếm `num` ($num == 0$ là rỗng, $num == N$ là đầy) hoặc điều kiện $(L + 1) \% N == F$.
7. **Công thức tính chỉ số trong Mảng Vòng:** Cách tính chỉ số phần tử cuối cùng `(L - 1 + N) % N`.
8. **Độ phức tạp các thao tác:** Chứng minh $O(1)$ cho mọi thao tác trên Circular Queue.
9. **Cài đặt Queue bằng DSLK đơn:** Tại sao `front` nằm ở `head` và `back` nằm ở `tail` (nếu đảo ngược, thao tác xóa ở `tail` sẽ mất $O(n)$).
10. **Ứng dụng hàng đợi trong Hệ điều hành:** Quản lý tiến trình CPU và bộ đệm in Spooler.
11. **Duyệt cây/đồ thị theo chiều rộng (BFS):** Tại sao hàng đợi là cấu trúc dữ liệu bắt buộc để thực hiện BFS từng mức (level-by-level).
12. **Thư viện STL `std::queue` trong C++:** Cú pháp khai báo, các phương thức chuẩn và container nền tảng mặc định (`std::deque`).
13. **Hàng đợi hai đầu (Deque - Double-ended Queue):** Phân biệt Deque với Queue thông thường (cho phép chèn/xóa ở cả hai đầu).
14. **Truy vết trạng thái Queue qua chuỗi thao tác:** Xác định giá trị trả về của `front()` sau một chuỗi các lệnh `push`, `pop`.
15. **Bài toán lồng cốc (Nested Cups Problem):** Ý tưởng áp dụng Queue để tìm số chồng cốc tối thiểu theo dung tích.

---

### 3.5. Topic 10: Trees (Binary Tree, BST, AVL, Traversals) (Lecture 10)

#### 3.5.1. Khái niệm cốt lõi & Cấu trúc Cây tổng quát (General Tree)
- **Định nghĩa Cây:** Là cấu trúc dữ liệu phi tuyến (Non-linear), phân cấp (Hierarchical), gồm tập hợp các nút (nodes) liên kết theo quan hệ cha - con (parent - child).
- **Các thuật ngữ cơ bản (Slide 14):**
  - **Gốc (Root):** Nút duy nhất không có nút cha (Node with no parent).
  - **Nút trong (Internal Node):** Nút có ít nhất một nút con.
  - **Nút ngoài / Lá (External Node / Leaf):** Nút không có bất kỳ nút con nào.
  - **Độ sâu của một nút (Depth):** Độ sâu của gốc bằng 0; độ sâu của nút con = độ sâu nút cha + 1.
  - **Chiều cao của cây (Height):** Là giá trị độ sâu lớn nhất trong tất cả các nút của cây.
  - **Cây con (Subtree):** Cây gồm một nút và tất cả các nút hậu duệ (descendants) của nó.
- **Biểu diễn Cây tổng quát trong C++ (Slide 16-17):**
  - Lớp `TreeNode`:
    - Thuộc tính: `Object elem`, `TreeNode *parent`, `vector<TreeNode*> child`.
    - Phương thức: `getParent()`, `getChild(int i)`, `insertChild(elem)`, `getElem()`.

#### 3.5.2. Các thuật toán duyệt Cây tổng quát
1. **Duyệt thứ tự trước (Preorder Traversal - Slide 19):**
   - Thăm nút cha trước, sau đó duyệt đệ quy các cây con từ trái qua phải.
   - Giải thuật:
     ```cpp
     void preOrder(TreeNode *v) {
         if (v != NULL) {
             visit(v);
             for (TreeNode *w : v->child)
                 preOrder(w);
         }
     }
     ```
   - Ứng dụng: In ấn mục lục sách, in phân cấp thư mục.
2. **Duyệt thứ tự sau (Postorder Traversal - Slide 24):**
   - Duyệt đệ quy tất cả các cây con trước, sau đó mới thăm nút cha.
   - Giải thuật:
     ```cpp
     void postOrder(TreeNode *v) {
         if (v != NULL) {
             for (TreeNode *w : v->child)
                 postOrder(w);
             visit(v);
         }
     }
     ```
   - Ứng dụng: Tính tổng dung lượng đĩa của một thư mục (cần tính dung lượng tất cả các file và thư mục con trước khi tính tổng tại thư mục cha).
3. **Duyệt thứ tự giữa (Inorder Traversal for General Tree - Slide 23):**
   - Duyệt cây con của con cả, thăm nút cha, sau đó duyệt các cây con còn lại.

#### 3.5.3. Cây Nhị Phân (Binary Tree) & Các Định Lý Toán Học
- **Định nghĩa Cây nhị phân:** Cây mà mỗi nút trong có tối đa 2 nút con, được phân biệt thứ tự rõ ràng là **con trái (Left child)** và **con phải (Right child)**.
- **Cây nhị phân hoàn chỉnh (Proper / Full Binary Tree - Slide 32):** Là cây nhị phân mà mọi nút trong đều có đúng 2 nút con (không có nút nào có đúng 1 con).
- **Cây nhị phân đầy đủ (Perfect Binary Tree):** Cây nhị phân hoàn chỉnh mà tất cả các lá đều nằm ở cùng một mức (cùng độ sâu).
- **Các tính chất toán học của Proper Binary Tree (Slide 33):**
  - Đặt: $n$ là tổng số nút, $e$ là số nút lá (external nodes), $i$ là số nút trong (internal nodes), $h$ là chiều cao cây.
  - Mối quan hệ giữa lá và nút trong:
    $$e = i + 1$$
  - Tổng số nút:
    $$n = 2e - 1 = 2i + 1$$
  - Giới hạn chiều cao và số nút:
    $$h \le i = \frac{n - 1}{2}$$
    $$e \le 2^h$$
    $$h \ge \log_2 e$$
    $$h \ge \log_2 (n + 1) - 1$$

#### 3.5.4. Duyệt Cây Nhị Phân & Cây Biểu Thức (Expression Trees)
- **Thuật toán Duyệt Inorder Cây Nhị Phân (Slide 35):**
  ```cpp
  void inOrder(BTreeNode *v) {
      if (v->hasLeft()) inOrder(v->left());
      visit(v);
      if (v->hasRight()) inOrder(v->right());
  }
  ```
- **Cây Biểu Thức Toán Học (Arithmetic Expression Tree - Slide 9, 30):**
  - Nút lá chứa các toán hạng (số hoặc biến).
  - Nút trong chứa các toán tử ($+, -, \times, /$).
  - Phép duyệt Preorder sinh ra biểu thức Tiền tố (Prefix).
  - Phép duyệt Inorder (kết hợp đóng mở ngoặc) sinh ra biểu thức Trung tố (Infix).
  - Phép duyệt Postorder sinh ra biểu thức Hậu tố (Postfix).

#### 3.5.5. Cây Tìm Kiếm Nhị Phân (BST) & Cây Cân Bằng AVL (Mở rộng bắt buộc theo R1)
- **Cây Tìm kiếm Nhị phân (Binary Search Tree - BST):**
  - Tính chất khóa: Mọi khóa trong cây con trái $< \text{khóa nút hiện tại} <$ Mọi khóa trong cây con phải.
  - Phép duyệt Inorder trên BST luôn sinh ra dãy khóa tăng dần có thứ tự.
  - Tìm kiếm, Chèn, Xóa: Trung bình mất $O(\log n)$, nhưng trường hợp xấu nhất (cây suy biến thành danh sách liên kết lệch một phía) mất $O(n)$.
- **Cây Cân Bằng AVL:**
  - Hệ số cân bằng (Balance Factor): $\text{height}(\text{left}) - \text{height}(\text{right}) \in \{-1, 0, 1\}$.
  - Cơ chế tự cân bằng: Khi chèn/xóa làm mất cân bằng, thực hiện các phép quay:
    - Quay đơn: Quay trái (LL), Quay phải (RR).
    - Quay kép: Quay trái-phải (LR), Quay phải-trái (RL).
  - Đảm bảo chiều cao luôn duy trì ở mức $O(\log n)$, đảm bảo mọi thao tác tìm kiếm, chèn, xóa đều đạt $O(\log n)$ trong mọi trường hợp.

#### 3.5.6. 15 Chủ đề câu hỏi trắc nghiệm ứng viên cho Topic 10
1. **Định nghĩa Cây và quan hệ phân cấp:** Khái niệm gốc (root), nút cha, con, anh em (siblings).
2. **Phân biệt Nút trong và Nút lá (Nút ngoài):** Điều kiện số con để xác định nút trong vs nút ngoài.
3. **Độ sâu nút và Chiều cao của cây:** Công thức tính độ sâu (root = 0) và chiều cao (độ sâu lớn nhất).
4. **Biểu diễn Cây tổng quát:** Cấu trúc nút lưu trữ con trỏ cha và mảng/vector con trỏ các con.
5. **Duyệt Preorder trên Cây:** Thứ tự thăm nút và ứng dụng hiển thị cấu trúc phân cấp.
6. **Duyệt Postorder trên Cây:** Thứ tự thăm các cây con trước nút cha và ứng dụng tính dung lượng thư mục file.
7. **Định nghĩa Cây Nhị Phân:** Điều kiện mỗi nút có tối đa 2 con và tính có thứ tự (con trái, con phải).
8. **Định lý Proper Binary Tree:** Công thức quan hệ giữa số lá và số nút trong ($e = i + 1$).
9. **Định lý tổng số nút của Proper Binary Tree:** Mối liên hệ $n = 2e - 1 = 2i + 1$.
10. **Giới hạn chiều cao của Cây Nhị Phân:** Chiều cao cực tiểu $\lceil \log_2(n+1) - 1 \rceil$ và chiều cao cực đại $(n-1)/2$.
11. **Duyệt Inorder trên Cây Nhị Phân:** Thuật toán duyệt Trái $\rightarrow$ Gốc $\rightarrow$ Phải.
12. **Cây biểu thức toán học (Expression Tree):** Cách bố trí toán tử ở nút trong và toán hạng ở lá; giá trị biểu thức.
13. **Mối liên hệ giữa Duyệt cây và Ký pháp:** Preorder $\rightarrow$ Tiền tố, Inorder $\rightarrow$ Trung tố, Postorder $\rightarrow$ Hậu tố.
14. **Tính chất Cây Tìm kiếm Nhị phân (BST):** Quan hệ thứ tự khóa và đặc tính sắp xếp tăng dần khi duyệt Inorder.
15. **Cây AVL và phép quay cân bằng:** Định nghĩa hệ số cân bằng và 4 dạng phép quay (LL, RR, LR, RL) để duy trì $O(\log n)$.

---

## 4. Tổng Hợp & Đề Xuất Quy Chuẩn Ngân Hàng Câu Hỏi

Để chuẩn bị hoàn hảo cho giai đoạn sinh câu hỏi (`questions.json`), các quy tắc kỹ thuật sau được xác lập:

1. **Ngôn ngữ & Thuật ngữ:**
   - Câu hỏi và lời giải thích sử dụng tiếng Việt chuẩn sư phạm.
   - Giữ nguyên các thuật ngữ kỹ thuật quốc tế của C++ & DSA (ví dụ: `vector`, `capacity`, `amortized`, `push_back`, `iterator invalidation`, `LIFO`, `FIFO`, `singly linked list`, `sentinel node`, `postfix`, `shunting-yard`, `monotonic stack`, `proper binary tree`, `inorder traversal`, `AVL balance factor`).
2. **Cấu trúc mỗi câu hỏi (Schema JSON):**
   - `id`: Mã định danh dạng chuỗi số hoặc slug duy nhất (ví dụ: `q-076` đến `q-150`).
   - `topicId`: Số nguyên định danh chủ đề từ `6` đến `10`.
   - `topicName`: Tên chủ đề rõ ràng (ví dụ: `"Vector & Dynamic Arrays"`, `"Linked List"`, `"Stack"`, `"Queue"`, `"Trees"`).
   - `question`: Nội dung câu hỏi ngắn gọn, rõ nghĩa, có thể chứa đoạn mã nguồn C++ minh họa.
   - `options`: Mảng gồm chính xác 4 phương án lựa chọn (A, B, C, D).
   - `answer`: Chuỗi chứa nội dung chính xác của phương án đúng (phải khớp tuyệt đối với 1 trong 4 lựa chọn trong `options`).
   - `explanation`: Giải thích cặn kẽ vì sao phương án đó đúng, cơ chế vận hành bên dưới và phân tích sai sót của các phương án còn lại.
3. **Phân bổ độ khó đồng đều trong mỗi chủ đề (~15 câu):**
   - **Nhận biết & Khái niệm cơ bản (4 câu):** Định nghĩa, nguyên lý hoạt động, cú pháp khai báo thư viện STL.
   - **Hiểu sâu & Phân tích cơ chế (5 câu):** So sánh ưu nhược điểm, độ phức tạp thời gian/không gian, cơ chế cấp phát bộ nhớ.
   - **Vận dụng & Phân tích mã nguồn (6 câu):** Truy vết giá trị biến trong code snippet, bắt lỗi ngoại lệ, tính toán toán học về cây và ký pháp.

---

Báo cáo khảo sát đã bao quát toàn diện các khía cạnh lý thuyết, thuật toán và mã nguồn từ Bài giảng 6 đến Bài giảng 10, sẵn sàng làm cơ sở kiến thức vững chắc cho giai đoạn triển khai câu hỏi.
