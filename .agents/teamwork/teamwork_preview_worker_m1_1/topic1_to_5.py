# -*- coding: utf-8 -*-
"""
Questions for Topics 1 to 5 (q001 - q075).
Topic 1: Introduction & Overview (q001 - q015)
Topic 2: Basic C++ Language (q016 - q030)
Topic 3: Classes & OOP in C++ (q031 - q045)
Topic 4: Algorithm Analysis & Big-O (q046 - q060)
Topic 5: Recursion (q061 - q075)
"""

def get_topics_1_to_5():
    questions = [
        # --- Topic 1: Introduction & Overview (q001 - q015) ---
        {
            "id": "q001",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Trong khoa học máy tính, khái niệm Cấu trúc dữ liệu (Data Structure) được định nghĩa chuẩn xác nhất là gì?",
            "options": [
                "Cách tổ chức, quản lý và lưu trữ dữ liệu trong bộ nhớ máy tính cho phép truy cập và sửa đổi hiệu quả",
                "Một chương trình phần mềm hoàn chỉnh dùng để quản lý hệ điều hành và phần cứng máy tính",
                "Tập hợp các câu lệnh ngôn ngữ máy được nạp trực tiếp vào thanh ghi của vi xử lý CPU",
                "Một thiết bị phần cứng chuyên dụng dùng để lưu trữ dữ liệu lâu dài trên đĩa từ"
            ],
            "answer": "Cách tổ chức, quản lý và lưu trữ dữ liệu trong bộ nhớ máy tính cho phép truy cập và sửa đổi hiệu quả",
            "explanation": "Theo bài giảng Lecture 1, Cấu trúc dữ liệu (Data Structure) là cách tổ chức, quản lý và lưu trữ dữ liệu trong bộ nhớ máy tính nhằm giúp cho việc truy cập, tìm kiếm và thao tác cập nhật dữ liệu được thực hiện một cách tối ưu và hiệu quả nhất."
        },
        {
            "id": "q002",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Ba tiêu chuẩn kỹ thuật cốt lõi dùng để đánh giá chất lượng của một Cấu trúc dữ liệu bao gồm những yếu tố nào?",
            "options": [
                "Tính đúng đắn (Correctness), Độ phức tạp thời gian (Time complexity), và Độ phức tạp không gian (Space complexity)",
                "Dung lượng dòng lệnh, số lượng hàm thành viên, và kích thước file mã nguồn",
                "Độ phân giải màn hình, tốc độ mạng Internet, và số lượng luồng đa nhiệm",
                "Tính bảo mật mã hóa, số lượng biến toàn cục, và khả năng tương thích phần cứng"
            ],
            "answer": "Tính đúng đắn (Correctness), Độ phức tạp thời gian (Time complexity), và Độ phức tạp không gian (Space complexity)",
            "explanation": "Theo Slide 8 Lecture 1, 3 đặc điểm cốt lõi đánh giá một CTDL là: Tính đúng đắn (thực thi chính xác các phép toán hỗ trợ), Chi phí thời gian (thực hiện công việc trong thời gian nhỏ nhất có thể), và Chi phí không gian bộ nhớ (sử dụng lượng RAM nhỏ nhất có thể)."
        },
        {
            "id": "q003",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Khi giải quyết bài toán trên máy tính, dữ liệu xử lý thường được phân loại thành ba nhóm nào sau đây?",
            "options": [
                "Dữ liệu đầu vào (Input), dữ liệu trung gian, và dữ liệu đầu ra (Output)",
                "Dữ liệu phần cứng, dữ liệu phần mềm, và dữ liệu mạng viễn thông",
                "Dữ liệu hệ điều hành, dữ liệu trình biên dịch, và dữ liệu thư viện liên kết",
                "Dữ liệu nhị phân, dữ liệu thập lục phân, và dữ liệu bát phân"
            ],
            "answer": "Dữ liệu đầu vào (Input), dữ liệu trung gian, và dữ liệu đầu ra (Output)",
            "explanation": "Theo bài giảng Lecture 1, trong quá trình xử lý bài toán, thông tin dữ liệu được chia thành: dữ liệu vào (Input - các thông tin đã biết ban đầu), dữ liệu trung gian (sinh ra trong quá trình tính toán), và dữ liệu ra (Output - kết quả cần đạt được)."
        },
        {
            "id": "q004",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Kiểu dữ liệu nào sau đây thuộc nhóm kiểu dữ liệu có cấu trúc (Structured Data Types)?",
            "options": [
                "Mảng (Array), Bản ghi (Struct / Record), và Chuỗi ký tự (String)",
                "Số nguyên (int), Số thực (float), và Ký tự đơn (char)",
                "Kiểu logic (bool), Con trỏ void (void*), và Số thực độ chính xác kép (double)",
                "Số nguyên không dấu (unsigned int) và Số nguyên dài (long long)"
            ],
            "answer": "Mảng (Array), Bản ghi (Struct / Record), và Chuỗi ký tự (String)",
            "explanation": "Các kiểu dữ liệu cơ sở (đơn giản, nguyên tử) là int, float, char, bool. Kiểu dữ liệu có cấu trúc là kiểu được tạo thành từ nhiều phần tử dữ liệu thành phần, ví dụ Mảng (Array), Cấu trúc (Struct), Lớp (Class), Chuỗi (String)."
        },
        {
            "id": "q005",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Khái niệm Giải thuật (Algorithm) được định nghĩa chuẩn xác nhất là gì?",
            "options": [
                "Tập hữu hạn có thứ tự các bước tác động lên dữ liệu để sau một số hữu hạn bước sẽ thu được kết quả mong muốn",
                "Một đoạn mã nguồn C++ bắt buộc phải biên dịch thành công mà không có cảnh báo",
                "Một tập hợp vô hạn các phép tính toán số học chạy liên tục trên bộ xử lý trung tâm",
                "Quy trình cài đặt một hệ quản trị cơ sở dữ liệu quan hệ trên máy chủ"
            ],
            "answer": "Tập hữu hạn có thứ tự các bước tác động lên dữ liệu để sau một số hữu hạn bước sẽ thu được kết quả mong muốn",
            "explanation": "Theo Slide 14 Lecture 1, Giải thuật là tập hữu hạn có thứ tự các bước tính toán, chỉ thị rõ ràng nhằm tác động lên dữ liệu đầu vào để sau một số hữu hạn lần thực hiện sẽ cho ra kết quả mong muốn, mang tính độc lập với ngôn ngữ lập trình."
        },
        {
            "id": "q006",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Đặc trưng \"Tính hữu hạn\" (Finiteness) của một giải thuật đòi hỏi điều kiện gì?",
            "options": [
                "Giải thuật bắt buộc phải dừng lại sau một số hữu hạn bước thực thi với mọi bộ dữ liệu đầu vào hợp lệ",
                "Kích thước file mã nguồn thuật toán không được vượt quá giới hạn 1 Megabyte",
                "Số lượng biến khai báo trong chương trình không được vượt quá 100 biến",
                "Thời gian chạy của chương trình trên máy tính không được vượt quá 1 giây thực tế"
            ],
            "answer": "Giải thuật bắt buộc phải dừng lại sau một số hữu hạn bước thực thi với mọi bộ dữ liệu đầu vào hợp lệ",
            "explanation": "Tính hữu hạn (Finiteness) là một trong 5 đặc trưng nền tảng của thuật toán: với mọi đầu vào hợp lệ, thuật toán không được rơi vào vòng lặp vô tận mà bắt buộc phải kết thúc và dừng lại sau một số bước tính toán hữu hạn."
        },
        {
            "id": "q007",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Đặc trưng \"Tính xác định / Tính đơn trị\" (Definiteness / Uniqueness) của một giải thuật có nghĩa là gì?",
            "options": [
                "Mỗi bước thực hiện phải được mô tả rõ ràng, không gây mập mờ, kết quả trung gian chỉ phụ thuộc vào đầu vào và các bước trước đó",
                "Thuật toán chỉ được phép có duy nhất một câu lệnh gán biến trong toàn bộ chương trình",
                "Mọi biến trong thuật toán chỉ được nhận một giá trị số nguyên duy nhất trong suốt vòng đời",
                "Thuật toán chỉ được phép chạy trên một nhân vi xử lý đơn độc"
            ],
            "answer": "Mỗi bước thực hiện phải được mô tả rõ ràng, không gây mập mờ, kết quả trung gian chỉ phụ thuộc vào đầu vào và các bước trước đó",
            "explanation": "Theo Slide 15 Lecture 1, Tính xác định / Tính đơn trị (Definiteness / Uniqueness) đòi hỏi mỗi bước chỉ dẫn phải thật sáng sủa, chính xác, không đa nghĩa; tại mỗi bước, hành động tiếp theo và kết quả sinh ra được xác định duy nhất từ dữ liệu đầu vào và các bước đã xử lý trước đó."
        },
        {
            "id": "q008",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Đặc trưng \"Tính tổng quát\" (Generality) của một thuật toán thể hiện ở điểm nào?",
            "options": [
                "Thuật toán áp dụng được để giải quyết cho cả một lớp các bài toán có cùng dạng chứ không chỉ riêng một bộ dữ liệu cụ thể",
                "Thuật toán có thể chạy trên mọi hệ điều hành mà không cần biên dịch lại",
                "Thuật toán có thể tự động viết ra mã nguồn của các thuật toán khác",
                "Thuật toán không sử dụng bất kỳ thư viện ngoài nào của ngôn ngữ lập trình"
            ],
            "answer": "Thuật toán áp dụng được để giải quyết cho cả một lớp các bài toán có cùng dạng chứ không chỉ riêng một bộ dữ liệu cụ thể",
            "explanation": "Tính tổng quát (Generality) nghĩa là giải thuật được xây dựng để giải quyết một lớp bài toán tổng quát với miền đầu vào xác định, chứ không phải một công thức riêng lẻ chỉ tính đúng cho một vài trường hợp cá biệt."
        },
        {
            "id": "q009",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Theo các đặc trưng chuẩn mực của giải thuật, một thuật toán có thể có bao nhiêu dữ liệu đầu vào (Input) và dữ liệu đầu ra (Output)?",
            "options": [
                "Có 0 hoặc nhiều đầu vào (>= 0) và có ít nhất 1 đầu ra (>= 1)",
                "Bắt buộc phải có ít nhất 1 đầu vào và không được có đầu ra",
                "Có chính xác 1 đầu vào và chính xác 1 đầu ra",
                "Có vô số đầu vào nhưng chỉ được có tối đa 0 đầu ra"
            ],
            "answer": "Có 0 hoặc nhiều đầu vào (>= 0) và có ít nhất 1 đầu ra (>= 1)",
            "explanation": "Theo Slide 15 Lecture 1, một giải thuật nhận vào 0 hoặc nhiều dữ liệu đầu vào (Input >= 0, ví dụ thuật toán sinh số Pi hoặc sinh số ngẫu nhiên không cần nhận tham số) và bắt buộc phải tạo ra ít nhất một kết quả đầu ra (Output >= 1)."
        },
        {
            "id": "q010",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Trong các phương pháp biểu diễn giải thuật, nhược điểm lớn nhất của phương pháp dùng \"Ngôn ngữ tự nhiên\" là gì?",
            "options": [
                "Dễ gây hiểu lầm đa nghĩa, diễn đạt dài dòng và không có cấu trúc cú pháp chuẩn hóa",
                "Không thể dịch sang tiếng Việt và chỉ hỗ trợ tiếng Anh kỹ thuật",
                "Yêu cầu cấu hình phần cứng đồ họa chuyên dụng mới có thể đọc được",
                "Bắt buộc phải cài đặt trình biên dịch GCC để dịch ra mã máy"
            ],
            "answer": "Dễ gây hiểu lầm đa nghĩa, diễn đạt dài dòng và không có cấu trúc cú pháp chuẩn hóa",
            "explanation": "Biểu diễn giải thuật bằng ngôn ngữ tự nhiên tuy dễ tiếp cận ban đầu nhưng có nhược điểm chí mạng là phụ thuộc ngữ cảnh, dễ phát sinh nhập nhằng (đa nghĩa), dài dòng và thiếu cấu trúc hình thức chặt chẽ."
        },
        {
            "id": "q011",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Trong biểu diễn thuật toán bằng Lưu đồ khối (Flowchart), hình thoi (Diamond) biểu thị cho thao tác nào?",
            "options": [
                "Thao tác kiểm tra điều kiện logic để rẽ nhánh thực thi chương trình",
                "Điểm bắt đầu (Start) hoặc kết thúc (End) của toàn bộ giải thuật",
                "Thao tác gán giá trị hoặc tính toán xử lý dữ liệu thông thường",
                "Thao tác nhập dữ liệu từ bàn phím hoặc xuất dữ liệu ra màn hình"
            ],
            "answer": "Thao tác kiểm tra điều kiện logic để rẽ nhánh thực thi chương trình",
            "explanation": "Trong chuẩn vẽ Lưu đồ khối (Flowchart): Hình thoi biểu thị khối điều kiện kiểm tra (Decision/Branching) với các nhánh ra True/False; Hình chữ nhật biểu thị thao tác tính toán; Hình bình hành là Nhập/Xuất; Hình Oval/Elip là Bắt đầu/Kết thúc."
        },
        {
            "id": "q012",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Trong Lưu đồ khối (Flowchart), hình bình hành (Parallelogram) được quy ước sử dụng cho mục đích nào?",
            "options": [
                "Thao tác nhập dữ liệu đầu vào (Input) hoặc xuất dữ liệu kết quả (Output)",
                "Thao tác tính toán số học và gán giá trị biểu thức",
                "Khối gọi hàm con đệ quy hoặc chương trình con",
                "Khối điều khiển rẽ nhánh Đúng/Sai"
            ],
            "answer": "Thao tác nhập dữ liệu đầu vào (Input) hoặc xuất dữ liệu kết quả (Output)",
            "explanation": "Theo quy ước quốc tế về sơ đồ khối thuật toán (Flowchart symbols), hình bình hành đại diện cho khối Nhập/Xuất (Input/Output operations)."
        },
        {
            "id": "q013",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Phát biểu nào sau đây đúng nhất về Mã giả (Pseudocode)?",
            "options": [
                "Là ngôn ngữ tựa mã lệnh có cấu trúc chặt chẽ, độc lập với cú pháp máy móc của trình biên dịch, dùng từ khóa gần gũi với toán học và logic",
                "Là đoạn mã độc hại được chèn vào chương trình để làm giả kết quả kiểm thử",
                "Là mã máy nhị phân 0 và 1 được vi xử lý thực thi trực tiếp không cần biên dịch",
                "Là tập hợp các sơ đồ đồ họa vẽ bằng phần mềm AutoCAD để mô phỏng thuật toán"
            ],
            "answer": "Là ngôn ngữ tựa mã lệnh có cấu trúc chặt chẽ, độc lập với cú pháp máy móc của trình biên dịch, dùng từ khóa gần gũi với toán học và logic",
            "explanation": "Mã giả (Pseudocode) là phương tiện biểu diễn thuật toán chuẩn tắc trong khoa học máy tính: vừa có cấu trúc rành mạch (như if-else, while, for), vừa súc tích và độc lập hoàn toàn với cú pháp cứng nhắc của ngôn ngữ lập trình cụ thể."
        },
        {
            "id": "q014",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Phương trình kinh điển của Giáo sư Niklaus Wirth (tác giả ngôn ngữ Pascal) tóm lược bản chất của một chương trình phần mềm là gì?",
            "options": [
                "Chương trình = Cấu trúc dữ liệu + Giải thuật (Programs = Data Structures + Algorithms)",
                "Chương trình = Phần cứng + Hệ điều hành (Programs = Hardware + Operating System)",
                "Chương trình = Cơ sở dữ liệu * Giao diện người dùng (Programs = Database * UI)",
                "Chương trình = Trình biên dịch / Ngôn ngữ máy (Programs = Compiler / Machine Code)"
            ],
            "answer": "Chương trình = Cấu trúc dữ liệu + Giải thuật (Programs = Data Structures + Algorithms)",
            "explanation": "Câu khẩu hiệu và tiêu đề cuốn sách kinh điển năm 1976 của Giáo sư Niklaus Wirth là: \"Algorithms + Data Structures = Programs\" (hoặc Data Structures + Algorithms = Programs), khẳng định CTDL và Giải thuật là 2 trụ cột tạo nên phần mềm."
        },
        {
            "id": "q015",
            "topicId": 1,
            "topicName": "Introduction & Overview",
            "question": "Năm thao tác cơ bản và thông dụng nhất trên các cấu trúc dữ liệu bao gồm những thao tác nào?",
            "options": [
                "Tìm kiếm (Search), Sắp xếp (Sort), Chèn (Insert), Cập nhật (Update), và Xóa (Delete)",
                "Biên dịch (Compile), Liên kết (Link), Nạp (Load), Gỡ lỗi (Debug), và Đóng gói (Package)",
                "Mã hóa (Encrypt), Giải mã (Decrypt), Nén (Compress), Giải nén (Decompress), và Băm (Hash)",
                "Cấp điện (Power On), Tắt máy (Shutdown), Khởi động lại (Restart), Ngủ đông (Hibernate), và Khóa (Lock)"
            ],
            "answer": "Tìm kiếm (Search), Sắp xếp (Sort), Chèn (Insert), Cập nhật (Update), và Xóa (Delete)",
            "explanation": "Theo Slide 26 Lecture 1, 5 thao tác cơ sở nền tảng được định nghĩa trên các cấu trúc dữ liệu là: Search (tìm kiếm phần tử), Sort (sắp xếp phần tử), Insert (chèn phần tử mới), Update (cập nhật giá trị), và Delete (loại bỏ phần tử)."
        },

        # --- Topic 2: Basic C++ Language (q016 - q030) ---
        {
            "id": "q016",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Bản chất của một biến con trỏ (Pointer) trong ngôn ngữ C++ là gì?",
            "options": [
                "Là một biến dùng để lưu trữ địa chỉ ô nhớ của một biến hoặc vùng nhớ khác",
                "Là một kiểu dữ liệu dùng để biểu diễn các số thực có dấu phẩy động cực lớn",
                "Là một chỉ thị tiền xử lý yêu cầu trình biên dịch nạp thêm thư viện ngoài",
                "Là một hàm đặc biệt tự động kích hoạt khi chương trình bị lỗi ngắt dòng"
            ],
            "answer": "Là một biến dùng để lưu trữ địa chỉ ô nhớ của một biến hoặc vùng nhớ khác",
            "explanation": "Theo Slide 7 Lecture 2, con trỏ (Pointer) là một biến đặc biệt trong C/C++, giá trị chứa bên trong nó không phải là dữ liệu thông thường mà chính là địa chỉ ô nhớ RAM của một biến hoặc vùng nhớ khác."
        },
        {
            "id": "q017",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Toán tử giải tham chiếu (Dereference Operator `*`) trong biểu thức `*p = 20;` có tác dụng gì?",
            "options": [
                "Truy xuất và ghi giá trị 20 vào ô nhớ mà con trỏ p đang trỏ tới",
                "Nhân giá trị của con trỏ p với số nguyên 20",
                "Khai báo một con trỏ mới có tên là p và gán giá trị 20",
                "Giải phóng vùng bộ nhớ mà con trỏ p đang chiếm giữ"
            ],
            "answer": "Truy xuất và ghi giá trị 20 vào ô nhớ mà con trỏ p đang trỏ tới",
            "explanation": "Toán tử `*` khi đứng trước một con trỏ đã khai báo đóng vai trò toán tử giải tham chiếu (Dereference operator), cho phép lập trình viên đọc hoặc ghi trực tiếp giá trị vào ô nhớ tại địa chỉ mà con trỏ đang lưu trữ."
        },
        {
            "id": "q018",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Phân biệt ý nghĩa của ký hiệu `&` trong hai câu lệnh: `int &r = x;` và `int *p = &x;`?",
            "options": [
                "`int &r = x;` khai báo biến tham chiếu r là bí danh của x; còn `&x` là toán tử lấy địa chỉ ô nhớ của x",
                "Cả hai câu lệnh đều là toán tử lấy địa chỉ ô nhớ và gán cho con trỏ",
                "`int &r = x;` tạo bản sao giá trị của x; còn `int *p = &x;` tạo bí danh cho x",
                "`&` trong cả hai trường hợp đều là phép toán logic bitwise AND"
            ],
            "answer": "`int &r = x;` khai báo biến tham chiếu r là bí danh của x; còn `&x` là toán tử lấy địa chỉ ô nhớ của x",
            "explanation": "Trong C++, khi `&` xuất hiện bên cạnh kiểu dữ liệu (`int &r`), nó biểu thị khai báo tham chiếu (Reference) tạo bí danh (alias) chung ô nhớ với biến `x`. Khi `&` đứng trước tên biến đã có (`&x`), nó là toán tử lấy địa chỉ (Address-of operator)."
        },
        {
            "id": "q019",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Để cấp phát động và giải phóng đúng cách một mảng gồm `n` số nguyên kiểu `int` trong C++, cặp lệnh nào sau đây là chuẩn xác?",
            "options": [
                "`int *a = new int[n];` và `delete[] a;`",
                "`int *a = new int(n);` và `delete a;`",
                "`int a = malloc(n);` và `free[] a;`",
                "`int *a = alloc int[n];` và `destruct a;`"
            ],
            "answer": "`int *a = new int[n];` và `delete[] a;`",
            "explanation": "Theo Slide 15 Lecture 2, trong C++ toán tử cấp phát mảng động là `new DataType[size]`, và khi giải phóng bộ nhớ mảng động bắt buộc phải dùng toán tử `delete[] pointer;` để tránh lỗi Undefined Behavior và rò rỉ bộ nhớ."
        },
        {
            "id": "q020",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Cho con trỏ `int *p` đang trỏ tới địa chỉ ô nhớ `0x1000`. Giả sử kích thước kiểu `int` là 4 bytes (`sizeof(int) == 4`). Biểu thức `p + 2` sẽ có giá trị địa chỉ là bao nhiêu?",
            "options": [
                "`0x1008`",
                "`0x1002`",
                "`0x1004`",
                "`0x1016`"
            ],
            "answer": "`0x1008`",
            "explanation": "Theo quy tắc số học con trỏ (Pointer Arithmetic - Slide 11 Lecture 2), phép cộng con trỏ `p + k` sẽ dịch chuyển địa chỉ một lượng bằng `k * sizeof(*p)` bytes. Ở đây: `0x1000 + 2 * 4 bytes = 0x1000 + 8 = 0x1008`."
        },
        {
            "id": "q021",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Mối quan hệ bản chất giữa tên mảng 1 chiều `a` và con trỏ trong C++ được thể hiện như thế nào?",
            "options": [
                "Tên mảng `a` đóng vai trò là con trỏ hằng trỏ tới phần tử đầu tiên `&a[0]`, và biểu thức `a[i]` tương đương với `*(a + i)`",
                "Tên mảng `a` là một biến con trỏ thông thường có thể thay đổi địa chỉ bằng phép gán `a = p;`",
                "Mảng và con trỏ hoàn toàn không có liên hệ gì về cách truy xuất bộ nhớ",
                "Biểu thức `a[i]` thực chất được trình biên dịch dịch thành `&a + i`"
            ],
            "answer": "Tên mảng `a` đóng vai trò là con trỏ hằng trỏ tới phần tử đầu tiên `&a[0]`, và biểu thức `a[i]` tương đương với `*(a + i)`",
            "explanation": "Trong C/C++, tên mảng `a` là con trỏ hằng (constant pointer) cố định trỏ vào `&a[0]`. Phép truy xuất `a[i]` thực chất là cú pháp rút gọn của phép toán giải tham chiếu con trỏ `*(a + i)`."
        },
        {
            "id": "q022",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Cho đoạn mã: `int x = 10; int *p = &x; int **pp = &p;`. Biểu thức nào sau đây truy xuất được giá trị `10` của biến `x`?",
            "options": [
                "`**pp`",
                "`*pp`",
                "`&pp`",
                "`pp`"
            ],
            "answer": "`**pp`",
            "explanation": "`pp` là con trỏ trỏ đến con trỏ (pointer to pointer). Giải tham chiếu cấp 1 `*pp` trả về con trỏ `p` (địa chỉ của `x`). Giải tham chiếu cấp 2 `**pp` trả về giá trị thực của `x`, tức là 10."
        },
        {
            "id": "q023",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Để cấp phát bộ nhớ động cho ma trận 2 chiều kích thước `m x n` kiểu `int` trong C++, quy trình chuẩn xác là gì?",
            "options": [
                "Cấp phát mảng con trỏ `int **a = new int*[m];` sau đó duyệt vòng lặp `for (int i=0; i<m; i++) a[i] = new int[n];`",
                "Chỉ cần gọi duy nhất một lệnh: `int **a = new int[m][n];`",
                "Gọi lệnh `int **a = new int*[m * n];` mà không cần vòng lặp",
                "Khai báo `int *a = new int[m];` rồi gán `a = new int[n];`"
            ],
            "answer": "Cấp phát mảng con trỏ `int **a = new int*[m];` sau đó duyệt vòng lặp `for (int i=0; i<m; i++) a[i] = new int[n];`",
            "explanation": "Theo Slide 19-20 Lecture 2, cấp phát ma trận động 2 chiều gồm 2 bước: Bước 1 cấp phát mảng chứa m con trỏ hàng `new int*[m]`, bước 2 lặp qua từng hàng để cấp phát n phần tử cho hàng đó `a[i] = new int[n]`."
        },
        {
            "id": "q024",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Khi giải phóng bộ nhớ của ma trận 2 chiều động `int **a` gồm `m` hàng, thứ tự gọi lệnh nào sau đây là bắt buộc để tránh rò rỉ bộ nhớ (Memory Leak)?",
            "options": [
                "Duyệt vòng lặp gọi `delete[] a[i];` cho từng hàng trước, sau đó mới gọi `delete[] a;`",
                "Gọi lệnh `delete[] a;` trước rồi mới lặp gọi `delete[] a[i];`",
                "Chỉ cần gọi một lệnh duy nhất: `delete[][] a;`",
                "Chỉ cần gọi lệnh `delete a;` là toàn bộ các hàng sẽ tự động được thu hồi"
            ],
            "answer": "Duyệt vòng lặp gọi `delete[] a[i];` cho từng hàng trước, sau đó mới gọi `delete[] a;`",
            "explanation": "Nếu gọi `delete[] a` trước, mảng con trỏ quản lý các hàng sẽ bị mất, khiến các vùng nhớ của từng hàng `a[i]` bị cô lập và không thể giải phóng được (dẫn đến rò rỉ bộ nhớ). Do đó bắt buộc phải giải phóng từng hàng trước rồi mới giải phóng `a`."
        },
        {
            "id": "q025",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Cho hàm hoán vị: `void swap(int &a, int &b) { int t = a; a = b; b = t; }`. Cơ chế truyền tham số này trong C++ được gọi là gì?",
            "options": [
                "Truyền theo tham chiếu (Pass-by-reference)",
                "Truyền theo tham trị (Pass-by-value)",
                "Truyền theo con trỏ hằng (Pass-by-const-pointer)",
                "Truyền theo địa chỉ macro tiền xử lý"
            ],
            "answer": "Truyền theo tham chiếu (Pass-by-reference)",
            "explanation": "Cú pháp `int &a, int &b` là cơ chế truyền tham số bằng tham chiếu (Pass-by-reference) trong C++. Hàm làm việc trực tiếp trên ô nhớ của đối số truyền vào, cho phép hoán vị trực tiếp giá trị của 2 biến bên ngoài hàm."
        },
        {
            "id": "q026",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Cho đoạn mã C++11: `string s = \"c++\"; for (char &c : s) c = toupper(c);`. Giá trị của chuỗi `s` sau vòng lặp là gì?",
            "options": [
                "`\"C++\"`",
                "`\"c++\"`",
                "`\"C\"`",
                "`\"\"` (chuỗi rỗng)"
            ],
            "answer": "`\"C++\"`",
            "explanation": "Trong vòng lặp for-each (`for (char &c : s)`), biến `c` được khai báo là tham chiếu (`&`) tới từng ký tự trong chuỗi gốc `s`. Do đó thao tác `c = toupper(c)` sẽ sửa đổi trực tiếp các ký tự của chuỗi `s`, biến `\"c++\"` thành `\"C++\"`."
        },
        {
            "id": "q027",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Quy tắc bắt buộc khi khai báo hàm có tham số mặc định (Default Arguments) trong C++ là gì?",
            "options": [
                "Các tham số có giá trị mặc định phải nằm liên tục ở cuối danh sách tham số",
                "Các tham số mặc định bắt buộc phải đặt ở đầu danh sách tham số",
                "Hàm chỉ được phép có tối đa một tham số mặc định duy nhất",
                "Tham số mặc định chỉ được áp dụng cho kiểu số thực float"
            ],
            "answer": "Các tham số có giá trị mặc định phải nằm liên tục ở cuối danh sách tham số",
            "explanation": "Theo chuẩn C++ (Slide 33 Lecture 2), nếu một tham số có giá trị mặc định thì tất cả các tham số nằm phía sau nó trong danh sách cũng bắt buộc phải có giá trị mặc định. Nói cách khác, các đối số mặc định phải nằm ở cuối danh sách tham số."
        },
        {
            "id": "q028",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Trong C++, hai hàm nào sau đây KHÔNG THỂ nạp chồng (Overload) hợp lệ với nhau và sẽ gây lỗi biên dịch?",
            "options": [
                "`int calc(int a, int b);` và `double calc(int a, int b);`",
                "`int calc(int a, int b);` và `int calc(double a, double b);`",
                "`int calc(int a);` và `int calc(int a, int b);`",
                "`void calc(char a);` và `void calc(int a);`"
            ],
            "answer": "`int calc(int a, int b);` và `double calc(int a, int b);`",
            "explanation": "Quy tắc nạp chồng hàm (Function Overloading - Slide 36 Lecture 2) quy định danh sách tham số phải khác nhau về số lượng hoặc kiểu dữ liệu. Hai hàm có danh sách tham số giống hệt nhau mà chỉ khác kiểu trả về (return type) sẽ không được coi là nạp chồng hợp lệ và báo lỗi biên dịch."
        },
        {
            "id": "q029",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Cú pháp chuẩn để định nghĩa một hàm mẫu (Function Template) trong C++ là gì?",
            "options": [
                "`template <class T> T getMax(T a, T b) { return (a > b) ? a : b; }`",
                "`generic <type T> T getMax(T a, T b) { return (a > b) ? a : b; }`",
                "`define <typename T> T getMax(T a, T b) { return (a > b) ? a : b; }`",
                "`macro <class T> T getMax(T a, T b) { return (a > b) ? a : b; }`"
            ],
            "answer": "`template <class T> T getMax(T a, T b) { return (a > b) ? a : b; }`",
            "explanation": "Cú pháp định nghĩa hàm mẫu trong C++ bắt đầu bằng từ khóa `template <class T>` hoặc `template <typename T>`, cho phép viết hàm tổng quát áp dụng cho nhiều kiểu dữ liệu khác nhau."
        },
        {
            "id": "q030",
            "topicId": 2,
            "topicName": "Basic C++ Language",
            "question": "Hiện tượng \"Con trỏ treo\" (Dangling Pointer) xảy ra trong tình huống nào?",
            "options": [
                "Khi con trỏ vẫn trỏ tới địa chỉ ô nhớ cũ đã bị thu hồi/giải phóng bởi lệnh delete",
                "Khi con trỏ được gán giá trị NULL hoặc nullptr an toàn",
                "Khi con trỏ được cấp phát bộ nhớ thành công nhưng chưa gán dữ liệu",
                "Khi con trỏ được khai báo là hằng số const pointer"
            ],
            "answer": "Khi con trỏ vẫn trỏ tới địa chỉ ô nhớ cũ đã bị thu hồi/giải phóng bởi lệnh delete",
            "explanation": "Con trỏ treo (Dangling pointer) là con trỏ lưu trữ địa chỉ của một vùng nhớ trên heap đã bị giải phóng bằng `delete`. Thao tác đọc/ghi qua con trỏ treo dẫn đến lỗi Undefined Behavior nghiêm trọng."
        },

        # --- Topic 3: Classes & OOP in C++ (q031 - q045) ---
        {
            "id": "q031",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Điểm khác biệt căn bản giữa Lập trình Hướng thủ tục (POP) và Lập trình Hướng đối tượng (OOP) là gì?",
            "options": [
                "POP tập trung vào hàm và phân rã chức năng; OOP đóng gói dữ liệu thuộc tính và phương thức hành vi vào cùng một thực thể đối tượng",
                "POP chỉ chạy được trên hệ điều hành Linux; OOP chỉ chạy được trên Windows",
                "POP không cho phép sử dụng vòng lặp; OOP cho phép sử dụng vòng lặp",
                "POP không có khái niệm biến số; OOP mới có khái niệm biến số"
            ],
            "answer": "POP tập trung vào hàm và phân rã chức năng; OOP đóng gói dữ liệu thuộc tính và phương thức hành vi vào cùng một thực thể đối tượng",
            "explanation": "Theo Slide 3-4 Lecture 3, POP tập trung vào các giải thuật và hàm chức năng, dữ liệu tách rời; trong khi OOP lấy đối tượng làm trung tâm, đóng gói (encapsulation) trạng thái dữ liệu và các hành vi thao tác trên dữ liệu đó trong cùng một thực thể lớp."
        },
        {
            "id": "q032",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Trong ngôn ngữ C++, điểm khác biệt duy nhất giữa từ khóa `struct` và `class` là gì?",
            "options": [
                "Quyền truy cập mặc định của các thành viên trong `struct` là `public`, còn trong `class` là `private`",
                "`struct` không thể chứa phương thức; chỉ `class` mới chứa được phương thức",
                "`struct` được cấp phát trên Stack; `class` bắt buộc phải cấp phát trên Heap",
                "`struct` không cho phép kế thừa; chỉ `class` mới có tính kế thừa"
            ],
            "answer": "Quyền truy cập mặc định của các thành viên trong `struct` là `public`, còn trong `class` là `private`",
            "explanation": "Trong C++, `struct` và `class` hầu như giống hệt nhau về khả năng (đều có thể có phương thức, cấu tử, kế thừa). Điểm khác biệt kỹ thuật duy nhất là quyền truy cập mặc định: `struct` mặc định là `public`, còn `class` mặc định là `private`."
        },
        {
            "id": "q033",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Đặc tả truy xuất `private` trong một `class` C++ có ý nghĩa bảo vệ như thế nào?",
            "options": [
                "Chỉ các phương thức thành viên của lớp đó hoặc các hàm bạn (friend) mới có quyền truy cập trực tiếp",
                "Bất kỳ hàm nào trong toàn bộ chương trình cũng đều có thể đọc và sửa đổi tự do",
                "Chỉ cho phép các hàm của hệ điều hành truy cập khi có quyền quản trị Administrator",
                "Dữ liệu được mã hóa và không bao giờ đọc được ngay cả từ các phương thức của lớp"
            ],
            "answer": "Chỉ các phương thức thành viên của lớp đó hoặc các hàm bạn (friend) mới có quyền truy cập trực tiếp",
            "explanation": "Theo Slide 8 Lecture 3, thành viên có phạm vi `private` chỉ có thể được truy xuất từ bên trong các hàm thành viên của chính lớp đó hoặc từ các hàm bạn/lớp bạn (`friend`). Bên ngoài lớp không thể truy cập trực tiếp."
        },
        {
            "id": "q034",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Đặc tả truy xuất `protected` trong C++ khác với `private` ở điểm mấu chốt nào?",
            "options": [
                "Thành viên `protected` cho phép các lớp con kế thừa từ lớp đó được quyền truy cập trực tiếp",
                "Thành viên `protected` có thể truy cập tự do từ hàm `main` bên ngoài",
                "Thành viên `protected` không thể truy xuất từ các phương thức trong cùng một lớp",
                "Thành viên `protected` bắt buộc phải là hằng số const"
            ],
            "answer": "Thành viên `protected` cho phép các lớp con kế thừa từ lớp đó được quyền truy cập trực tiếp",
            "explanation": "`protected` là mức bảo vệ trung gian: đối với bên ngoài lớp nó đóng vai trò ẩn như `private`, nhưng đối với các lớp con dẫn xuất (derived classes) kế thừa từ lớp đó thì các thành viên `protected` lại cho phép truy cập trực tiếp."
        },
        {
            "id": "q035",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Toán tử định phạm vi (Scope Resolution Operator `::`) được sử dụng trong C++ với mục đích gì khi lập trình OOP?",
            "options": [
                "Định nghĩa mã nguồn của các phương thức thành viên ở bên ngoài phần khai báo của lớp",
                "Giải phóng ô nhớ của đối tượng tương đương lệnh delete",
                "Khai báo một biến con trỏ cấp hai trỏ tới đối tượng",
                "Thực hiện phép chia lấy phần nguyên giữa hai đối tượng số học"
            ],
            "answer": "Định nghĩa mã nguồn của các phương thức thành viên ở bên ngoài phần khai báo của lớp",
            "explanation": "Theo Slide 10 Lecture 3, cú pháp `ReturnType ClassName::MethodName(args)` sử dụng toán tử `::` để chỉ định phương thức `MethodName` thuộc phạm vi của lớp `ClassName` khi viết định nghĩa thân hàm bên ngoài lớp."
        },
        {
            "id": "q036",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Khi một phương thức thành viên được viết mã cài đặt ngay bên trong định nghĩa của `class`, trình biên dịch C++ sẽ mặc định coi phương thức đó là gì?",
            "options": [
                "Phương thức nội tuyến (Inline method)",
                "Phương thức tĩnh (Static method)",
                "Phương thức trừu tượng thuần ảo (Pure virtual method)",
                "Hàm bạn toàn cục (Global friend function)"
            ],
            "answer": "Phương thức nội tuyến (Inline method)",
            "explanation": "Theo Slide 11 Lecture 3, các phương thức được định nghĩa thân hàm ngay trong phần khai báo lớp sẽ tự động được xem là hàm `inline` (nội tuyến), trình biên dịch sẽ cố gắng chèn trực tiếp mã lệnh tại vị trí gọi để tối ưu tốc độ."
        },
        {
            "id": "q037",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Để gọi phương thức `area()` thông qua con trỏ đối tượng `CRectangle *rect = new CRectangle();`, cú pháp nào sau đây là đúng?",
            "options": [
                "`rect->area();` hoặc `(*rect).area();`",
                "`rect.area();`",
                "`*rect->area();`",
                "`rect::area();`"
            ],
            "answer": "`rect->area();` hoặc `(*rect).area();`",
            "explanation": "Khi thao tác với biến đối tượng thông thường, ta dùng toán tử dấu chấm (`obj.method()`). Khi thao tác với con trỏ đối tượng, ta dùng toán tử mũi tên (`ptr->method()`) hoặc giải tham chiếu rồi chấm (`(*ptr).method()`)."
        },
        {
            "id": "q038",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Phát biểu nào sau đây về Hàm khởi tạo (Constructor) trong C++ là SAI?",
            "options": [
                "Hàm khởi tạo có kiểu trả về mặc định là `void`",
                "Hàm khởi tạo có tên trùng hoàn toàn với tên của lớp",
                "Hàm khởi tạo tự động kích hoạt khi một đối tượng thuộc lớp được tạo ra",
                "Hàm khởi tạo có thể được nạp chồng (Overloading) với nhiều danh sách tham số khác nhau"
            ],
            "answer": "Hàm khởi tạo có kiểu trả về mặc định là `void`",
            "explanation": "Constructor KHÔNG CÓ kiểu trả về, kể cả kiểu `void`. Khai báo `void ClassName()` sẽ bị trình biên dịch báo lỗi hoặc coi là một hàm thành viên thông thường chứ không phải constructor."
        },
        {
            "id": "q039",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Phát biểu nào sau đây về Hàm hủy (Destructor) trong C++ là ĐÚNG?",
            "options": [
                "Tên hàm hủy bắt đầu bằng dấu ngã `~`, không nhận tham số, không có kiểu trả về, và mỗi lớp chỉ có duy nhất 1 hàm hủy",
                "Hàm hủy có thể được nạp chồng giống như hàm khởi tạo",
                "Hàm hủy phải nhận tham số là con trỏ của đối tượng cần hủy",
                "Hàm hủy phải trả về giá trị kiểu boolean thông báo việc giải phóng thành công"
            ],
            "answer": "Tên hàm hủy bắt đầu bằng dấu ngã `~`, không nhận tham số, không có kiểu trả về, và mỗi lớp chỉ có duy nhất 1 hàm hủy",
            "explanation": "Theo Slide 16-17 Lecture 3, Destructor có tên dạng `~ClassName()`, không có tham số và không có kiểu trả về. Do không có tham số nên hàm hủy KHÔNG THỂ nạp chồng, mỗi lớp chỉ có duy nhất một hàm hủy."
        },
        {
            "id": "q040",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Nếu một lớp quản lý mảng động cấp phát qua `new` nhưng không cài đặt giải phóng trong hàm hủy (Destructor), hậu quả gì sẽ xảy ra?",
            "options": [
                "Gây rò rỉ bộ nhớ (Memory Leak) khi đối tượng bị hủy vì vùng nhớ trên heap không được giải phóng",
                "Chương trình sẽ tự động kích hoạt bộ thu gom rác tự động Garbage Collector giống như Java",
                "Trình biên dịch sẽ từ chối biên dịch mã nguồn",
                "Hệ điều hành sẽ tự động thu hồi ngay lập tức mà không ảnh hưởng gì"
            ],
            "answer": "Gây rò rỉ bộ nhớ (Memory Leak) khi đối tượng bị hủy vì vùng nhớ trên heap không được giải phóng",
            "explanation": "C++ không có Garbage Collector tự động thu gom rác như Java/C#. Nếu lớp sở hữu vùng nhớ cấp phát động bằng `new` mà không gọi `delete[]` trong destructor, khi đối tượng bị hủy (ra khỏi scope), vùng nhớ động trên heap vẫn bị chiếm dụng, gây ra hiện tượng rò rỉ bộ nhớ (Memory Leak)."
        },
        {
            "id": "q041",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Bản chất của con trỏ `this` trong một phương thức thành viên không tĩnh của C++ là gì?",
            "options": [
                "Là một con trỏ ngầm định trỏ tới địa chỉ của chính đối tượng đang gọi phương thức đó",
                "Là con trỏ trỏ tới đối tượng cha trong quan hệ kế thừa",
                "Là biến toàn cục lưu trữ số lượng đối tượng đã được khởi tạo",
                "Là con trỏ trỏ tới hàm `main` của chương trình"
            ],
            "answer": "Là một con trỏ ngầm định trỏ tới địa chỉ của chính đối tượng đang gọi phương thức đó",
            "explanation": "Theo Slide 19 Lecture 3, con trỏ `this` là một tham số ẩn truyền vào mọi phương thức thành viên không tĩnh, trỏ trực tiếp đến địa chỉ của đối tượng đang thực thi phương thức (`this->member`)."
        },
        {
            "id": "q042",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Cú pháp khai báo một lớp mẫu (Class Template) nhận 2 kiểu dữ liệu tổng quát trong C++ là gì?",
            "options": [
                "`template <class T1, class T2> class MyClass { ... };`",
                "`class <typename T1, T2> MyClass { ... };`",
                "`template MyClass<class T1, class T2> { ... };`",
                "`interface <T1, T2> class MyClass { ... };`"
            ],
            "answer": "`template <class T1, class T2> class MyClass { ... };`",
            "explanation": "Cú pháp lớp mẫu bắt đầu bằng `template <class T1, class T2>` (hoặc `typename`), sau đó là định nghĩa `class MyClass { ... };` cho phép tạo lớp hoạt động với các kiểu dữ liệu tùy chọn khi khởi tạo."
        },
        {
            "id": "q043",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Khi quá tải toán tử hai ngôi cộng `+` dưới dạng phương thức thành viên: `PhanSo PhanSo::operator+(const PhanSo &b);`, toán hạng bên trái của phép cộng là đối tượng nào?",
            "options": [
                "Chính là đối tượng đang gọi phương thức, được đại diện bởi con trỏ `*this`",
                "Là đối tượng tham số `b` truyền vào",
                "Là một đối tượng tạm thời rỗng được tạo mới trên heap",
                "Là biến toàn cục được định nghĩa trong thư viện `<iostream>`"
            ],
            "answer": "Chính là đối tượng đang gọi phương thức, được đại diện bởi con trỏ `*this`",
            "explanation": "Khi cài đặt toán tử hai ngôi dưới dạng member function, toán hạng bên trái chính là đối tượng đang kích hoạt phương thức (`*this`), và biểu thức `a + b` được biên dịch tương đương lời gọi `a.operator+(b)`."
        },
        {
            "id": "q044",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Tại sao toán tử chèn luồng xuất `<<` (`cout << obj`) bắt buộc phải được quá tải dưới dạng hàm bạn (`friend`) hoặc hàm độc lập thay vì phương thức thành viên của lớp?",
            "options": [
                "Vì toán hạng bên trái là đối tượng của luồng xuất `ostream` (`cout`), không phải là đối tượng của lớp tự định nghĩa",
                "Vì toán tử `<<` là từ khóa cấm không được nạp chồng trong C++",
                "Vì phương thức thành viên không thể trả về kiểu tham chiếu luồng",
                "Vì luồng `cout` được lưu trữ trên thanh ghi của CPU không cho phép lớp truy cập"
            ],
            "answer": "Vì toán hạng bên trái là đối tượng của luồng xuất `ostream` (`cout`), không phải là đối tượng của lớp tự định nghĩa",
            "explanation": "Trong biểu thức `cout << obj`, toán hạng bên trái là `cout` (thuộc lớp `ostream`). Nếu cài đặt dưới dạng member function, ta sẽ phải sửa đổi mã nguồn lớp `ostream` (điều không thể). Do đó bắt buộc phải nạp chồng `<<` dưới dạng hàm tự do/hàm bạn với tham số đầu tiên là `ostream&`."
        },
        {
            "id": "q045",
            "topicId": 3,
            "topicName": "Classes & OOP in C++",
            "question": "Cú pháp chuẩn khai báo hàm bạn quá tải toán tử xuất luồng `<<` cho lớp `PhanSo` là gì?",
            "options": [
                "`friend ostream& operator<<(ostream &os, const PhanSo &p);`",
                "`friend void operator<<(const PhanSo &p, ostream &os);`",
                "`ostream operator<<(PhanSo p);`",
                "`friend istream& operator<<(ostream &os, PhanSo &p);`"
            ],
            "answer": "`friend ostream& operator<<(ostream &os, const PhanSo &p);`",
            "explanation": "Cú pháp chuẩn khai báo trong lớp: `friend ostream& operator<<(ostream &os, const PhanSo &p);`. Trả về tham chiếu `ostream&` cho phép ghép nối toán tử liên tiếp (chaining), ví dụ: `cout << p1 << p2;`."
        },

        # --- Topic 4: Algorithm Analysis & Big-O (q046 - q060) ---
        {
            "id": "q046",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Hai yếu tố tài nguyên chính cần được đánh giá khi phân tích hiệu năng của một thuật toán là gì?",
            "options": [
                "Độ phức tạp thời gian thực thi (Running Time) và Độ phức tạp không gian bộ nhớ (Space Complexity)",
                "Băng thông mạng truyền tải và dung lượng màn hình hiển thị",
                "Số lượng comment giải thích và số dòng thụt lề trong mã nguồn",
                "Nhiệt độ tỏa ra của vi xử lý CPU và điện năng tiêu thụ của nguồn điện"
            ],
            "answer": "Độ phức tạp thời gian thực thi (Running Time) và Độ phức tạp không gian bộ nhớ (Space Complexity)",
            "explanation": "Theo Slide 3-4 Lecture 4, hai tài nguyên cốt lõi cần tối ưu khi đánh giá một thuật toán là: Thời gian thực thi (Running Time - mất bao nhiêu thời gian như hàm theo kích thước n) và Bộ nhớ sử dụng (Space Complexity - tiêu tốn bao nhiêu RAM để lưu trữ dữ liệu)."
        },
        {
            "id": "q047",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Trong phân tích thuật toán, tại sao trường hợp xấu nhất (Worst-case) luôn được ưu tiên phân tích hàng đầu?",
            "options": [
                "Vì nó cung cấp cận trên bảo đảm thuật toán sẽ không bao giờ chạy chậm hơn mức đó trên bất kỳ đầu vào nào",
                "Vì trường hợp xấu nhất luôn xảy ra thường xuyên hơn trường hợp trung bình",
                "Vì trường hợp xấu nhất chỉ xuất hiện khi thuật toán bị lỗi biên dịch",
                "Vì trường hợp xấu nhất luôn có độ phức tạp là hàm hằng số O(1)"
            ],
            "answer": "Vì nó cung cấp cận trên bảo đảm thuật toán sẽ không bao giờ chạy chậm hơn mức đó trên bất kỳ đầu vào nào",
            "explanation": "Theo Slide 5 Lecture 4, Worst-case cung cấp trần giới hạn trên (Upper bound) được đảm bảo tuyệt đối: hệ thống sẽ không bao giờ tốn nhiều thời gian hơn mức phân tích đó, rất quan trọng đối với các hệ thống thời gian thực và kiểm soát rủi ro."
        },
        {
            "id": "q048",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Nhược điểm lớn nhất của phương pháp đánh giá thuật toán bằng thực nghiệm (Experimental Studies) là gì?",
            "options": [
                "Phải viết mã nguồn hoàn chỉnh và kết quả đo phụ thuộc vào phần cứng, hệ điều hành, trình biên dịch cụ thể",
                "Không thể đo được thời gian bằng các hàm đồng hồ trong thư viện",
                "Không áp dụng được cho các thuật toán đệ quy",
                "Chỉ chạy được trên các siêu máy tính máy chủ chuyên dụng"
            ],
            "answer": "Phải viết mã nguồn hoàn chỉnh và kết quả đo phụ thuộc vào phần cứng, hệ điều hành, trình biên dịch cụ thể",
            "explanation": "Theo Slide 7-8 Lecture 4, đánh giá thực nghiệm có hạn chế: phải cài đặt code hoàn chỉnh, chỉ kiểm tra được trên tập hữu hạn các test cases, và kết quả phụ thuộc chặt chẽ vào môi trường phần cứng máy tính chạy thử."
        },
        {
            "id": "q049",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Mô hình máy tính trừu tượng RAM (Random Access Machine) giả định điều gì về thời gian truy xuất ô nhớ?",
            "options": [
                "Mọi truy xuất tới bất kỳ ô nhớ nào đều tiêu tốn một khoảng thời gian hằng số cố định O(1)",
                "Thời gian truy xuất tăng dần tỉ lệ thuận với địa chỉ ô nhớ lớn hay nhỏ",
                "Ô nhớ ở đầu RAM truy xuất nhanh gấp đôi ô nhớ ở cuối RAM",
                "Thời gian truy xuất ô nhớ luôn là hàm số mũ O(2^n)"
            ],
            "answer": "Mọi truy xuất tới bất kỳ ô nhớ nào đều tiêu tốn một khoảng thời gian hằng số cố định O(1)",
            "explanation": "Theo Slide 10 Lecture 4, mô hình máy tính RAM giả định CPU đơn và bộ nhớ ô nhớ không giới hạn; thời gian truy xuất tới bất kỳ ô nhớ nào là ngẫu nhiên và đồng đều, tốn thời gian hằng số O(1)."
        },
        {
            "id": "q050",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Thao tác nào sau đây KHÔNG PHẢI là một phép toán cơ sở (Primitive Operation) trong mô hình tính toán RAM?",
            "options": [
                "Duyệt tìm kiếm một phần tử trong mảng gồm n phần tử chưa có thứ tự",
                "Phép gán giá trị một biến số học: `x = y + 1;`",
                "Phép so sánh hai số nguyên: `if (a > b)`",
                "Truy xuất một phần tử mảng qua chỉ số: `a[i]`"
            ],
            "answer": "Duyệt tìm kiếm một phần tử trong mảng gồm n phần tử chưa có thứ tự",
            "explanation": "Theo Slide 12 Lecture 4, Phép toán cơ sở (Primitive Operation) là các phép tính cấp thấp thực thi trong thời gian hằng số O(1) như: gán, so sánh, truy xuất mảng, gọi hàm, return. Việc duyệt tìm kiếm trên mảng n phần tử tốn thời gian O(n), không phải phép toán cơ sở."
        },
        {
            "id": "q051",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Sắp xếp 6 hàm số sau theo tốc độ tăng trưởng tiệm cận TĂNG DẦN: `n^2, log n, 1, 2^n, n, n log n`?",
            "options": [
                "`1 < log n < n < n log n < n^2 < 2^n`",
                "`1 < n < log n < n log n < n^2 < 2^n`",
                "`log n < 1 < n < n log n < 2^n < n^2`",
                "`1 < log n < n < n^2 < n log n < 2^n`"
            ],
            "answer": "`1 < log n < n < n log n < n^2 < 2^n`",
            "explanation": "Theo Slide 14-16 Lecture 4 về 7 hàm tăng trưởng thông dụng: Hằng số (1) < Logarit (log n) < Tuyến tính (n) < Tuyến tính log (n log n) < Bậc hai (n^2) < Hàm mũ (2^n)."
        },
        {
            "id": "q052",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Định nghĩa toán học hình thức của ký hiệu Ô-lớn: Ta nói hàm $f(n)$ là $O(g(n))$ khi nào?",
            "options": [
                "Tồn tại các hằng số thực dương $c > 0$ và số nguyên $n_0 \\ge 1$ sao cho $f(n) \\le c \\cdot g(n)$ với mọi $n \\ge n_0$",
                "Hàm $f(n)$ luôn luôn bằng đúng $g(n)$ với mọi giá trị $n$",
                "Tồn tại hằng số $c > 0$ sao cho $f(n) \\ge c \\cdot g(n)$ với mọi $n \\ge 1$",
                "Đạo hàm bậc nhất của $f(n)$ nhỏ hơn đạo hàm của $g(n)$ tại mọi điểm"
            ],
            "answer": "Tồn tại các hằng số thực dương $c > 0$ và số nguyên $n_0 \\ge 1$ sao cho $f(n) \\le c \\cdot g(n)$ với mọi $n \\ge n_0$",
            "explanation": "Theo Slide 17 Lecture 4: $f(n) \\text{ is } O(g(n))$ nếu tồn tại hằng số thực $c > 0$ và số nguyên $n_0 \\ge 1$ sao cho với mọi $n \\ge n_0$, ta luôn có $f(n) \\le c \\cdot g(n)$ (cận trên tiệm cận)."
        },
        {
            "id": "q053",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Để chứng minh hàm $f(n) = 3n + 7$ là $O(n)$, ta có thể chọn cặp hằng số $(c, n_0)$ hợp lệ nào sau đây?",
            "options": [
                "$c = 4, n_0 = 7$ (vì khi $n \\ge 7$ thì $3n + 7 \\le 3n + n = 4n$)",
                "$c = 1, n_0 = 1$ (vì $3n + 7 \\le n$)",
                "$c = 2, n_0 = 5$ (vì $3n + 7 \\le 2n$)",
                "$c = 0.5, n_0 = 10$"
            ],
            "answer": "$c = 4, n_0 = 7$ (vì khi $n \\ge 7$ thì $3n + 7 \\le 3n + n = 4n$)",
            "explanation": "Khi $n \\ge 7$, ta có $7 \\le n$, do đó $3n + 7 \\le 3n + n = 4n$. Vậy chọn $c = 4$ và $n_0 = 7$ thỏa mãn định nghĩa $f(n) \\le c \\cdot n$ với mọi $n \\ge n_0$."
        },
        {
            "id": "q054",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Tại sao hàm $f(n) = n^2$ KHÔNG THỂ là $O(n)$?",
            "options": [
                "Vì không tồn tại bất kỳ hằng số $c > 0$ cố định nào để $n^2 \\le c \\cdot n$ (tương đương $n \\le c$) với mọi $n$ lớn tùy ý",
                "Vì hàm $n^2$ luôn cho ra kết quả là số chẵn",
                "Vì $n^2$ không thể tính được khi $n$ âm",
                "Vì đồ thị của $n^2$ là một đường thẳng dốc đứng"
            ],
            "answer": "Vì không tồn tại bất kỳ hằng số $c > 0$ cố định nào để $n^2 \\le c \\cdot n$ (tương đương $n \\le c$) với mọi $n$ lớn tùy ý",
            "explanation": "Theo Slide 21 Lecture 4: Giả sử $n^2 \\le c \\cdot n$, chia cả hai vế cho $n > 0$ ta được $n \\le c$. Tuy nhiên, biến $n$ có thể tiến tới vô cùng lớn, trong khi $c$ là hằng số cố định, điều này mâu thuẫn. Do đó $n^2$ không thể là $O(n)$."
        },
        {
            "id": "q055",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Quy tắc bỏ qua hệ số hằng số trong ký hiệu Big-O có ý nghĩa là gì?",
            "options": [
                "Hằng số nhân không làm thay đổi lớp hàm tăng trưởng tiệm cận, ví dụ $1000n$ vẫn thuộc lớp $O(n)$",
                "Mọi số nguyên trong biểu thức đều phải được thay thế bằng số 0",
                "Chỉ được phép bỏ qua hằng số nếu hằng số đó nhỏ hơn 10",
                "Thuật toán chạy nhanh gấp 1000 lần trên máy tính cá nhân"
            ],
            "answer": "Hằng số nhân không làm thay đổi lớp hàm tăng trưởng tiệm cận, ví dụ $1000n$ vẫn thuộc lớp $O(n)$",
            "explanation": "Theo Slide 22 Lecture 4: Trong phân tích tiệm cận khi $n$ tiến ra vô cùng, các hệ số hằng số nhân không làm thay đổi tốc độ tăng trưởng cơ bản của lớp hàm (ví dụ $cf(n)$ vẫn là $O(f(n))$)."
        },
        {
            "id": "q056",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Cho đa thức thời gian: $f(n) = 5n^3 + 120n^2 + 8000$. Theo quy tắc số hạng bậc cao nhất, $f(n)$ thuộc lớp Big-O nào sau đây?",
            "options": [
                "$O(n^3)$",
                "$O(n^2)$",
                "$O(n^5)$",
                "$O(1)$"
            ],
            "answer": "$O(n^3)$",
            "explanation": "Theo quy tắc đa thức (Slide 22 Lecture 4): Nếu $f(n)$ là đa thức bậc $d$, ta bỏ qua tất cả các số hạng bậc thấp và các hệ số hằng số, chỉ giữ lại số hạng có bậc cao nhất. Bậc cao nhất ở đây là $n^3$, vậy $f(n) \\in O(n^3)$."
        },
        {
            "id": "q057",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Cho chương trình gồm hai khối lệnh tuần tự độc lập: khối 1 tốn thời gian $O(n)$, khối 2 tốn thời gian $O(n^2)$. Theo Quy tắc cộng, tổng thời gian thực thi của cả chương trình là bao nhiêu?",
            "options": [
                "$O(n^2)$",
                "$O(n^3)$",
                "$O(n)$",
                "$O(n + n^2)$"
            ],
            "answer": "$O(n^2)$",
            "explanation": "Theo Quy tắc cộng (Slide 30 Lecture 4): Nếu chương trình gồm các khối tuần tự thực thi độc lập $P_1, P_2$ với độ phức tạp $O(f(n))$ và $O(g(n))$, thì tổng độ phức tạp là $O(\\max(f(n), g(n)))$. Ở đây $\\max(n, n^2) = n^2$, do đó là $O(n^2)$."
        },
        {
            "id": "q058",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Cho đoạn mã gồm 2 vòng lặp lồng nhau: vòng ngoài lặp $n$ lần, vòng trong lặp $n$ lần, bên trong thực hiện phép gán $O(1)$. Theo Quy tắc nhân, độ phức tạp thời gian là bao nhiêu?",
            "options": [
                "$O(n^2)$",
                "$O(2n)$",
                "$O(n)$",
                "$O(n^3)$"
            ],
            "answer": "$O(n^2)$",
            "explanation": "Theo Quy tắc nhân (Slide 30 Lecture 4): Nếu một khối lệnh có độ phức tạp $O(g(n))$ được lồng bên trong một vòng lặp chạy $O(f(n))$ lần, thì tổng thời gian thực hiện là tích $O(f(n) \\times g(n))$. Ở đây $n \\times n = n^2$ nên độ phức tạp là $O(n^2)$."
        },
        {
            "id": "q059",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Trong bài toán tính mảng trung bình cộng tiền tố (Prefix Averages - Slide 26-28), thuật toán cải tiến sử dụng một biến cộng dồn tích lũy đạt độ phức tạp thời gian là bao nhiêu so với cách ngây thơ hai vòng lặp?",
            "options": [
                "$O(n)$ so với $O(n^2)$",
                "$O(\\log n)$ so với $O(n)$",
                "$O(n \\log n)$ so với $O(n^3)$",
                "$O(1)$ so với $O(n)$"
            ],
            "answer": "$O(n)$ so với $O(n^2)$",
            "explanation": "Thuật toán 1 dùng 2 vòng lặp lồng nhau tính lại tổng từ đầu ở mỗi chỉ số $i$ tốn $O(n^2)$ phép toán. Thuật toán 2 tận dụng biến tích lũy $s = s + X[i]$ chỉ cần 1 vòng lặp duy nhất, giảm độ phức tạp thời gian xuống còn $O(n)$ tuyến tính."
        },
        {
            "id": "q060",
            "topicId": 4,
            "topicName": "Algorithm Analysis & Big-O",
            "question": "Nguyên tắc chọn cận trên chặt nhất (Tightest Upper Bound) trong phân tích Big-O yêu cầu điều gì?",
            "options": [
                "Nên chọn lớp hàm tăng trưởng nhỏ nhất và đơn giản nhất mô tả sát thực tế (ví dụ: phát biểu $2n$ là $O(n)$ thay vì $O(n^2)$)",
                "Luôn chọn hàm số mũ $O(2^n)$ cho an toàn tuyệt đối",
                "Bắt buộc phải nhân đôi giá trị hàm để tránh sai số đo đạc",
                "Không được sử dụng ký hiệu logarit trong bất kỳ trường hợp nào"
            ],
            "answer": "Nên chọn lớp hàm tăng trưởng nhỏ nhất và đơn giản nhất mô tả sát thực tế (ví dụ: phát biểu $2n$ là $O(n)$ thay vì $O(n^2)$)",
            "explanation": "Theo Slide 23 Lecture 4: Dù về mặt toán học hàm tuyến tính $2n$ cũng thuộc $O(n^2)$, nhưng trong khoa học máy tính chuẩn tắc ta luôn chọn cận trên chặt chẽ nhất (tightest bound) là $O(n)$ để phản ánh chính xác hiệu năng thực tế của thuật toán."
        },

        # --- Topic 5: Recursion (q061 - q075) ---
        {
            "id": "q061",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Khái niệm Hàm đệ quy (Recursive Function) trong lập trình được định nghĩa là gì?",
            "options": [
                "Là một hàm tự gọi lại chính nó trực tiếp hoặc gián tiếp để giải quyết bài toán con có quy mô nhỏ hơn",
                "Là một hàm được gọi lặp đi lặp lại bên trong một vòng lặp `while(true)`",
                "Là một hàm chỉ có thể chạy được một lần duy nhất khi chương trình khởi động",
                "Là một hàm không chứa bất kỳ câu lệnh `return` nào"
            ],
            "answer": "Là một hàm tự gọi lại chính nó trực tiếp hoặc gián tiếp để giải quyết bài toán con có quy mô nhỏ hơn",
            "explanation": "Theo Slide 2-3 Lecture 5, Đệ quy (Recursion) xảy ra khi một hàm tự gọi lại chính nó (trực tiếp hoặc thông qua một hàm khác) nhằm chia bài toán ban đầu thành các bài toán con cùng cấu trúc nhưng kích thước nhỏ hơn."
        },
        {
            "id": "q062",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Hai thành phần cốt lõi bắt buộc phải có trong bất kỳ một giải thuật đệ quy đúng đắn nào là gì?",
            "options": [
                "Trường hợp cơ sở (Base case) và Bước đệ quy (Recursive step)",
                "Hàm khởi tạo (Constructor) và Hàm hủy (Destructor)",
                "Vòng lặp `for` và Vòng lặp `while`",
                "Khối `try` và Khối `catch`"
            ],
            "answer": "Trường hợp cơ sở (Base case) và Bước đệ quy (Recursive step)",
            "explanation": "Một hàm đệ quy hợp lệ bắt buộc gồm 2 phần: Base case (điều kiện dừng trực tiếp không cần gọi đệ quy tiếp) và Recursive step (lời gọi hàm thu hẹp quy mô bài toán tiến dần về base case)."
        },
        {
            "id": "q063",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Hiện tượng Tràn ngăn xếp (Stack Overflow Error) trong chương trình đệ quy nguyên nhân chủ yếu do đâu?",
            "options": [
                "Do đệ quy vô hạn vì thiếu điều kiện dừng (Base case) hoặc tham số không tiến về điều kiện dừng, làm cạn kiệt bộ nhớ Call Stack",
                "Do RAM máy tính bị mất điện đột ngột",
                "Do chương trình sử dụng quá nhiều câu lệnh `cout` xuất ra màn hình",
                "Do file mã nguồn C++ có dung lượng quá lớn"
            ],
            "answer": "Do đệ quy vô hạn vì thiếu điều kiện dừng (Base case) hoặc tham số không tiến về điều kiện dừng, làm cạn kiệt bộ nhớ Call Stack",
            "explanation": "Mỗi lần gọi hàm đệ quy, một khung ngăn xếp (Stack Frame) được cấp phát trên Call Stack. Nếu thiếu điều kiện dừng hoặc điều kiện dừng không bao giờ đạt tới, hàm tự gọi vô tận khiến Call Stack bị đầy tràn, gây lỗi Crash / Stack Overflow."
        },
        {
            "id": "q064",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Mỗi khi một hàm đệ quy được gọi, hệ thống lưu trữ những thông tin gì trong một Khung ngăn xếp (Stack Frame) trên Call Stack?",
            "options": [
                "Các biến cục bộ, giá trị tham số truyền vào, và địa chỉ lệnh hồi quy (Return address)",
                "Toàn bộ mã nguồn C++ dưới dạng văn bản ASCII",
                "Kích thước file thực thi `.exe` trên ổ cứng",
                "Mật khẩu tài khoản người dùng đang đăng nhập"
            ],
            "answer": "Các biến cục bộ, giá trị tham số truyền vào, và địa chỉ lệnh hồi quy (Return address)",
            "explanation": "Mỗi Stack Frame (Activation Record) lưu giữ: các tham số hàm được truyền vào, các biến cục bộ khai báo trong hàm, và địa chỉ lệnh quay về (return address) để CPU tiếp tục thực thi sau khi hàm con hoàn tất."
        },
        {
            "id": "q065",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Khái niệm Đệ quy tuyến tính (Linear Recursion) có đặc điểm nổi bật nào sau đây?",
            "options": [
                "Trong mỗi lần thực thi hàm, chỉ có tối đa duy nhất một lời gọi đệ quy được kích hoạt",
                "Hàm chứa ít nhất hai lời gọi đệ quy rẽ nhánh độc lập",
                "Thời gian chạy của hàm bắt buộc phải là hằng số O(1)",
                "Hàm chỉ được phép nhận đối số là các số nguyên dương lẻ"
            ],
            "answer": "Trong mỗi lần thực thi hàm, chỉ có tối đa duy nhất một lời gọi đệ quy được kích hoạt",
            "explanation": "Theo Slide 8 Lecture 5, Đệ quy tuyến tính (Linear Recursion) là dạng đệ quy mà mỗi bước thực thi chỉ gọi đệ quy tối đa đúng một lần (ví dụ: hàm tính giai thừa n!, duyệt mảng tuyến tính)."
        },
        {
            "id": "q066",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Cho hàm: `int fact(int n) { if (n <= 1) return 1; return n * fact(n - 1); }`. Độ phức tạp thời gian và không gian ngăn xếp của hàm khi tính `fact(n)` là bao nhiêu?",
            "options": [
                "Thời gian $O(n)$ và không gian bộ nhớ ngăn xếp $O(n)$",
                "Thời gian $O(n^2)$ và không gian $O(1)$",
                "Thời gian $O(\\log n)$ và không gian $O(\\log n)$",
                "Thời gian $O(1)$ và không gian $O(n)$"
            ],
            "answer": "Thời gian $O(n)$ và không gian bộ nhớ ngăn xếp $O(n)$",
            "explanation": "Hàm thực hiện $n$ lần gọi đệ quy, mỗi lần tốn $O(1)$ phép nhân $\\implies$ thời gian $O(n)$. Do Call Stack phải lưu $n$ khung ngăn xếp lồng nhau cho tới khi chạm base case $\\implies$ không gian bộ nhớ ngăn xếp là $O(n)$."
        },
        {
            "id": "q067",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Trong bài toán đảo ngược mảng bằng đệ quy `ReverseArray(A, i, j)` (Slide 13 Lecture 5), tại sao lại thiết kế bổ sung hai tham số chỉ số $i$ và $j$?",
            "options": [
                "Để thu hẹp phạm vi đoạn mảng cần đảo qua mỗi bước đệ quy ($i+1, j-1$) mà không cần tạo mảng mới",
                "Để đếm số lần đảo ngược đã thực hiện trong chương trình",
                "Vì ngôn ngữ C++ không cho phép truyền mảng vào hàm nếu không có 2 chỉ số",
                "Để hoán đổi kiểu dữ liệu của các phần tử trong mảng"
            ],
            "answer": "Để thu hẹp phạm vi đoạn mảng cần đảo qua mỗi bước đệ quy ($i+1, j-1$) mà không cần tạo mảng mới",
            "explanation": "Theo Slide 13 Lecture 5, việc bổ sung tham số phạm vi ($i, j$) là kỹ thuật thiết kế đệ quy kinh điển trên mảng: hoán đổi $A[i]$ và $A[j]$, sau đó gọi đệ quy với đoạn con thu hẹp `ReverseArray(A, i + 1, j - 1)` cho đến khi $i \\ge j$."
        },
        {
            "id": "q068",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Thuật toán tính tổng mảng `LinearSum(A, n)` bằng cách đệ quy `LinearSum(A, n - 1) + A[n - 1]` có độ phức tạp thời gian là bao nhiêu?",
            "options": [
                "$O(n)$",
                "$O(n^2)$",
                "$O(\\log n)$",
                "$O(1)$"
            ],
            "answer": "$O(n)$",
            "explanation": "Hàm gọi đệ quy $n$ lần cho $n$ phần tử, mỗi bước chỉ thực hiện một phép cộng hằng số $O(1)$, do đó tổng thời gian thực thi là $O(n)$."
        },
        {
            "id": "q069",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Thuật toán tính lũy thừa nhanh (Repeated Squaring) $p(x, n) = x^n$ bằng cách chia đôi số mũ có độ phức tạp thời gian là bao nhiêu?",
            "options": [
                "$O(\\log n)$",
                "$O(n)$",
                "$O(n^2)$",
                "$O(n \\log n)$"
            ],
            "answer": "$O(\\log n)$",
            "explanation": "Theo Slide 15-18 Lecture 5, phương pháp chia đôi số mũ (Repeated Squaring): nếu $n$ chẵn $x^n = (x^{n/2})^2$, nếu $n$ lẻ $x^n = x \\cdot (x^{(n-1)/2})^2$. Số mũ giảm đi một nửa qua mỗi bước đệ quy nên số bước tính là $\\log_2 n$, đạt độ phức tạp $O(\\log n)$."
        },
        {
            "id": "q070",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Trong thuật toán lũy thừa nhanh đệ quy, tại sao cần lưu kết quả vào biến tạm `y = Power(x, n/2)` trước khi nhân?",
            "options": [
                "Để tránh việc gọi lại hàm đệ quy 2 lần riêng biệt làm bùng nổ độ phức tạp lên hàm tuyến tính",
                "Để ép kiểu dữ liệu từ số nguyên sang số thực",
                "Vì trình biên dịch C++ bắt buộc phải dùng biến y",
                "Để xóa giá trị x khỏi bộ nhớ sau khi tính toán"
            ],
            "answer": "Để tránh việc gọi lại hàm đệ quy 2 lần riêng biệt làm bùng nổ độ phức tạp lên hàm tuyến tính",
            "explanation": "Nếu viết `Power(x, n/2) * Power(x, n/2)`, hàm đệ quy sẽ bị gọi 2 lần cho cùng một giá trị, làm cây đệ quy nhân đôi và mất đi lợi thế $O(\\log n)$. Bằng cách gán vào biến tạm `y`, hàm chỉ gọi đúng 1 lần cho mỗi cấp số mũ."
        },
        {
            "id": "q071",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Khái niệm Đệ quy nhị phân (Binary Recursion) được định nghĩa là gì?",
            "options": [
                "Là hàm mà trong thân của nó thực hiện hai lời gọi đệ quy độc lập với nhau",
                "Là hàm chỉ nhận dữ liệu đầu vào là các bit nhị phân 0 và 1",
                "Là hàm chỉ gọi đệ quy khi chỉ số mảng là số chẵn",
                "Là hàm đệ quy bắt buộc phải trả về kiểu boolean"
            ],
            "answer": "Là hàm mà trong thân của nó thực hiện hai lời gọi đệ quy độc lập với nhau",
            "explanation": "Theo Slide 19 Lecture 5, Đệ quy nhị phân (Binary Recursion) là trường hợp hàm thực hiện hai lời gọi đệ quy riêng biệt để giải quyết hai nửa bài toán (ví dụ: vẽ thước đo inch, duyệt cây nhị phân, MergeSort)."
        },
        {
            "id": "q072",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Thuật toán vẽ thước đo inch (English Ruler) trong bài giảng áp dụng dạng đệ quy nào?",
            "options": [
                "Đệ quy nhị phân (hàm `drawticks` gọi đệ quy 2 lần với chiều dài vạch giảm đi 1)",
                "Đệ quy tuyến tính 1 lần",
                "Đệ quy đuôi (Tail recursion)",
                "Không sử dụng đệ quy mà dùng vòng lặp lồng nhau"
            ],
            "answer": "Đệ quy nhị phân (hàm `drawticks` gọi đệ quy 2 lần với chiều dài vạch giảm đi 1)",
            "explanation": "Theo Slide 20-21 Lecture 5, thuật toán vẽ vạch thước inch `drawticks(k)` gọi `drawticks(k - 1)` để vẽ nửa trên, vẽ vạch giữa độ dài $k$, rồi lại gọi `drawticks(k - 1)` để vẽ nửa dưới, là cấu trúc đệ quy nhị phân kinh điển."
        },
        {
            "id": "q073",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Hàm tính số Fibonacci đệ quy ngây thơ: `int fib(int n) { if (n <= 1) return n; return fib(n-1) + fib(n-2); }` có độ phức tạp thời gian là bao nhiêu?",
            "options": [
                "$O(2^n)$ (thời gian hàm mũ)",
                "$O(n)$ (thời gian tuyến tính)",
                "$O(\\log n)$ (thời gian logarit)",
                "$O(n^2)$ (thời gian bậc hai)"
            ],
            "answer": "$O(2^n)$ (thời gian hàm mũ)",
            "explanation": "Theo Slide 24 Lecture 5, hàm Fibonacci đệ quy 2 nhánh ngây thơ dẫn đến cây đệ quy bùng nổ kích thước hàm mũ $O(2^n)$. Rất nhiều bài toán con như `fib(n-2)`, `fib(n-3)` bị tính đi tính lại hàng ngàn lần một cách lãng phí."
        },
        {
            "id": "q074",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Thuật toán `LinearFibonacci(k)` (Slide 25 Lecture 5) tối ưu hóa việc tính số Fibonacci như thế nào so với đệ quy ngây thơ?",
            "options": [
                "Trả về một cặp số $(F_k, F_{k-1})$ qua đệ quy tuyến tính giúp giảm thời gian chạy xuống $O(k)$",
                "Chuyển đổi hoàn toàn sang tính bằng bảng lượng giác",
                "Bỏ qua các số Fibonacci lẻ để chỉ tính số chẵn",
                "Dùng con trỏ mảng tĩnh để lưu trữ trước vô hạn số Fibonacci"
            ],
            "answer": "Trả về một cặp số $(F_k, F_{k-1})$ qua đệ quy tuyến tính giúp giảm thời gian chạy xuống $O(k)$",
            "explanation": "Theo Slide 25 Lecture 5, `LinearFibonacci(k)` sử dụng đệ quy tuyến tính trả về cặp 2 số liền kề $(F_k, F_{k-1})$. Mỗi bước chỉ gọi đệ quy 1 lần, giúp triệt tiêu việc tính toán trùng lặp và giảm thời gian từ $O(2^k)$ xuống còn $O(k)$ tuyến tính."
        },
        {
            "id": "q075",
            "topicId": 5,
            "topicName": "Recursion",
            "question": "Thuật toán tính tổng mảng `BinarySum(A, i, n)` chia mảng thành hai nửa và cộng kết quả đệ quy của hai nửa có chiều sâu ngăn xếp Call Stack tối đa là bao nhiêu?",
            "options": [
                "$O(\\log n)$",
                "$O(n)$",
                "$O(n^2)$",
                "$O(1)$"
            ],
            "answer": "$O(\\log n)$",
            "explanation": "Theo Slide 22 Lecture 5, khi chia đôi mảng đều đặn qua mỗi bước đệ quy nhị phân, cây đệ quy có chiều sâu là $\\lceil \\log_2 n \\rceil$. Do đó độ sâu tối đa của Call Stack tại một thời điểm chỉ là $O(\\log n)$ thay vì $O(n)$ như `LinearSum`."
        }
    ]
    return questions
