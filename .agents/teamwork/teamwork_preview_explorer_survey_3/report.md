# Báo Cáo Khảo Sát Kỹ Thuật (Explorer Survey 3)
## Khảo Sát Chuyên Sâu Bài Giảng 11 - 14 & Đặc Tả Kiến Trúc Hệ Thống Quiz Game C++ / DSA

---

## 1. Tóm Tắt Tổng Quan (Executive Summary)

Báo cáo này hoàn thành khảo sát chi tiết cho 4 chuyên đề nâng cao về Thuật toán & Cấu trúc dữ liệu trong chương trình học (Bài giảng 11 đến 14) cùng toàn bộ đặc tả kiến trúc cho hệ thống Web Quiz Game tương tác:
1. **Bài giảng 11 — Sắp xếp thời gian $O(n^2)$ (`Lectures 11 Sorting - nn.ppt`, 19 slides):**
   - Các thuật toán cơ bản: Nổi bọt (Bubble Sort), Chọn (Selection Sort), Chèn (Insertion Sort).
   - Phân tích chi tiết số phép toán cơ bản, chứng minh toán học thời gian chạy $O(n^2)$, đánh giá tính ổn định (stability) và không gian bộ nhớ tại chỗ $O(1)$.
2. **Bài giảng 12 — Sắp xếp thời gian $O(n \log n)$ (`Lectures 12 Sorting - nlogn.pptx`, 57 slides):**
   - Chiến lược Chia và trị (Divide and Conquer): Quick Sort (phân hoạch 2 con trỏ, chọn chốt, trường hợp xấu $O(n^2)$ vs trung bình $O(n \log n)$).
   - Merge Sort: Kỹ thuật trộn hai dãy đã sắp bằng mảng phụ $B$, đệ quy chia đôi, thời gian luôn đạt $\Theta(n \log n)$ trong mọi trường hợp, ổn định, bộ nhớ phụ $O(n)$.
   - Heap Sort: Cây nhị phân gần hoàn chỉnh, tính chất Max-Heap, biểu diễn mảng 1-based index ($2i, 2i+1, \lfloor i/2 \rfloor$), thủ tục `Pushdown` (vun đống) $O(\log n)$, tạo đống ban đầu trong thời gian tuyến tính $O(n)$, trích xuất sắp xếp toàn bộ trong $O(n \log n)$, bộ nhớ $O(1)$, không ổn định.
3. **Bài giảng 13 — Thuật toán Tìm kiếm (`Lectures 13 Search.ppt`, 39 slides):**
   - Bài toán tìm kiếm theo khóa $k$ trên tập các cặp khóa-giá trị (Key-Value).
   - Tìm kiếm tuần tự (Sequential/Linear Search): Mảng hoặc danh sách liên kết, không cần sắp thứ tự, thời gian $O(n)$.
   - Tìm kiếm nhị phân trên mảng (Binary Search): Yêu cầu mảng đã sắp, chia đôi khoảng tìm kiếm, thời gian $O(\log_2 n)$.
   - Cây tìm kiếm nhị phân (Binary Search Tree - BST): Tính chất khóa cây con trái $<$ nút gốc $<$ cây con phải; duyệt trung thứ tự (In-Order) cho dãy khóa tăng dần; tìm kiếm `TreeSearch` và chèn `InsertNode` trong $O(h)$; xóa nút `Remove` với 3 trường hợp (lá, 1 con, 2 con dùng nút tiền nhiệm / kế vị); độ phức tạp phụ thuộc chiều cao $h$ ($O(\log n)$ cân bằng, $O(n)$ suy biến).
4. **Bài giảng 14 — Bảng băm (`Lectures 14 Hash tables.ppt`, 19 slides):**
   - Cấu trúc Bảng băm (Hash Table) và Hàm băm $h: K \to [0..m-1]$.
   - Các phương pháp xây dựng hàm băm: Phương pháp chia ($h(k) = k \bmod m$, $m$ là số nguyên tố), phương pháp nhân/bình phương giữa (Mid-Square), phương pháp phân đoạn (Folding: Tách dóng lề và Gấp mép).
   - Hiện tượng đụng độ (Collision) theo nguyên lý Dirichlet.
   - Giải quyết đụng độ bằng Danh sách liên kết trực tiếp (Separate Chaining): Cài đặt C++ hoàn chỉnh với `SingleList<Keys, T> *table` và con trỏ hàm băm `int (*hash)(Keys, int)`. Các phương thức `Add`, `Find`, `Remove`, `Contains`, `Count`.
   - Giải quyết đụng độ bằng Địa chỉ mở (Open Addressing): Thử tuyến tính (Linear Probing), Thử bậc hai (Quadratic Probing), Băm kép (Double Hashing), kỹ thuật đánh dấu ô xóa (Tombstone).
   - Hệ số tải (Load factor $\alpha = n/m$) và thời gian trung bình $O(1)$ vs xấu nhất $O(n)$.
5. **Đặc tả Hệ Thống Quiz Game:**
   - Cấu trúc Schema chuẩn cho `questions.json` với 200+ câu hỏi trắc nghiệm tiếng Việt.
   - Thiết kế Quiz Engine: Chế độ 5 câu ngẫu nhiên đa dạng chủ đề, thuật toán trộn đáp án Fisher-Yates, tính điểm, đếm thời gian, chấm điểm tức thì, xem lại đáp án sai, chơi lại tức thì, chế độ luyện tập theo chủ đề và tra cứu toàn bộ ngân hàng câu hỏi.
   - Kiến trúc Frontend: Web SPA hoàn toàn chạy trên client (zero-install), giao diện hiện đại với Tailwind CSS, icon Lucide, hiệu ứng pháo hoa Confetti, âm thanh tổng hợp thuần Web Audio API (không phụ thuộc file âm thanh ngoài), tương thích 100% khi mở trực tiếp file `index.html`.
   - Bộ công cụ kiểm thử tự động (Verification & Test Runner) bằng Python/Node.js để nghiệm thu chất lượng câu hỏi và logic chơi.

---

## 2. Khảo Sát Chi Tiết Nội Dung Bài Giảng 11 - 14

### 2.1. Bài Giảng 11: Sắp Xếp Thời Gian $O(n^2)$ (Sorting $O(n^2)$)

#### Khái niệm & Định dạng bài toán
- **Input:** Dãy các phần tử $A[0..n-1]$ chưa có thứ tự, lưu trữ bằng mảng.
- **Thuộc tính khóa (Key):** Thuộc tính dùng để so sánh giữa các phần tử.
- **Hàm so sánh:** Toán tử logic (ví dụ $\le$ cho sắp tăng dần, $\ge$ cho sắp giảm dần).
- **Output:** Dãy các phần tử được sắp theo thứ tự tăng hoặc giảm theo khóa.

#### Thuật toán 1: Sắp xếp nổi bọt (Bubble Sort)
- **Ý tưởng:** Lần lượt so sánh các cặp phần tử liền kề từ cuối dãy về đầu (hoặc từ đầu về cuối). Nếu phần tử đứng sau nhỏ hơn phần tử đứng trước thì thực hiện tráo đổi (swap). Qua mỗi vòng lặp ngoài $i$, phần tử nhỏ nhất trong đoạn chưa sắp sẽ "nổi bọt" về đúng vị trí đầu tiên $i$.
- **Mã giả (theo slide):**
  ```pascal
  Algorithm BubbleSort(Array A, n)
  Input: Mảng A có n phần tử
  Output: Mảng A được sắp theo thứ tự tăng dần của khóa
  for i <- 0 to n-2 do
      for j <- n-1 downto i+1 do
          if A[j].Key < A[j-1].Key then
              swap(A[j-1], A[j]);
  ```
- **Hàm hoán vị (Swap) trong C++:**
  ```cpp
  void Swap(object &a, object &b) {
      object tg;
      tg = a;
      a = b;
      b = tg;
  }
  ```
