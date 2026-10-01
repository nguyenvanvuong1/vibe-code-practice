"""
Phat hien giao dich ke toan can kiem tra (KHONG ket luan gian lan) tu data/accounting/transactions.csv.

3 tieu chi doc lap:
  1. IQR outlier theo (type) - amount nam ngoai [Q1-1.5*IQR, Q3+1.5*IQR] trong nhom Revenue/Expense.
  2. Nguong nghiep vu - giao dich Cash co gia tri lon (thieu dau vet kiem toan ro rang).
  3. Giao dich trung lap - cung department + type + amount xuat hien nhieu lan (nguy co ghi so hai lan).

Ket qua xuat ra: transaction_id | rule | evidence | priority | suggested_check
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "accounting" / "transactions.csv"
OUT_DIR = Path(__file__).resolve().parent

CASH_THRESHOLD = 10000.0  # nguong nghiep vu: giao dich tien mat tren muc nay can doi chieu


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    return df


def rule_iqr_by_type(df: pd.DataFrame) -> list[dict]:
    """Tieu chi 1: IQR outlier tinh rieng cho Revenue va Expense (hai nhom co phan phoi khac nhau)."""
    flags = []
    for txn_type, group in df.groupby("type"):
        q1 = group["amount"].quantile(0.25)
        q3 = group["amount"].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers = group[(group["amount"] < lower) | (group["amount"] > upper)]
        for _, row in outliers.iterrows():
            ratio = row["amount"] / upper if upper > 0 else float("inf")
            priority = "High" if ratio >= 2 else "Medium"
            flags.append(
                {
                    "transaction_id": row["transaction_id"],
                    "rule": "IQR outlier (theo type)",
                    "evidence": (
                        f"amount={row['amount']:.2f}, type={txn_type}, "
                        f"nguong tren={upper:.2f} (Q1={q1:.2f}, Q3={q3:.2f}, IQR={iqr:.2f})"
                    ),
                    "priority": priority,
                    "suggested_check": "Doi chieu chung tu goc va nguoi phe duyet cho giao dich gia tri bat thuong",
                }
            )
    return flags


def rule_cash_threshold(df: pd.DataFrame) -> list[dict]:
    """Tieu chi 2: nguong nghiep vu - giao dich tien mat lon, kho xac minh doi tac/nguon goc."""
    flags = []
    cash_df = df[(df["payment_method"] == "Cash") & (df["amount"] > CASH_THRESHOLD)]
    for _, row in cash_df.iterrows():
        ratio = row["amount"] / CASH_THRESHOLD
        priority = "High" if ratio >= 1.3 else "Medium"
        flags.append(
            {
                "transaction_id": row["transaction_id"],
                "rule": "Nguong nghiep vu (Cash lon)",
                "evidence": f"amount={row['amount']:.2f}, payment_method=Cash, nguong={CASH_THRESHOLD:.2f}",
                "priority": priority,
                "suggested_check": "Yeu cau bien lai/chung tu thu chi tien mat va xac minh nguoi nhan/nguoi chi",
            }
        )
    return flags


def rule_duplicate_same_day(df: pd.DataFrame) -> list[dict]:
    """Tieu chi 3: cung ngay + department + type xuat hien > 1 lan, nguy co ghi so/boc tach but toan trung."""
    flags = []
    groups = df.groupby(["date", "department", "type"])["transaction_id"].agg(list)
    groups = groups[groups.apply(len) > 1]
    amount_by_id = df.set_index("transaction_id")["amount"]
    for (date, department, txn_type), ids in groups.items():
        for txn_id in ids:
            other_ids = [i for i in ids if i != txn_id]
            others_desc = ", ".join(f"{i} ({amount_by_id[i]:.2f})" for i in other_ids)
            flags.append(
                {
                    "transaction_id": txn_id,
                    "rule": "Trung ngay+phong ban+loai",
                    "evidence": (
                        f"date={date.date()}, department={department}, type={txn_type}, "
                        f"amount={amount_by_id[txn_id]:.2f}, cung nhom voi {others_desc}"
                    ),
                    "priority": "Medium",
                    "suggested_check": "Xac minh day co phai hai but toan doc lap hay mot giao dich bi tach/ghi lap hai lan",
                }
            )
    return flags


def main() -> None:
    df = load_data()

    all_flags = []
    all_flags.extend(rule_iqr_by_type(df))
    all_flags.extend(rule_cash_threshold(df))
    all_flags.extend(rule_duplicate_same_day(df))

    result_df = pd.DataFrame(all_flags, columns=["transaction_id", "rule", "evidence", "priority", "suggested_check"])
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    result_df["_sort"] = result_df["priority"].map(priority_order)
    result_df = result_df.sort_values(["_sort", "transaction_id"]).drop(columns="_sort")

    out_csv = OUT_DIR / "flags.csv"
    result_df.to_csv(out_csv, index=False)

    print(f"Tong so dong du lieu: {len(df)}")
    print(f"Tong so canh bao: {len(result_df)}")
    print(result_df["rule"].value_counts())
    print(f"\nDa luu chi tiet vao: {out_csv}")


if __name__ == "__main__":
    main()
