# Handoff Report: Survey Explorer 3 (Lectures 11 - 14 & Systems Specs)

## 1. Observation
- **Direct File Observations:**
  - `D:\c++\drive-download-20261028T155811Z-1-001\Lectures 11 Sorting - nn.ppt` (356,352 bytes, 19 slides, binary OLE2 Compound Document format).
    - Slide 3: Classification of $O(n^2)$ sorting: "Nổi bọt – Bubble sort, Chèn – Insertion sort, Chọn – Selection sort".
    - Slide 5: Exact BubbleSort pseudocode and C++ `void Swap(object &a, object &b)`.
    - Slide 8: Exact operation count: $T(n) = (n+2) + (n-1)*2 + 10*[(n-1) + (n-2) + \dots + 1] = O(n^2)$.
    - Slide 11: Exact SelectionSort pseudocode with `posmin` and single swap at loop end.
    - Slide 16: Exact InsertionSort pseudocode with inner `while (A[j].Key > x.Key) and (j >= 0)`.
  - `D:\c++\drive-download-20261028T155811Z-1-001\Lectures 12 Sorting - nlogn.pptx` (33,397,143 bytes, 57 slides, OpenXML ZIP format).
    - Slide 4: Divide and conquer into $S_1 (\le p)$, $S_2 (p)$, $S_3 (> p)$.
    - Slide 11: Exact Partition pseudocode: pivot $p = A[i]$, two pointers `left` and `right`, final swap of $A[i]$ and $A[right]$.
    - Slide 25: Exact `Merge` pseudocode with auxiliary array $B[i..j]$.
    - Slide 27: Exact `Mergesort` recursive algorithm with split point $k = (i+j)/2$.
    - Slide 38: Time complexity proof: height $h = O(\log n)$, work per level $O(n)$, total $O(n \log n)$.
    - Slide 39: Complete binary tree definition of Heap, Max-Heap property ($key(root) \ge key(children)$).
    - Slide 41: Array representation: children at $2i$ and $2i+1$, parent at $\lfloor i/2 \rfloor$, leaves from $\lfloor n/2 \rfloor + 1$ to $n$.
    - Slide 52: Exact `Pushdown(Array A, i, n)` pseudocode (heapify/sift-down).
    - Slide 53: Exact `Heapsort(Array A, n)` pseudocode: Phase 1 build heap from $n/2$ down to 1; Phase 2 extract root to $A[i]$ and `Pushdown(A, 1, i-1)`.
    - Slide 55: Complexity proof: Pushdown $O(\log(n/i))$, Build Heap $O(n)$, total sorting $O(n \log n)$.
  - `D:\c++\drive-download-20261028T155811Z-1-001\Lectures 13 Search.ppt` (984,576 bytes, 39 slides, binary OLE2 Compound Document format).
    - Slide 2: Three search methods: "Tìm kiếm tuần tự (sequence search), Tìm kiếm nhị phân (Binary search), Bảng băm (hash table)".
    - Slide 6: Sequential search pseudocode on array/list, worst case $O(n)$.
    - Slide 12: Binary search on sorted array pseudocode, worst case $O(\log_2 n)$.
    - Slide 14: BST definition: left subtree keys $< key(node) <$ right subtree keys.
    - Slide 17-18: C++ Node structure (`Keys key`, `T elem`, `Node *Parent`, `Node *Left`, `Node *Right`) and BST class interface.
    - Slide 20: Exact `TreeSearch(Keys k, Node<T>* v)` recursive pseudocode.
    - Slide 25: Exact `InsertNode(Node *&root, Node *newNode)` recursive pseudocode.
    - Slide 27-30: Deletion cases: leaf node, node with 1 child, node with 2 children using in-order predecessor (nút tiền nhiệm) or successor (nút kế vị).
    - Slide 37: Complexity: $O(h)$ for search, insert, remove; best/balanced $O(\log n)$, worst/skewed $O(n)$.
  - `D:\c++\drive-download-20261028T155811Z-1-001\Lectures 14 Hash tables.ppt` (680,960 bytes, 19 slides, binary OLE2 Compound Document format).
    - Slide 2: Hash function $h: K \to 0..m-1$.
    - Slide 5-8: Hash function methods: Division $h(k) = k \bmod m$ ($m$ prime), Mid-Square (nhân/bình phương giữa), Folding (phân đoạn: tách và gấp).
    - Slide 9-10: Separate Chaining (thùng chứa/danh sách liên kết) for collision resolution.
    - Slide 13, 15, 16, 17: Concrete C++ code for `Node`, `Hashtable` with `SingleList<Keys, T> *table` and function pointer `int (*hash)(Keys, int)`. Methods `Add`, `Remove`, `Find`, `Contains`, `Count`.
    - Slide 17: `DEMO.CPP` initializing `Hashtable<int, float> ht(97);` with $h(key, n) = key \bmod n$.
