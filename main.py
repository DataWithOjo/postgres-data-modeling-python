import psycopg2
import csv


def connect():
    return psycopg2.connect(
        dbname="postgres", user="postgres", password="postgres", host="db", port="5432"
    )


def execute_schema(cursor):
    with open("schema.sql", "r") as f:
        cursor.execute(f.read())


def load_accounts(cursor):
    with open("data/accounts.csv", newline="") as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [h.strip() for h in reader.fieldnames]  # trim header keys
        for row in reader:
            row = {k.strip(): v.strip() for k, v in row.items()}  # trim row values
            cursor.execute(
                """
                INSERT INTO accounts (customer_id, first_name, last_name, address_1, address_2, city, state, zip_code, join_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
                (
                    int(row["customer_id"]),
                    row["first_name"],
                    row["last_name"],
                    row["address_1"],
                    row.get("address_2") or None,
                    row["city"],
                    row["state"],
                    row["zip_code"],
                    row["join_date"],
                ),
            )


def load_products(cursor):
    with open("data/products.csv", newline="") as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [h.strip() for h in reader.fieldnames]  # clean headers
        for row in reader:
            row = {k.strip(): v.strip() for k, v in row.items()}  # clean values
            cursor.execute(
                """
                INSERT INTO products (product_id, product_code, product_description)
                VALUES (%s, %s, %s)
            """,
                (
                    int(row["product_id"]),
                    row["product_code"],
                    row["product_description"],
                ),
            )


def load_transactions(cursor):
    with open("data/transactions.csv", newline="") as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [h.strip() for h in reader.fieldnames]
        for row in reader:
            row = {k.strip(): v.strip() for k, v in row.items()}
            cursor.execute(
                """
                INSERT INTO transactions (
                    transaction_id, transaction_date, product_id,
                    product_code, product_description, quantity, account_id
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
                (
                    row["transaction_id"],
                    row["transaction_date"],
                    int(row["product_id"]),
                    row["product_code"],
                    row["product_description"],
                    int(row["quantity"]),
                    int(row["account_id"]),
                ),
            )


def main():
    conn = connect()
    cursor = conn.cursor()

    # Create tables
    execute_schema(cursor)

    # Insert data
    load_accounts(cursor)
    load_products(cursor)
    load_transactions(cursor)

    conn.commit()
    cursor.close()
    conn.close()
    print("All tables created and data loaded.")


if __name__ == "__main__":
    main()
