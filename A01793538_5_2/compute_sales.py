"""Modulos estandar para ejecucion de programa calculo de ventas"""
import json
import sys
import time


def load_json_file(filename):
    """Funcion para leer archivo JSON"""

    try:
        with open(filename, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{filename}'.")
        return None


def print_results(t_cost, items_list, exec_time):
    """Funcion para imprimir resultados"""

    p = "Product"
    q = "Quantity"
    u = "Unit Price"
    s = "Subtotal"

    with open("SalesResults.txt", 'w', encoding="utf-8") as r_file:
        print("\n" + "*"*40 + "Invoice" + "*"*40)
        r_file.write("*"*40 + "Invoice" + "*"*40)
        print(f"\n{p:30}{q:20}{u:20}{s:20}")
        r_file.write(f"\n{p:30}{q:20}{u:20}{s:20}\n")
        print("-"*90)
        r_file.write("-"*90 + "\n")

        for item in items_list:
            prod, sold, p_unit, s_total = item
            print(f"{prod:30}{sold:15}{p_unit:15.2f}{s_total:15.2f}")
            r_file.write(f"{prod:30}{sold:15}{p_unit:15.2f}{s_total:15.2f}\n")

        print("-"*90)
        r_file.write("-"*90 + "\n")
        t = "Total:"
        print(f"{t:70}{t_cost:.2f}")
        r_file.write(f"{t:70}{t_cost:.2f}\n")
        print("*"*90)
        r_file.write("*"*90 + "\n")
        print(f"\nTime elapsed: {exec_time} seconds")
        r_file.write(f"\nTime elapsed: {exec_time} seconds")


def compute_total_sales(p_catalogue, sales_record):
    """Funcion para calcular ventas"""

    total_cost = 0
    items_list = []

    for sale in sales_record:
        prod = sale.get("Product")
        sold = sale.get("Quantity")
        if sold > 0:
            match_products = [p for p in p_catalogue if p.get("title") == prod]
            if match_products:
                price_per_unit = match_products[0].get("price")
                subtotal = price_per_unit * sold
                total_cost += subtotal
                items_list.append((prod, sold, price_per_unit, subtotal))
            else:
                print(f"Product '{prod}' not found in the price catalogue.\n")
        else:
            print(f"'{prod}' cannot be sold {sold} times.\n")

    return total_cost, items_list


def main():
    """Funcion principal"""

    start_time = time.time()

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    price_catalogue = load_json_file(price_catalogue_file)
    sales_record = load_json_file(sales_record_file)

    if price_catalogue is None or sales_record is None:
        return

    print("\n")
    t_cost, items_list = compute_total_sales(price_catalogue, sales_record)

    end_time = time.time()

    print_results(t_cost, items_list, end_time - start_time)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: ")
        print("python compute_sales.py \"catalogue\".json \"sales\".json")
        sys.exit()

    main()