- **Phân tích số phép toán & Độ phức tạp:**
  - Vòng ngoài $i$ lặp $n-1$ lần ($i = 0 \dots n-2$).
  - Vòng trong $j$ chạy từ $n-1$ về $i+1$, số lần so sánh ở vòng lặp thứ $i$ là $n-1-i$.
  - Tổng số phép so sánh:
    $$\sum_{i=0}^{n-2} (n-1-i) = (n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2} = \frac{n^2 - n}{2}$$
  - Mỗi phép so sánh tốn 4 phép toán cơ bản; mỗi phép swap tốn 6 phép toán cơ bản.
  - Tổng thời gian chạy trong trường hợp xấu nhất:
    $$T(n) = (n+2) + (n-1) \cdot 2 + 10 \cdot \frac{n(n-1)}{2} = O(n^2)$$
  - **Tối ưu hóa (Optimized Bubble Sort):** Nếu bổ sung cờ hiệu `bool swapped = false`, khi qua một lượt duyệt mà không có cặp nào bị tráo đổi thì mảng đã có thứ tự và dừng ngay. Khi đó thời gian tốt nhất là $O(n)$.
  - **Tính chất:** Ổn định (Stable), sắp xếp tại chỗ ($O(1)$ bộ nhớ phụ).

#### Thuật toán 2: Sắp xếp chọn (Selection Sort)
- **Ý tưởng:** Ở bước thứ $i$, tìm phần tử có khóa nhỏ nhất trong các phần tử còn lại từ $A[i]$ đến $A[n-1]$ (lưu vị trí vào biến `posmin`). Sau đó, nếu `posmin != i`, thực hiện tráo đổi $A[i]$ và $A[posmin]$. Sau $n-1$ bước, toàn bộ mảng được sắp xếp.
- **Mã giả (theo slide):**
  ```pascal
  Algorithm SelectionSort(Array A, n)
  Input: Mảng A có n phần tử
  Output: Mảng A được sắp theo thứ tự tăng dần của khóa
  for i <- 0 to n-2 do
      posmin <- i;
      for j <- i+1 to n-1 do
          if A[posmin].Key > A[j].Key then
              posmin <- j;
      if posmin != i then
          swap(A[i], A[posmin]);
  ```
- **Phân tích chi tiết:**
  - Số phép so sánh luôn là $\frac{n(n-1)}{2}$ trong mọi trường hợp (tốt nhất, trung bình, xấu nhất đều là $\Theta(n^2)$).
  - Số phép tráo đổi (swap): Tối đa chỉ $n-1$ lần swap! Đây là ưu điểm lớn nhất của Selection Sort khi việc tráo đổi các bản ghi lớn tốn nhiều chi phí hơn việc so sánh khóa.
  - **Tính chất:** Không ổn định (Unstable - ví dụ dãy `[5a, 5b, 2]` khi swap `5a` với `2` sẽ làm `5a` nhảy ra sau `5b`), sắp xếp tại chỗ ($O(1)$ extra space).

#### Thuật toán 3: Sắp xếp chèn (Insertion Sort)
- **Ý tưởng:** Giả sử đoạn $A[0..i-1]$ đã được sắp xếp tăng dần. Xét phần tử $x = A[i]$, tìm vị trí thích hợp của $x$ trong đoạn $A[0..i-1]$ bằng cách duyệt lùi từ $j = i-1$ về $0$, liên tục dịch các phần tử $A[j] > x$ sang phải một vị trí ($A[j+1] = A[j]$). Khi gặp phần tử $\le x$ hoặc chạm đầu mảng thì chèn $x$ vào vị trí $A[j+1]$.
- **Mã giả (theo slide):**
  ```pascal
  Algorithm InsertionSort(Array A, n)
  Input: Mảng A có n phần tử
  Output: Mảng A được sắp theo thứ tự tăng dần của khóa
  for i <- 1 to n-1 do
      j <- i - 1;
      x <- A[i];
      while (j >= 0) and (A[j].Key > x.Key) do
          A[j+1] <- A[j];
          j <- j - 1;
      A[j+1] <- x;
  ```
- **Phân tích chi tiết:**
  - **Trường hợp tốt nhất (Best Case):** Mảng đã được sắp sẵn theo thứ tự tăng dần. Vòng lặp `while` chỉ kiểm tra điều kiện 1 lần rồi kết thúc ngay mà không dịch chuyển phần tử nào. Số phép so sánh là $n-1$, thời gian chạy là $O(n)$.
  - **Trường hợp xấu nhất (Worst Case):** Mảng có thứ tự giảm dần ngược lại. Mỗi phần tử $A[i]$ phải so sánh và dịch chuyển qua tất cả $i$ phần tử đứng trước nó. Tổng số phép dịch chuyển là $\sum_{i=1}^{n-1} i = \frac{n(n-1)}{2} = O(n^2)$.
  - **Trường hợp trung bình:** $O(n^2)$.
  - **Tính chất:** Ổn định (Stable), sắp xếp tại chỗ ($O(1)$ extra space), tính thích nghi cao (rất nhanh đối với mảng gần như đã sắp sẵn).

---

### 2.2. Bài Giảng 12: Sắp Xếp Thời Gian $O(n \log n)$ (Sorting $O(n \log n)$)

#### Thuật toán 1: Sắp xếp nhanh (Quick Sort)
- **Nguyên lý:** Áp dụng phương pháp Chia và trị (Divide and Conquer). Phân hoạch dãy cần sắp thành 3 phần:
  - $S_2$: Chứa đúng 1 phần tử gọi là chốt (pivot).
  - $S_1$: Gồm các phần tử $\le$ pivot.
  - $S_3$: Gồm các phần tử $>$ pivot.
  - Sau khi phân hoạch xong, pivot đã nằm ở vị trí chính xác cuối cùng trong mảng đã sắp. Tiếp tục gọi đệ quy phân hoạch độc lập trên $S_1$ và $S_3$.
- **Thuật toán đệ quy:**
  ```pascal
  Algorithm QuickSort(array A, int i, int j)
  if i < j then
      k = Partition(A, i, j); // k nhận chỉ số vị trí chốt
      QuickSort(A, i, k-1);
      QuickSort(A, k+1, j);
  ```
- **Thuật toán Phân hoạch (Partition - theo slide):**
  ```pascal
  Algorithm Partition(Array A, int i, int j, int &right)
  p <- A[i]; // Chọn phần tử đầu làm chốt
  left <- i; right <- j;
  while (left < right) do
      while (left <= right and A[left].Key <= p.Key) do
          left <- left + 1;
      while (A[right].Key > p.Key) do
          right <- right - 1;
      if left < right then
          SWAP(A[left], A[right]);
  if i <> right then
      A[i] <- A[right];
      A[right] <- p;
  ```
- **Đánh giá hiệu năng:**
  - Thủ tục phân hoạch duyệt qua mỗi phần tử tối đa một lần, tốn thời gian $O(n)$.
  - **Trường hợp tốt nhất:** Pivot luôn chia dãy thành 2 nửa bằng nhau ($n/2$). Cây đệ quy có độ sâu $\log_2 n$. Thời gian $T(n) = 2T(n/2) + O(n) = O(n \log n)$.
  - **Trường hợp trung bình:** Thời gian $O(n \log n)$.
  - **Trường hợp xấu nhất:** Pivot luôn là phần tử nhỏ nhất hoặc lớn nhất (ví dụ mảng đã sắp xếp và luôn chọn phần tử đầu làm pivot). Dãy bị phân hoạch thành 1 phần có 0 phần tử và 1 phần có $n-1$ phần tử. Chiều sâu đệ quy là $n$. Thời gian $T(n) = T(n-1) + O(n) = O(n^2)$.
  - **Bộ nhớ phụ:** Ngăn xếp đệ quy tốn $O(\log n)$ trong trường hợp tốt/trung bình, và $O(n)$ trong trường hợp xấu nhất.
  - **Tính chất:** Không ổn định (Unstable).