- **Tool Executions & Observations:**
  - PowerShell COM automation: `New-Object -ComObject PowerPoint.Application` successfully extracted all slides from both `.ppt` (Lectures 11, 13, 14) and `.pptx` (Lecture 12) without external dependencies.
  - Windows console encoding required `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8` for correct Vietnamese diacritic rendering.

## 2. Logic Chain
1. **Extraction Consistency:**
   - As observed in Survey 1, the slide repository mixes legacy `.ppt` files with `.pptx` files. PowerPoint COM automation was utilized to inspect and extract all 134 slides across Lectures 11-14.
2. **Pedagogical & Algorithmic Mapping:**
   - Lecture 11 focuses on foundational $O(n^2)$ sorting: step-by-step invariants, exact comparison/swap counts, stability, and in-place memory.
   - Lecture 12 moves to advanced $O(n \log n)$ sorting: QuickSort (partition mechanics, worst case $O(n^2)$ vs average $O(n \log n)$), MergeSort (guaranteed $O(n \log n)$, $O(n)$ space, stable), and HeapSort (binary heap array mapping, $O(n)$ build heap, in-place, unstable).
   - Lecture 13 formalizes searching: Linear search ($O(n)$), Binary search on sorted arrays ($O(\log n)$), and Binary Search Trees (in-order traversal properties, 3-case deletion, $O(h)$ operations).
   - Lecture 14 completes data structures with Hash Tables: hash functions (division, mid-square, folding), collisions (Dirichlet), Separate Chaining (C++ array of `SingleList` with function pointer hash), Open Addressing (linear, quadratic, double hashing, tombstones), and load factor $\alpha$.
3. **Question Theme Formulation:**
   - Formulated exactly 60 candidate question themes (15 themes $\times$ 4 topics) covering theoretical concepts, code tracing, time/space complexity, and syntax.
4. **Architectural & Verification Requirements:**
   - Derived the full JSON schema for `questions.json` ensuring 100% compatibility with shuffling algorithms (bare string options with dynamic A-D badge assignment).
   - Designed the 5-question random round engine with Fisher-Yates shuffling, topic diversity, instant feedback, scoring, timer, and replayability.
   - Defined the standalone SPA architecture for `index.html` featuring Tailwind CSS, Lucide icons, synthesized Web Audio sound effects, and dual data loading (`questions.json` + `questions.js` fallback) to eliminate local CORS errors.
   - Defined verification scripts (`verify_bank.py` and `test_quiz_engine.py`) to enforce bank integrity and engine randomness.

## 3. Caveats
- Lectures 1 to 10 were surveyed by Survey Explorer 1 (Lectures 1-5) and Survey Explorer 2 (Lectures 6-10).
- In Lecture 14, slides 13-17 contained embedded source code bitmaps (`NODE.CPP`, `HASHTBL.CPP`, `DEMO.CPP`); these were visually inspected using `view_file` on exported frames and transcribed verbatim into `report.md`.
- Open Addressing is mentioned conceptually in standard curricula and the project request, but the lecture slide code specifically implements Separate Chaining (`SingleList`); questions should cover both Separate Chaining (with C++ code) and Open Addressing (probing formulas).

## 4. Conclusion
- Complete technical survey and architectural analysis for Lectures 11-14, Quiz Engine, Question Schema, Frontend SPA, and Verification Runner are finished.
- 134 slides across 4 lectures were cataloged and analyzed.
- 60 candidate question themes (15 themes $\times$ 4 topics) and the complete architectural blueprint are documented in `D:\c++\quiz_game\.agents\teamwork\teamwork_preview_explorer_survey_3\report.md`.
- Downstream workers (Question Author, Frontend Developer, Test Engineer) have complete, unambiguous specifications to proceed.

## 5. Verification Method
- **Inspect Generated Artifacts:**
  - View report: `D:\c++\quiz_game\.agents\teamwork\teamwork_preview_explorer_survey_3\report.md`
  - View handoff: `D:\c++\quiz_game\.agents\teamwork\teamwork_preview_explorer_survey_3\handoff.md`
- **Verify Slide Counts via PowerShell:**
  ```powershell
  $ppt = New-Object -ComObject PowerPoint.Application
  @("Lectures 11 Sorting - nn.ppt", "Lectures 12 Sorting - nlogn.pptx", "Lectures 13 Search.ppt", "Lectures 14 Hash tables.ppt") | ForEach-Object {
      $path = Join-Path "D:\c++\drive-download-20261028T155811Z-1-001" $_
      $pres = $ppt.Presentations.Open($path, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)
      Write-Host "$_: $($pres.Slides.Count) slides"
      $pres.Close()
  }
  $ppt.Quit()
  ```
  Expected slide counts:
  - `Lectures 11 Sorting - nn.ppt`: 19 slides
  - `Lectures 12 Sorting - nlogn.pptx`: 57 slides
  - `Lectures 13 Search.ppt`: 39 slides
  - `Lectures 14 Hash tables.ppt`: 19 slides
  Total: 134 slides.
