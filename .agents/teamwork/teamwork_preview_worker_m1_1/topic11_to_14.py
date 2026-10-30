# -*- coding: utf-8 -*-
"""
Questions for Topics 11 to 14 (q151 - q210).
Topic 11: Sorting O(n^2) (Bubble, Selection, Insertion) (q151 - q165)
Topic 12: Sorting O(n log n) (Merge, Quick, Heap) (q166 - q180)
Topic 13: Search Algorithms (Linear, Binary, BST) (q181 - q195)
Topic 14: Hash Tables (Hashing, Collisions, Chaining, Open Addressing) (q196 - q210)
"""

def get_topics_11_to_14():
    questions = [
        # --- Topic 11: Sorting O(n^2) (q151 - q165) ---
        {
            "id": "q151",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Ý tưởng cốt lõi của thuật toán Sắp xếp nổi bọt (Bubble Sort) là gì?",
            "options": [
                "Liên tục so sánh các cặp phần tử liền kề và tráo đổi nếu chúng sai thứ tự để đưa phần tử nhỏ nhất nổi dần về đầu mảng",
                "Tìm phần tử nhỏ nhất trong toàn bộ mảng và đưa ngay về vị trí đầu tiên sau một bước",
                "Chia đôi mảng thành hai nửa bằng nhau rồi trộn lại bằng mảng phụ",
                "Xây dựng cây nhị phân đống rồi trích xuất phần tử lớn nhất ở gốc"
            ],
            "answer": "Liên tục so sánh các cặp phần tử liền kề và tráo đổi nếu chúng sai thứ tự để đưa phần tử nhỏ nhất nổi dần về đầu mảng",
            "explanation": "Theo Slide 4-5 Lecture 11, Bubble Sort duyệt qua các cặp phần tử kề nhau từ cuối dãy về đầu (hoặc từ đầu về cuối). Nếu cặp phần tử sai thứ tự thì hoán đổi (swap), làm cho các phần tử nhẹ hơn (nhỏ hơn) \"nổi bọt\" dần về đúng vị trí phía trước."
        },
        {
            "id": "q152",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Trong thuật toán Bubble Sort tăng dần phiên bản cơ bản chưa tối ưu, tổng số phép so sánh khóa trên mảng gồm $n$ phần tử luôn cố định bằng bao nhiêu trong mọi trường hợp?",
            "options": [
                "$\\frac{n(n-1)}{2}$",
                "$n - 1$",
                "$n^2$",
                "$n \\log_2 n$"
            ],
            "answer": "$\\frac{n(n-1)}{2}$",
            "explanation": "Theo Slide 6 Lecture 11: Vòng ngoài lặp $n-1$ lần ($i=0 \\dots n-2$). Vòng trong thực hiện $n-1-i$ phép so sánh. Tổng số phép so sánh là cấp số cộng $(n-1) + (n-2) + ... + 1 = \\frac{n(n-1)}{2} = O(n^2)$."
        },
        {
            "id": "q153",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Kỹ thuật tối ưu hóa Bubble Sort bằng cờ hiệu `swapped` giúp cải thiện thời gian chạy trong trường hợp tốt nhất (mảng đã có thứ tự sẵn) thành bao nhiêu?",
            "options": [
                "$O(n)$",
                "$O(1)$",
                "$O(n \\log n)$",
                "$O(n^2)$"
            ],
            "answer": "$O(n)$",
            "explanation": "Nếu sau một lượt quét đầu tiên mà không có bất kỳ cặp phần tử nào bị tráo đổi (`swapped == false`), thuật toán nhận biết mảng đã hoàn toàn có thứ tự và dừng ngay lập tức. Khi đó chỉ tốn $n-1$ phép so sánh, đạt thời gian tốt nhất là $O(n)$."
        },
        {
            "id": "q154",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Phát biểu nào sau đây đúng về tính ổn định (Stability) và không gian bộ nhớ phụ của thuật toán Bubble Sort?",
            "options": [
                "Là thuật toán sắp xếp ổn định (Stable) và sắp xếp tại chỗ ($O(1)$ bộ nhớ phụ)",
                "Là thuật toán không ổn định và đòi hỏi $O(n)$ bộ nhớ phụ",
                "Là thuật toán ổn định nhưng đòi hỏi $O(n)$ mảng phụ",
                "Là thuật toán không ổn định nhưng sắp xếp tại chỗ"
            ],
            "answer": "Là thuật toán sắp xếp ổn định (Stable) và sắp xếp tại chỗ ($O(1)$ bộ nhớ phụ)",
            "explanation": "Bubble Sort chỉ hoán đổi hai phần tử kề nhau khi $A[j] < A[j-1]$. Nếu hai phần tử bằng nhau, nó không hoán đổi nên giữ nguyên thứ tự tương đối ban đầu $\\implies$ Ổn định (Stable). Thuật toán chỉ dùng biến tạm để swap $\\implies$ Sắp xếp tại chỗ ($O(1)$ space)."
        },
        {
            "id": "q155",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Cho mảng số nguyên: `A = [5, 1, 4, 2, 8]`. Thực hiện thuật toán Bubble Sort nổi phần tử nhỏ nhất từ cuối mảng về đầu theo mã giả slide bài giảng. Sau khi kết thúc lượt lặp ngoài đầu tiên ($i = 0$), trạng thái của mảng là gì?",
            "options": [
                "`[1, 5, 2, 4, 8]`",
                "`[1, 2, 4, 5, 8]`",
                "`[5, 1, 2, 4, 8]`",
                "`[1, 4, 2, 5, 8]`"
            ],
            "answer": "`[1, 5, 2, 4, 8]`",
            "explanation": "Truy vết Bubble Sort duyệt từ $j = 4$ về $1$:\n- So sánh $A[4]=8, A[3]=2 \\implies$ giữ nguyên\n- So sánh $A[3]=2, A[2]=4 \\implies$ swap $\\implies [5, 1, 2, 4, 8]$\n- So sánh $A[2]=2, A[1]=1 \\implies$ giữ nguyên\n- So sánh $A[1]=1, A[0]=5 \\implies$ swap $\\implies [1, 5, 2, 4, 8]$.\nPhần tử nhỏ nhất 1 đã nổi về vị trí $A[0]$."
        },
        {
            "id": "q156",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Ý tưởng cốt lõi của thuật toán Sắp xếp chọn (Selection Sort) là gì?",
            "options": [
                "Tại mỗi bước $i$, tìm phần tử có khóa nhỏ nhất trong đoạn chưa sắp từ $i$ đến $n-1$ và tráo đổi với phần tử $A[i]$",
                "Chèn lần lượt từng phần tử vào một cây nhị phân tìm kiếm",
                "Liên tục chia mảng làm đôi cho tới khi mỗi đoạn chỉ còn 1 phần tử",
                "So sánh các phần tử cách nhau một khoảng bước nhảy giảm dần (Shell sort)"
            ],
            "answer": "Tại mỗi bước $i$, tìm phần tử có khóa nhỏ nhất trong đoạn chưa sắp từ $i$ đến $n-1$ và tráo đổi với phần tử $A[i]$",
            "explanation": "Theo Slide 8-9 Lecture 11, Selection Sort chia mảng thành 2 phần: đoạn đã sắp $A[0..i-1]$ và đoạn chưa sắp $A[i..n-1]$. Ở bước $i$, tìm vị trí `posmin` có giá trị nhỏ nhất trong đoạn chưa sắp, rồi tráo đổi $A[i]$ với $A[posmin]$."
        },
        {
            "id": "q157",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Ưu điểm nổi bật nhất của Selection Sort so với Bubble Sort và Insertion Sort là gì?",
            "options": [
                "Số phép tráo đổi (Swap) dữ liệu là ít nhất, tối đa chỉ thực hiện đúng $n-1$ lần swap trong suốt quá trình chạy",
                "Tốc độ so sánh khóa nhanh gấp 10 lần các thuật toán khác",
                "Có khả năng sắp xếp mảng vô hạn phần tử",
                "Hoàn toàn không cần so sánh khóa các phần tử"
            ],
            "answer": "Số phép tráo đổi (Swap) dữ liệu là ít nhất, tối đa chỉ thực hiện đúng $n-1$ lần swap trong suốt quá trình chạy",
            "explanation": "Trong Selection Sort, mỗi lượt lặp ngoài chỉ thực hiện tối đa đúng 1 lần swap (khi `posmin != i`). Tổng số lần swap trên toàn bộ mảng tối đa là $n-1$. Đây là ưu thế lớn khi kích thước bản ghi phần tử rất lớn và chi phí sao chép/swap đắt đỏ."
        },
        {
            "id": "q158",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Thuật toán Selection Sort có tính ổn định (Stability) hay không, và tại sao?",
            "options": [
                "Không ổn định (Unstable), vì phép tráo đổi các phần tử ở khoảng cách xa có thể làm đảo lộn thứ tự tương đối ban đầu của các phần tử có cùng giá trị",
                "Có tính ổn định tuyệt đối trong mọi trường hợp",
                "Chỉ ổn định khi sắp xếp mảng số thực",
                "Chỉ ổn định khi số phần tử n là số chẵn"
            ],
            "answer": "Không ổn định (Unstable), vì phép tráo đổi các phần tử ở khoảng cách xa có thể làm đảo lộn thứ tự tương đối ban đầu của các phần tử có cùng giá trị",
            "explanation": "Selection Sort là thuật toán không ổn định (Unstable). Ví dụ với dãy `[5a, 5b, 2]`, phần tử nhỏ nhất là 2 sẽ tráo đổi với vị trí đầu tiên là `5a`, tạo ra dãy `[2, 5b, 5a]`. Thứ tự ban đầu của `5a` đứng trước `5b` đã bị đảo lộn."
        },
        {
            "id": "q159",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Độ phức tạp thời gian của Selection Sort trong trường hợp tốt nhất (mảng đã được sắp xếp sẵn từ trước) là bao nhiêu?",
            "options": [
                "$O(n^2)$ vì vẫn phải duyệt qua tất cả các phần tử còn lại để tìm giá trị nhỏ nhất",
                "$O(n)$ vì mảng đã có thứ tự",
                "$O(\\log n)$",
                "$O(1)$"
            ],
            "answer": "$O(n^2)$ vì vẫn phải duyệt qua tất cả các phần tử còn lại để tìm giá trị nhỏ nhất",
            "explanation": "Dù mảng đã sắp xếp sẵn, Selection Sort vẫn không thể phát hiện dừng sớm mà vẫn phải chạy đủ 2 vòng lặp để tìm giá trị nhỏ nhất trong đoạn còn lại. Số phép so sánh luôn là $\\frac{n(n-1)}{2}$, do đó thời gian trong mọi trường hợp đều là $\\Theta(n^2)$."
        },
        {
            "id": "q160",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Ý tưởng cốt lõi của thuật toán Sắp xếp chèn (Insertion Sort) là gì?",
            "options": [
                "Giả sử đoạn $A[0..i-1]$ đã có thứ tự, tìm vị trí thích hợp trong đoạn này để chèn phần tử $A[i]$ bằng cách dịch chuyển các phần tử lớn hơn sang phải",
                "Chèn một phần tử ngẫu nhiên vào giữa mảng rồi hoán đổi hai đầu",
                "Chọn một phần tử chốt pivot rồi phân hoạch mảng thành hai nửa",
                "Trộn hai mảng con đã sắp xếp vào một mảng phụ"
            ],
            "answer": "Giả sử đoạn $A[0..i-1]$ đã có thứ tự, tìm vị trí thích hợp trong đoạn này để chèn phần tử $A[i]$ bằng cách dịch chuyển các phần tử lớn hơn sang phải",
            "explanation": "Theo Slide 12-13 Lecture 11, Insertion Sort tương tự cách xếp bài tây trên tay: coi đoạn đầu đã sắp, lấy lá bài tiếp theo $A[i]$, duyệt lùi dịch các lá bài lớn hơn sang phải một vị trí để tạo khoảng trống chèn $A[i]$ vào đúng vị trí."
        },
        {
            "id": "q161",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Độ phức tạp thời gian của Insertion Sort trong trường hợp tốt nhất (Best-case: mảng đã được sắp xếp tăng dần từ trước) là bao nhiêu?",
            "options": [
                "$O(n)$ vì vòng lặp `while` dịch phần tử dừng ngay sau 1 lần so sánh ở mỗi bước $i$",
                "$O(n^2)$",
                "$O(1)$",
                "$O(n \\log n)$"
            ],
            "answer": "$O(n)$ vì vòng lặp `while` dịch phần tử dừng ngay sau 1 lần so sánh ở mỗi bước $i$",
            "explanation": "Khi mảng đã tăng dần sẵn, ở mỗi bước $i$, phần tử $A[i] > A[i-1]$ nên điều kiện vòng lặp `while` bị sai ngay lập tức mà không dịch chuyển phần tử nào. Thuật toán chỉ thực hiện đúng $n-1$ phép so sánh, đạt thời gian tuyến tính $O(n)$."
        },
        {
            "id": "q162",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Trong trường hợp mảng ban đầu có thứ tự giảm dần ngược lại hoàn toàn, độ phức tạp thời gian của Insertion Sort là bao nhiêu?",
            "options": [
                "$O(n^2)$",
                "$O(n)$",
                "$O(n \\log n)$",
                "$O(n^3)$"
            ],
            "answer": "$O(n^2)$",
            "explanation": "Khi mảng giảm dần hoàn toàn (trường hợp xấu nhất), mỗi phần tử $A[i]$ nhỏ hơn tất cả $i$ phần tử đứng trước nó, nên phải so sánh và dịch chuyển toàn bộ $i$ phần tử. Tổng số phép toán là $\\sum_{i=1}^{n-1} i = \\frac{n(n-1)}{2} = O(n^2)$."
        },
        {
            "id": "q163",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Thuật toán Insertion Sort có đặc điểm nào nổi trội sau đây?",
            "options": [
                "Là thuật toán ổn định (Stable) và có tính thích ứng rất cao (chạy cực nhanh gần $O(n)$ khi mảng gần như đã có thứ tự sẵn)",
                "Không ổn định và không thể chạy trên mảng nhỏ",
                "Đòi hỏi bộ nhớ phụ bằng kích thước mảng ban đầu",
                "Luôn chạy chậm hơn Bubble Sort trong mọi tình huống"
            ],
            "answer": "Là thuật toán ổn định (Stable) và có tính thích ứng rất cao (chạy cực nhanh gần $O(n)$ khi mảng gần như đã có thứ tự sẵn)",
            "explanation": "Insertion Sort là thuật toán ổn định (Stable) và có tính thích ứng (Adaptive): khi mảng gần như đã sắp xếp, số phép dịch chuyển rất ít, thời gian chạy tiệm cận $O(n)$. Do đó trong thực tế nó thường được dùng để sắp xếp các đoạn con nhỏ trong QuickSort/Timsort."
        },
        {
            "id": "q164",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "Trong mã giả Insertion Sort sắp xếp tăng dần, điều kiện lặp của vòng `while` để dịch chuyển các phần tử sang phải là gì?",
            "options": [
                "`(j >= 0) and (A[j].Key > x.Key)`",
                "`(j > 0) and (A[j].Key < x.Key)`",
                "`(j < n) and (A[j].Key == x.Key)`",
                "`(j >= 0) or (A[j].Key > x.Key)`"
            ],
            "answer": "`(j >= 0) and (A[j].Key > x.Key)`",
            "explanation": "Theo Slide 14 Lecture 11: Vòng lặp duyệt lùi từ $j = i - 1$ về 0. Điều kiện tiếp tục dịch chuyển là chưa vượt quá đầu mảng (`j >= 0`) VÀ phần tử đang xét lớn hơn giá trị cần chèn (`A[j].Key > x.Key`). Khi dừng lại, ta chèn $x$ vào `A[j + 1]`."
        },
        {
            "id": "q165",
            "topicId": 11,
            "topicName": "Sorting O(n^2)",
            "question": "So sánh nào sau đây là chính xác về Tính ổn định (Stability) và Bộ nhớ phụ của 3 thuật toán sắp xếp $O(n^2)$?",
            "options": [
                "Bubble Sort (Ổn định, $O(1)$ phụ); Selection Sort (Không ổn định, $O(1)$ phụ); Insertion Sort (Ổn định, $O(1)$ phụ)",
                "Cả ba thuật toán đều là không ổn định và tốn $O(n)$ bộ nhớ phụ",
                "Bubble Sort (Không ổn định); Selection Sort (Ổn định); Insertion Sort (Ổn định)",
                "Cả ba thuật toán đều ổn định và đều tốn $O(1)$ bộ nhớ phụ"
            ],
            "answer": "Bubble Sort (Ổn định, $O(1)$ phụ); Selection Sort (Không ổn định, $O(1)$ phụ); Insertion Sort (Ổn định, $O(1)$ phụ)",
            "explanation": "Cả ba thuật toán đều là sắp xếp tại chỗ (in-place) với chi phí bộ nhớ phụ $O(1)$. Về tính ổn định: Bubble Sort và Insertion Sort bảo toàn thứ tự ban đầu của các phần tử bằng nhau (Ổn định - Stable); trong khi Selection Sort có thể hoán đổi nhảy cóc làm đảo lộn thứ tự (Không ổn định - Unstable)."
        },

        # --- Topic 12: Sorting O(n log n) (q166 - q180) ---
        {
            "id": "q166",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Thuật toán Sắp xếp nhanh (Quick Sort) áp dụng phương pháp thiết kế giải thuật nào sau đây?",
            "options": [
                "Chia và trị (Divide and Conquer)",
                "Quy hoạch động (Dynamic Programming)",
                "Thuật toán tham lam (Greedy Algorithm)",
                "Tìm kiếm nhánh cận (Branch and Bound)"
            ],
            "answer": "Chia và trị (Divide and Conquer)",
            "explanation": "Theo Slide 4 Lecture 12, Quick Sort áp dụng mô hình Chia và trị (Divide and Conquer): phân hoạch dãy thành các bài toán con độc lập dựa trên phần tử chốt, sau đó gọi đệ quy sắp xếp từng bài toán con."
        },
        {
            "id": "q167",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Trong thuật toán Quick Sort, phần tử được chọn làm mốc để phân hoạch dãy thành các phần tử nhỏ hơn và lớn hơn được gọi là gì?",
            "options": [
                "Chốt (Pivot)",
                "Nút gốc (Root)",
                "Nút canh gác (Sentinel)",
                "Phần tử trung vị lý thuyết (Median)"
            ],
            "answer": "Chốt (Pivot)",
            "explanation": "Theo Slide 5 Lecture 12, phần tử chốt (Pivot) là phần tử được chọn từ dãy ban đầu, dùng để chia mảng thành 3 phần: các phần tử nhỏ hơn hoặc bằng chốt ($S_1$), chính phần tử chốt ($S_2$), và các phần tử lớn hơn chốt ($S_3$)."
        },
        {
            "id": "q168",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Vị trí của phần tử chốt (Pivot) sau khi hoàn thành thủ tục Phân hoạch (Partition) trong Quick Sort có tính chất gì?",
            "options": [
                "Đã nằm ở vị trí chính xác cuối cùng của nó trong mảng khi đã sắp xếp hoàn chỉnh",
                "Luôn nằm ở vị trí chính giữa mảng $n/2$",
                "Luôn bị đưa về vị trí đầu mảng chỉ số 0",
                "Vị trí của chốt vẫn có thể bị xáo trộn ở các bước đệ quy tiếp theo"
            ],
            "answer": "Đã nằm ở vị trí chính xác cuối cùng của nó trong mảng khi đã sắp xếp hoàn chỉnh",
            "explanation": "Sau thủ tục Partition, tất cả phần tử bên trái chốt đều $\\le$ chốt và tất cả phần tử bên phải chốt đều $>$ chốt. Do đó, phần tử chốt đã nằm ở vị trí đúng tuyệt đối của nó trong mảng đích và không bao giờ bị di chuyển nữa."
        },
        {
            "id": "q169",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Độ phức tạp thời gian của thủ tục phân hoạch `Partition` trên một đoạn gồm $m$ phần tử trong Quick Sort là bao nhiêu?",
            "options": [
                "$O(m)$ tuyến tính",
                "$O(m^2)$",
                "$O(\\log m)$",
                "$O(m \\log m)$"
            ],
            "answer": "$O(m)$ tuyến tính",
            "explanation": "Thủ tục phân hoạch sử dụng hai con trỏ `left` và `right` duyệt từ hai đầu tiến dần vào giữa, mỗi phần tử được xét đúng 1 lần. Do đó thời gian phân hoạch một đoạn $m$ phần tử luôn là $O(m)$ tuyến tính."
        },
        {
            "id": "q170",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Độ phức tạp thời gian trong trường hợp trung bình (Average-case) của Quick Sort là bao nhiêu?",
            "options": [
                "$O(n \\log n)$",
                "$O(n^2)$",
                "$O(n)$",
                "$O(\\log n)$"
            ],
            "answer": "$O(n \\log n)$",
            "explanation": "Theo Slide 11 Lecture 12: Trong trường hợp trung bình, chốt chia mảng thành các phần tương đối cân xứng. Chiều sâu cây đệ quy là $O(\\log n)$, mỗi tầng tốn $O(n)$ công phân hoạch, do đó thời gian trung bình đạt $O(n \\log n)$."
        },
        {
            "id": "q171",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Trường hợp xấu nhất (Worst-case) của Quick Sort dẫn đến thời gian thực thi bị suy thoái thành $O(n^2)$ xảy ra khi nào?",
            "options": [
                "Khi chốt chọn luôn là phần tử nhỏ nhất hoặc lớn nhất ở mọi bước đệ quy (ví dụ mảng đã sắp xếp sẵn và luôn chọn phần tử đầu làm chốt)",
                "Khi tất cả các phần tử trong mảng đều là số nguyên tố",
                "Khi kích thước mảng là lũy thừa của 2",
                "Khi chốt luôn chia mảng thành 2 nửa có kích thước hoàn toàn bằng nhau"
            ],
            "answer": "Khi chốt chọn luôn là phần tử nhỏ nhất hoặc lớn nhất ở mọi bước đệ quy (ví dụ mảng đã sắp xếp sẵn và luôn chọn phần tử đầu làm chốt)",
            "explanation": "Nếu luôn chọn phần tử đầu làm chốt trên mảng đã sắp xếp, dãy bị chia thành 1 phần có 0 phần tử và 1 phần có $n-1$ phần tử. Chiều sâu đệ quy tăng lên thành $n$, phương trình $T(n) = T(n-1) + O(n) \\implies T(n) = O(n^2)$."
        },
        {
            "id": "q172",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Không gian bộ nhớ ngăn xếp đệ quy của Quick Sort trong trường hợp trung bình và trường hợp xấu nhất lần lượt là bao nhiêu?",
            "options": [
                "$O(\\log n)$ trong trường hợp trung bình và $O(n)$ trong trường hợp xấu nhất",
                "Luôn luôn là $O(1)$ trong mọi trường hợp",
                "$O(n)$ trong trường hợp trung bình và $O(n^2)$ trong trường hợp xấu nhất",
                "$O(\\log n)$ trong mọi trường hợp"
            ],
            "answer": "$O(\\log n)$ trong trường hợp trung bình và $O(n)$ trong trường hợp xấu nhất",
            "explanation": "Ngăn xếp Call Stack phải lưu trữ các khung đệ quy. Trong trường hợp trung bình/tốt nhất, độ sâu cây đệ quy là $\\log_2 n \\implies O(\\log n)$. Trong trường hợp xấu nhất khi phân hoạch lệch hoàn toàn, độ sâu đệ quy là $n \\implies O(n)$."
        },
        {
            "id": "q173",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Nguyên lý hoạt động của thuật toán Sắp xếp trộn (Merge Sort) là gì?",
            "options": [
                "Chia đôi mảng thành 2 nửa tại chỉ số giữa, gọi đệ quy sắp xếp từng nửa rồi dùng mảng phụ trộn (Merge) hai nửa đã sắp lại thành dãy hoàn chỉnh",
                "Chọn phần tử nhỏ nhất đưa về đầu rồi sắp xếp đoạn còn lại",
                "Phân hoạch mảng quanh một phần tử chốt pivot",
                "Đổi chỗ các phần tử cách nhau một bước nhảy giảm dần"
            ],
            "answer": "Chia đôi mảng thành 2 nửa tại chỉ số giữa, gọi đệ quy sắp xếp từng nửa rồi dùng mảng phụ trộn (Merge) hai nửa đã sắp lại thành dãy hoàn chỉnh",
            "explanation": "Theo Slide 13-14 Lecture 12: Merge Sort chia đôi mảng tại $k = \\lfloor(i+j)/2\\rfloor$, gọi đệ quy `Mergesort` trên hai nửa, sau đó dùng thủ tục `Merge` kết hợp mảng phụ $B$ để trộn hai dãy con đã có thứ tự thành dãy tăng dần."
        },
        {
            "id": "q174",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Độ phức tạp thời gian của Merge Sort trong các trường hợp: tốt nhất, trung bình và xấu nhất lần lượt là bao nhiêu?",
            "options": [
                "Luôn luôn là $\\Theta(n \\log n)$ trong TẤT CẢ các trường hợp",
                "Tốt nhất $O(n)$, trung bình $O(n \\log n)$, xấu nhất $O(n^2)$",
                "Tốt nhất $O(\\log n)$, trung bình $O(n)$, xấu nhất $O(n \\log n)$",
                "Tốt nhất $O(1)$, trung bình và xấu nhất $O(n^2)$"
            ],
            "answer": "Luôn luôn là $\\Theta(n \\log n)$ trong TẤT CẢ các trường hợp",
            "explanation": "Theo Slide 17 Lecture 12: Merge Sort luôn chia mảng làm đôi chính xác tại vị trí giữa độc lập với nội dung dữ liệu. Chiều cao cây đệ quy luôn là $\\lceil \\log_2 n \\rceil$ và chi phí trộn ở mỗi tầng luôn là $O(n)$. Do đó thời gian luôn đạt $O(n \\log n)$ trong mọi tình huống."
        },
        {
            "id": "q175",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Nhược điểm lớn nhất của thuật toán Merge Sort khi cài đặt trên mảng một chiều thông thường là gì?",
            "options": [
                "Đòi hỏi không gian bộ nhớ phụ là $O(n)$ để cấp phát mảng đệm phục vụ thủ tục trộn (không phải thuật toán tại chỗ in-place)",
                "Có thể bị suy thoái thời gian chạy lên thành $O(n^2)$ khi mảng đã sắp xếp",
                "Không có tính ổn định khi sắp xếp các phần tử trùng lặp",
                "Chỉ sắp xếp được các mảng có kích thước nhỏ hơn 1000 phần tử"
            ],
            "answer": "Đòi hỏi không gian bộ nhớ phụ là $O(n)$ để cấp phát mảng đệm phục vụ thủ tục trộn (không phải thuật toán tại chỗ in-place)",
            "explanation": "Thủ tục trộn `Merge` cần một mảng phụ $B$ có kích thước tương đương mảng cần sắp ($O(n)$ bộ nhớ phụ). Đây là nhược điểm chính của Merge Sort so với QuickSort và HeapSort (chỉ cần $O(1)$ phụ)."
        },
        {
            "id": "q176",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Tính chất ổn định (Stability) của hai thuật toán Quick Sort và Merge Sort lần lượt là gì?",
            "options": [
                "Quick Sort là Không ổn định (Unstable); Merge Sort là Ổn định (Stable)",
                "Quick Sort là Ổn định (Stable); Merge Sort là Không ổn định (Unstable)",
                "Cả hai thuật toán đều là Ổn định (Stable)",
                "Cả hai thuật toán đều là Không ổn định (Unstable)"
            ],
            "answer": "Quick Sort là Không ổn định (Unstable); Merge Sort là Ổn định (Stable)",
            "explanation": "Quick Sort tráo đổi các phần tử ở khoảng cách xa qua chốt nên không ổn định. Trong khi đó, thủ tục `Merge` khi gặp hai phần tử bằng nhau ở nửa trái và nửa phải luôn ưu tiên chọn phần tử nửa trái trước, do đó Merge Sort bảo toàn thứ tự ban đầu $\\implies$ Ổn định (Stable)."
        },
        {
            "id": "q177",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Trong cấu trúc Max-Heap biểu diễn trên mảng với chỉ số từ 1 đến $n$, nút cha của nút nằm tại chỉ số $i$ được xác định ở vị trí nào?",
            "options": [
                "$\\lfloor i / 2 \\rfloor$",
                "$2i$",
                "$2i + 1$",
                "$i - 1$"
            ],
            "answer": "$\\lfloor i / 2 \\rfloor$",
            "explanation": "Theo Slide 23 Lecture 12: Trong biểu diễn mảng 1-based index của cây nhị phân gần hoàn chỉnh: Nút cha của nút $i$ nằm ở $\\lfloor i / 2 \\rfloor$; Con trái nằm ở $2i$; Con phải nằm ở $2i + 1$."
        },
        {
            "id": "q178",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Trong mảng biểu diễn cây Max-Heap gồm có $n$ phần tử (chỉ số 1 đến $n$), các nút lá (không có nút con nào) nằm ở khoảng chỉ số nào?",
            "options": [
                "Từ $\\lfloor n/2 \\rfloor + 1$ đến $n$",
                "Từ $1$ đến $\\lfloor n/2 \\rfloor$",
                "Chỉ nằm tại chỉ số $n$",
                "Từ $1$ đến $n - 1$"
            ],
            "answer": "Từ $\\lfloor n/2 \\rfloor + 1$ đến $n$",
            "explanation": "Các nút nội (Internal nodes - có con) có chỉ số thỏa mãn $2i \\le n \\implies i \\le \\lfloor n/2 \\rfloor$. Do đó các nút có chỉ số lớn hơn $\\lfloor n/2 \\rfloor$, tức từ $\\lfloor n/2 \\rfloor + 1$ đến $n$, không có con và đương nhiên là các nút lá."
        },
        {
            "id": "q179",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Giai đoạn tạo đống ban đầu (Build Heap) từ một mảng bất kỳ bằng cách gọi thủ tục `Pushdown` lùi dần từ $\\lfloor n/2 \\rfloor$ về 1 có độ phức tạp thời gian là bao nhiêu?",
            "options": [
                "$O(n)$ tuyến tính",
                "$O(n \\log n)$",
                "$O(n^2)$",
                "$O(\\log n)$"
            ],
            "answer": "$O(n)$ tuyến tính",
            "explanation": "Theo Slide 29 Lecture 12: Mặc dù gọi $n/2$ lần `Pushdown`, nhưng đa số các nút ở gần đáy cây chỉ có chiều cao nhỏ và di chuyển ít bước. Tổng số bước tính theo chuỗi hình học toán học chứng minh được thời gian tạo đống chỉ là $O(n)$ tuyến tính."
        },
        {
            "id": "q180",
            "topicId": 12,
            "topicName": "Sorting O(n log n)",
            "question": "Độ phức tạp thời gian tổng thể và không gian bộ nhớ phụ của thuật toán Sắp xếp vun đống (Heap Sort) lần lượt là bao nhiêu?",
            "options": [
                "Thời gian $O(n \\log n)$ trong mọi trường hợp và bộ nhớ phụ tại chỗ $O(1)$",
                "Thời gian $O(n)$ tốt nhất, $O(n^2)$ xấu nhất và bộ nhớ phụ $O(n)$",
                "Thời gian $O(n \\log n)$ và bộ nhớ phụ $O(n)$",
                "Thời gian $O(n^2)$ trong mọi trường hợp và bộ nhớ phụ $O(1)$"
            ],
            "answer": "Thời gian $O(n \\log n)$ trong mọi trường hợp và bộ nhớ phụ tại chỗ $O(1)$",
            "explanation": "Theo Slide 31 Lecture 12: Heap Sort gồm 2 giai đoạn: Tạo đống $O(n)$ và Trích xuất $n-1$ phần tử gốc với mỗi lần vun đống tốn $O(\\log n) \\implies (n-1) \\times O(\\log n) = O(n \\log n)$. Tổng thời gian luôn là $O(n \\log n)$ trong mọi trường hợp, và sắp xếp tại chỗ $O(1)$ bộ nhớ phụ."
        },

        # --- Topic 13: Search Algorithms (q181 - q195) ---
        {
            "id": "q181",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Mô hình bài toán tìm kiếm chuẩn mực trong khoa học máy tính tổ chức dữ liệu dưới dạng các cặp phần tử nào sau đây?",
            "options": [
                "Khóa - Giá trị (Key - Value)",
                "Đầu vào - Đầu ra (Input - Output)",
                "Chỉ số mảng - Độ dài mảng (Index - Length)",
                "Tên biến - Kiểu dữ liệu (Name - Type)"
            ],
            "answer": "Khóa - Giá trị (Key - Value)",
            "explanation": "Theo Slide 3-4 Lecture 13: Tập dữ liệu tìm kiếm $S$ gồm các phần tử là các bộ Khóa - Giá trị (Key-Value). Mục tiêu bài toán là tìm phần tử trong $S$ có thuộc tính khóa trùng với khóa tìm kiếm $k$ cho trước."
        },
        {
            "id": "q182",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Ưu điểm lớn nhất của thuật toán Tìm kiếm tuần tự (Sequential / Linear Search) là gì?",
            "options": [
                "Áp dụng được trên mọi tập dữ liệu mảng hoặc danh sách liên kết mà không yêu cầu dữ liệu phải được sắp xếp trước",
                "Có tốc độ tìm kiếm nhanh bằng logarit O(log n)",
                "Chỉ cần so sánh đúng 1 lần là tìm thấy kết quả",
                "Không tiêu tốn điện năng khi thực thi"
            ],
            "answer": "Áp dụng được trên mọi tập dữ liệu mảng hoặc danh sách liên kết mà không yêu cầu dữ liệu phải được sắp xếp trước",
            "explanation": "Theo Slide 5 Lecture 13: Tìm kiếm tuần tự duyệt lần lượt từng phần tử từ đầu đến cuối dãy, do đó áp dụng được cho dữ liệu hoàn toàn ngẫu nhiên chưa sắp xếp và hỗ trợ tốt cả trên mảng lẫn danh sách liên kết."
        },
        {
            "id": "q183",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Số phép so sánh trung bình của thuật toán Tìm kiếm tuần tự trên mảng gồm $n$ phần tử khi tìm kiếm thành công (giả thiết xác suất xuất hiện ở các vị trí là như nhau) là bao nhiêu?",
            "options": [
                "$\\frac{n+1}{2}$",
                "$n$",
                "$\\log_2 n$",
                "$\\frac{n}{4}$"
            ],
            "answer": "$\\frac{n+1}{2}$",
            "explanation": "Theo Slide 6 Lecture 13: Nếu phần tử ở vị trí thứ $i$, cần $i$ phép so sánh. Trung bình: $\\frac{1}{n} \\sum_{i=1}^n i = \\frac{1}{n} \\frac{n(n+1)}{2} = \\frac{n+1}{2} = O(n)$."
        },
        {
            "id": "q184",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Điều kiện tiên quyết bắt buộc để có thể áp dụng thuật toán Tìm kiếm nhị phân (Binary Search) trên mảng là gì?",
            "options": [
                "Mảng dữ liệu BẮT BUỘC phải được sắp xếp trước theo thứ tự của khóa (tăng dần hoặc giảm dần)",
                "Số lượng phần tử của mảng bắt buộc phải là một số chẵn",
                "Mảng bắt buộc phải chứa toàn các số nguyên dương",
                "Mảng bắt buộc phải được cấp phát động trên vùng nhớ Heap"
            ],
            "answer": "Mảng dữ liệu BẮT BUỘC phải được sắp xếp trước theo thứ tự của khóa (tăng dần hoặc giảm dần)",
            "explanation": "Theo Slide 7-8 Lecture 13: Binary Search dựa trên tính chất thứ tự để loại bỏ một nửa khoảng tìm kiếm sau mỗi phép so sánh. Nếu mảng chưa có thứ tự, việc so sánh với phần tử ở giữa không thể cho biết phần tử cần tìm nằm ở nửa trái hay nửa phải."
        },
        {
            "id": "q185",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Trong thuật toán Binary Search trên mảng tăng dần đoạn $[i, j]$, nếu khóa tìm kiếm $k$ nhỏ hơn giá trị tại chỉ số giữa $mid = \\lfloor(i+j)/2\\rfloor$, khoảng tìm kiếm tiếp theo sẽ được cập nhật như thế nào?",
            "options": [
                "$j = mid - 1$ (thu hẹp tìm kiếm về nửa bên trái)",
                "$i = mid + 1$ (thu hẹp tìm kiếm về nửa bên phải)",
                "$j = mid$ và giữ nguyên $i$",
                "Dừng thuật toán và thông báo tìm thấy"
            ],
            "answer": "$j = mid - 1$ (thu hẹp tìm kiếm về nửa bên trái)",
            "explanation": "Do mảng tăng dần, nếu $k < S[mid].Key$, toàn bộ các phần tử từ $mid$ đến $j$ đều lớn hơn $k$ nên không thể chứa $k$. Do đó ta thu hẹp khoảng tìm kiếm sang nửa trái: đặt biên phải $j = mid - 1$."
        },
        {
            "id": "q186",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Độ phức tạp thời gian trong trường hợp xấu nhất của thuật toán Tìm kiếm nhị phân trên mảng gồm $n$ phần tử là bao nhiêu?",
            "options": [
                "$O(\\log n)$",
                "$O(n)$",
                "$O(1)$",
                "$O(n \\log n)$"
            ],
            "answer": "$O(\\log n)$",
            "explanation": "Sau mỗi phép so sánh, kích thước khoảng tìm kiếm giảm đi một nửa: $n, n/2, n/4, ..., 1$. Số lần chia đôi tối đa là $\\lfloor \\log_2 n \\rfloor + 1$. Do đó thời gian chạy xấu nhất chỉ là $O(\\log n)$."
        },
        {
            "id": "q187",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Cây tìm kiếm nhị phân (Binary Search Tree - BST) định nghĩa mối quan hệ khóa tại nút $v$ như thế nào?",
            "options": [
                "Mọi khóa ở cây con trái $< v->getKey() <$ Mọi khóa ở cây con phải",
                "Mọi khóa ở cây con trái phải lớn hơn khóa nút $v$",
                "Khóa nút $v$ phải bằng trung bình cộng khóa hai con",
                "Cây con trái và cây con phải phải có cùng số lượng nút"
            ],
            "answer": "Mọi khóa ở cây con trái $< v->getKey() <$ Mọi khóa ở cây con phải",
            "explanation": "Theo Slide 14 Lecture 13: Định nghĩa BST yêu cầu tại mọi nút $v$, tất cả các khóa ở cây con trái của $v$ đều nhỏ hơn khóa của $v$, và tất cả các khóa ở cây con phải của $v$ đều lớn hơn khóa của $v$."
        },
        {
            "id": "q188",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Phép duyệt cây nào trên Cây tìm kiếm nhị phân (BST) luôn đảm bảo liệt kê danh sách các khóa theo thứ tự tăng dần?",
            "options": [
                "Duyệt trung thứ tự (In-Order Traversal: Trái $\\to$ Gốc $\\to$ Phải)",
                "Duyệt tiền thứ tự (Pre-Order Traversal: Gốc $\\to$ Trái $\\to$ Phải)",
                "Duyệt hậu thứ tự (Post-Order Traversal: Trái $\\to$ Phải $\\to$ Gốc)",
                "Duyệt theo mức (Level-Order Traversal bằng Queue)"
            ],
            "answer": "Duyệt trung thứ tự (In-Order Traversal: Trái $\\to$ Gốc $\\to$ Phải)",
            "explanation": "Theo Slide 15 Lecture 13: Do tính chất BST Khóa trái < Gốc < Khóa phải, nên phép duyệt In-Order (thăm cây con trái trước, thăm gốc ở giữa, thăm cây con phải sau) sẽ lần lượt in ra các khóa theo đúng thứ tự tăng dần hoàn hảo."
        },
        {
            "id": "q189",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Độ phức tạp thời gian của thao tác tìm kiếm đệ quy `TreeSearch` trên Cây BST phụ thuộc trực tiếp vào yếu tố nào?",
            "options": [
                "Chiều cao $h$ của cây ($O(h)$)",
                "Tổng số lượng nút lá của cây",
                "Số lượng nút con của nút gốc",
                "Kích thước bộ nhớ RAM máy tính"
            ],
            "answer": "Chiều cao $h$ của cây ($O(h)$)",
            "explanation": "Theo Slide 19-20 Lecture 13: Thao tác `TreeSearch` duyệt từ gốc dọc theo một đường đi đơn duy nhất xuống tới nút lá. Số bước so sánh tối đa bằng chiều cao $h$ của cây, do đó thời gian chạy là $O(h)$."
        },
        {
            "id": "q190",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Khi chèn một nút mới vào Cây tìm kiếm nhị phân (BST) bằng thuật toán chuẩn `InsertNode`, nút mới sẽ luôn luôn được gắn vào vị trí nào trên cây?",
            "options": [
                "Vị trí một nút lá mới của cây",
                "Vị trí nút gốc thay thế nút gốc cũ",
                "Vị trí nút trong có đúng một con",
                "Vị trí ngẫu nhiên do hệ điều hành chọn"
            ],
            "answer": "Vị trí một nút lá mới của cây",
            "explanation": "Theo Slide 21 Lecture 13: Thuật toán chèn vào BST duyệt so sánh khóa từ gốc xuống tương tự tìm kiếm. Khi gặp con trỏ liên kết rỗng (`NULL`), nó cấp phát nút mới và gắn làm lá mới của cây tại vị trí đó."
        },
        {
            "id": "q191",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Khi xóa một nút lá (nút không có con nào) trên Cây tìm kiếm nhị phân (BST), thao tác được thực hiện như thế nào?",
            "options": [
                "Giải phóng trực tiếp nút lá bằng `delete` và gán con trỏ tương ứng của nút cha trỏ về `NULL`",
                "Tìm nút thế mạng ở cây con bên phải",
                "Chuyển toàn bộ cây con trái sang nút cha",
                "Xóa luôn cả nút cha của nút lá đó"
            ],
            "answer": "Giải phóng trực tiếp nút lá bằng `delete` và gán con trỏ tương ứng của nút cha trỏ về `NULL`",
            "explanation": "Trường hợp 1 khi xóa nút trên BST (Slide 24 Lecture 13): Nút cần xóa là nút lá (không có con). Ta chỉ việc ngắt liên kết từ nút cha của nó (gán con trỏ `Left` hoặc `Right` của cha về `NULL`) và giải phóng ô nhớ của nút lá."
        },
        {
            "id": "q192",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Khi xóa một nút có đúng 1 con (chỉ có con trái hoặc chỉ có con phải) trên Cây tìm kiếm nhị phân (BST), thao tác được xử lý như thế nào?",
            "options": [
                "Nối trực tiếp con duy nhất của nút bị xóa vào nút cha của nút bị xóa, sau đó giải phóng nút",
                "Báo lỗi không thể xóa vì cây sẽ mất tính chất nhị phân",
                "Xóa luôn cả nút con duy nhất đó cùng lúc",
                "Thay thế giá trị của nút bị xóa bằng 0"
            ],
            "answer": "Nối trực tiếp con duy nhất của nút bị xóa vào nút cha của nút bị xóa, sau đó giải phóng nút",
            "explanation": "Trường hợp 2 khi xóa nút trên BST (Slide 25 Lecture 13): Nút có đúng 1 con. Ta \"bỏ qua\" nút bị xóa bằng cách nối trực tiếp con duy nhất của nó với nút cha của nút bị xóa, sau đó giải phóng ô nhớ của nút cần xóa."
        },
        {
            "id": "q193",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Khi xóa một nút có đủ cả 2 con trên Cây tìm kiếm nhị phân (BST), nút thế mạng (sao chép giá trị thay thế) được chọn là nút nào sau đây?",
            "options": [
                "Nút tiền nhiệm (In-order Predecessor: nút lớn nhất cây con trái) hoặc Nút kế vị (In-order Successor: nút nhỏ nhất cây con phải)",
                "Nút gốc của toàn bộ cây",
                "Một nút ngẫu nhiên bất kỳ ở cây con trái",
                "Nút lá có độ sâu lớn nhất trong toàn bộ cây"
            ],
            "answer": "Nút tiền nhiệm (In-order Predecessor: nút lớn nhất cây con trái) hoặc Nút kế vị (In-order Successor: nút nhỏ nhất cây con phải)",
            "explanation": "Trường hợp 3 khi xóa nút trên BST (Slide 26 Lecture 13): Để bảo toàn tính chất thứ tự của BST, ta tìm nút đứng liền trước (nút cực phải của cây con trái) hoặc nút đứng liền sau (nút cực trái của cây con phải) trong thứ tự duyệt In-Order để chép dữ liệu đè lên nút bị xóa, sau đó xóa nút thế mạng."
        },
        {
            "id": "q194",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "Trong trường hợp xấu nhất khi các phần tử được chèn vào BST theo thứ tự đã được sắp xếp tăng dần sẵn, cây sẽ bị suy thoái như thế nào và độ phức tạp tìm kiếm là bao nhiêu?",
            "options": [
                "Cây suy thoái thành một danh sách liên kết lệch hoàn toàn về bên phải với chiều cao $h = n$, độ phức tạp tìm kiếm thoái hóa thành $O(n)$",
                "Cây vẫn giữ được cân bằng hoàn hảo và thời gian tìm kiếm là $O(\\log n)$",
                "Cây bị lỗi tràn ngăn xếp ngay khi chèn phần tử thứ 3",
                "Cây tự động biến thành Max-Heap"
            ],
            "answer": "Cây suy thoái thành một danh sách liên kết lệch hoàn toàn về bên phải với chiều cao $h = n$, độ phức tạp tìm kiếm thoái hóa thành $O(n)$",
            "explanation": "Nếu chèn dãy đã sắp xếp (ví dụ 1, 2, 3, 4, 5), mỗi nút mới luôn lớn hơn nút trước nên luôn được gắn vào con phải. Cây thoái hóa thành một đường thẳng (danh sách liên kết) có chiều cao $h = n$, khiến thao tác tìm kiếm mất $O(n)$ thay vì $O(\\log n)$."
        },
        {
            "id": "q195",
            "topicId": 13,
            "topicName": "Search Algorithms",
            "question": "So sánh nào sau đây là chính xác giữa Mảng đã sắp xếp và Cây BST cân bằng về chi phí các thao tác tìm kiếm, chèn và xóa?",
            "options": [
                "Mảng tìm kiếm $O(\\log n)$ nhưng chèn/xóa tốn $O(n)$; BST cân bằng cho phép tìm kiếm, chèn và xóa đều đạt $O(\\log n)$",
                "Mảng chèn nhanh hơn BST cân bằng trong mọi trường hợp",
                "BST cân bằng tốn $O(n)$ cho thao tác tìm kiếm",
                "Cả hai cấu trúc đều có chi phí tìm kiếm, chèn và xóa là $O(1)$"
            ],
            "answer": "Mảng tìm kiếm $O(\\log n)$ nhưng chèn/xóa tốn $O(n)$; BST cân bằng cho phép tìm kiếm, chèn và xóa đều đạt $O(\\log n)$",
            "explanation": "Mảng đã sắp cho phép Binary Search trong $O(\\log n)$ nhưng khi chèn/xóa phần tử phải dịch chuyển mảng tốn $O(n)$. Cây BST cân bằng (như AVL hay Đỏ-Đen) khắc phục nhược điểm này: cả 3 thao tác Tìm kiếm, Chèn và Xóa đều đạt thời gian tối ưu $O(\\log n)$."
        },

        # --- Topic 14: Hash Tables (q196 - q210) ---
        {
            "id": "q196",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Mục đích cốt lõi của cấu trúc dữ liệu Bảng băm (Hash Table) là gì?",
            "options": [
                "Cho phép truy cập, thêm và xóa phần tử trực tiếp thông qua địa chỉ tính bằng hàm băm $h(k)$ với thời gian trung bình $O(1)$",
                "Sắp xếp các phần tử theo thứ tự tăng dần với chi phí bộ nhớ nhỏ nhất",
                "Nén dung lượng dữ liệu xuống một nửa",
                "Tự động mã hóa dữ liệu theo chuẩn quân sự AES"
            ],
            "answer": "Cho phép truy cập, thêm và xóa phần tử trực tiếp thông qua địa chỉ tính bằng hàm băm $h(k)$ với thời gian trung bình $O(1)$",
            "explanation": "Theo Slide 3-4 Lecture 14: Bảng băm là cấu trúc dữ liệu lưu trữ các cặp Khóa-Giá trị. Bằng cách sử dụng hàm băm $h(k)$ ánh xạ trực tiếp khóa vào vị trí ô nhớ trong mảng, bảng băm hỗ trợ tìm kiếm, chèn và xóa với hiệu năng vượt trội đạt thời gian trung bình $O(1)$."
        },
        {
            "id": "q197",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Tiêu chí nào sau đây KHÔNG PHẢI là yêu cầu đối với một Hàm băm (Hash Function) tốt?",
            "options": [
                "Hàm băm phải trả về các giá trị băm khác nhau mỗi lần gọi với cùng một khóa để tăng tính ngẫu nhiên",
                "Hàm băm phải phân bổ đều các khóa trên toàn bộ không gian địa chỉ của bảng",
                "Tốc độ tính toán của hàm băm phải đơn giản và nhanh chóng",
                "Hàm băm phải có tính xác định (Deterministic): cùng một khóa luôn cho ra cùng một giá trị băm"
            ],
            "answer": "Hàm băm phải trả về các giá trị băm khác nhau mỗi lần gọi với cùng một khóa để tăng tính ngẫu nhiên",
            "explanation": "Hàm băm BẮT BUỘC phải có tính xác định (Deterministic): với cùng một khóa $k$, hàm luôn phải trả về cùng một giá trị băm $h(k)$. Nếu trả về giá trị khác nhau, ta sẽ không bao giờ tìm lại được phần tử đã lưu trước đó!"
        },
        {
            "id": "q198",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Trong Phương pháp chia (Division Method) để xây dựng hàm băm: $h(k) = k \\bmod m$, tại sao kích thước bảng $m$ thường được chọn là một số nguyên tố?",
            "options": [
                "Để các giá trị băm phân bố đồng đều trên toàn bảng và hạn chế tối đa các quy luật tuần hoàn của khóa gây đụng độ",
                "Vì ngôn ngữ C++ chỉ hỗ trợ toán tử `%` với số nguyên tố",
                "Để tiết kiệm dung lượng RAM máy tính",
                "Vì số nguyên tố giúp hàm băm chạy nhanh gấp 10 lần"
            ],
            "answer": "Để các giá trị băm phân bố đồng đều trên toàn bảng và hạn chế tối đa các quy luật tuần hoàn của khóa gây đụng độ",
            "explanation": "Theo Slide 5 Lecture 14: Chọn $m$ là số nguyên tố (prime number) không quá gần lũy thừa của 2 hoặc 10 giúp giảm thiểu hiện tượng đụng độ, vì số nguyên tố không chia hết cho các ước số chung phổ biến của tập khóa trong thực tế."
        },
        {
            "id": "q199",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Nguyên lý hoạt động của Phương pháp bình phương giữa (Mid-Square Method) khi tạo hàm băm là gì?",
            "options": [
                "Bình phương giá trị khóa ($k^2$) rồi trích lấy một số chữ số nằm ở phần giữa làm địa chỉ băm",
                "Lấy căn bậc hai của khóa rồi làm tròn xuống",
                "Chia khóa cho 2 rồi bình phương kết quả",
                "Cộng các chữ số đầu và cuối của khóa lại với nhau"
            ],
            "answer": "Bình phương giá trị khóa ($k^2$) rồi trích lấy một số chữ số nằm ở phần giữa làm địa chỉ băm",
            "explanation": "Theo Slide 6 Lecture 14: Phương pháp Mid-Square bình phương khóa $k^2$, sau đó lấy các chữ số ở đoạn giữa làm giá trị băm. Ưu điểm là các chữ số ở giữa phụ thuộc vào tất cả các chữ số của khóa ban đầu, tạo ra sự phân tán rất tốt."
        },
        {
            "id": "q200",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Trong Phương pháp phân đoạn (Folding Method) tạo hàm băm, kỹ thuật Gấp mép biên (Boundary Folding) khác kỹ thuật Tách dóng lề (Shift Folding) ở điểm nào?",
            "options": [
                "Kỹ thuật gấp mép thực hiện đảo ngược thứ tự các chữ số của các đoạn biên/xen kẽ trước khi cộng dồn lại",
                "Kỹ thuật gấp mép nhân các đoạn với nhau thay vì cộng",
                "Kỹ thuật gấp mép chỉ áp dụng cho chuỗi ký tự",
                "Kỹ thuật gấp mép luôn bỏ qua đoạn chính giữa"
            ],
            "answer": "Kỹ thuật gấp mép thực hiện đảo ngược thứ tự các chữ số của các đoạn biên/xen kẽ trước khi cộng dồn lại",
            "explanation": "Theo Slide 7-8 Lecture 14: Trong Shift Folding, các đoạn được dóng lề cùng chiều rồi cộng. Trong Boundary Folding, các đoạn được coi như dải giấy gấp khúc lại ở mép biên, nghĩa là các đoạn xen kẽ bị đảo ngược thứ tự các chữ số trước khi cộng lại."
        },
        {
            "id": "q201",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Hiện tượng Đụng độ (Collision) trong Bảng băm được giải thích tất yếu bởi nguyên lý toán học nào?",
            "options": [
                "Nguyên lý chuồng bồ câu Dirichlet (Pigeonhole Principle) vì số lượng khóa khả dĩ luôn lớn hơn kích thước bảng băm",
                "Định lý Pytago",
                "Định lý giới hạn trung tâm xác suất",
                "Tiên đề Euclid về đường thẳng song song"
            ],
            "answer": "Nguyên lý chuồng bồ câu Dirichlet (Pigeonhole Principle) vì số lượng khóa khả dĩ luôn lớn hơn kích thước bảng băm",
            "explanation": "Theo Slide 9 Lecture 14: Tập không gian khóa $K$ thường rất lớn hoặc vô hạn, trong khi kích thước bảng băm $m$ là hữu hạn ($|K| > m$). Theo nguyên lý Dirichlet, chắc chắn sẽ tồn tại ít nhất hai khóa khác nhau $k_1 \\ne k_2$ có cùng giá trị băm $h(k_1) = h(k_2)$, gây ra đụng độ."
        },
        {
            "id": "q202",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Cơ chế giải quyết đụng độ bằng Danh sách liên kết ngoài (Separate Chaining) hoạt động như thế nào?",
            "options": [
                "Mỗi ô trong bảng băm đóng vai trò là một thùng chứa (Bucket) quản lý một danh sách liên kết chứa tất cả các phần tử có cùng giá trị băm",
                "Ghi đè phần tử mới lên phần tử cũ và vứt bỏ phần tử cũ",
                "Mở rộng kích thước bảng băm gấp 10 lần mỗi khi có đụng độ",
                "Dò tìm ô trống tiếp theo liền kề trong mảng để lưu"
            ],
            "answer": "Mỗi ô trong bảng băm đóng vai trò là một thùng chứa (Bucket) quản lý một danh sách liên kết chứa tất cả các phần tử có cùng giá trị băm",
            "explanation": "Theo Slide 10-12 Lecture 14: Trong Separate Chaining, bảng băm là một mảng các danh sách liên kết. Khi xảy ra đụng độ (nhiều khóa có cùng $h(k)$), tất cả các phần tử này đều được thêm vào danh sách liên kết tại ô $table[h(k)]$ đó."
        },
        {
            "id": "q203",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Trong mã nguồn cài đặt C++ của Bảng băm Separate Chaining ở Slide 13 Lecture 14, biến thành viên `table` được khai báo dưới dạng cấu trúc dữ liệu nào?",
            "options": [
                "`SingleList<Keys, T> *table;` (Mảng động các danh sách liên kết đơn)",
                "`int **table;` (Ma trận số nguyên hai chiều)",
                "`vector<T> table;` (Một vector đơn độc)",
                "`stack<T> table;` (Một ngăn xếp)"
            ],
            "answer": "`SingleList<Keys, T> *table;` (Mảng động các danh sách liên kết đơn)",
            "explanation": "Trong mã nguồn bài giảng Slide 13 Lecture 14: Lớp `Hashtable` khai báo `SingleList<Keys, T> *table;` và khởi tạo bằng `table = new SingleList<Keys, T>[N];`, tức là một mảng gồm $N$ danh sách liên kết đơn."
        },
        {
            "id": "q204",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Hệ số tải (Load Factor $\\alpha$) của một Bảng băm được định nghĩa bằng công thức nào sau đây?",
            "options": [
                "$\\alpha = \\frac{n}{m}$ ($n$ là số phần tử đã lưu trữ, $m$ là kích thước sức chứa của bảng)",
                "$\\alpha = n \\times m$",
                "$\\alpha = m - n$",
                "$\\alpha = \\frac{m}{n^2}$"
            ],
            "answer": "$\\alpha = \\frac{n}{m}$ ($n$ là số phần tử đã lưu trữ, $m$ là kích thước sức chứa của bảng)",
            "explanation": "Hệ số tải $\\alpha = n/m$ phản ánh mức độ lấp đầy của bảng băm. Với Separate Chaining, $\\alpha$ biểu thị độ dài trung bình của các danh sách liên kết tại mỗi ô."
        },
        {
            "id": "q205",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Trong phương pháp Separate Chaining, phát biểu nào sau đây về Hệ số tải $\\alpha$ là đúng?",
            "options": [
                "Hệ số tải $\\alpha$ hoàn toàn có thể lớn hơn 1 vì mỗi ô mảng có thể chứa một danh sách gồm nhiều phần tử",
                "Hệ số tải $\\alpha$ bắt buộc phải luôn luôn nhỏ hơn 0.5",
                "Hệ số tải $\\alpha$ không bao giờ vượt quá 1",
                "Hệ số tải $\\alpha$ luôn luôn bằng 0"
            ],
            "answer": "Hệ số tải $\\alpha$ hoàn toàn có thể lớn hơn 1 vì mỗi ô mảng có thể chứa một danh sách gồm nhiều phần tử",
            "explanation": "Khác với Địa chỉ mở (Open Addressing) bắt buộc $\\alpha < 1$ do các ô mảng chỉ chứa 1 phần tử, trong Separate Chaining các phần tử được nối ngoài bằng danh sách liên kết. Do đó số phần tử $n$ có thể lớn hơn nhiều kích thước bảng $m$, dẫn đến $\\alpha > 1$."
        },
        {
            "id": "q206",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Độ phức tạp thời gian của thao tác tìm kiếm trên Bảng băm trong trường hợp xấu nhất (Worst-case) là bao nhiêu và xảy ra khi nào?",
            "options": [
                "$O(n)$, xảy ra khi tất cả các khóa chèn vào đều bị hàm băm ánh xạ về cùng một ô địa chỉ duy nhất",
                "$O(1)$ trong mọi trường hợp xấu nhất",
                "$O(\\log n)$",
                "$O(n^2)$"
            ],
            "answer": "$O(n)$, xảy ra khi tất cả các khóa chèn vào đều bị hàm băm ánh xạ về cùng một ô địa chỉ duy nhất",
            "explanation": "Nếu hàm băm quá kém hoặc bị kẻ tấn công cố tình chọn các khóa đụng độ (Hash Collision Attack), toàn bộ $n$ phần tử sẽ rơi vào cùng một danh sách liên kết tại ô đó. Khi đó việc tìm kiếm suy thoái thành tìm kiếm tuần tự trên DSLK tốn thời gian $O(n)$."
        },
        {
            "id": "q207",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Trong phương pháp Địa chỉ mở (Open Addressing), kỹ thuật Thử tuyến tính (Linear Probing) sử dụng công thức dò tìm nào?",
            "options": [
                "$h(k, i) = (h(k) + i) \\bmod m \\quad (i = 0, 1, 2, \\dots)$",
                "$h(k, i) = (h(k) + i^2) \\bmod m$",
                "$h(k, i) = (h(k) \\times i) \\bmod m$",
                "$h(k, i) = (h_1(k) + i \\cdot h_2(k)) \\bmod m$"
            ],
            "answer": "$h(k, i) = (h(k) + i) \\bmod m \\quad (i = 0, 1, 2, \\dots)$",
            "explanation": "Theo nguyên lý Thử tuyến tính (Linear Probing): Nếu ô $h(k)$ bị đụng độ, thuật toán sẽ lần lượt thử các ô kế tiếp liền kề: $(h(k)+1) \\% m, (h(k)+2) \\% m, ...$ cho tới khi tìm thấy ô trống."
        },
        {
            "id": "q208",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Hiện tượng Kết chùm nguyên phát (Primary Clustering) là nhược điểm đặc trưng của phương pháp giải quyết đụng độ nào trong Địa chỉ mở?",
            "options": [
                "Thử tuyến tính (Linear Probing)",
                "Danh sách liên kết ngoài (Separate Chaining)",
                "Băm kép (Double Hashing)",
                "Cây nhị phân tìm kiếm AVL"
            ],
            "answer": "Thử tuyến tính (Linear Probing)",
            "explanation": "Trong Linear Probing, khi các ô bị chiếm đóng nằm liền kề nhau sẽ tạo thành các cụm dài (cluster). Bất kỳ khóa nào bị băm vào trong cụm đó đều phải dò qua toàn bộ cụm rồi gắn tiếp vào cuối cụm, khiến cụm càng ngày càng phình to và làm chậm đáng kể tốc độ tìm kiếm."
        },
        {
            "id": "q209",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Kỹ thuật Băm kép (Double Hashing) trong Địa chỉ mở sử dụng công thức dò tìm nào sau đây để loại bỏ hiện tượng kết chùm?",
            "options": [
                "$h(k, i) = (h_1(k) + i \\cdot h_2(k)) \\bmod m$",
                "$h(k, i) = (h(k) + i) \\bmod m$",
                "$h(k, i) = (h(k) + i^2) \\bmod m$",
                "$h(k, i) = (h_1(k) + h_2(k)) \\bmod m$"
            ],
            "answer": "$h(k, i) = (h_1(k) + i \\cdot h_2(k)) \\bmod m$",
            "explanation": "Băm kép (Double Hashing) sử dụng hàm băm thứ hai $h_2(k)$ để xác định bước nhảy cho chuỗi dò tìm: $h(k, i) = (h_1(k) + i \\cdot h_2(k)) \\bmod m$. Do bước nhảy phụ thuộc vào từng khóa $k$, các khóa đụng độ tại $h_1(k)$ sẽ phân tán theo các bước nhảy khác nhau, triệt tiêu hiện tượng kết chùm."
        },
        {
            "id": "q210",
            "topicId": 14,
            "topicName": "Hash Tables",
            "question": "Khi xóa một phần tử trong Bảng băm sử dụng phương pháp Địa chỉ mở (Open Addressing), tại sao không được gán ô đó thành ô trống (Empty) mà phải đánh dấu là `DELETED` (Tombstone)?",
            "options": [
                "Vì nếu gán thành rỗng sẽ làm ngắt quãng chuỗi dò tìm của các phần tử được chèn sau đó nhưng bị đụng độ cùng mã băm",
                "Vì trình biên dịch C++ cấm sửa đổi giá trị các ô trong mảng",
                "Vì ô trống sẽ làm mất điện áp của thanh ghi RAM",
                "Vì nếu gán rỗng thì bảng băm sẽ tự động xóa tất cả các phần tử khác"
            ],
            "answer": "Vì nếu gán thành rỗng sẽ làm ngắt quãng chuỗi dò tìm của các phần tử được chèn sau đó nhưng bị đụng độ cùng mã băm",
            "explanation": "Trong Địa chỉ mở, thao tác tìm kiếm dừng lại khi gặp một ô rỗng (Empty) vì suy luận rằng phần tử chưa từng tồn tại. Nếu ta xóa bằng cách gán ô về rỗng, những phần tử chèn sau đó từng bị đụng độ nhảy qua ô này sẽ không bao giờ được tìm thấy nữa! Do đó phải dùng cờ đánh dấu `DELETED` (xóa lười / Tombstone) để chuỗi dò tìm tiếp tục đi qua."
        }
    ]
    return questions