#### Thuật toán 2: Sắp xếp trộn (Merge Sort)
- **Nguyên lý:** Chia mảng cần sắp thành hai nửa độc lập tại vị trí giữa $k = \lfloor(i+j)/2\rfloor$. Gọi đệ quy sắp xếp từng nửa. Sau khi hai nửa đã có thứ tự, thực hiện thao tác trộn (Merge) hai nửa thành dãy có thứ tự hoàn chỉnh.
- **Mã giả MergeSort:**
  ```pascal
  Algorithm Mergesort(array A, int i, int j)
  if i < j then
      k <- (i + j) / 2;
      Mergesort(A, i, k);
      Mergesort(A, k+1, j);
      Merge(A, i, k, j);
  ```
- **Mã giả thủ tục Trộn (Merge):**
  - Sử dụng mảng phụ $B[i..j]$ và 2 con trỏ `left = i`, `right = k+1`, con trỏ đích `t = i`.
  - So sánh $A[left].key$ và $A[right].key$, phần tử nào nhỏ hơn thì chuyển sang $B[t]$ và tăng chỉ số tương ứng.
  - Khi một trong hai dãy con hết, chép nốt các phần tử còn lại của dãy kia sang $B$.
  - Sao chép toàn bộ các phần tử từ mảng phụ $B[i..j]$ trở lại mảng gốc $A[i..j]$.
- **Đánh giá hiệu năng:**
  - Chiều cao cây đệ quy $h = \lceil \log_2 n \rceil$.
  - Ở mỗi tầng của cây đệ quy, tổng công việc trộn trên tất cả các khối con đúng bằng $O(n)$.
  - **Thời gian chạy:** Luôn luôn là $O(n \log n)$ trong TẤT CẢ các trường hợp (tốt nhất, trung bình, xấu nhất).
  - **Không gian bộ nhớ phụ:** $O(n)$ cho mảng phụ $B$ (không phải là thuật toán tại chỗ).
  - **Tính chất:** Ổn định (Stable).

#### Thuật toán 3: Sắp xếp vun đống (Heap Sort)
- **Khái niệm Cây Heap (Đống):** Là một cây nhị phân gần hoàn chỉnh (complete binary tree) thỏa mãn tính chất Max-Heap:
  1. Giá trị khóa của nút gốc $\ge$ giá trị khóa của hai con.
  2. Tất cả các mức đều đầy, trừ mức thấp nhất có thể thiếu một số nút ở bên phải.
  3. Các nút lá xuất hiện liên tiếp từ trái qua phải.
  $\implies$ Nút gốc luôn lưu giữ phần tử có khóa lớn nhất.
- **Biểu diễn Cây Heap trên mảng (1-based index $A[1..n]$):**
  - Con trái của nút $i$: $2i$.
  - Con phải của nút $i$: $2i+1$.
  - Nút cha của nút $i$: $\lfloor i/2 \rfloor$.
  - Các nút nội (nút có con): từ $1$ đến $\lfloor n/2 \rfloor$.
  - Các nút lá (không có con, đương nhiên thỏa mãn tính chất đống): từ $\lfloor n/2 \rfloor + 1$ đến $n$.
- **Thủ tục Vun đống (Pushdown / Heapify):**
  - Nhận vào mảng $A$, chỉ số nút $i$ cần vun xuống, và kích thước hiện tại $n$.
  - So sánh khóa của $A[i]$ với các con của nó ($2i$ và $2i+1$). Tìm con có khóa lớn nhất (`max`).
  - Nếu $A[i].key < A[max].key$, thực hiện `swap(A[i], A[max])` và tiếp tục lặp/đệ quy xuống nút `max`. Dừng lại khi không còn con hoặc khi $A[i] \ge$ cả hai con.
  - Thời gian thực hiện `Pushdown`: Tỉ lệ thuận với chiều cao của cây con, tối đa $\log_2(n/i) \implies O(\log n)$.
- **Thuật toán HeapSort toàn diện (theo slide):**
  ```pascal
  Algorithm Heapsort(Array A, n)
  // Giai đoạn 1: Tạo đống ban đầu (Build Heap)
  for i <- n/2 downto 1 do
      Pushdown(A, i, n);

  // Giai đoạn 2: Trích xuất phần tử lớn nhất và sắp xếp
  for i <- n downto 2 do
      swap(A[1], A[i]);      // Đưa phần tử lớn nhất về cuối dãy
      Pushdown(A, 1, i-1);   // Vun lại đống trên mảng con kích thước i-1
  ```
- **Đánh giá hiệu năng:**
  - Giai đoạn tạo đống: Mặc dù gọi $n/2$ lần `Pushdown`, nhưng các nút ở gần đáy chỉ cần đi xuống ít bước. Tổng số phép toán chứng minh theo chuỗi hình học là $O(n)$ (thời gian tuyến tính).
  - Giai đoạn sắp xếp: Thực hiện $n-1$ lần hoán đổi và gọi `Pushdown` trên cây có chiều cao $\le \log_2 n \implies (n-1) \cdot O(\log n) = O(n \log n)$.
  - **Tổng thời gian chạy:** Luôn là $O(n \log n)$ trong mọi trường hợp (tốt nhất, trung bình, xấu nhất).
  - **Bộ nhớ phụ:** $O(1)$ (sắp xếp tại chỗ, không cần mảng phụ).
  - **Tính chất:** Không ổn định (Unstable).

---

### 2.3. Bài Giảng 13: Thuật Toán Tìm Kiếm (Search Algorithms)

#### Bài toán & Phân loại
- **Input:** Tập $S$ gồm $n$ phần tử, mỗi phần tử là một bộ Khóa - Giá trị (Key - Value), và một khóa cần tìm $k$.
- **Output:** Cho biết có phần tử mang khóa $k$ trong $S$ hay không, và trả về con trỏ/vị trí của phần tử đó.
- **3 phương pháp chính:**
  1. Tìm kiếm tuần tự (Sequential Search)
  2. Tìm kiếm nhị phân (Binary Search)
  3. Bảng băm (Hash Tables)

#### Tìm kiếm tuần tự (Sequential / Linear Search)
- **Tổ chức dữ liệu:** Mảng hoặc danh sách liên kết. Các phần tử không bắt buộc phải có thứ tự.
- **Thuật toán:** Duyệt từ đầu đến cuối dãy, so sánh lần lượt khóa của từng phần tử với $k$. Nếu trùng thì dừng và trả về thành công. Nếu duyệt hết dãy mà không thấy thì trả về thất bại.
- **Thời gian chạy:**
  - Tốt nhất: $O(1)$ (phần tử cần tìm nằm ngay vị trí đầu tiên).
  - Xấu nhất: $O(n)$ (phần tử nằm ở vị trí cuối cùng hoặc không tồn tại trong dãy).
  - Trung bình: $\frac{n+1}{2}$ phép so sánh $\implies O(n)$.

#### Tìm kiếm nhị phân trên mảng (Binary Search on Array)
- **Điều kiện tiên quyết:** Mảng $S$ BẮT BUỘC ĐÃ ĐƯỢC SẮP XẾP theo thứ tự tăng dần (hoặc giảm dần) của khóa.
- **Chiến lược:** Chia để trị (Divide and Conquer).
- **Thuật toán:**
  - Duy trì khoảng tìm kiếm $[i, j]$ (ban đầu $i = 1, j = n$).
  - Trong khi $i \le j$ và chưa tìm thấy:
    - Tính chỉ số giữa: `mid = (i + j) / 2`.
    - Nếu $k == S[mid].Key \implies$ tìm thấy, kết thúc.
    - Nếu $k < S[mid].Key \implies$ thu hẹp khoảng tìm kiếm sang nửa trái: $j = mid - 1$.
    - Nếu $k > S[mid].Key \implies$ thu hẹp khoảng tìm kiếm sang nửa phải: $i = mid + 1$.
- **Thời gian chạy:**
  - Sau mỗi phép so sánh, kích thước khoảng tìm kiếm giảm đi một nửa ($n, n/2, n/4, \dots$).
  - Tốt nhất: $O(1)$ (phần tử tìm thấy ngay tại vị trí giữa mảng ban đầu).
  - Xấu nhất: $O(\log_2 n)$ (khi không tìm thấy, số lần chia đôi tối đa là $\lfloor \log_2 n \rfloor + 1$).

