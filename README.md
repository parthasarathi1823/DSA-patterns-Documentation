# DSA Patterns Documentation

Personal learning journal for Data Structures & Algorithms: **patterns first**, then **solved problems**.

## How this repo is organized

```text
patterns/     → How do I think?   (technique docs + templates)
problems/     → What did I solve? (one folder per LeetCode problem)
```

| Pillar | Purpose |
|--------|---------|
| [patterns/](patterns/) | Intuition, ASCII/Mermaid visuals, templates, common mistakes |
| [problems/](problems/) | Solutions grouped by primary topic |

### Learning flow

1. Open a pattern under `patterns/` (README + `template.py`)
2. Solve → put code in `problems/<topic>/NNNN-slug/`
3. Link it from that pattern’s `problems-solved.md`

### Patterns available

| Topic | Start here |
|-------|------------|
| Arrays | [Brute force](patterns/arrays/brute-force/) → [Single pass](patterns/arrays/single-pass/) → [Prefix sum](patterns/arrays/prefix-sum/) |
| Stack | [Basics](patterns/stack/basics/) → [Monotonic stack](patterns/stack/monotonic-stack/) |

### Problems by topic

| Topic | Folder |
|-------|--------|
| Arrays | [problems/arrays/](problems/arrays/) |
| Stack | [problems/stack/](problems/stack/) |
| Linked List | [problems/linked_list/](problems/linked_list/) |
| SQL | [problems/sql/](problems/sql/) |
| Math / DP | [problems/math/](problems/math/) |
| Bit Manipulation | [problems/bit_manipulation/](problems/bit_manipulation/) |

### Conventions

- **One problem → one path** (primary pattern/topic only)
- Problem folders: `problems/<topic>/NNNN-kebab-slug/` (e.g. `problems/stack/0020-valid-parentheses/`)
- Pattern folders store notes + templates; they link to solutions, they don’t duplicate them
- Prefer `template.py` and `problems-solved.md` naming

