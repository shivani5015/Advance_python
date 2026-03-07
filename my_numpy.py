import numpy as np

# --- 1. ARRAY CREATION ---
# Manual creation
a = np.array([1, 2, 3])                 # 1D array
b = np.array([(1, 2, 3), (4, 5, 6)])    # 2D array (Matrix)

# Pre-filled placeholders
zeros = np.zeros((3, 4))                # 3x4 array of 0.0
ones = np.ones((2, 2), dtype=np.int16)  # 2x2 array of 1
eye = np.eye(3)                         # 3x3 identity matrix
empty = np.empty((2, 2))                # Random values (uninitialized)

# Sequences
arr_range = np.arange(10, 25, 5)        # Start, Stop, Step -> [10, 15, 20]
lin_space = np.linspace(0, 2, 9)        # 9 evenly spaced values between 0 and 2
random_arr = np.random.random((2, 2))   # 2x2 array of random floats [0, 1)

# --- 2. INSPECTION & PROPERTIES ---
print(f"Shape: {b.shape}")              # (rows, cols) -> (2, 3)
print(f"Dimensions: {b.ndim}")          # 2
print(f"Total Elements: {b.size}")      # 6
print(f"Data Type: {b.dtype}")          # int64 or int32
b_float = b.astype(float)               # Convert type

# --- 3. MATH & STATISTICS ---
# Element-wise operations
x = np.array([1, 2], dtype=np.float64)
y = np.array([5, 6], dtype=np.float64)

add = x + y                             # np.add(x, y)
sub = x - y                             # np.subtract(x, y)
mul = x * y                             # np.multiply(x, y)
div = x / y                             # np.divide(x, y)
exp = np.exp(x)                         # Exponential
sqrt = np.sqrt(x)                       # Square root

# Aggregates
print(f"Sum: {b.sum()}")
print(f"Min: {b.min()}")
print(f"Max along columns: {b.max(axis=0)}")
print(f"Mean: {b.mean()}")
print(f"Median: {np.median(b)}")

# --- 4. SLICING & INDEXING ---
# [row_start:row_stop, col_start:col_stop]
# 
slice_val = b[0, 1]                     # Row 0, Col 1 -> 2
row_slice = b[0:2, 1]                   # Rows 0-1, Col 1 -> [2, 5]
last_elem = b[-1, -1]                   # Last row, last col

# Boolean Indexing (Filtering)
filtered = b[b > 3]                     # Elements greater than 3 -> [4, 5, 6]

# --- 5. SHAPE MANIPULATION ---
reshaped = b.reshape(3, 2)              # Change to 3 rows, 2 cols
flattened = b.ravel()                   # Flatten to 1D array
transposed = b.T                        # Flip rows and columns

# Joining Arrays
c = np.array([7, 8, 9])
v_stack = np.vstack((a, c))             # Stack vertically
h_stack = np.hstack((a, c))             # Stack horizontally