#### Cây tìm kiếm nhị phân (Binary Search Tree - BST)
- **Định nghĩa:** Cây nhị phân mà tại mọi nút $v$:
  - Tất cả các nút thuộc cây con trái của $v$ có khóa $< v->getKey()$.
  - Tất cả các nút thuộc cây con phải của $v$ có khóa $> v->getKey()$.
  - Cả cây con trái và cây con phải cũng là cây tìm kiếm nhị phân.
- **Đặc điểm duyệt In-Order (Trung thứ tự: Left - Root - Right):**
  - Duyệt cây tìm kiếm nhị phân theo thứ tự giữa luôn cho ra danh sách các khóa theo thứ tự tăng dần!
- **Cấu trúc lớp Node và BST trong C++ (theo slide):**
  ```cpp
  template <class Keys, class T>
  class Node {
  private:
      Keys key;
      T elem;
      Node *Parent;
      Node *Left;
      Node *Right;
  public:
      Keys getKey();
      void setKey(Keys k);
      T getElem();
      void setElem(T o);
      Node* Left();
      Node* Right();
      Node* Parent();
      void setLeft(Node*);
      void setRight(Node*);
      void setParent(Node*);
  };
  ```
- **Thuật toán tìm kiếm trên BST (`TreeSearch`):**
  ```cpp
  Node* TreeSearch(Keys k, Node<T>* v) {
      if (v == NULL) return v;
      else if (k < v->getKey()) return TreeSearch(k, v->Left());
      else if (k == v->getKey()) return v;
      else return TreeSearch(k, v->Right());
  }
  ```
- **Thuật toán chèn (`InsertNode`):**
  ```cpp
  void InsertNode(Node *&root, Node *newNode) {
      if (root == NULL) root = newNode;
      else if (newNode->getKey() < root->getKey())
          InsertNode(root->Left(), newNode);
      else
          InsertNode(root->Right(), newNode);
  }
  ```
- **Thuật toán xóa nút (`Remove`):** Gồm 3 trường hợp:
  1. *Trường hợp 1 (Nút lá / Nút ngoài):* Nút không có con nào $\implies$ Xóa trực tiếp nút và gán con trỏ của nút cha trỏ tới NULL.
  2. *Trường hợp 2 (Nút có đúng 1 con):* Nút chỉ có con trái hoặc chỉ có con phải $\implies$ Xóa nút và nối trực tiếp con duy nhất đó vào nút cha của nút bị xóa.
  3. *Trường hợp 3 (Nút có cả 2 con):*
     - Tìm nút thế mạng: Là **nút tiền nhiệm (In-order predecessor)** - nút có khóa lớn nhất ở cây con trái (nút cực phải của cây con trái), HOẶC **nút kế vị (In-order successor)** - nút có khóa nhỏ nhất ở cây con phải (nút cực trái của cây con phải).
     - Sao chép khóa và dữ liệu của nút thế mạng vào nút cần xóa.
     - Sau đó gọi xóa nút thế mạng (nút này đảm bảo chỉ có tối đa 1 con, quy về Trường hợp 1 hoặc 2).
- **Phân tích độ phức tạp theo chiều cao $h$:**
  - Các thao tác `TreeSearch`, `InsertNode`, `Remove` đều đi dọc theo một đường đi từ gốc xuống lá, do đó tốn thời gian $O(h)$ với $h$ là chiều cao cây.
  - *Cây cân bằng (Balanced / Complete):* Chiều cao $h = \lfloor \log_2 n \rfloor \implies$ Thời gian các thao tác là $O(\log n)$.
  - *Cây suy biến (Degenerate / Skewed - như danh sách liên kết khi chèn dãy đã sắp xếp):* Chiều cao $h = n \implies$ Thời gian thao tác thoái hóa thành $O(n)$.

---

### 2.4. Bài Giảng 14: Bảng Băm (Hash Tables)

#### Khái niệm & Yêu cầu của Hàm Băm
- **Bảng băm:** Cấu trúc dữ liệu dựa trên mảng có kích thước $m$ (hoặc $N$), lưu trữ các cặp Khóa-Giá trị (Key-Value), cho phép truy xuất trực tiếp phần tử thông qua địa chỉ tính bằng hàm băm $h(k)$.
- **Hàm băm (Hash Function):** $h: K \to [0..m-1]$ ánh xạ không gian khóa $K$ vào tập các chỉ số số nguyên hợp lệ trong bảng.
- **Yêu cầu đối với hàm băm tốt:**
  1. Dải đều các khóa một cách ngẫu nhiên và đồng đều trên toàn bộ bảng địa chỉ.
  2. Tính toán đơn giản, tốc độ thực thi nhanh.
  3. Xác định (Deterministic): Cùng một khóa phải luôn cho ra cùng một giá trị băm.

#### Các phương pháp xây dựng hàm băm (Slide 5-8)
1. **Phương pháp chia (Division Method):**
   $$h(k) = k \bmod m$$
   - Trong đó $m$ là kích thước bảng.
   - *Quy tắc chọn $m$:* Thường chọn $m$ là một số nguyên tố (prime number) không quá gần với các lũy thừa của 2 hoặc 10 (ví dụ trong mã nguồn slide dùng $m = 97$).
2. **Phương pháp nhân / bình phương giữa (Mid-Square Method):**
   - Lấy giá trị khóa bình phương lên ($k^2$), sau đó trích lấy một số chữ số nằm ở phần giữa của kết quả để làm địa chỉ băm.
   - *Ưu điểm:* Các chữ số ở giữa phụ thuộc vào tất cả các chữ số của khóa ban đầu, do đó hai khóa chỉ khác nhau một chữ số nhỏ cũng sẽ tạo ra các địa chỉ băm rất khác nhau (hiệu ứng tuyết lở - avalanche effect).
3. **Phương pháp phân đoạn (Folding Method):**
   - Chia khóa thành các đoạn có độ dài bằng nhau (bằng độ dài của địa chỉ bảng).
   - *Kỹ thuật tách (Shift Folding):* Các đoạn được xếp thành từng hàng dóng lề rồi cộng lại với nhau.
   - *Kỹ thuật gấp (Boundary Folding):* Gấp các đoạn lại theo mép biên (như gấp giấy), đảo ngược chiều các đoạn xen kẽ rồi cộng lại.

#### Hiện tượng Đụng độ (Collision) & Giải quyết đụng độ
- **Đụng độ (Collision):** Xảy ra khi hai khóa khác nhau $k_1 \ne k_2$ nhưng cho cùng giá trị băm $h(k_1) = h(k_2)$. Do không gian khóa $|K| > m$, theo nguyên lý Dirichlet (Pigeonhole Principle), đụng độ là không thể tránh khỏi.
- **Phương pháp 1: Kết nối trực tiếp / Danh sách liên kết ngoài (Separate Chaining):**
  - Mỗi ô trong bảng băm $table[i]$ không chứa trực tiếp dữ liệu mà quản lý một danh sách liên kết (`SingleList<Keys, T>`).
  - Khi có nhiều phần tử có cùng mã băm $h(k)$, các phần tử này được chèn nối tiếp vào danh sách liên kết tại vị trí ô $table[h(k)]$.
  - *Minh họa slide (h(k) = k % 5):*
    - Bucket 1: $11 \to 21 \to 41$
    - Bucket 2: $12$
    - Bucket 3: $23$
    - Bucket 4: $44 \to 4 \to 34$
  - *Cài đặt C++ từ Slide 13 - 17:*
    ```cpp
    template <class Keys, class T>
    class Hashtable {
    private:
        int N;
        SingleList<Keys, T> *table;
    public:
        Hashtable(int n) {
            N = n;
            table = new SingleList<Keys, T>[N];
        }
        Node<Keys, T>* Add(Keys key, T obj, int (*hash)(Keys, int)) {
            int h = hash(key, N);
            Node<Keys, T> *p = table[h].getNode(key);
            if (p == NULL)
                return table[h].insertLast(key, obj);
            else
                return NULL; // Khóa đã tồn tại
        }
        void Remove(Keys key, int (*hash)(Keys, int)) {
            int h = hash(key, N);
            Node<Keys, T> *p = table[h].getNode(key);
            if (p != NULL) table[h].remove(p);
        }
        Node<Keys, T>* Find(Keys key, int (*hash)(Keys, int)) {
            int h = hash(key, N);
            return table[h].getNode(key);
        }
        int Contains(Keys key, int (*hash)(Keys, int)) {
            int h = hash(key, N);
            return (table[h].getNode(key) == NULL) ? 0 : 1;
        }
        int Count() {
            int t = 0;
            for (int i = 0; i < N; i++) t += table[i].size();
            return t;
        }
    };
    ```