---

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](problems/arrays/0001-two-sum) |
| [0066-plus-one](problems/arrays/0066-plus-one) |
| [0136-single-number](problems/bit_manipulation/0136-single-number) |
| [0169-majority-element](problems/arrays/0169-majority-element) |
| [0414-third-maximum-number](problems/arrays/0414-third-maximum-number) |
| [0456-132-pattern](problems/stack/0456-132-pattern) |
| [0485-max-consecutive-ones](problems/arrays/0485-max-consecutive-ones) |
| [0496-next-greater-element-i](problems/stack/0496-next-greater-element-i) |
| [0503-next-greater-element-ii](problems/stack/0503-next-greater-element-ii) |
| [1365-how-many-numbers-are-smaller-than-the-current-number](problems/arrays/1365-how-many-numbers-are-smaller-than-the-current-number) |
| [1475-final-prices-with-a-special-discount-in-a-shop](problems/stack/1475-final-prices-with-a-special-discount-in-a-shop) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](problems/arrays/0001-two-sum) |
| [0169-majority-element](problems/arrays/0169-majority-element) |
| [0496-next-greater-element-i](problems/stack/0496-next-greater-element-i) |
| [1365-how-many-numbers-are-smaller-than-the-current-number](problems/arrays/1365-how-many-numbers-are-smaller-than-the-current-number) |
## Stack
|  |
| ------- |
| [0020-valid-parentheses](problems/stack/0020-valid-parentheses) |
| [0155-min-stack](problems/stack/0155-min-stack) |
| [0402-remove-k-digits](problems/stack/0402-remove-k-digits) |
| [0456-132-pattern](problems/stack/0456-132-pattern) |
| [0496-next-greater-element-i](problems/stack/0496-next-greater-element-i) |
| [0503-next-greater-element-ii](problems/stack/0503-next-greater-element-ii) |
| [0901-online-stock-span](problems/stack/0901-online-stock-span) |
| [1475-final-prices-with-a-special-discount-in-a-shop](problems/stack/1475-final-prices-with-a-special-discount-in-a-shop) |
| [1544-make-the-string-great](problems/stack/1544-make-the-string-great) |
| [3174-clear-digits](problems/stack/3174-clear-digits) |
## Monotonic Stack
|  |
| ------- |
| [0402-remove-k-digits](problems/stack/0402-remove-k-digits) |
| [0456-132-pattern](problems/stack/0456-132-pattern) |
| [0496-next-greater-element-i](problems/stack/0496-next-greater-element-i) |
| [0503-next-greater-element-ii](problems/stack/0503-next-greater-element-ii) |
| [0901-online-stock-span](problems/stack/0901-online-stock-span) |
| [1475-final-prices-with-a-special-discount-in-a-shop](problems/stack/1475-final-prices-with-a-special-discount-in-a-shop) |
## String
|  |
| ------- |
| [0020-valid-parentheses](problems/stack/0020-valid-parentheses) |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](problems/arrays/0028-find-the-index-of-the-first-occurrence-in-a-string) |
| [0058-length-of-last-word](problems/arrays/0058-length-of-last-word) |
| [0402-remove-k-digits](problems/stack/0402-remove-k-digits) |
| [1544-make-the-string-great](problems/stack/1544-make-the-string-great) |
| [3174-clear-digits](problems/stack/3174-clear-digits) |
## Linked List
|  |
| ------- |
| [0019-remove-nth-node-from-end-of-list](problems/linked_list/0019-remove-nth-node-from-end-of-list) |
| [0092-reverse-linked-list-ii](problems/linked_list/0092-reverse-linked-list-ii) |
| [0206-reverse-linked-list](problems/linked_list/0206-reverse-linked-list) |
## Two Pointers
|  |
| ------- |
| [0019-remove-nth-node-from-end-of-list](problems/linked_list/0019-remove-nth-node-from-end-of-list) |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](problems/arrays/0028-find-the-index-of-the-first-occurrence-in-a-string) |
## Recursion
|  |
| ------- |
| [0206-reverse-linked-list](problems/linked_list/0206-reverse-linked-list) |
## Greedy
|  |
| ------- |
| [0402-remove-k-digits](problems/stack/0402-remove-k-digits) |
## Math
|  |
| ------- |
| [0009-palindrome-number](problems/arrays/0009-palindrome-number) |
| [0066-plus-one](problems/arrays/0066-plus-one) |
| [0070-climbing-stairs](problems/math/0070-climbing-stairs) |
## Binary Search
|  |
| ------- |
| [0456-132-pattern](problems/stack/0456-132-pattern) |
## Ordered Set
|  |
| ------- |
| [0456-132-pattern](problems/stack/0456-132-pattern) |
## Design
|  |
| ------- |
| [0155-min-stack](problems/stack/0155-min-stack) |
| [0901-online-stock-span](problems/stack/0901-online-stock-span) |
## String Matching
|  |
| ------- |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](problems/arrays/0028-find-the-index-of-the-first-occurrence-in-a-string) |
## Divide and Conquer
|  |
| ------- |
| [0169-majority-element](problems/arrays/0169-majority-element) |
## Sorting
|  |
| ------- |
| [0169-majority-element](problems/arrays/0169-majority-element) |
| [1365-how-many-numbers-are-smaller-than-the-current-number](problems/arrays/1365-how-many-numbers-are-smaller-than-the-current-number) |
## Counting
|  |
| ------- |
| [0169-majority-element](problems/arrays/0169-majority-element) |
## Boyer–Moore Majority Vote Algorithm
|  |
| ------- |
| [0169-majority-element](problems/arrays/0169-majority-element) |
## Database
|  |
| ------- |
| [0175-combine-two-tables](problems/sql/0175-combine-two-tables) |
| [0577-employee-bonus](problems/sql/0577-employee-bonus) |
| [0595-big-countries](problems/sql/0595-big-countries) |
## Data Stream
|  |
| ------- |
| [0901-online-stock-span](problems/stack/0901-online-stock-span) |
## Dynamic Programming
|  |
| ------- |
| [0070-climbing-stairs](problems/math/0070-climbing-stairs) |
## Memoization
|  |
| ------- |
| [0070-climbing-stairs](problems/math/0070-climbing-stairs) |
## Bit Manipulation
|  |
| ------- |
| [0136-single-number](problems/bit_manipulation/0136-single-number) |
## Counting Sort
|  |
| ------- |
| [1365-how-many-numbers-are-smaller-than-the-current-number](problems/arrays/1365-how-many-numbers-are-smaller-than-the-current-number) |
## Simulation
|  |
| ------- |
| [3174-clear-digits](problems/stack/3174-clear-digits) |
<!---LeetCode Topics End-->
