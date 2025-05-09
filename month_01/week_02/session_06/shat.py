total_purchase = float(input("Худалдан авалтын дүн: "))
discount = 0  # discount-г эхэнд нь тодорхойлж өгнө

if total_purchase >= 200:
    discount = 0.3  # 30% хөнгөлөлт
else:
    is_member = input("Та гишүүн үү? (Tiim/Ugui): ").lower() == "tiim"
    
    if total_purchase >= 100:
        if is_member:
            discount = 0.2  # 20%
        else:
            discount = 0.1  # 10%
    elif total_purchase >= 50:
        if is_member:
            discount = 0.1  # 10%
        else:
            discount = 0.05  # 5%
    else:
        if is_member:
            discount = 0.05  # 5%
        else:
            discount = 0  # хөнгөлөлтгүй

final_price = total_purchase * (1 - discount)
print(f"Таны төлөх дүн: {final_price:.2f} төгрөг")

