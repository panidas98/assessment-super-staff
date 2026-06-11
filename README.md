# Technical Assessment Solution

Solutions to technical assessment covering debugging, SQL, and Python.

---

## Files

| File | What it covers |
|---|---|
| `yoy_calculator.py` | Debugging — fixed YoY spending function + unit tests |
| `open_tickets_query.sql` | SQL — filtering open high-priority tickets |
| `aggregate_sales.py` | Python — aggregating sales transactions by product |

---

## 1. Debugging – Year-Over-Year Calculator

**What was broken:**

The original loop started at `range(0, len(sorted_years))`, which meant on the very first iteration `i = 0`, and `sorted_years[i - 1]` would evaluate to `sorted_years[-1]` — Python's way of accessing the *last* element. So the first year in the dataset was being compared against the last one, which produced a bogus result and polluted the output with an extra key that shouldn't be there.

On top of that, there was no guard against division by zero, so passing `0` as a previous year's spending would crash immediately.

**Fixes applied:**

- Changed loop to `range(1, len(sorted_years))` so iteration starts at the second year, with a valid previous year to compare against
- Added a zero-division check: if `previous_spending == 0`, the change is recorded as `None` instead of raising an error

```python
# before (broken)
for i in range(0, len(sorted_years)):

# after (fixed)
for i in range(1, len(sorted_years)):
```

**Running the tests:**

```bash
python yoy_calculator.py
```

All three unit tests should pass.

---

## 2. SQL – Open High-Priority Tickets

Query lives in `open_tickets_query.sql`. It filters the `tickets` table on three conditions at once: status, assignee, and priority.

```sql
SELECT ticket_id, status, priority, assigned_to
FROM tickets
WHERE status = 'open'
  AND assigned_to = 'engineer1'
  AND priority = 'high';
```

If the table grows large and this query gets slow, an index on `(status, assigned_to, priority)` would help a lot.

---

## 3. Python – Sales Aggregation

`aggregate_sales.py` takes a list of transaction dicts and returns a product → total quantity mapping.

```python
transactions = [
    {"product": "apple", "quantity": 10},
    {"product": "banana", "quantity": 5},
    {"product": "apple", "quantity": 3},
    ...
]

aggregate_sales(transactions)
# → {'apple': 13, 'banana': 7, 'orange': 8}
```

The logic is a simple accumulator loop — check if the product key exists, add to it if so, initialize it if not. Could also be done with `collections.defaultdict(int)` or `dict.get()` as alternatives, but the explicit check keeps it readable.

**Running it:**

```bash
python aggregate_sales.py
```

---
