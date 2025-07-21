# 🍵 Cafe Order System - Python Practice Project
# سیستم سفارش‌گیری ساده برای کافی‌شاپ (تمرین پایتون)

# Define menu with item prices / تعریف منو با قیمت آیتم‌ها
menu = {
    "قهوه": 30000,
    "چای": 15000,
    "کیک شکلاتی": 40000,
    "هات چاکلت": 25000
}

# Show the menu / نمایش منو
print("منوی کافه ما 🍵🍩")
for name, price in menu.items():
    print(f"{name}: {price} تومان")

# Take orders from user / گرفتن سفارش‌ها از کاربر
orders = []
while True:
    item = input("چی میل دارید؟ (برای اتمام بنویسید 'تمام') : ")
    if item == "تمام":
        break
    elif item in menu:
        orders.append(item)
        print(f"{item} به لیست اضافه شد ✅")
    else:
        print("این آیتم در منو وجود ندارد ❌")

# Display ordered items and calculate total price / نمایش سفارش و جمع‌زنی قیمت
total_price = 0
print("\nلیست سفارش شما:")
for i in orders:
    print(f"{i}: {menu[i]} تومان")
    total_price += menu[i]
print(f"قیمت نهایی: {total_price} تومان")

# Option to remove items before final confirmation / امکان حذف آیتم قبل از ثبت نهایی
while True:
    remove_i = input("آیا می‌خواید آیتمی رو حذف کنید؟ (بله/خیر): ")
    if remove_i.lower().strip() == "بله":
        remove_item = input("نام آیتمی که می‌خواید حذف کنید: ")
        if remove_item in orders:
            orders.remove(remove_item)
            total_price -= menu[remove_item]
            print(f"{remove_item} حذف شد ✅")
            print(f"قیمت جدید: {total_price} تومان")
        else:
            print("آیتمی با این نام در لیست سفارش نیست ❌")
    else:
        break

# Final confirmation and discount check / تأیید نهایی و بررسی تخفیف
sabt = input("آیا از سفارش خود مطمئنید؟ (بله/خیر): ")
if sabt.lower().strip() == "بله":
    print("\n🧾 فاکتور خرید شما:")
    for i in orders:
        print(f"{i}: {menu[i]} تومان")
    print(f"قیمت نهایی: {total_price} تومان")

    # Apply discount if eligible / اعمال تخفیف در صورت واجد شرایط بودن
    if total_price > 100000:
        discount = total_price * 0.10
        final_price = total_price - discount
        print("🎉 تبریک! چون مبلغ سفارش‌تون بالای ۱۰۰,۰۰۰ تومان هست، ۱۰٪ تخفیف گرفتید!")
        print(f"مبلغ قابل پرداخت بعد از تخفیف: {final_price} تومان")

    

    
    
    
    