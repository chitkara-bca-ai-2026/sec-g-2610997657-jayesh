# Question 04: Supermarket Bill Generator with Coupon Codes

> **Test:** Functions Practice Test  
> **Topic:** Functions, Default Arguments & Slabs  
> **Difficulty:** Medium | **Max Marks:** 10

---

## 📌 Problem Statement
A supermarket checkout system needs a modular bill generator function `generate_bill(cart_items, discount_code="")`.

### Parameters:
- `cart_items`: A list of tuples, where each tuple is `(item_name, quantity, unit_price)`
  - `item_name` (str)
  - `quantity` (int)
  - `unit_price` (float)
- `discount_code` (str, optional): A coupon code string. Defaults to `""`.

### Discount Rules:
1. **`"FESTIVE10"`**: Gives an unconditional **10% discount** on the subtotal.
2. **`"SUPER20"`**: Gives a **20% discount** ONLY IF the subtotal is **>= 1000.0**. If subtotal is < 1000.0, discount is **0%**.
3. **Any other code or empty string**: Gives **0% discount**.

### Returns:
Return a tuple of three floats:
`(subtotal, discount_amount, net_total)`

---

## 📥 Function Signature
```python
def generate_bill(cart_items, discount_code=""):
    # Returns (subtotal, discount_amount, net_total)
    pass
```

---

## 🧪 Sample Cases

### Sample 1:
- **Input:**
  `cart_items = [("Milk", 2, 40.0), ("Bread", 1, 30.0)]`, `discount_code = "FESTIVE10"`
- **Calculation:**
  - Subtotal = (2 * 40.0) + (1 * 30.0) = 80.0 + 30.0 = 110.0
  - Discount (10%) = 11.0
  - Net Total = 110.0 - 11.0 = 99.0
- **Expected Return:** `(110.0, 11.0, 99.0)`

### Sample 2:
- **Input:**
  `cart_items = [("Bag", 1, 500.0)]`, `discount_code = "SUPER20"`
- **Calculation:**
  - Subtotal = 500.0 (< 1000.0 threshold for SUPER20)
  - Discount = 0.0
  - Net Total = 500.0
- **Expected Return:** `(500.0, 0.0, 500.0)`