- **Phương pháp 2: Địa chỉ mở (Open Addressing):**
  - Tất cả các phần tử được lưu trực tiếp trong các ô của mảng bảng băm (không dùng danh sách liên kết ngoài).
  - Khi ô $h(k)$ đã bị chiếm dụng, thuật toán sử dụng một chuỗi dò tìm (probing sequence) để tìm ô trống tiếp theo:
    1. *Thử tuyến tính (Linear Probing):*
       $$h(k, i) = (h(k) + i) \bmod m \quad (i = 0, 1, 2, \dots)$$
       Nhược điểm: Gây ra hiện tượng kết chùm nguyên phát (Primary Clustering) — các phần tử đụng độ dồn thành từng cụm dài liên tục, làm tăng mạnh số lần dò tìm.
    2. *Thử bậc hai (Quadratic Probing):*
       $$h(k, i) = (h(k) + c_1 i + c_2 i^2) \bmod m$$
       Khắc phục được hiện tượng kết chùm nguyên phát, nhưng có thể gặp kết chùm thứ phát (Secondary Clustering).
    3. *Băm kép (Double Hashing):*
       $$h(k, i) = (h_1(k) + i \cdot h_2(k)) \bmod m$$
       Sử dụng hai hàm băm độc lập. Yêu cầu $h_2(k)$ phải nguyên tố cùng nhau với kích thước bảng $m$ để có thể duyệt qua toàn bộ các ô trong bảng.
  - *Xóa phần tử trong Địa chỉ mở:* Không thể đơn giản gán ô thành rỗng (Empty), vì sẽ làm ngắt quãng chuỗi dò tìm của các phần tử được chèn sau đó. Cần dùng kỹ thuật xóa lười (Lazy Deletion) bằng cách đánh dấu ô là `DELETED` (hoặc Tombstone).
- **Hệ số tải (Load Factor) & Đánh giá hiệu năng:**
  - Hệ số tải: $\alpha = \frac{n}{m}$ ($n$ là số phần tử đã lưu, $m$ là kích thước bảng).
  - Với Separate Chaining: $\alpha$ có thể lớn hơn 1. Thời gian tìm kiếm trung bình là $O(1 + \alpha)$.
  - Với Open Addressing: Bắt buộc $\alpha < 1$ (thường duy trì $\alpha \le 0.7$ để đảm bảo hiệu năng).
  - *Thời gian chạy:*
    - Trường hợp tốt nhất / trung bình: $O(1)$ cho cả thêm, tìm, xóa.
    - Trường hợp xấu nhất: $O(n)$ (khi tất cả các khóa đều bị băm vào cùng một địa chỉ duy nhất).
  - *Ứng dụng trong C++ STL:* `std::unordered_map`, `std::unordered_set` cài đặt dựa trên bảng băm Separate Chaining.

---

## 3. Danh Mục Chủ Đề Câu Hỏi Ứng Viên (Candidate Question Themes)

Dưới đây là 60 chủ đề câu hỏi (15 chủ đề cho mỗi bài giảng từ 11 đến 14) được thiết kế chi tiết để làm đầu vào cho Agent tác giả ngân hàng câu hỏi (`questions.json`).

### 3.1. Chủ đề Câu hỏi — Bài Giảng 11: Sorting $O(n^2)$ (15 chủ đề)
1. **Định nghĩa bài toán sắp xếp:** Ý nghĩa của thuộc tính khóa (Key), hàm so sánh logic và tiêu chí sắp xếp tăng/giảm.
2. **Ý tưởng thuật toán Bubble Sort:** Cơ chế "nổi bọt" của các phần tử nhỏ về đầu dãy và các phần tử lớn chìm về cuối dãy.
3. **Mã giả vòng lặp Bubble Sort:** Xác định đúng cận vòng lặp ($i$ từ $0$ đến $n-2$; $j$ từ $n-1$ về $i+1$).
4. **Điều kiện tráo đổi trong Bubble Sort:** Biểu thức điều kiện `A[j].Key < A[j-1].Key` khi sắp tăng dần.
5. **Cơ chế hàm Swap trong C++:** Truyền tham chiếu (`&`) để hoán vị giá trị 2 biến qua biến phụ tạm thời.
6. **Tổng số phép so sánh của Bubble Sort:** Công thức tính tổng số lần so sánh cố định $\frac{n(n-1)}{2}$.
7. **Độ phức tạp thời gian Bubble Sort chưa tối ưu:** $O(n^2)$ trong cả trường hợp tốt nhất, trung bình và xấu nhất.
8. **Kỹ thuật tối ưu hóa Bubble Sort với cờ hiệu:** Cơ chế cờ `swapped` dừng thuật toán sớm, đưa thời gian tốt nhất về $O(n)$.
9. **Trace từng bước thuật toán Bubble Sort:** Xác định trạng thái của mảng sau lượt lặp $i=0$ hoặc $i=1$ với dãy số cụ thể.
10. **Ý tưởng thuật toán Selection Sort:** Tìm phần tử nhỏ nhất trong đoạn chưa sắp và tráo đổi với phần tử đầu đoạn.
11. **Mã giả và vị trí hoán đổi của Selection Sort:** Chỉ thực hiện `swap` đúng 1 lần sau khi kết thúc vòng lặp trong tìm `posmin`.
12. **Số phép tráo đổi tối đa của Selection Sort:** Tối đa $n-1$ phép tráo đổi; so sánh hiệu năng swap với Bubble Sort.
13. **Ý tưởng thuật toán Insertion Sort:** Chèn phần tử $A[i]$ vào đúng vị trí trong đoạn đã sắp $A[0..i-1]$ bằng cách dịch phần tử.
14. **Mã giả vòng lặp `while` dịch phần tử của Insertion Sort:** Điều kiện dừng `(j >= 0 && A[j].Key > x.Key)`.
15. **So sánh tính ổn định (Stability) & Không gian bộ nhớ:** Bubble Sort (ổn định), Insertion Sort (ổn định), Selection Sort (không ổn định); cả ba đều là in-place $O(1)$.

