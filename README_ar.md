# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" /> مستودع سكريبتات بايثون <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Logo" width="52" height="30" />

![قيد التطوير](https://img.shields.io/badge/الحالة-قيد%20التطوير-yellow)

## 🌐 
[![البرتغالية](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![الإسبانية](https://img.shields.io/badge/Español-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![الإنجليزية](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![الروسية](https://img.shields.io/badge/Russian-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![الصينية](https://img.shields.io/badge/Chinese-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![العربية](https://img.shields.io/badge/Arabic-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

<details>
<summary> 
  <h2>
    حول المستودع
  </h2>
</summary>

هذا المستودع يحتوي على سكريبتات بايثون قيد التطوير. حاليًا، يتضمن المستودع سكريبت يستخدم Selenium WebDriver للتفاعل مع صفحات الويب.

</details>

<details>
<summary><h2>المتطلبات</h2></summary>

قبل تشغيل السكريبت، تحتاج إلى تثبيت بعض المتطلبات الأساسية:

- بايثون 3.x
- Pip (مدير حزم بايثون)
- [جوجل كروم](https://www.google.com/chrome/) (أو أي متصفح آخر متوافق مع Selenium WebDriver)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (إذا لم تستخدم `webdriver_manager`)

</details>

<details>
<summary><h2>إعداد البيئة</h2></summary>

1. **استنساخ المستودع:**

   ```bash
   git clone https://github.com/usuario/repo.git
   cd repo
   ```

2. **إنشاء ملف `.env` في جذر المشروع** مع تحديد موقع الملف الثنائي للمتصفح:

   ```env
   CHROME_BINARY_LOCATION=/المسار/إلى/جوجل/كروم
   ```

   **ملاحظة:** تأكد من استبدال `/المسار/إلى/جوجل/كروم` بالمسار الفعلي للملف الثنائي للمتصفح على جهازك.

3. **تثبيت تبعيات المشروع:**

   ```bash
   pip install -r requirements.txt
   ```

   يجب أن يحتوي ملف `requirements.txt` على المكتبات التالية:

   ```
   selenium
   webdriver-manager
   python-dotenv
   ```

   يمكنك إنشاء هذا الملف باستخدام الأمر التالي:

   ```bash
   pip freeze > requirements.txt
   ```

</details>

<details>
<summary><h2>تشغيل السكريبت</h2></summary>

1. **قم بتشغيل سكريبت بايثون:**

   ```bash
   python3 /المسار/إلى/سكريبتك/vagas.py
   ```

   تأكد من تعديل مسار السكريبت حسب الحاجة.

</details>

<details>
<summary><h2>مشاريع أخرى</h2></summary>

-  [طلبات المطعم](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ar.md)
-  [الخوارزميات](https://github.com/SamuelRocha91/Algorithms/blob/main/README_ar.md)
-  [Trybe ليس جوجل](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

</details>