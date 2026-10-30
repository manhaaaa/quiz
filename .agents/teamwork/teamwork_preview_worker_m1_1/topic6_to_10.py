# -*- coding: utf-8 -*-
"""
Questions for Topics 6 to 10 (q076 - q150).
Topic 6: Vector & Dynamic Arrays (q076 - q090)
Topic 7: Linked List (Singly, Doubly, Circular) (q091 - q105)
Topic 8: Stack (q106 - q120)
Topic 9: Queue (q121 - q135)
Topic 10: Trees (Binary Tree, BST, AVL) (q136 - q150)
"""

def get_topics_6_to_10():
    questions = [
        # --- Topic 6: Vector & Dynamic Arrays (q076 - q090) ---
        {
            "id": "q076",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Khái niệm Kiểu dữ liệu trừu tượng Vector (Vector ADT) trong C++ khác biệt căn bản nhất với Mảng tĩnh (Static Array) ở điểm nào?",
            "options": [
                "Vector có khả năng tự động co giãn kích thước linh hoạt trên heap và quản lý bộ nhớ tự động theo cơ chế RAII",
                "Vector chỉ lưu trữ được kiểu dữ liệu chuỗi ký tự string",
                "Mảng tĩnh có thể mở rộng kích thước bất kỳ lúc nào mà không cần cấp phát lại",
                "Vector không cho phép truy xuất phần tử ngẫu nhiên qua chỉ số O(1)"
            ],
            "answer": "Vector có khả năng tự động co giãn kích thước linh hoạt trên heap và quản lý bộ nhớ tự động theo cơ chế RAII",
            "explanation": "Theo Slide Lecture 6, Vector ADT mở rộng khái niệm mảng: nó quản lý một vùng nhớ liên tục trên Heap, có khả năng tự động cấp phát mở rộng kích thước khi đầy và tự động giải phóng vùng nhớ khi hủy theo nguyên lý RAII."
        },
        {
            "id": "q077",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Trong thư viện chuẩn C++ `std::vector`, phương thức `size()` và phương thức `capacity()` khác nhau như thế nào?",
            "options": [
                "`size()` là số lượng phần tử thực tế đang có; còn `capacity()` là dung lượng bộ nhớ tối đa đã được cấp phát trước khi phải tái cấp phát",
                "`size()` luôn luôn lớn hơn hoặc bằng `capacity()` trong mọi thời điểm",
                "`capacity()` là số lượng phần tử hiện tại; còn `size()` là kích thước tối đa của bộ nhớ RAM máy tính",
                "Hai phương thức này hoàn toàn đồng nghĩa và luôn trả về cùng một giá trị như nhau"
            ],
            "answer": "`size()` là số lượng phần tử thực tế đang có; còn `capacity()` là dung lượng bộ nhớ tối đa đã được cấp phát trước khi phải tái cấp phát",
            "explanation": "Trong `std::vector`, `size()` là số phần tử hiện hữu đang lưu trong vector, trong khi `capacity()` là dung lượng ô nhớ buffer đã được hệ thống cấp phát trước. Bất đẳng thức luôn thỏa mãn là: `capacity >= size`."
        },
        {
            "id": "q078",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Sự khác biệt cốt lõi giữa hai phương thức `v.reserve(n)` và `v.resize(n)` trong `std::vector` là gì?",
            "options": [
                "`reserve(n)` chỉ đặt trước dung lượng bộ nhớ `capacity`, không thay đổi `size()`; còn `resize(n)` thay đổi trực tiếp `size()` và khởi tạo các phần tử mới",
                "`reserve(n)` thêm n phần tử vào cuối vector; còn `resize(n)` chỉ thay đổi dung lượng bộ nhớ",
                "`reserve(n)` chỉ dùng được khi vector rỗng; `resize(n)` chỉ dùng khi vector đã đầy",
                "Cả hai phương thức đều làm tăng `size()` và gán giá trị mặc định cho các phần tử mới"
            ],
            "answer": "`reserve(n)` chỉ đặt trước dung lượng bộ nhớ `capacity`, không thay đổi `size()`; còn `resize(n)` thay đổi trực tiếp `size()` và khởi tạo các phần tử mới",
            "explanation": "Phương thức `reserve(n)` chỉ cấp phát trước bộ nhớ để `capacity >= n` nhằm tránh tái cấp phát liên tục khi push_back, `size()` không đổi. Trong khi `resize(n)` thay đổi số phần tử thực tế thành $n$, nếu $n > size$ sẽ khởi tạo thêm các phần tử mới."
        },
        {
            "id": "q079",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Khi truy cập phần tử tại chỉ số `i` trong `std::vector`, điểm khác biệt giữa toán tử `v[i]` và phương thức `v.at(i)` là gì?",
            "options": [
                "`operator[]` không kiểm tra biên chỉ số; còn `at(i)` có kiểm tra biên và ném ra ngoại lệ `std::out_of_range` nếu vượt quá kích thước",
                "`operator[]` có tốc độ chậm hơn `at(i)` vì phải giải mã chuỗi con trỏ",
                "`at(i)` không cho phép sửa đổi giá trị phần tử; chỉ `operator[]` mới sửa được",
                "`operator[]` sẽ tự động mở rộng vector nếu chỉ số vượt quá giới hạn"
            ],
            "answer": "`operator[]` không kiểm tra biên chỉ số; còn `at(i)` có kiểm tra biên và ném ra ngoại lệ `std::out_of_range` nếu vượt quá kích thước",
            "explanation": "Toán tử `v[i]` ưu tiên tốc độ tối đa nên không kiểm tra biên (no bounds checking), nếu truy cập ngoài chỉ số sẽ dẫn đến Undefined Behavior. Ngược lại, `v.at(i)` kiểm tra an toàn nếu $i \\ge v.size()$ sẽ ném ngoại lệ `std::out_of_range`."
        },
        {
            "id": "q080",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Độ phức tạp thời gian của thao tác chèn phần tử vào cuối vector `v.push_back(val)` trong C++ được đánh giá chuẩn xác nhất là gì?",
            "options": [
                "Chi phí trung bình khấu hao (Amortized Time) là $O(1)$",
                "Luôn luôn là hằng số $O(1)$ trong mọi trường hợp xấu nhất",
                "Chi phí luôn là $O(n)$ trong mọi lần gọi",
                "Chi phí là $O(\\log n)$"
            ],
            "answer": "Chi phí trung bình khấu hao (Amortized Time) là $O(1)$",
            "explanation": "Phần lớn các thao tác `push_back` chỉ tốn $O(1)$ khi buffer còn chỗ. Khi buffer bị đầy, vector phải tái cấp phát và copy $n$ phần tử ($O(n)$). Tuy nhiên nhờ chiến lược nhân đôi dung lượng, chi phí trung bình khấu hao (Amortized time) cho mỗi thao tác push_back vẫn đạt $O(1)$."
        },
        {
            "id": "q081",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Tại sao các thao tác chèn `v.insert(pos, val)` hoặc xóa `v.erase(pos)` ở vị trí bất kỳ trong `std::vector` lại có độ phức tạp thời gian là $O(n)$?",
            "options": [
                "Vì vector phải dịch chuyển tất cả các phần tử nằm phía sau vị trí thao tác sang phải (khi chèn) hoặc sang trái (khi xóa)",
                "Vì vector phải duyệt qua toàn bộ RAM máy tính để tìm ô nhớ trống",
                "Vì trình biên dịch C++ bắt buộc phải sắp xếp lại toàn bộ vector sau mỗi thao tác",
                "Vì vector chuyển đổi nội bộ thành danh sách liên kết đơn khi chèn"
            ],
            "answer": "Vì vector phải dịch chuyển tất cả các phần tử nằm phía sau vị trí thao tác sang phải (khi chèn) hoặc sang trái (khi xóa)",
            "explanation": "Do vector lưu trữ các phần tử trên một vùng nhớ liên tục (contiguous array), nên khi chèn một phần tử vào giữa, tất cả các phần tử từ vị trí đó về cuối phải dịch sang phải 1 bước ($O(n)$). Tương tự khi xóa, các phần tử phía sau phải dịch sang trái 1 bước."
        },
        {
            "id": "q082",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Trong `std::vector`, bộ duyệt (Iterator) trả về bởi phương thức `v.end()` trỏ tới vị trí nào?",
            "options": [
                "Vị trí ngay sau phần tử cuối cùng trong vector (past-the-end element)",
                "Chính xác phần tử cuối cùng đang có trong vector",
                "Phần tử đầu tiên ở vị trí chỉ số 0",
                "Địa chỉ ô nhớ của biến `size()`"
            ],
            "answer": "Vị trí ngay sau phần tử cuối cùng trong vector (past-the-end element)",
            "explanation": "Trong chuẩn C++ STL, nửa khoảng duyệt là $[begin, end)$. Iterator `v.begin()` trỏ tới phần tử đầu tiên, còn `v.end()` trỏ tới vị trí ảo ngay sau phần tử cuối cùng (past-the-end element), dùng làm mốc dừng cho vòng lặp."
        },
        {
            "id": "q083",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Để duyệt ngược các phần tử của một `std::vector` từ phần tử cuối cùng về phần tử đầu tiên, ta sử dụng cặp bộ duyệt nào sau đây?",
            "options": [
                "`v.rbegin()` và `v.rend()`",
                "`v.begin()` và `v.end()`",
                "`v.front()` và `v.back()`",
                "`v.head()` và `v.tail()`"
            ],
            "answer": "`v.rbegin()` và `v.rend()`",
            "explanation": "Trong C++, Reverse Iterators cho phép duyệt ngược dãy: `v.rbegin()` trỏ tới phần tử cuối cùng (đóng vai trò bắt đầu khi duyệt ngược), và `v.rend()` trỏ tới vị trí trước phần tử đầu tiên."
        },
        {
            "id": "q084",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Khi gọi phương thức `v.clear()` trên một vector đang chứa nhiều dữ liệu, trạng thái của `size()` và `capacity()` sẽ như thế nào?",
            "options": [
                "`size()` trở về 0, nhưng `capacity()` vẫn được giữ nguyên không tự động giải phóng",
                "Cả `size()` và `capacity()` đều lập tức trở về 0",
                "`capacity()` trở về 0, còn `size()` giữ nguyên",
                "Vector bị xóa bỏ hoàn toàn khỏi bộ nhớ và không thể sử dụng lại"
            ],
            "answer": "`size()` trở về 0, nhưng `capacity()` vẫn được giữ nguyên không tự động giải phóng",
            "explanation": "Theo chuẩn C++ STL, `v.clear()` hủy bỏ toàn bộ các phần tử hiện có, đưa `size()` về 0, nhưng vùng đệm bộ nhớ `capacity()` vẫn được giữ nguyên để tái sử dụng hiệu quả cho các lần chèn tiếp theo."
        },
        {
            "id": "q085",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Hiện tượng mất hiệu lực của bộ lặp (Iterator Invalidation) trong `std::vector` xảy ra khi nào?",
            "options": [
                "Khi các thao tác chèn hoặc xóa làm dịch chuyển phần tử, hoặc khi thao tác thêm phần tử kích hoạt tái cấp phát lại bộ nhớ (Reallocation)",
                "Chỉ khi chương trình bị tắt hoặc máy tính hết pin",
                "Chỉ khi ta gán giá trị của vector cho một biến kiểu số nguyên",
                "Khi gọi phương thức `v.size()` quá nhiều lần trong vòng lặp"
            ],
            "answer": "Khi các thao tác chèn hoặc xóa làm dịch chuyển phần tử, hoặc khi thao tác thêm phần tử kích hoạt tái cấp phát lại bộ nhớ (Reallocation)",
            "explanation": "Trong `std::vector`, khi thêm phần tử vượt quá `capacity`, vector sẽ cấp phát vùng nhớ mới, copy dữ liệu sang và hủy vùng nhớ cũ, khiến tất cả iterator trỏ vào vùng nhớ cũ bị vô hiệu hóa (invalidation). Thao tác xóa `erase` cũng làm mất hiệu lực các iterator từ vị trí xóa về sau."
        },
        {
            "id": "q086",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Tại sao các thư viện vector hiện đại áp dụng Chiến lược nhân đôi dung lượng (Doubling Strategy $\\times 2$) thay vì tăng một lượng cố định ($+c$) khi mảng đầy?",
            "options": [
                "Vì chiến lược nhân đôi đảm bảo tổng thời gian copy dữ liệu khi thêm $n$ phần tử là $O(n)$, mang lại chi phí khấu hao $O(1)$ cho mỗi thao tác",
                "Vì bộ nhớ RAM của máy tính chỉ cho phép cấp phát theo lũy thừa của 2",
                "Vì chiến lược tăng cố định $+c$ sẽ gây lỗi biên dịch trong C++",
                "Vì nhân đôi dung lượng giúp vector không bao giờ bị đầy"
            ],
            "answer": "Vì chiến lược nhân đôi đảm bảo tổng thời gian copy dữ liệu khi thêm $n$ phần tử là $O(n)$, mang lại chi phí khấu hao $O(1)$ cho mỗi thao tác",
            "explanation": "Phân tích khấu hao (Amortized Analysis): Nếu tăng $+c$, cần copy $n/c$ lần với tổng chi phí $O(n^2)$, trung bình mỗi lần push tốn $O(n)$. Nếu nhân đôi ($\times 2$), tổng chi phí copy chuỗi hình học là $1 + 2 + 4 + ... + n = 2n - 1 = O(n)$, chi phí khấu hao trung bình mỗi lần push là $O(n)/n = O(1)$."
        },
        {
            "id": "q087",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Phương thức `v.front()` và `v.back()` trong `std::vector` trả về kết quả gì?",
            "options": [
                "Tham chiếu tới phần tử đầu tiên (`v[0]`) và phần tử cuối cùng (`v[v.size() - 1]`)",
                "Địa chỉ con trỏ tới vùng nhớ buffer và dung lượng capacity",
                "Chỉ số nguyên 0 và chỉ số nguyên n-1",
                "Bộ duyệt iterator trỏ tới đầu và cuối vector"
            ],
            "answer": "Tham chiếu tới phần tử đầu tiên (`v[0]`) và phần tử cuối cùng (`v[v.size() - 1]`)",
            "explanation": "`v.front()` trả về tham chiếu trực tiếp đến phần tử đầu tiên `v[0]`, còn `v.back()` trả về tham chiếu đến phần tử cuối cùng `v[v.size() - 1]`. Chúng trả về giá trị/tham chiếu phần tử chứ không phải iterator."
        },
        {
            "id": "q088",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Độ phức tạp thời gian của phương thức `v1.swap(v2)` hoán đổi hai `std::vector` cùng kiểu dữ liệu là bao nhiêu?",
            "options": [
                "$O(1)$ vì chỉ hoán đổi con trỏ buffer nội bộ và các biến quản trị size, capacity",
                "$O(n)$ vì phải duyệt sao chép toàn bộ các phần tử từ vector này sang vector kia",
                "$O(n^2)$ vì phải cấp phát lại bộ nhớ cho cả hai vector",
                "$O(\\log n)$"
            ],
            "answer": "$O(1)$ vì chỉ hoán đổi con trỏ buffer nội bộ và các biến quản trị size, capacity",
            "explanation": "Phương thức `swap` giữa hai vector cùng kiểu đạt độ phức tạp $O(1)$ hằng số vì nó không hề sao chép các phần tử bên trong, mà chỉ đơn giản tráo đổi con trỏ vùng nhớ nội bộ, biến kích thước `size` và dung lượng `capacity` giữa hai đối tượng."
        },
        {
            "id": "q089",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Cho đoạn mã: `vector<int> v = {10, 20, 30}; v.pop_back(); v.push_back(40);`. Giá trị của `v.back()` và `v.size()` lần lượt là bao nhiêu?",
            "options": [
                "40 và 3",
                "30 và 3",
                "40 và 4",
                "20 và 2"
            ],
            "answer": "40 và 3",
            "explanation": "Ban đầu $v = [10, 20, 30]$ (size = 3). Lệnh `v.pop_back()` xóa phần tử cuối 30 $\\implies v = [10, 20]$ (size = 2). Lệnh `v.push_back(40)` thêm 40 vào cuối $\\implies v = [10, 20, 40]$ (size = 3). Vậy `v.back() == 40` và `v.size() == 3`."
        },
        {
            "id": "q090",
            "topicId": 6,
            "topicName": "Vector & Dynamic Arrays",
            "question": "Trong chuẩn C++11 trở lên, phương thức nào sau đây được cung cấp để yêu cầu vector giải phóng lượng bộ nhớ đệm thừa, đưa `capacity()` về sát với `size()` hiện tại?",
            "options": [
                "`v.shrink_to_fit();`",
                "`v.compact();`",
                "`v.truncate();`",
                "`v.free_capacity();`"
            ],
            "answer": "`v.shrink_to_fit();`",
            "explanation": "Trong C++11, `shrink_to_fit()` là phương thức chuẩn của `std::vector` để giải phóng bộ nhớ không sử dụng, giúp giảm `capacity` về bằng với `size` hiện tại của vector."
        },

        # --- Topic 7: Linked List (Singly, Doubly, Circular) (q091 - q105) ---
        {
            "id": "q091",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Trong cấu trúc Danh sách liên kết đơn (Singly Linked List), mỗi nút (Node) bắt buộc phải bao gồm những thành phần cơ bản nào?",
            "options": [
                "Trường dữ liệu chứa phần tử (Element) và một con trỏ trỏ tới nút kế tiếp (`next`)",
                "Trường dữ liệu và hai con trỏ `prev` và `next`",
                "Một mảng tĩnh 100 phần tử và một biến chỉ số `top`",
                "Một mã băm nguyên tố và một con trỏ trỏ về chính nó"
            ],
            "answer": "Trường dữ liệu chứa phần tử (Element) và một con trỏ trỏ tới nút kế tiếp (`next`)",
            "explanation": "Theo Slide 4-5 Lecture 7, một Node trong DSLK đơn bao gồm 2 thành phần chính: phần tử dữ liệu (`Element elem`) và con trỏ liên kết đơn hướng trỏ tới nút tiếp theo (`Node *next`). Nút cuối cùng trỏ tới `NULL`."
        },
        {
            "id": "q092",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Trong Danh sách liên kết kép (Doubly Linked List), mỗi nút (Node) có thêm con trỏ nào so với danh sách liên kết đơn?",
            "options": [
                "Con trỏ `prev` trỏ tới nút đứng ngay trước nó",
                "Con trỏ `child` trỏ tới nút con bên trái",
                "Con trỏ `random` trỏ tới một nút ngẫu nhiên trong bộ nhớ",
                "Con trỏ `parent` trỏ tới nút gốc cây"
            ],
            "answer": "Con trỏ `prev` trỏ tới nút đứng ngay trước nó",
            "explanation": "Theo Slide 15 Lecture 7, mỗi Node trong DSLK kép có hai con trỏ liên kết: `next` trỏ tới nút kế tiếp (successor) và `prev` trỏ tới nút liền trước (predecessor), cho phép duyệt danh sách theo cả hai chiều."
        },
        {
            "id": "q093",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Độ phức tạp thời gian của thao tác chèn một phần tử vào đầu Danh sách liên kết đơn (`push_front`) là bao nhiêu?",
            "options": [
                "$O(1)$",
                "$O(n)$",
                "$O(\\log n)$",
                "$O(n^2)$"
            ],
            "answer": "$O(1)$",
            "explanation": "Chèn vào đầu DSLK đơn chỉ tốn 3 bước: tạo nút mới `q = new Node(e)`, gán `q->next = head`, và cập nhật `head = q`. Toàn bộ thao tác chỉ mất vài phép gán con trỏ hằng số, đạt thời gian tuyệt đối $O(1)$."
        },
        {
            "id": "q094",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Tại sao trong Danh sách liên kết đơn, thao tác xóa phần tử ở cuối danh sách (`pop_back`) luôn mất thời gian $O(n)$ ngay cả khi có con trỏ `tail` trỏ sẵn vào phần tử cuối?",
            "options": [
                "Vì cần duyệt tuần tự từ đầu danh sách để tìm nút nằm ngay trước `tail` nhằm cập nhật con trỏ `next` của nó thành NULL",
                "Vì hệ điều hành cấm gọi lệnh delete trên con trỏ tail",
                "Vì DSLK đơn tự động sắp xếp lại các phần tử mỗi khi xóa",
                "Vì phải giải phóng toàn bộ các nút trong danh sách trước khi xóa nút cuối"
            ],
            "answer": "Vì cần duyệt tuần tự từ đầu danh sách để tìm nút nằm ngay trước `tail` nhằm cập nhật con trỏ `next` của nó thành NULL",
            "explanation": "Trong DSLK đơn, liên kết chỉ có một chiều từ trước ra sau. Để xóa nút cuối `tail`, ta phải cập nhật con trỏ `next` của nút áp chót về `NULL` và gán `tail` mới là nút áp chót. Do không có con trỏ lùi, ta bắt buộc phải duyệt từ `head` mất $O(n)$ bước để tìm nút áp chót."
        },
        {
            "id": "q095",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Vai trò cốt lõi của các Nút canh gác (Sentinel Nodes: `header` và `trailer`) trong Danh sách liên kết kép là gì?",
            "options": [
                "Triệt tiêu các trường hợp biên đặc biệt khi danh sách rỗng hoặc thao tác ở hai đầu, giúp giải thuật thêm/xóa đồng nhất không cần kiểm tra `NULL`",
                "Lưu trữ dữ liệu mã hóa mật khẩu của danh sách",
                "Đóng vai trò là bộ nhớ cache tăng tốc độ truy xuất",
                "Tự động giải phóng danh sách khi bộ nhớ RAM đạt ngưỡng 90%"
            ],
            "answer": "Triệt tiêu các trường hợp biên đặc biệt khi danh sách rỗng hoặc thao tác ở hai đầu, giúp giải thuật thêm/xóa đồng nhất không cần kiểm tra `NULL`",
            "explanation": "Theo Slide 16-17 Lecture 7, các nút canh gác (`header` và `trailer`) là các nút giả không chứa dữ liệu thực tế, đứng ở hai đầu danh sách. Mọi nút dữ liệu thực đều nằm giữa `header` và `trailer`. Nhờ đó, việc chèn hay xóa bất kỳ vị trí nào đều áp dụng cùng một công thức cập nhật 4 con trỏ mà không lo lỗi con trỏ `NULL`."
        },
        {
            "id": "q096",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Trong DSLK kép có nút canh gác, thứ tự các bước để chèn nút mới `q` vào ngay sau nút `p` (`insertAfter(p, q)`) sao cho không làm đứt gãy liên kết là gì?",
            "options": [
                "`q->setNext(p->getNext()); p->getNext()->setPrev(q); q->setPrev(p); p->setNext(q);`",
                "`p->setNext(q); q->setPrev(p); q->setNext(p->getNext()); p->getNext()->setPrev(q);`",
                "`delete p; q->setNext(p); p->setPrev(q);`",
                "`q = p; p->setNext(q->getNext());`"
            ],
            "answer": "`q->setNext(p->getNext()); p->getNext()->setPrev(q); q->setPrev(p); p->setNext(q);`",
            "explanation": "Theo Slide 18 Lecture 7: Đầu tiên nối hai liên kết của nút mới `q` với nút sau của `p`: `q->next = p->next` và `p->next->prev = q`. Sau đó mới gắn liên kết giữa `p` và `q`: `q->prev = p` và `p->next = q`. Nếu gán `p->next = q` trước sẽ làm mất con trỏ tới nút sau của `p`."
        },
        {
            "id": "q097",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Độ phức tạp thời gian của thao tác xóa một nút `p` khi đã có sẵn con trỏ trỏ tới `p` trong Danh sách liên kết kép (`remove(p)`) là bao nhiêu?",
            "options": [
                "$O(1)$",
                "$O(n)$",
                "$O(\\log n)$",
                "$O(n^2)$"
            ],
            "answer": "$O(1)$",
            "explanation": "Trong DSLK kép, mỗi nút biết cả nút trước `p->prev` và nút sau `p->next`. Để xóa `p`, chỉ cần: `p->prev->next = p->next; p->next->prev = p->prev; delete p;`. Toàn bộ thao tác chỉ gồm vài phép gán con trỏ hằng số, đạt thời gian $O(1)$ mà không cần duyệt danh sách."
        },
        {
            "id": "q098",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Đặc điểm cấu trúc nhận diện của Danh sách liên kết vòng (Circular Linked List) là gì?",
            "options": [
                "Con trỏ `next` của nút cuối cùng trỏ ngược lại nút đầu tiên của danh sách thay vì trỏ tới `NULL`",
                "Mỗi nút trong danh sách đều có đúng 3 con trỏ liên kết",
                "Danh sách không cho phép chứa các phần tử có giá trị trùng lặp",
                "Dữ liệu trong các nút bắt buộc phải được sắp xếp theo hình tròn số học"
            ],
            "answer": "Con trỏ `next` của nút cuối cùng trỏ ngược lại nút đầu tiên của danh sách thay vì trỏ tới `NULL`",
            "explanation": "Trong Danh sách liên kết vòng (Circular Linked List), nút cuối cùng không trỏ tới `NULL` mà trỏ quay trở lại nút đầu tiên (nút `head`), tạo thành một vòng khép kín liên tục không có điểm kết thúc."
        },
        {
            "id": "q099",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Ứng dụng thực tế kinh điển của Danh sách liên kết vòng trong hệ điều hành là gì?",
            "options": [
                "Thuật toán lập lịch phân phối thời gian CPU xoay vòng (Round-Robin CPU Scheduling)",
                "Thuật toán tìm kiếm nhị phân trên bộ nhớ phụ",
                "Lưu trữ bảng phân bổ file FAT32",
                "Mã hóa khóa công khai RSA"
            ],
            "answer": "Thuật toán lập lịch phân phối thời gian CPU xoay vòng (Round-Robin CPU Scheduling)",
            "explanation": "DSLK vòng là cấu trúc dữ liệu lý tưởng cho thuật toán điều phối CPU Round-Robin: các tiến trình được xếp vào một vòng tròn, CPU cấp một lượng thời gian quantum cho tiến trình hiện tại rồi tự động chuyển sang tiến trình kế tiếp theo vòng tròn."
        },
        {
            "id": "q100",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Về mặt chi phí bộ nhớ phụ trội (Memory Overhead), cấu trúc Danh sách liên kết có đặc điểm gì so với Mảng tĩnh?",
            "options": [
                "Danh sách liên kết tốn thêm bộ nhớ cho các biến con trỏ liên kết (`next`, `prev`) tại mỗi nút dữ liệu",
                "Danh sách liên kết tiết kiệm bộ nhớ hơn mảng 100% trong mọi tình huống",
                "Danh sách liên kết không tốn thêm bất kỳ byte bộ nhớ phụ nào",
                "Mảng tốn nhiều bộ nhớ con trỏ hơn danh sách liên kết"
            ],
            "answer": "Danh sách liên kết tốn thêm bộ nhớ cho các biến con trỏ liên kết (`next`, `prev`) tại mỗi nút dữ liệu",
            "explanation": "Theo bảng so sánh Slide 28 Lecture 7: Trong mảng/vector, các phần tử nằm liền kề chỉ chứa dữ liệu thuần. Trong DSLK, mỗi nút bắt buộc phải tốn thêm bộ nhớ cho con trỏ (4 hoặc 8 bytes trên máy 64-bit cho mỗi con trỏ `next` và `prev`), tạo ra chi phí phụ trội bộ nhớ (overhead)."
        },
        {
            "id": "q101",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Tại sao việc duyệt tuần tự các phần tử trên Mảng (Array/Vector) thường chạy nhanh hơn đáng kể so với duyệt trên Danh sách liên kết trên các máy tính hiện đại?",
            "options": [
                "Mảng có tính định vị bộ nhớ đệm (Cache Locality) vượt trội do các phần tử nằm liên tục trong RAM, giảm thiểu hiện tượng Cache Miss",
                "Vì ngôn ngữ C++ tự động bỏ qua các phần tử trong danh sách liên kết",
                "Vì con trỏ trong danh sách liên kết luôn có tốc độ truyền tải 1 byte/giây",
                "Vì vi xử lý CPU không hỗ trợ câu lệnh giải tham chiếu con trỏ"
            ],
            "answer": "Mảng có tính định vị bộ nhớ đệm (Cache Locality) vượt trội do các phần tử nằm liên tục trong RAM, giảm thiểu hiện tượng Cache Miss",
            "explanation": "Mảng lưu trữ trên một dải ô nhớ liên tục (contiguous memory), khi CPU nạp dữ liệu vào Cache Line sẽ nạp luôn các phần tử liền kề kế tiếp (Spatial Locality). Trong khi DSLK cấp phát các nút rải rác trên Heap, việc nhảy con trỏ liên tục gây Cache Miss thường xuyên, làm chậm tốc độ thực thi."
        },
        {
            "id": "q102",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Thao tác truy xuất phần tử tại chỉ số ngẫu nhiên `i` trên Danh sách liên kết có độ phức tạp thời gian là bao nhiêu?",
            "options": [
                "$O(n)$ vì bắt buộc phải duyệt tuần tự qua $i$ nút từ đầu danh sách",
                "$O(1)$ nhờ cơ chế con trỏ nhảy cóc trực tiếp",
                "$O(\\log n)$ bằng thuật toán tìm kiếm nhị phân",
                "$O(n^2)$"
            ],
            "answer": "$O(n)$ vì bắt buộc phải duyệt tuần tự qua $i$ nút từ đầu danh sách",
            "explanation": "Danh sách liên kết không hỗ trợ truy cập ngẫu nhiên (No Random Access). Để truy xuất phần tử thứ $i$, chương trình bắt buộc phải lần theo con trỏ `next` từ nút đầu qua từng nút một, tốn $O(n)$ bước."
        },
        {
            "id": "q103",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Container `std::list` trong thư viện chuẩn C++ STL được cài đặt dựa trên cấu trúc dữ liệu nền tảng nào?",
            "options": [
                "Danh sách liên kết kép (Doubly Linked List)",
                "Mảng động tự co giãn kích thước (Dynamic Array)",
                "Danh sách liên kết đơn không có nút canh gác",
                "Cây tìm kiếm nhị phân tự cân bằng AVL"
            ],
            "answer": "Danh sách liên kết kép (Doubly Linked List)",
            "explanation": "Trong C++ STL, `std::list` được cài đặt chuẩn mực dưới dạng Danh sách liên kết kép (Doubly Linked List), cung cấp các thao tác chèn/xóa hai đầu và chèn/xóa tại vị trí iterator trong thời gian $O(1)$."
        },
        {
            "id": "q104",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Tại sao lập trình viên KHÔNG THỂ sử dụng toán tử truy xuất chỉ số `mylist[k]` trên đối tượng `std::list<int> mylist` trong C++?",
            "options": [
                "Vì `std::list` chỉ cung cấp bộ duyệt hai chiều (Bidirectional Iterator), không hỗ trợ toán tử ngẫu nhiên truy cập $O(1)$",
                "Vì thư viện STL cấm sử dụng số nguyên làm chỉ số danh sách",
                "Vì `std::list` chỉ cho phép truy xuất qua giao thức mạng",
                "Vì `std::list` luôn tự động xóa phần tử sau khi đọc"
            ],
            "answer": "Vì `std::list` chỉ cung cấp bộ duyệt hai chiều (Bidirectional Iterator), không hỗ trợ toán tử ngẫu nhiên truy cập $O(1)$",
            "explanation": "Nguyên tắc thiết kế của C++ STL là không cung cấp `operator[]` cho các cấu trúc không hỗ trợ truy cập ngẫu nhiên $O(1)$. Do `std::list` là DSLK kép mất $O(n)$ để truy cập vị trí $k$, nên STL không hỗ trợ `operator[]` để tránh việc lập trình viên vô tình viết vòng lặp $O(n^2)$."
        },
        {
            "id": "q105",
            "topicId": 7,
            "topicName": "Linked List",
            "question": "Trong hàm hủy (Destructor) của một lớp Danh sách liên kết tự cài đặt trong C++, thao tác nào bắt buộc phải thực hiện để tránh rò rỉ bộ nhớ (Memory Leak)?",
            "options": [
                "Duyệt qua toàn bộ danh sách và gọi lệnh `delete` giải phóng lần lượt từng nút một",
                "Chỉ cần gán con trỏ `head = NULL;`",
                "Gọi lệnh `delete head;` một lần duy nhất mà không cần vòng lặp",
                "Chỉ cần gọi lệnh `free(this);`"
            ],
            "answer": "Duyệt qua toàn bộ danh sách và gọi lệnh `delete` giải phóng lần lượt từng nút một",
            "explanation": "Mỗi nút trong DSLK là một vùng nhớ độc lập được cấp phát riêng rẽ bằng `new`. Nếu chỉ gán `head = NULL` hoặc chỉ `delete head`, tất cả các nút còn lại sẽ bị cô lập trên Heap và gây rò rỉ bộ nhớ nghiêm trọng. Hàm hủy bắt buộc phải có vòng lặp duyệt xóa từng nút."
        },

        # --- Topic 8: Stack (q106 - q120) ---
        {
            "id": "q106",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Kiểu dữ liệu trừu tượng Ngăn xếp (Stack ADT) hoạt động nghiêm ngặt theo nguyên lý truy cập dữ liệu nào sau đây?",
            "options": [
                "LIFO (Last In, First Out) - Vào sau ra trước",
                "FIFO (First In, First Out) - Vào trước ra trước",
                "LILO (Last In, Last Out) - Vào sau ra sau",
                "Random Access - Truy xuất ngẫu nhiên bất kỳ vị trí nào"
            ],
            "answer": "LIFO (Last In, First Out) - Vào sau ra trước",
            "explanation": "Theo Slide 4-5 Lecture 8, Stack là cấu trúc dữ liệu tuyến tính tuân thủ nghiêm ngặt nguyên lý LIFO (Last In, First Out): phần tử được thêm vào cuối cùng sẽ là phần tử đầu tiên được lấy ra khỏi ngăn xếp."
        },
        {
            "id": "q107",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Hai thao tác cơ bản nhất của Ngăn xếp: bổ sung một phần tử vào đỉnh và loại bỏ một phần tử khỏi đỉnh lần lượt có tên chuẩn là gì?",
            "options": [
                "`push` và `pop`",
                "`enqueue` và `dequeue`",
                "`insert` và `remove`",
                "`append` và `delete`"
            ],
            "answer": "`push` và `pop`",
            "explanation": "Theo quy ước chuẩn của Stack ADT (Slide 5-6 Lecture 8): `push(o)` là thao tác đẩy một phần tử mới vào đỉnh ngăn xếp, và `pop()` là thao tác loại bỏ phần tử ở đỉnh ngăn xếp."
        },
        {
            "id": "q108",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Hiện tượng Ngoại lệ `Stack Underflow` (Ngăn xếp rỗng) xảy ra trong tình huống nào sau đây?",
            "options": [
                "Khi chương trình cố gắng thực hiện thao tác `pop()` hoặc `top()` trên một ngăn xếp đang không có phần tử nào (rỗng)",
                "Khi thực hiện `push()` vào một ngăn xếp đã đầy dung lượng bộ nhớ",
                "Khi số lượng phần tử trong ngăn xếp vượt quá giới hạn kiểu số nguyên int",
                "Khi khai báo ngăn xếp mà không khởi tạo giá trị ban đầu"
            ],
            "answer": "Khi chương trình cố gắng thực hiện thao tác `pop()` hoặc `top()` trên một ngăn xếp đang không có phần tử nào (rỗng)",
            "explanation": "Theo Slide 7 Lecture 8: `StackEmptyException` (hay Underflow) xảy ra khi gọi `pop()` hoặc `top()` trên một stack rỗng. Ngược lại, `StackFullException` (Overflow) xảy ra khi gọi `push()` vào stack mảng cố định đã đầy."
        },
        {
            "id": "q109",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Khi cài đặt Stack bằng mảng một chiều tĩnh kích thước $N$ với biến chỉ số đỉnh `t` (khởi tạo ban đầu `t = -1`), thao tác `push(o)` được cài đặt bằng dòng lệnh nào?",
            "options": [
                "`S[++t] = o;`",
                "`S[t++] = o;`",
                "`S[--t] = o;`",
                "`S[t] = o; t--;`"
            ],
            "answer": "`S[++t] = o;`",
            "explanation": "Theo Slide 14 Lecture 8: Khởi tạo stack rỗng có `t = -1`. Khi thêm phần tử, ta cần tăng chỉ số đỉnh lên trước rồi mới gán dữ liệu vào ô nhớ mới đó: `S[++t] = o;` (tiền tố `++`)."
        },
        {
            "id": "q110",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Khi cài đặt Stack bằng mảng động, nếu áp dụng Chiến lược tăng kích thước cố định ($+c$ ô nhớ) mỗi khi mảng bị đầy, tổng thời gian copy dữ liệu khi thực hiện chuỗi $n$ thao tác push là bao nhiêu?",
            "options": [
                "$O(n^2)$, dẫn đến chi phí trung bình cho mỗi thao tác push là $O(n)$",
                "$O(n)$, dẫn đến chi phí trung bình là $O(1)$",
                "$O(n \\log n)$, dẫn đến chi phí trung bình là $O(\\log n)$",
                "$O(1)$ trong mọi trường hợp"
            ],
            "answer": "$O(n^2)$, dẫn đến chi phí trung bình cho mỗi thao tác push là $O(n)$",
            "explanation": "Theo Slide 27-28 Lecture 8: Nếu tăng thêm $c$ ô nhớ mỗi lần đầy, sau $k = n/c$ lần cấp phát lại, tổng chi phí copy là chuỗi số học $c(1 + 2 + ... + k) = c \\frac{k(k+1)}{2} = O(k^2) = O(n^2)$. Do đó chi phí trung bình mỗi lần push là $O(n^2)/n = O(n)$ (kém hiệu quả)."
        },
        {
            "id": "q111",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Khi cài đặt Stack bằng mảng động, Chiến lược nhân đôi kích thước ($\\times 2$) mang lại chi phí khấu hao (Amortized Time) cho mỗi thao tác `push` là bao nhiêu?",
            "options": [
                "$O(1)$",
                "$O(n)$",
                "$O(\\log n)$",
                "$O(n^2)$"
            ],
            "answer": "$O(1)$",
            "explanation": "Theo Slide 29-30 Lecture 8: Khi nhân đôi dung lượng mỗi lần đầy mảng, tổng chi phí copy chuỗi hình học là $1 + 2 + 4 + ... + 2^k \\approx 2n = O(n)$. Chia đều cho $n$ thao tác push, thời gian trung bình khấu hao (Amortized Time) cho mỗi phép push là $O(n)/n = O(1)$."
        },
        {
            "id": "q112",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Khi cài đặt Stack bằng Danh sách liên kết đơn, vị trí nào của danh sách nên được chọn làm Đỉnh ngăn xếp (Top) để đảm bảo thời gian $O(1)$ cho cả hai thao tác `push` và `pop`?",
            "options": [
                "Đầu danh sách (Head)",
                "Cuối danh sách (Tail)",
                "Chính giữa danh sách",
                "Vị trí ngẫu nhiên"
            ],
            "answer": "Đầu danh sách (Head)",
            "explanation": "Trong DSLK đơn, các thao tác ở đầu danh sách (`push_front` và `pop_front`) đều tốn $O(1)$. Nếu chọn cuối danh sách làm Top, thao tác `pop` sẽ tốn $O(n)$ do phải tìm nút liền trước. Do đó đỉnh ngăn xếp Top luôn gắn với đầu danh sách (Head)."
        },
        {
            "id": "q113",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Khung ngăn xếp (Stack Frame / Activation Record) trên Call Stack của chương trình C++ được tạo ra và giải phóng vào những thời điểm nào?",
            "options": [
                "Được đẩy vào (push) khi gọi hàm và được lấy ra giải phóng (pop) khi hàm kết thúc thực thi (return)",
                "Được tạo ra khi bật máy tính và giải phóng khi tắt máy tính",
                "Được tạo ra khi lưu file mã nguồn và giải phóng khi biên dịch",
                "Được tạo ra ngẫu nhiên bởi trình điều khiển card mạng"
            ],
            "answer": "Được đẩy vào (push) khi gọi hàm và được lấy ra giải phóng (pop) khi hàm kết thúc thực thi (return)",
            "explanation": "Theo Slide 8-9 Lecture 8: Quá trình thực thi hàm trong C++ hoạt động theo cơ chế Call Stack: khi một hàm được gọi, hệ thống đẩy một Frame chứa biến cục bộ và địa chỉ trở về vào đỉnh Stack; khi hàm gặp lệnh return, Frame đó được pop ra và CPU quay lại hàm gọi."
        },
        {
            "id": "q114",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Trong thuật toán kiểm tra tính hợp lệ của các dấu ngoặc (Balanced Parentheses), khi duyệt gặp một ký tự mở ngoặc `(`, thuật toán sẽ xử lý như thế nào?",
            "options": [
                "Đẩy (push) ký tự mở ngoặc đó vào đỉnh ngăn xếp",
                "Lấy một phần tử ra khỏi ngăn xếp bằng thao tác pop",
                "Dừng chương trình và thông báo biểu thức không hợp lệ ngay lập tức",
                "Xóa sạch toàn bộ ngăn xếp"
            ],
            "answer": "Đẩy (push) ký tự mở ngoặc đó vào đỉnh ngăn xếp",
            "explanation": "Theo Slide 34 Lecture 8: Khi duyệt chuỗi biểu thức, gặp bất kỳ dấu mở ngoặc nào `(`, `[`, `{` ta đều đẩy nó vào Stack. Khi gặp dấu đóng ngoặc tương ứng, ta lấy dấu mở ngoặc ở đỉnh Stack ra kiểm tra xem có khớp cặp hay không."
        },
        {
            "id": "q115",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Ưu điểm vượt trội nhất của biểu thức toán học biểu diễn dưới dạng Ký pháp Hậu tố (Postfix / Reverse Polish Notation) so với Trung tố (Infix) là gì?",
            "options": [
                "Hoàn toàn không cần sử dụng dấu ngoặc và thứ tự thực hiện các phép toán hoàn toàn đơn trị từ trái qua phải",
                "Dung lượng chuỗi ký tự luôn ngắn hơn một nửa so với trung tố",
                "Có thể tính toán trực tiếp mà không cần dùng đến vi xử lý",
                "Chỉ thực hiện được các phép cộng và trừ"
            ],
            "answer": "Hoàn toàn không cần sử dụng dấu ngoặc và thứ tự thực hiện các phép toán hoàn toàn đơn trị từ trái qua phải",
            "explanation": "Theo Slide 22-25 Lecture 8: Trong ký pháp Hậu tố (Postfix), toán tử đứng ngay sau các toán hạng của nó. Do đó cấu trúc này không cần đến dấu ngoặc hay quy tắc ưu tiên toán tử phức tạp, máy tính có thể đánh giá kết quả dễ dàng bằng một Stack duy nhất."
        },
        {
            "id": "q116",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Biểu thức Trung tố (Infix) sau: `(A + B) * C` khi chuyển đổi sang dạng Ký pháp Hậu tố (Postfix) sẽ có kết quả là gì?",
            "options": [
                "`A B + C *`",
                "`A B C + *`",
                "`* + A B C`",
                "`A B + * C`"
            ],
            "answer": "`A B + C *`",
            "explanation": "Trong biểu thức `(A + B) * C`, phép cộng `A + B` nằm trong ngoặc nên được thực hiện trước $\\implies `A B +`$. Kết quả này sau đó được nhân với $C \\implies `A B + C *`$."
        },
        {
            "id": "q117",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Trong thuật toán tính giá trị biểu thức Hậu tố (Postfix Evaluation) sử dụng Stack, khi gặp một toán tử hai ngôi số học (ví dụ dấu trừ `-`), thứ tự lấy các toán hạng ra khỏi Stack như thế nào?",
            "options": [
                "Toán hạng lấy ra đầu tiên là toán hạng bên phải ($op2$), toán hạng lấy ra thứ hai là toán hạng bên trái ($op1$), sau đó tính $op1 - op2$",
                "Toán hạng lấy ra đầu tiên là toán hạng bên trái ($op1$), toán hạng lấy ra thứ hai là toán hạng bên phải ($op2$), sau đó tính $op1 - op2$",
                "Lấy ra một toán hạng duy nhất rồi trừ cho 0",
                "Lấy ra 3 toán hạng cùng một lúc và cộng dồn lại"
            ],
            "answer": "Toán hạng lấy ra đầu tiên là toán hạng bên phải ($op2$), toán hạng lấy ra thứ hai là toán hạng bên trái ($op1$), sau đó tính $op1 - op2$",
            "explanation": "Do cơ chế LIFO của Stack, phần tử được push vào sau cùng nằm ở đỉnh stack chính là toán hạng bên phải ($op2$). Khi pop phần tử đầu tiên ta nhận được $op2$, pop phần tử tiếp theo nhận được $op1$. Phép toán được thực hiện là $op1 \\text{ operator } op2$ (đặc biệt quan trọng với phép trừ và phép chia)."
        },
        {
            "id": "q118",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Trong bài toán Computing Spans (Stock Span Problem) ở Slide 18-21 Lecture 8, giải thuật tối ưu sử dụng Stack đơn điệu (Monotonic Stack) đạt độ phức tạp thời gian là bao nhiêu so với cách vét cạn 2 vòng lặp $O(n^2)$?",
            "options": [
                "$O(n)$ tuyến tính",
                "$O(n \\log n)$",
                "$O(\\log n)$",
                "$O(n^3)$"
            ],
            "answer": "$O(n)$ tuyến tính",
            "explanation": "Thuật toán tối ưu dùng Stack lưu trữ chỉ số các phần tử. Mỗi phần tử trong mảng được push vào stack đúng 1 lần và bị pop ra tối đa 1 lần trong toàn bộ tiến trình. Tổng số thao tác trên stack tối đa là $2n$, do đó thuật toán đạt độ phức tạp thời gian tuyến tính $O(n)$."
        },
        {
            "id": "q119",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Khi sử dụng Stack để chuyển đổi một số nguyên dương hệ thập phân sang hệ nhị phân, thuật toán liên tục chia số đó cho 2 và đẩy phần dư vào Stack. Kết quả chuỗi nhị phân thu được bằng cách nào?",
            "options": [
                "Lấy lần lượt các phần dư ra khỏi Stack từ đỉnh về đáy cho tới khi Stack rỗng",
                "Đọc các phần tử từ đáy Stack lên đỉnh Stack",
                "Nhân các phần tử trong Stack với số 2 rồi cộng lại",
                "Chỉ cần lấy phần tử ở đáy Stack là đủ"
            ],
            "answer": "Lấy lần lượt các phần dư ra khỏi Stack từ đỉnh về đáy cho tới khi Stack rỗng",
            "explanation": "Trong phép đổi cơ số, chữ số dư đầu tiên tính được là bit trọng số thấp nhất (LSB) nằm ở bên phải cùng, còn số dư cuối cùng là bit trọng số cao nhất (MSB). Bằng cách đẩy vào Stack và sau đó pop ra lần lượt, thứ tự các bit được đảo ngược lại một cách tự nhiên và chính xác."
        },
        {
            "id": "q120",
            "topicId": 8,
            "topicName": "Stack",
            "question": "Trong thư viện chuẩn C++ STL `std::stack`, phương thức nào được sử dụng để đọc giá trị phần tử ở đỉnh ngăn xếp mà không loại bỏ phần tử đó khỏi ngăn xếp?",
            "options": [
                "`top()`",
                "`pop()`",
                "`peek_back()`",
                "`front()`"
            ],
            "answer": "`top()`",
            "explanation": "Trong C++ STL `std::stack`: hàm `pop()` chỉ loại bỏ phần tử ở đỉnh và có kiểu trả về `void` (không trả về giá trị). Để xem giá trị phần tử đỉnh ngăn xếp, ta phải gọi phương thức `top()`."
        },

        # --- Topic 9: Queue (q121 - q135) ---
        {
            "id": "q121",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Kiểu dữ liệu trừu tượng Hàng đợi (Queue ADT) hoạt động nghiêm ngặt theo nguyên lý truy cập dữ liệu nào sau đây?",
            "options": [
                "FIFO (First In, First Out) - Vào trước ra trước",
                "LIFO (Last In, First Out) - Vào sau ra trước",
                "FILO (First In, Last Out) - Vào trước ra sau",
                "LILO (Last In, Lowest Out) - Ưu tiên phần tử giá trị nhỏ nhất"
            ],
            "answer": "FIFO (First In, First Out) - Vào trước ra trước",
            "explanation": "Theo Slide 3-4 Lecture 9, Hàng đợi (Queue) là cấu trúc dữ liệu tuyến tính hoạt động theo nguyên lý FIFO (First In, First Out): phần tử nào được thêm vào trước sẽ là phần tử đầu tiên được lấy ra, tương tự dòng người xếp hàng mua vé."
        },
        {
            "id": "q122",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Trong Hàng đợi chuẩn (Standard Queue), thao tác bổ sung phần tử mới và thao tác lấy phần tử ra được thực hiện ở những vị trí nào?",
            "options": [
                "Bổ sung ở Cuối hàng (Rear / Back) và lấy ra ở Đầu hàng (Front)",
                "Bổ sung ở Đầu hàng (Front) và lấy ra ở Cuối hàng (Rear)",
                "Cả thêm và lấy ra đều thực hiện ở cùng một vị trí Đỉnh (Top)",
                "Bổ sung và lấy ra ở vị trí chính giữa hàng đợi"
            ],
            "answer": "Bổ sung ở Cuối hàng (Rear / Back) và lấy ra ở Đầu hàng (Front)",
            "explanation": "Theo Slide 4 Lecture 9, Queue có hai đầu tách biệt: phần tử mới luôn được thêm vào ở cuối hàng (Rear/Back - Enqueue/Push), và phần tử bị loại bỏ luôn ở đầu hàng (Front - Dequeue/Pop)."
        },
        {
            "id": "q123",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Hiện tượng \"Trôi mảng / Đầy giả tạo\" (Array Drifting / False Overflow) khi cài đặt Hàng đợi bằng mảng tuyến tính thông thường là hiện tượng gì?",
            "options": [
                "Chỉ số cuối hàng chạm giới hạn mảng nhưng các ô nhớ phía trước đã bị bỏ trống do các thao tác lấy ra, khiến mảng báo đầy dù dung lượng thực tế vẫn còn dư",
                "Mảng bị tràn bộ nhớ do chứa quá nhiều số âm",
                "Các phần tử trong mảng tự động dịch chuyển ngẫu nhiên khi không có thao tác",
                "Hệ điều hành tự động xóa các ô nhớ sau 10 giây không truy cập"
            ],
            "answer": "Chỉ số cuối hàng chạm giới hạn mảng nhưng các ô nhớ phía trước đã bị bỏ trống do các thao tác lấy ra, khiến mảng báo đầy dù dung lượng thực tế vẫn còn dư",
            "explanation": "Nếu dùng mảng tuyến tính với 2 con trỏ `front` và `rear` tăng dần, sau một loạt thao tác enqueue và dequeue, cả hai con trỏ đều dịch dần về cuối mảng. Dù các ô ở đầu mảng đã trống nhưng con trỏ `rear` chạm $N-1$ khiến hàng đợi báo đầy giả (False Overflow)."
        },
        {
            "id": "q124",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Cơ chế Mảng vòng (Circular Array) giải quyết hiện tượng trôi mảng trong Hàng đợi bằng cách áp dụng toán tử toán học nào?",
            "options": [
                "Toán tử chia lấy phần dư (Modulo `% N`)",
                "Toán tử căn bậc hai",
                "Toán tử nhân đôi bitwise shift left",
                "Toán tử logarit cơ số e"
            ],
            "answer": "Toán tử chia lấy phần dư (Modulo `% N`)",
            "explanation": "Theo Slide 6, 8 Lecture 9: Mảng vòng sử dụng phép toán Modulo `% N` để nối vòng ô cuối cùng $N-1$ quay trở lại ô đầu tiên chỉ số $0$, cho phép tái sử dụng các ô nhớ trống ở đầu mảng mà không cần dịch chuyển dữ liệu."
        },
        {
            "id": "q125",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Trong Hàng đợi mảng vòng kích thước $N$ với chỉ số đầu $F$, chỉ số ô kế tiếp nhận phần tử mới $L$, công thức cập nhật chỉ số $L$ khi thêm phần tử (`push`) là gì?",
            "options": [
                "`L = (L + 1) % N;`",
                "`L = L + 1;`",
                "`L = (L - 1) % N;`",
                "`L = (F + L) / 2;`"
            ],
            "answer": "`L = (L + 1) % N;`",
            "explanation": "Theo Slide 8 Lecture 9: Khi thêm một phần tử vào vị trí $L$, phần tử mới chiếm ô $Q[L]$, sau đó con trỏ $L$ dịch chuyển sang ô kế tiếp theo quy tắc vòng tròn: `L = (L + 1) % N;`."
        },
        {
            "id": "q126",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Trong Queue mảng vòng kích thước $N$, nếu chỉ số ô tiếp theo nhận phần tử mới là $L$, công thức tính chỉ số của phần tử cuối cùng hiện tại trong hàng đợi (`back()`) là gì?",
            "options": [
                "`(L - 1 + N) % N`",
                "`L - 1`",
                "`(L + 1) % N`",
                "`F % N`"
            ],
            "answer": "`(L - 1 + N) % N`",
            "explanation": "Do $L$ luôn trỏ tới ô trống kế tiếp sau phần tử cuối, nên phần tử cuối cùng nằm ở ô liền trước $L$, tức là $L - 1$. Để tránh giá trị âm khi $L = 0$, ta cộng thêm chu kỳ $N$ trước khi modulo: `(L - 1 + N) % N`."
        },
        {
            "id": "q127",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Khi cài đặt Queue bằng mảng vòng có sử dụng biến đếm số lượng phần tử hiện tại $num$, điều kiện để kiểm tra Hàng đợi rỗng và Hàng đợi đầy lần lượt là gì?",
            "options": [
                "Rỗng khi `num == 0`; Đầy khi `num == N`",
                "Rỗng khi `F == L`; Đầy khi `F == 0`",
                "Rỗng khi `num == N`; Đầy khi `num == 0`",
                "Rỗng khi `F == -1`; Đầy khi `L == -1`"
            ],
            "answer": "Rỗng khi `num == 0`; Đầy khi `num == N`",
            "explanation": "Theo Slide 8-10 Lecture 9: Sử dụng biến đếm $num$ ($0 \\le num \\le N$) là giải pháp hoàn hảo để phân biệt rõ ràng giữa trạng thái rỗng (`num == 0`) và trạng thái đầy (`num == N`), tránh được sự nhập nhằng của điều kiện $F == L$."
        },
        {
            "id": "q128",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Độ phức tạp thời gian của các thao tác `enqueue` (thêm vào) và `dequeue` (lấy ra) trên Hàng đợi mảng vòng tròn (Circular Queue) là bao nhiêu?",
            "options": [
                "$O(1)$ cho cả hai thao tác",
                "$O(n)$ cho thao tác lấy ra do phải dịch chuyển các phần tử",
                "$O(\\log n)$",
                "$O(n)$ cho thao tác thêm vào"
            ],
            "answer": "$O(1)$ cho cả hai thao tác",
            "explanation": "Nhờ cơ chế vòng tròn bằng phép toán modulo `% N`, việc thêm vào cuối và lấy ra ở đầu chỉ bao gồm việc tăng chỉ số con trỏ $L$ hoặc $F$ và tăng/giảm biến đếm $num$. Hoàn toàn không có thao tác dồn dịch mảng, do đó thời gian đạt hằng số $O(1)$ tuyệt đối."
        },
        {
            "id": "q129",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Khi cài đặt Queue bằng Danh sách liên kết đơn có hai con trỏ `head` và `tail`, cách thiết lập vị trí `Front` và `Rear` nào sau đây giúp cả hai thao tác thêm và lấy ra đều đạt $O(1)$?",
            "options": [
                "Đặt `Front` ở `head` (lấy ra ở đầu) và `Rear` ở `tail` (thêm vào ở cuối)",
                "Đặt `Front` ở `tail` (lấy ra ở cuối) và `Rear` ở `head` (thêm vào ở đầu)",
                "Đặt cả `Front` và `Rear` cùng ở vị trí `head`",
                "Đặt cả `Front` và `Rear` cùng ở vị trí `tail`"
            ],
            "answer": "Đặt `Front` ở `head` (lấy ra ở đầu) và `Rear` ở `tail` (thêm vào ở cuối)",
            "explanation": "Trong DSLK đơn: thêm vào cuối `push_back` (qua `tail->next`) tốn $O(1)$, và xóa ở đầu `pop_front` (qua `head = head->next`) tốn $O(1)$. Do đó chọn `Front = head` và `Rear = tail` sẽ đảm bảo mọi thao tác của Queue đều đạt $O(1)$."
        },
        {
            "id": "q130",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Nếu cài đặt Queue bằng DSLK đơn nhưng đảo ngược lại: đặt `Front` ở `tail` và `Rear` ở `head`, thì thao tác nào sẽ bị suy giảm hiệu năng nghiêm trọng thành $O(n)$?",
            "options": [
                "Thao tác lấy phần tử ra (`dequeue`)",
                "Thao tác thêm phần tử vào (`enqueue`)",
                "Thao tác kiểm tra rỗng (`isEmpty`)",
                "Thao tác lấy kích thước (`size`)"
            ],
            "answer": "Thao tác lấy phần tử ra (`dequeue`)",
            "explanation": "Nếu `Front` ở `tail`, khi lấy phần tử ra khỏi hàng đợi (`dequeue`), ta phải xóa nút ở cuối DSLK đơn (`pop_back`). Thao tác này bắt buộc phải duyệt tuần tự từ đầu để tìm nút áp chót nhằm cập nhật liên kết, khiến chi phí bị đội lên $O(n)$."
        },
        {
            "id": "q131",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Ứng dụng thực tế nào sau đây trong Hệ điều hành sử dụng trực tiếp cấu trúc Hàng đợi (Queue)?",
            "options": [
                "Hàng đợi điều phối tiến trình CPU (CPU Scheduling) và Hàng đợi đệm in ấn (Printer Spooler)",
                "Trình soạn thảo văn bản hỗ trợ chức năng Undo/Redo",
                "Bộ nhớ Call Stack quản lý các hàm đệ quy",
                "Thuật toán tìm kiếm sâu (DFS) trên đồ thị"
            ],
            "answer": "Hàng đợi điều phối tiến trình CPU (CPU Scheduling) và Hàng đợi đệm in ấn (Printer Spooler)",
            "explanation": "Theo Slide 5 Lecture 9: Hàng đợi Queue áp dụng rộng rãi trong các hệ thống dùng chung tài nguyên theo thứ tự đến trước phục vụ trước: hàng đợi in ấn (Printer Spooler), điều phối tiến trình CPU đa nhiệm (Multiprogramming), bộ đệm truyền gói tin mạng (Packet Buffering)."
        },
        {
            "id": "q132",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Thuật toán duyệt đồ thị hoặc duyệt cây theo chiều rộng (BFS - Breadth-First Search) bắt buộc phải sử dụng cấu trúc dữ liệu nào để lưu trữ danh sách các đỉnh cần thăm theo từng mức?",
            "options": [
                "Hàng đợi (Queue)",
                "Ngăn xếp (Stack)",
                "Bảng băm (Hash Table)",
                "Cây nhị phân tìm kiếm (BST)"
            ],
            "answer": "Hàng đợi (Queue)",
            "explanation": "Thuật toán BFS duyệt các đỉnh theo từng tầng/mức (level by level). Đỉnh nào được phát hiện trước sẽ được thăm và mở rộng trước, do đó bắt buộc phải sử dụng cấu trúc Hàng đợi (Queue) tuân thủ nguyên lý FIFO."
        },
        {
            "id": "q133",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Trong thư viện chuẩn C++ STL, container nền tảng mặc định (Underlying Container) của bộ điều hợp `std::queue` là gì?",
            "options": [
                "`std::deque` (Double-ended Queue)",
                "`std::vector`",
                "`std::list`",
                "`std::array`"
            ],
            "answer": "`std::deque` (Double-ended Queue)",
            "explanation": "Trong C++ STL, `std::queue` không phải là một container độc lập mà là một container adaptor. Container cơ sở mặc định của nó là `std::deque` (hàng đợi 2 đầu), cho phép thao tác `push_back` và `pop_front` đều đạt hiệu năng tối ưu $O(1)$ mà không bị phân mảnh bộ nhớ."
        },
        {
            "id": "q134",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Cấu trúc Hàng đợi hai đầu (Deque - Double-Ended Queue) có đặc điểm gì khác biệt so với Queue thông thường?",
            "options": [
                "Cho phép thực hiện cả thao tác chèn và xóa phần tử ở cả hai đầu (Front và Back) trong thời gian $O(1)$",
                "Chỉ cho phép thêm ở đầu và chỉ cho phép xóa ở cuối",
                "Tự động sắp xếp các phần tử theo thứ tự tăng dần mỗi khi chèn",
                "Bắt buộc kích thước phải là số lẻ"
            ],
            "answer": "Cho phép thực hiện cả thao tác chèn và xóa phần tử ở cả hai đầu (Front và Back) trong thời gian $O(1)$",
            "explanation": "Deque (Double-Ended Queue) là cấu trúc tổng quát hóa kết hợp giữa Stack và Queue: hỗ trợ đồng thời cả 4 thao tác `push_front`, `push_back`, `pop_front`, `pop_back` với chi phí thời gian hằng số $O(1)$."
        },
        {
            "id": "q135",
            "topicId": 9,
            "topicName": "Queue",
            "question": "Cho một hàng đợi rỗng, thực hiện lần lượt chuỗi thao tác sau: `push(5); push(8); pop(); push(12); push(15); pop();`. Giá trị trả về khi gọi `front()` là bao nhiêu?",
            "options": [
                "12",
                "15",
                "8",
                "5"
            ],
            "answer": "12",
            "explanation": "Truy vết chuỗi thao tác trên Queue:\n1. `push(5)` $\\implies [5]$\n2. `push(8)` $\\implies [5, 8]$\n3. `pop()` loại bỏ 5 $\\implies [8]$\n4. `push(12)` $\\implies [8, 12]$\n5. `push(15)` $\\implies [8, 12, 15]$\n6. `pop()` loại bỏ 8 $\\implies [12, 15]$\nKhi đó phần tử ở đầu hàng đợi là 12 (`front() == 12`)."
        },

        # --- Topic 10: Trees (Binary Tree, BST, AVL) (q136 - q150) ---
        {
            "id": "q136",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Cấu trúc dữ liệu Cây (Tree) thuộc nhóm cấu trúc dữ liệu nào sau đây?",
            "options": [
                "Cấu trúc dữ liệu phi tuyến tính (Non-linear) và phân cấp (Hierarchical)",
                "Cấu trúc dữ liệu tuyến tính liên tục giống như mảng 1 chiều",
                "Cấu trúc dữ liệu ngăn xếp truy xuất theo cơ chế LIFO",
                "Cấu trúc dữ liệu dạng bảng quan hệ SQL"
            ],
            "answer": "Cấu trúc dữ liệu phi tuyến tính (Non-linear) và phân cấp (Hierarchical)",
            "explanation": "Theo Slide 13 Lecture 10: Cây (Tree) là cấu trúc dữ liệu phi tuyến (Non-linear) lưu trữ các phần tử theo quan hệ thứ bậc phân cấp (Hierarchical relationship) cha - con (parent - child)."
        },
        {
            "id": "q137",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Trong cấu trúc Cây tổng quát, Nút gốc (Root) được định nghĩa là nút như thế nào?",
            "options": [
                "Nút duy nhất trong cây không có bất kỳ nút cha nào (Node with no parent)",
                "Nút có giá trị khóa lớn nhất trong toàn bộ cây",
                "Nút nằm ở mức sâu nhất của cây",
                "Nút không có bất kỳ nút con nào"
            ],
            "answer": "Nút duy nhất trong cây không có bất kỳ nút cha nào (Node with no parent)",
            "explanation": "Theo Slide 14 Lecture 10: Gốc (Root) là điểm khởi đầu duy nhất của cây, đặc trưng bởi việc nó không có nút cha (Node with no parent). Mọi nút khác trong cây đều có duy nhất 1 nút cha."
        },
        {
            "id": "q138",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Nút lá (External Node / Leaf) trong cấu trúc Cây là nút thỏa mãn điều kiện nào sau đây?",
            "options": [
                "Là nút không có bất kỳ nút con nào (Node with no children)",
                "Là nút có cả con trái và con phải",
                "Là nút có độ sâu bằng 0",
                "Là nút nằm ở vị trí chính giữa cây"
            ],
            "answer": "Là nút không có bất kỳ nút con nào (Node with no children)",
            "explanation": "Theo Slide 14 Lecture 10: Nút ngoài (External Node hay Lá - Leaf) là nút không có con nào. Ngược lại, Nút trong (Internal Node) là nút có ít nhất một nút con."
        },
        {
            "id": "q139",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Độ sâu (Depth) của nút gốc trong cây theo quy ước chuẩn của giáo trình bằng bao nhiêu?",
            "options": [
                "0",
                "1",
                "-1",
                "Vô cùng"
            ],
            "answer": "0",
            "explanation": "Theo Slide 14 Lecture 10: Độ sâu (Depth) của nút gốc bằng 0. Độ sâu của một nút con bất kỳ bằng độ sâu của nút cha cộng thêm 1."
        },
        {
            "id": "q140",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Trong thuật toán Duyệt cây thứ tự trước (Preorder Traversal), thứ tự các bước thăm nút được thực hiện như thế nào?",
            "options": [
                "Thăm nút gốc/nút cha trước, sau đó duyệt đệ quy lần lượt các cây con từ trái qua phải",
                "Duyệt đệ quy tất cả các cây con trước rồi mới thăm nút cha",
                "Duyệt cây con bên phải trước, sau đó thăm nút gốc, rồi đến cây con bên trái",
                "Thăm các nút lá trước rồi mới duyệt lên các nút trong"
            ],
            "answer": "Thăm nút gốc/nút cha trước, sau đó duyệt đệ quy lần lượt các cây con từ trái qua phải",
            "explanation": "Theo Slide 19 Lecture 10: Duyệt Preorder (Thứ tự trước) thăm nút hiện tại trước (`visit(v)`), sau đó lần lượt duyệt đệ quy các cây con của nó từ trái sang phải. Ứng dụng: in mục lục sách, in phân cấp thư mục."
        },
        {
            "id": "q141",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Ứng dụng thực tế điển hình của phép Duyệt cây thứ tự sau (Postorder Traversal) là gì?",
            "options": [
                "Tính tổng dung lượng đĩa của một thư mục (cần tính dung lượng các tệp và thư mục con trước khi cộng dồn lên thư mục cha)",
                "Tìm kiếm phần tử nhỏ nhất trong cây tìm kiếm nhị phân",
                "In ấn danh sách học sinh theo thứ tự điểm số giảm dần",
                "Đo độ dài của cáp mạng LAN"
            ],
            "answer": "Tính tổng dung lượng đĩa của một thư mục (cần tính dung lượng các tệp và thư mục con trước khi cộng dồn lên thư mục cha)",
            "explanation": "Theo Slide 24-25 Lecture 10: Trong Postorder, các cây con được xử lý trước rồi mới đến nút cha. Khi tính dung lượng thư mục file của hệ điều hành, hệ thống phải cộng dồn dung lượng tất cả các file và thư mục con bên dưới trước rồi mới ra kết quả của thư mục cha."
        },
        {
            "id": "q142",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Cây nhị phân hoàn chỉnh (Proper / Full Binary Tree) được định nghĩa là cây nhị phân thỏa mãn điều kiện nào?",
            "options": [
                "Mỗi nút trong đều có đúng 2 nút con (nói cách khác: mỗi nút đều có 0 hoặc 2 con)",
                "Mọi nút trong cây bắt buộc phải có đúng 1 nút con",
                "Tất cả các nút lá đều chứa giá trị là số nguyên tố",
                "Chiều cao của cây bắt buộc phải bằng số lượng nút trừ đi 1"
            ],
            "answer": "Mỗi nút trong đều có đúng 2 nút con (nói cách khác: mỗi nút đều có 0 hoặc 2 con)",
            "explanation": "Theo Slide 32 Lecture 10: Cây nhị phân hoàn chỉnh (Proper / Full Binary Tree) là cây nhị phân mà mọi nút trong (Internal node) đều có chính xác 2 nút con (không tồn tại nút nào có đúng 1 con)."
        },
        {
            "id": "q143",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Trong một Cây nhị phân hoàn chỉnh (Proper Binary Tree), nếu số nút lá là $e$ và số nút trong là $i$, mối quan hệ toán học nào sau đây luôn luôn đúng?",
            "options": [
                "$e = i + 1$",
                "$e = 2i$",
                "$e = i - 1$",
                "$e = i^2$"
            ],
            "answer": "$e = i + 1$",
            "explanation": "Theo Định lý toán học tại Slide 33 Lecture 10: Trong mọi Proper Binary Tree, số nút lá (external nodes $e$) luôn nhiều hơn số nút trong (internal nodes $i$) đúng 1 nút: $e = i + 1$."
        },
        {
            "id": "q144",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Trong một Cây nhị phân hoàn chỉnh (Proper Binary Tree) có tổng cộng $n$ nút và $e$ nút lá, mối liên hệ nào sau đây là chính xác?",
            "options": [
                "$n = 2e - 1$",
                "$n = 2e + 1$",
                "$n = e^2$",
                "$n = 3e - 2$"
            ],
            "answer": "$n = 2e - 1$",
            "explanation": "Tổng số nút $n = i + e$. Do $i = e - 1$, thay vào ta có $n = (e - 1) + e = 2e - 1$. Tương tự theo số nút trong: $n = 2i + 1$ (Slide 33 Lecture 10)."
        },
        {
            "id": "q145",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Chiều cao nhỏ nhất có thể đạt được $h_{min}$ của một cây nhị phân gồm có $n$ nút là bao nhiêu?",
            "options": [
                "$\\lceil \\log_2(n + 1) \\rceil - 1$",
                "$n - 1$",
                "$\\sqrt{n}$",
                "$n / 2$"
            ],
            "answer": "$\\lceil \\log_2(n + 1) \\rceil - 1$",
            "explanation": "Theo Slide 33 Lecture 10: Ở mỗi mức $d$, số nút tối đa là $2^d$. Tổng số nút lớn nhất của cây chiều cao $h$ là $2^{h+1} - 1$. Do đó $n \\le 2^{h+1} - 1 \\implies h \\ge \\log_2(n + 1) - 1$. Chiều cao tối thiểu đạt xấp xỉ $\\log_2 n$."
        },
        {
            "id": "q146",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Phép duyệt Inorder (Thứ tự giữa) trên Cây nhị phân được thực hiện tuần tự theo quy tắc nào?",
            "options": [
                "Duyệt đệ quy cây con trái $\\to$ Thăm nút gốc $\\to$ Duyệt đệ quy cây con phải",
                "Thăm nút gốc $\\to$ Duyệt cây con trái $\\to$ Duyệt cây con phải",
                "Duyệt cây con trái $\\to$ Duyệt cây con phải $\\to$ Thăm nút gốc",
                "Thăm nút gốc $\\to$ Duyệt cây con phải $\\to$ Duyệt cây con trái"
            ],
            "answer": "Duyệt đệ quy cây con trái $\\to$ Thăm nút gốc $\\to$ Duyệt đệ quy cây con phải",
            "explanation": "Theo Slide 35 Lecture 10: Thuật toán duyệt Inorder trên cây nhị phân thực hiện theo thứ tự: Left $\\to$ Root $\\to$ Right (Duyệt con trái trước, thăm nút gốc ở giữa, duyệt con phải sau cùng)."
        },
        {
            "id": "q147",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Trong một Cây biểu thức toán học (Arithmetic Expression Tree), các nút lá và các nút trong lần lượt lưu trữ những đối tượng nào?",
            "options": [
                "Nút lá lưu trữ các toán hạng (số hoặc biến); Nút trong lưu trữ các toán tử số học ($+, -, \\times, /$)",
                "Nút lá lưu trữ toán tử; Nút trong lưu trữ toán hạng",
                "Tất cả các nút đều chỉ lưu trữ dấu ngoặc đơn",
                "Nút gốc lưu trữ toán hạng; các nút lá lưu trữ toán tử"
            ],
            "answer": "Nút lá lưu trữ các toán hạng (số hoặc biến); Nút trong lưu trữ các toán tử số học ($+, -, \\times, /$)",
            "explanation": "Theo Slide 9, 30 Lecture 10: Cây biểu thức số học tổ chức toán tử ($+, -, *, /$) tại các nút trong (Internal nodes) và các toán hạng (biến, hằng số) tại các nút lá (External nodes). Khi duyệt Inorder có ngoặc sẽ sinh biểu thức Trung tố."
        },
        {
            "id": "q148",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Tính chất sắp xếp cốt lõi của Cây tìm kiếm nhị phân (Binary Search Tree - BST) tại mỗi nút $v$ là gì?",
            "options": [
                "Mọi khóa trong cây con trái $< v->getKey() <$ Mọi khóa trong cây con phải",
                "Mọi khóa trong cây con trái phải lớn hơn khóa nút gốc",
                "Tất cả các nút con đều phải có cùng một giá trị khóa",
                "Khóa của nút gốc luôn luôn bằng tổng khóa của hai nút con"
            ],
            "answer": "Mọi khóa trong cây con trái $< v->getKey() <$ Mọi khóa trong cây con phải",
            "explanation": "Tính chất định nghĩa BST: Với mọi nút $v$, tất cả các khóa ở cây con trái của $v$ đều nhỏ hơn khóa tại $v$, và tất cả các khóa ở cây con phải của $v$ đều lớn hơn khóa tại $v$."
        },
        {
            "id": "q149",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Khi thực hiện phép duyệt Inorder (Thứ tự giữa) trên một Cây tìm kiếm nhị phân (BST), dãy khóa thu được có đặc điểm đặc biệt gì?",
            "options": [
                "Dãy khóa luôn luôn được sắp xếp theo thứ tự tăng dần",
                "Dãy khóa luôn được sắp xếp theo thứ tự giảm dần",
                "Dãy khóa có thứ tự ngẫu nhiên hoàn toàn",
                "Dãy khóa chỉ chứa toàn số chẵn"
            ],
            "answer": "Dãy khóa luôn luôn được sắp xếp theo thứ tự tăng dần",
            "explanation": "Do tính chất BST: Cây con trái < Gốc < Cây con phải. Phép duyệt Inorder duyệt Trái trước $\\to$ Gốc $\\to$ Phải sau, do đó các khóa được thăm theo đúng thứ tự tăng dần từ nhỏ nhất đến lớn nhất."
        },
        {
            "id": "q150",
            "topicId": 10,
            "topicName": "Trees",
            "question": "Trong Cây tự cân bằng AVL, Hệ số cân bằng (Balance Factor) của một nút được tính bằng gì và nhận các giá trị hợp lệ nào?",
            "options": [
                "Hiệu số giữa chiều cao cây con trái và chiều cao cây con phải: $height(Left) - height(Right)$, chỉ nhận các giá trị $\\{-1, 0, 1\\}$",
                "Tổng số nút con của cây con trái cộng với cây con phải, nhận giá trị bất kỳ",
                "Tỉ số giữa số nút lá và số nút trong",
                "Hiệu số giữa độ sâu lớn nhất và độ sâu nhỏ nhất, nhận giá trị $\\{0, 2\\}$"
            ],
            "answer": "Hiệu số giữa chiều cao cây con trái và chiều cao cây con phải: $height(Left) - height(Right)$, chỉ nhận các giá trị $\\{-1, 0, 1\\}$",
            "explanation": "Cây AVL là cây BST tự cân bằng có điều kiện nghiêm ngặt: tại mọi nút, độ chênh lệch chiều cao giữa cây con trái và cây con phải (Hệ số cân bằng) không vượt quá 1, tức là chỉ được phép nhận giá trị trong tập $\\{-1, 0, 1\\}$. Khi mất cân bằng, cây sử dụng các phép quay (LL, RR, LR, RL) để tái cân bằng về $O(\\log n)$."
        }
    ]
    return questions