### 3.2. Chủ đề Câu hỏi — Bài Giảng 12: Sorting $O(n \log n)$ (15 chủ đề)
16. **Nguyên lý Chia và trị (Divide & Conquer) trong QuickSort:** Phân hoạch dãy thành $S_1 (\le p), S_2 (p), S_3 (> p)$ và đệ quy.
17. **Vai trò và vị trí của Pivot (Chốt):** Khái niệm chốt và việc chốt luôn nằm ở vị trí đúng cuối cùng sau phân hoạch.
18. **Cơ chế 2 con trỏ trong thuật toán Partition:** Quy tắc tăng `left` khi $A[left].key \le p.key$ và giảm `right` khi $A[right].key > p.key$.
19. **Thời gian chạy của thủ tục Partition:** Chứng minh thời gian phân hoạch tuyến tính $O(n)$.
20. **Độ phức tạp QuickSort trường hợp trung bình & tốt nhất:** $O(n \log n)$ khi pivot chia dãy thành các phần xấp xỉ bằng nhau.
21. **Trường hợp xấu nhất của QuickSort:** Thời gian $O(n^2)$ khi dãy đã có thứ tự và chọn pivot là phần tử đầu.
22. **Không gian bộ nhớ ngăn xếp đệ quy của QuickSort:** $O(\log n)$ trung bình và $O(n)$ trường hợp xấu nhất; tính không ổn định.
23. **Nguyên lý phân chia và trộn trong MergeSort:** Chia đôi tại $\lfloor(i+j)/2\rfloor$ và trộn 2 dãy con đã sắp xếp.
24. **Hoạt động của thủ tục Merge:** Sử dụng mảng phụ $B$, so sánh 2 con trỏ và sao chép ngược lại mảng gốc $A$.
25. **Độ phức tạp thời gian của MergeSort:** Luôn là $O(n \log n)$ trong TẤT CẢ các trường hợp; chiều cao cây $\log n$.
26. **Chi phí bộ nhớ phụ và tính ổn định của MergeSort:** Bộ nhớ phụ $O(n)$; MergeSort là thuật toán sắp xếp ổn định.
27. **Định nghĩa Cây Heap và tính chất Max-Heap:** Cây nhị phân gần hoàn chỉnh, nút gốc $\ge$ nút con, gốc chứa giá trị lớn nhất.
28. **Biểu diễn Heap trên mảng 1-based index:** Vị trí con trái ($2i$), con phải ($2i+1$), nút cha ($\lfloor i/2 \rfloor$), các nút lá ($> n/2$).
29. **Thuật toán Vun đống (Pushdown / Heapify):** So sánh với con lớn nhất, hoán vị và tiếp tục hạ thấp; thời gian $O(\log n)$.
30. **Quy trình 2 giai đoạn của HeapSort:** Tạo đống $O(n)$ từ $n/2$ về 1, sau đó liên tục tráo đổi gốc $A[1]$ với $A[i]$ và vun đống lại; thời gian $O(n \log n)$, bộ nhớ $O(1)$, không ổn định.

### 3.3. Chủ đề Câu hỏi — Bài Giảng 13: Search Algorithms (15 chủ đề)
31. **Khái niệm bài toán tìm kiếm:** Mô hình bộ dữ liệu Khóa - Giá trị (Key-Value) và mục tiêu tìm kiếm theo khóa $k$.
32. **Nguyên lý Tìm kiếm tuần tự (Sequential Search):** Duyệt lần lượt trên mảng/danh sách không yêu cầu sắp thứ tự.
33. **Thời gian chạy của Tìm kiếm tuần tự:** Tốt nhất $O(1)$, xấu nhất $O(n)$, trung bình $(n+1)/2$ phép so sánh $\implies O(n)$.
34. **Điều kiện áp dụng Tìm kiếm nhị phân:** Mảng BẮT BUỘC phải được sắp xếp trước theo thứ tự khóa.
35. **Chiến lược chia đôi trong Binary Search:** Công thức tính `mid = (i + j) / 2` và cách cập nhật $j = mid - 1$ hoặc $i = mid + 1$.
36. **Thời gian chạy của Tìm kiếm nhị phân trên mảng:** $O(\log_2 n)$ trong trường hợp xấu nhất; $O(1)$ tốt nhất.
37. **Định nghĩa Cây tìm kiếm nhị phân (BST):** Quan hệ khóa cây con trái $<$ gốc $<$ cây con phải tại mọi nút.
38. **Duyệt trung thứ tự (In-Order Traversal) trên BST:** Thứ tự Left - Root - Right luôn sinh ra dãy khóa tăng dần.
39. **Thuật toán tìm kiếm đệ quy `TreeSearch`:** So sánh khóa và rẽ nhánh trái/phải; thời gian $O(h)$ với $h$ là chiều cao cây.
40. **Thao tác chèn nút `InsertNode` vào BST:** Tìm vị trí thích hợp và gán nút mới làm lá của cây; thời gian $O(h)$.
41. **Thao tác xóa nút lá trên BST:** Hủy nút và gán liên kết của nút cha về NULL; không ảnh hưởng cấu trúc cây còn lại.
42. **Thao tác xóa nút có 1 con trên BST:** Nối trực tiếp con duy nhất của nút bị xóa vào nút cha.
43. **Thao tác xóa nút có 2 con trên BST:** Tìm nút tiền nhiệm (cực phải cây con trái) hoặc nút kế vị (cực trái cây con phải) để thế thân.
44. **Chiều cao cây BST trong trường hợp tốt nhất vs xấu nhất:** $h = O(\log n)$ khi cân bằng; $h = O(n)$ khi cây suy biến thành đường thẳng.
45. **So sánh hiệu năng BST với Mảng đã sắp:** Mảng tìm $O(\log n)$ nhưng chèn/xóa $O(n)$; BST cân bằng tìm, chèn, xóa đều đạt $O(\log n)$.

### 3.4. Chủ đề Câu hỏi — Bài Giảng 14: Hash Tables (15 chủ đề)
46. **Khái niệm Bảng băm & Hàm băm:** Mục tiêu ánh xạ trực tiếp khóa vào vị trí lưu trữ trong bảng thông qua $h(k)$.
47. **Tiêu chuẩn của một hàm băm tốt:** Phân bổ đồng đều ngẫu nhiên, tính toán nhanh chóng, mang tính xác định.
48. **Phương pháp chia (Division Method):** Công thức $h(k) = k \bmod m$; lý do chọn $m$ là số nguyên tố không gần lũy thừa của 2 hoặc 10.
49. **Phương pháp bình phương giữa (Mid-Square Method):** Bình phương $k^2$ và lấy các chữ số ở giữa; tính phụ thuộc vào toàn bộ chữ số của khóa.
50. **Phương pháp phân đoạn (Folding Method):** Kỹ thuật tách dóng lề (Shift folding) và kỹ thuật gấp mép (Boundary folding).
51. **Hiện tượng đụng độ (Collision) & Nguyên lý Dirichlet:** Lý do tất yếu xảy ra đụng độ khi không gian khóa lớn hơn kích thước bảng.
52. **Cơ chế Separate Chaining (Danh sách liên kết ngoài):** Mỗi ô mảng là một thùng chứa (bucket) quản lý danh sách liên kết các phần tử đụng độ.
53. **Cài đặt C++ của bảng băm Separate Chaining:** Mảng danh sách `table = new SingleList<Keys, T>[N]` và con trỏ hàm băm `int (*hash)(Keys, int)`.
54. **Thao tác thêm phần tử `Add` trong C++:** Tính chỉ số băm, kiểm tra trùng khóa qua `getNode(key)`, chèn đuôi nếu chưa có.
55. **Hàm đếm số lượng `Count()`:** Duyệt qua tất cả $N$ thùng chứa và cộng dồn kích thước `size()` của từng danh sách.
56. **Khái niệm Hệ số tải (Load Factor $\alpha$):** Định nghĩa $\alpha = n / m$; ý nghĩa đối với hiệu năng và độ dài trung bình của các bucket.
57. **Độ phức tạp thời gian của Bảng băm:** Trung bình $O(1)$ cho tìm, thêm, xóa; xấu nhất $O(n)$ khi toàn bộ khóa rơi vào cùng 1 ô.
58. **Địa chỉ mở — Thử tuyến tính (Linear Probing):** Công thức $h(k, i) = (h(k) + i) \bmod m$ và hiện tượng kết chùm nguyên phát (Primary Clustering).
59. **Địa chỉ mở — Thử bậc hai & Băm kép (Quadratic Probing & Double Hashing):** Công thức và ưu thế giảm thiểu hiện tượng kết chùm.
60. **Xóa phần tử trong Địa chỉ mở (Tombstone):** Lý do phải đánh dấu ô xóa (`DELETED`) thay vì làm rỗng để duy trì chuỗi dò tìm.

---

## 4. Phân Tích & Thiết Kế Kiến Trúc Hệ Thống Quiz Game

### 4.1. Cấu Trúc Ngân Hàng Câu Hỏi (`questions.json`)
Ngân hàng câu hỏi cần được chuẩn hóa cao để phục vụ hiển thị mượt mà trên giao diện Web cũng như kiểm tra tự động qua các script:

