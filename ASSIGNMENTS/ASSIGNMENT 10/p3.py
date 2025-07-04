import numpy as np

arr = np.array([[6, np.nan, 73],
                [4, 12, np.nan]])
print(arr)
col_mean = np.nanmean(arr, axis=0)
ind = np.where(np.isnan(arr))
arr[ind] = np.take(col_mean, ind[1])
print("NaN replaced with column mean:\n", arr)