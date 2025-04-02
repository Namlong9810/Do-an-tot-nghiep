import pandas as pd
import numpy as np
from datetime import datetime, timedelta

df = pd.read_csv("fraud_dataset.csv")


# Chuyển đổi TransactionDate & PreviousTransactionDate về datetime

df["TransactionDate"] = pd.to_datetime(df["TransactionDate"], errors="coerce")
df["PreviousTransactionDate"] = pd.to_datetime(df["PreviousTransactionDate"], errors="coerce")


# Loại bỏ dữ liệu có ngày không hợp lệ

df = df.dropna(subset=["TransactionDate", "PreviousTransactionDate"])

# Cố đinh khoảng thời gian trong năm 2024 từ
start_date = datetime(2023,6,1)


# Xác đinh ngày đầu tiên thực hiện giao dịch của mỗi User

df["DateMin"] =  df.groupby("UserID")["TransactionDate"].transform("min")
# Tính khoảng cách giữa các giao dịch
df["TimeDiff"] = (df["TransactionDate"] - df["DateMin"]).dt.total_seconds()
# Tính khoảng cách giữa Thời gian giao dịch với thời gian giao dịch trước đó
df["TimeDiffWithTransaction"] = (df["TransactionDate"] - df["PreviousTransactionDate"]).dt.total_seconds()

# Cập nhật lại khoảng thời gian
df["TransactionDate"] = start_date + pd.to_timedelta(df["TimeDiff"], unit="s")
df["PreviousTransactionDate"] = df["TransactionDate"] - pd.to_timedelta(df["TimeDiffWithTransaction"], unit="s")

# Xóa cột tạm thời
df.drop(columns=["TimeDiff", "TimeDiffWithTransaction", "DateMin"], inplace= True)

df.to_csv("Transaction_date_fixed.csv", index = False)
print("cập nhật ngày tháng thành công")