#### JSON Schema Chuẩn
```json
[
  {
    "id": 151,
    "topicId": 11,
    "topicName": "Sorting O(n²)",
    "question": "Trong thuật toán Bubble Sort tăng dần, khi nào thì thủ tục tráo đổi swap(A[j-1], A[j]) được thực hiện?",
    "options": [
      "A[j].Key < A[j-1].Key",
      "A[j].Key > A[j-1].Key",
      "A[j].Key == A[j-1].Key",
      "A[j].Key >= A[j-1].Key"
    ],
    "answer": "A[j].Key < A[j-1].Key",
    "explanation": "Trong Bubble Sort theo slide bài giảng, vòng lặp j duyệt từ cuối mảng về đầu (n-1 downto i+1). Khi phần tử đứng sau nhỏ hơn phần tử đứng trước (A[j].Key < A[j-1].Key), hai phần tử này bị tráo đổi để nổi bọt phần tử nhỏ hơn về phía trước."
  }
]
```

#### Các Quy Tắc Kiểm Soát Dữ Liệu (Constraints)
1. `id`: Số nguyên dương duy nhất tăng dần từ 1 đến $N \ge 200$.
2. `topicId`: Số nguyên từ 1 đến 14 tương ứng chính xác với 14 bài giảng:
   - 1: Introduction & Overview
   - 2: Basic C++ Language
   - 3: Classes & OOP in C++
   - 4: Algorithm Analysis & Big-O
   - 5: Recursion
   - 6: Vector & Dynamic Arrays
   - 7: Linked List
   - 8: Stack
   - 9: Queue
   - 10: Trees
   - 11: Sorting O(n²)
   - 12: Sorting O(n log n)
   - 13: Search Algorithms
   - 14: Hash Tables
3. `topicName`: Chuỗi định danh thống nhất cho từng chuyên đề.
4. `question`: Câu hỏi bằng tiếng Việt rõ ràng, giữ nguyên thuật ngữ kỹ thuật tiếng Anh (ví dụ: `pivot`, `heapify`, `in-order`, `pushdown`, `chaining`, `worst-case`).
5. `options`: Mảng gồm ĐÚNG 4 chuỗi lựa chọn phân biệt (distinct).
   - *Khuyến nghị kiến trúc:* Chuỗi trong `options` KHÔNG nên gắn cứng tiền tố `"A. "`, `"B. "`, `"C. "`, `"D. "` trong JSON. Thay vào đó, để chuỗi nội dung thuần (bare strings). Khi Quiz Engine xáo trộn các lựa chọn bằng thuật toán Fisher-Yates, giao diện Web sẽ tự động gán nhãn A, B, C, D động dựa trên chỉ số vị trí hiện tại. Điều này loại bỏ hoàn toàn nguy cơ xáo trộn bị hiển thị sai thứ tự như `"B. ..."` đứng ở dòng đầu tiên!
6. `answer`: Chuỗi đáp án chính xác, BẮT BUỘC phải trùng khớp 100% với một trong 4 phần tử trong mảng `options`.
7. `explanation`: Giải thích sư phạm chi tiết bằng tiếng Việt, phân tích tại sao đáp án đó đúng, chỉ rõ mã giả hoặc slide liên quan.

---

### 4.2. Thiết Kế Quiz Engine & Gameplay Logic

Hệ thống Quiz Engine được thiết kế theo hướng module hóa, xử lý thuần túy bằng JavaScript trên trình duyệt (client-side):

```
+-------------------------------------------------------------------+
|                        Quiz Engine Core                           |
+-------------------------------------------------------------------+
|  1. Bank Loader & Validator                                       |
|     - Loads questions.json (hoặc nạp từ window.QUIZ_QUESTIONS)    |
|     - Cung cấp phương thức lọc theo Topic, tìm kiếm từ khóa       |
+-------------------------------------------------------------------+
|  2. Session Generator                                             |
|     - Random Round: Chọn ngẫu nhiên 5 câu từ 200+ câu             |
|     - Phân bổ chủ đề: Ưu tiên chọn 5 câu từ 5 chủ đề khác nhau     |
|     - Option Shuffler: Fisher-Yates shuffle trên mảng options     |
+-------------------------------------------------------------------+
|  3. Game State Manager                                            |
|     - Trạng thái vòng chơi: currentIndex, score, timer, answers   |
|     - Xử lý tương tác: chọn đáp án, khóa nút, hiển thị đúng/sai   |
|     - Tính toán kết quả: điểm số, phần trăm, thời gian hoàn thành |
+-------------------------------------------------------------------+
|  4. Review & Replay System                                        |
|     - Review Mode: Xem lại các câu sai kèm giải thích chi tiết    |
|     - Restart Mode: Làm mới vòng chơi 5 câu chỉ với 1 click       |
|     - Practice Mode: Luyện tập toàn bộ câu hỏi theo từng chủ đề   |
+-------------------------------------------------------------------+
```

#### Chi Tiết Các Cơ Chế Chính:
1. **Chế độ Chơi Nhanh 5 Câu (Quick 5-Question Session):**
   - Lựa chọn 5 chủ đề ngẫu nhiên khác nhau từ 14 chủ đề. Với mỗi chủ đề được chọn, bốc ngẫu nhiên 1 câu hỏi. Nếu số câu hỏi không đủ, bốc ngẫu nhiên từ ngân hàng chung không trùng lặp.
2. **Xáo Trộn Đáp Án (Answer Shuffling):**
   - Áp dụng thuật toán Fisher-Yates shuffle chuẩn:
     ```javascript
     function shuffleOptions(options) {
       const array = [...options];
       for (let i = array.length - 1; i > 0; i--) {
         const j = Math.floor(Math.random() * (i + 1));
         [array[i], array[j]] = [array[j], array[i]];
       }
       return array;
     }
     ```
   - Đáp án đúng được lưu dưới dạng giá trị chuỗi thuần, do đó sau khi xáo trộn, logic so sánh `selectedOption === currentQuestion.answer` luôn hoạt động tuyệt đối chính xác.
3. **Phản Hồi Tức Thì & Trải Nghiệm Người Dùng (Immediate Feedback):**
   - Khi người dùng click chọn 1 lựa chọn:
     - Nếu đúng: Nút đổi màu xanh lá (`bg-emerald-500/emerald-600`), phát âm thanh chúc mừng ngắn (ting), tăng điểm.
     - Nếu sai: Nút vừa bấm đổi màu đỏ (`bg-rose-500`), đồng thời nút chứa đáp án đúng tự động sáng xanh lá để người chơi nhận biết ngay.
     - Khóa ngay lập tức 4 nút lựa chọn để chống bấm nhiều lần.
     - Hiển thị khối Giải thích (Explanation Box) có màu sắc nổi bật, trích dẫn kiến thức bài giảng.
     - Nút "Câu tiếp theo" xuất hiện với hiệu ứng mượt mà.
4. **Màn Hình Kết Quả & Chúc Mừng (Session Summary & Celebration):**
   - Tổng kết điểm: ví dụ `Điểm số: 5/5 (100%)`.
   - Thời gian làm bài: định dạng `mm:ss`.
   - Huy hiệu đánh giá:
     - 5/5: "Xuất sắc! Bậc thầy C++ & Cấu trúc dữ liệu! 🏆"
     - 4/5: "Làm rất tốt! Nắm vững kiến thức! 🌟"
     - 3/5: "Khá tốt! Hãy ôn lại một số khái niệm nhé! 💡"
     - $\le 2/5$: "Cần cố gắng thêm! Hãy xem lại phần giải thích! 📚"
   - Hiệu ứng pháo hoa Confetti kích hoạt khi đạt điểm cao ($\ge 80\%$).
   - Các nút thao tác: "Chơi lại vòng mới (5 câu ngẫu nhiên)", "Xem lại các câu sai", "Luyện tập theo chuyên đề".
5. **Chế Độ Luyện Tập & Tra Cứu (Practice & Explorer Mode):**
   - Cho phép người dùng lọc câu hỏi theo bất kỳ chủ đề nào trong 14 chủ đề để ôn tập chuyên sâu.
   - Thanh tìm kiếm tức thì theo từ khóa câu hỏi hoặc code snippet.

---

### 4.3. Kiến Trúc Frontend Độc Lập (`index.html`)

Nhằm đảm bảo yêu cầu "Standalone, zero-install runnable directly in modern browsers", Frontend được xây dựng theo kiến trúc Single Page Application (SPA) gói gọn:

1. **Giao Diện & Thư Viện UI:**
   - **Tailwind CSS:** Tải qua CDN (`https://cdn.tailwindcss.com`) với cấu hình bảng màu Slate/Indigo hiện đại, bo góc mềm mại, đổ bóng cao cấp.
   - **Biểu tượng (Icons):** Thư viện Lucide Icons qua CDN (`https://unpkg.com/lucide@latest`) hoặc nhúng trực tiếp SVG để đảm bảo hiển thị hoàn hảo ngay cả khi ngắt kết nối mạng.
   - **Phông chữ:** Sử dụng font Inter / system-ui hiện đại cho văn bản tiếng Việt và `JetBrains Mono` / `Courier New` cho các đoạn mã nguồn C++.
2. **Âm Thanh Tương Tác Thuần Web Audio API:**
   - Hoàn toàn KHÔNG sử dụng file âm thanh `.mp3` / `.wav` tải ngoài (tránh lỗi 404 hoặc CORS khi chạy qua file://).
   - Tự động tổng hợp âm thanh bằng `AudioContext`:
     - Âm thanh Đúng: Tần số dao động mượt từ 523Hz (C5) lên 659Hz (E5) tạo tiếng chuông vui tươi.
     - Âm thanh Sai: Tần số dao động trầm từ 220Hz xuống 160Hz với sóng răng cưa (sawtooth) tạo cảm giác nhắc nhở nhẹ nhàng.
     - Âm thanh Chiến thắng: Hợp âm rộn rã khi hoàn thành xuất sắc vòng chơi.
3. **Hiệu Ứng Pháo Hoa (Confetti):**
   - Nhúng Canvas-Confetti qua CDN hoặc cung cấp module rơi hoa giấy bằng Canvas JS thuần dự phòng (zero-dependency fallback).
4. **Cơ Chế Nạp Dữ Liệu Chống Lỗi CORS trên Trình Duyệt:**
   - *Vấn đề bảo mật trình duyệt:* Khi mở file trực tiếp dạng `file:///D:/c++/quiz_game/index.html`, lệnh `fetch('questions.json')` có thể bị trình duyệt (đặc biệt là Chrome) chặn theo chính sách CORS cục bộ.
   - *Giải pháp tối ưu:* Cung cấp song song 2 cơ chế:
     - Gói ngân hàng câu hỏi thành cả `questions.json` VÀ một file `questions.js` (gán biến `window.QUIZ_QUESTIONS = [...]`).
     - Khi chạy, `index.html` nhúng thẻ `<script src="questions.js"></script>`. Nếu biến `window.QUIZ_QUESTIONS` đã có sẵn dữ liệu thì nạp trực tiếp ngay lập tức mà không cần gọi `fetch()`. Nếu mở qua máy chủ HTTP (Live Server, Vite, Nginx...), ứng dụng có thể fetch `questions.json` linh hoạt. Điều này đảm bảo 100% trải nghiệm "Double click là chạy ngay trên mọi máy tính"!

---

### 4.4. Đặc Tả Bộ Công Cụ Kiểm Thử Tự Động (Verification & Test Runner)

Cần cung cấp 2 kịch bản kiểm thử độc lập có thể chạy bằng dòng lệnh (Python 3.11):

#### 1. Kịch bản Xác thực Dữ liệu Ngân hàng Câu hỏi (`verify_bank.py`)
Kiểm tra tính toàn vẹn và chất lượng của `questions.json`:
- [x] Định dạng JSON hợp lệ, không có lỗi cú pháp.
- [x] Tổng số lượng câu hỏi $\ge 200$.
- [x] Đủ 14 `topicId` từ 1 đến 14; mỗi chủ đề có $\ge 14$ câu hỏi (đảm bảo phân bổ đều).
- [x] Mỗi bản ghi có đầy đủ các trường: `id`, `topicId`, `topicName`, `question`, `options`, `answer`, `explanation`.
- [x] Trường `options` là mảng có ĐÚNG 4 chuỗi, không có phần tử rỗng và không có 2 lựa chọn trùng nhau trong cùng một câu.
- [x] Trường `answer` phải trùng khớp chính xác tuyệt đối với 1 trong 4 lựa chọn trong `options`.
- [x] Trường `explanation` có độ dài tối thiểu $\ge 20$ ký tự để đảm bảo tính giải thích sư phạm.
- [x] Không có câu hỏi nào bị trùng lặp nội dung hoàn toàn (`question` duy nhất).

#### 2. Kịch bản Kiểm tra Quiz Engine Logic (`test_quiz_engine.py`)
Mô phỏng hoạt động của engine trong môi trường kiểm thử tự động:
- [x] **Test 5-Question Selection:** Chạy 100 phiên chơi ngẫu nhiên, xác nhận mỗi phiên luôn trả về đúng 5 câu hỏi phân biệt, và các câu hỏi đến từ ít nhất 4-5 chủ đề khác nhau.
- [x] **Test Option Shuffling:** Với cùng một câu hỏi, thực hiện xáo trộn 50 lần; xác minh thứ tự các lựa chọn thay đổi ngẫu nhiên nhưng đáp án đúng `answer` vẫn luôn tồn tại trong danh sách xáo trộn và được nhận diện chính xác.
- [x] **Test Scoring & State Transition:** Mô phỏng trả lời đúng/sai từng câu và kiểm tra tính toán điểm số, phần trăm chính xác 100%.

---

## 5. Đề Xuất Kế Hoạch Triển Khai (Actionable Recommendations)

1. **Tạo Ngân Hàng Câu Hỏi Toàn Diện 200+ Câu:**
   - Phân chia đều: Mỗi chủ đề từ 1 đến 14 đóng góp từ 15 đến 16 câu hỏi chất lượng cao.
   - Nhóm 1-5: Kiến thức nền tảng C++, con trỏ, OOP, phân tích giải thuật, đệ quy (~75 câu).
   - Nhóm 6-10: Cấu trúc dữ liệu tuyến tính và phi tuyến: Vector, Linked List, Stack, Queue, Binary Tree & AVL (~75 câu).
   - Nhóm 11-14: Sắp xếp $O(n^2)$, Sắp xếp $O(n \log n)$, Tìm kiếm & Cây BST, Bảng băm (~60 câu).
   - Đảm bảo câu hỏi bám sát các đoạn mã giả, mã C++, và các bài toán tính toán độ phức tạp trong slide.
2. **Cấu Trúc Tệp Dự Án Chuẩn:**
   ```
   D:\c++\quiz_game\
   ├── index.html              # Standalone Single-Page Application (HTML + Tailwind + Lucide + JS)
   ├── questions.json          # File ngân hàng câu hỏi JSON chuẩn (>= 200 câu)
   ├── questions.js            # Dữ liệu ngân hàng câu hỏi bọc trong window.QUIZ_QUESTIONS (chống CORS)
   ├── verify_bank.py          # Script kiểm tra hợp lệ dữ liệu JSON (schema, số lượng, tính duy nhất)
   ├── test_quiz_engine.py     # Script kiểm tra logic chọn 5 câu, xáo trộn, tính điểm
   └── README.md               # Hướng dẫn mở và chơi, chạy test kiểm thử
   ```
3. **Phân Định Công Việc Giữa Các Agent:**
   - **Question Author Worker:** Dựa vào danh mục 60 chủ đề của Survey 3 và 150 chủ đề của Survey 1 & 2 để sinh file `questions.json` và `questions.js`.
   - **Frontend Developer Worker:** Hiện thực hóa giao diện `index.html` với đầy đủ chế độ 5 câu, hiệu ứng âm thanh Web Audio, pháo hoa, luyện tập theo chủ đề và tra cứu.
   - **QA / Test Engineer:** Chạy `verify_bank.py` và `test_quiz_engine.py` để nghiệm thu sản phẩm.
