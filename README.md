
# BomberPlusV2

[🇮🇷 مشاهده توضیحات فارسی](#-توضیحات-فارسی)

---

## 🇬🇧 English Description

**BomberPlusV2** is a Python-based email and SMS bomber tool designed for educational and testing purposes. It enables users to test bulk email delivery (via SMTP) and simulate OTP SMS delivery through public APIs of Iranian services.

> ⚠️ **Disclaimer:** This tool is intended for educational and authorized testing purposes only. Misuse can lead to legal consequences.

### ✨ Features

- 📧 **Email Bomber:** Send bulk emails with a custom SMTP account
- 📱 **SMS Bomber:** Send OTP requests to phone numbers using various Iranian services (Snapp, Divar, Tap30, etc.)
- 🚦 Internet connectivity check
- 🎯 Progress bar for email bombing
- 🎨 Beautiful CLI interface with colored output
- 🧵 Multi-threaded performance

### 🛠 Requirements

- Python 3.x
- `requests` library

Install requirements (if not already installed):

```bash
pip install requests
```

### 🚀 Usage

```bash
python BomberPlusV2.py
```
---

## 📧 **How to Enable Gmail for Email Sending in BomberPlusV2**

### Step 1: Enable **2-Step Verification** in Gmail

To use Gmail as the SMTP server in BomberPlusV2, you must first enable **2-Step Verification** on your Google account:

1. Log in to your Gmail account.
2. Go to the Google Account Security settings page: [Security](https://myaccount.google.com/security).
3. Under **"Signing in to Google"**, find and click **2-Step Verification**.
4. Follow the steps to activate 2-Step Verification.

### Step 2: Generate an **App Password**

After enabling 2-Step Verification, you need to create an **App Password** so BomberPlusV2 can access your Gmail account to send emails:

1. Visit the **App Passwords** page: [App Passwords](https://myaccount.google.com/apppasswords).
2. Log into your Gmail account if prompted.
3. Under **Select App**, choose **Mail**.
4. Under **Select Device**, choose **Other (Custom name)** and enter a name like "BomberPlusV2".
5. Click **Generate**. A 16-character app password will be shown.
6. Copy this password and use it as your sender password when running BomberPlusV2.

### Step 3: Configure BomberPlusV2

When you run BomberPlusV2 and choose the **Email Bomber** mode, you will be asked to enter the following:

- **Sender Email:** Your Gmail address (e.g., your_email@gmail.com).
- **Sender Password:** The App Password you generated in step 2.
- **Target Email:** The recipient email you want to bomb.
- **Email Count & Delay:** Number of emails to send and time delay between them.

### ⚠️ Important Note:
Never share your App Password with anyone. Keep it safe and use it only in trusted applications.

---

## 🇮🇷 توضیحات فارسی

[🔝 بازگشت به بخش انگلیسی](#-english-description)

**BomberPlusV2** یک ابزار تست ارسال انبوه پیامک و ایمیل بر پایه پایتون است که برای اهداف آموزشی و تست نفوذ طراحی شده.

> ⚠️ **هشدار:** استفاده از این ابزار فقط باید با رضایت هدف و برای اهداف قانونی باشد. سوء‌استفاده می‌تواند پیگرد قانونی داشته باشد.

### ✨ ویژگی‌ها

- 📧 ارسال انبوه ایمیل با استفاده از SMTP
- 📱 ارسال پیامک‌های OTP با استفاده از سرویس‌های ایرانی مانند Snapp، Tap30، Divar و ...
- 🚦 بررسی اتصال اینترنت
- 🎯 نمایش نوار پیشرفت در حالت ایمیل
- 🎨 رابط CLI زیبا با خروجی رنگی
- 🧵 اجرای چندنخی (Multi-threaded)

### 🛠 پیش‌نیازها

- پایتون ۳ به بالا
- نصب کتابخانه `requests`

برای نصب پیش‌نیاز:

```bash
pip install requests
```

### 🚀 نحوه استفاده

```bash
python BomberPlusV2.py
```

---

## 📧 **آموزش فعال‌سازی ارسال ایمیل با جیمیل در BomberPlusV2**

### مرحله ۱: فعال‌سازی **2-Step Verification** در جیمیل

برای استفاده از جیمیل به عنوان سرویس ارسال ایمیل در BomberPlusV2، ابتدا باید **2-Step Verification** (احراز هویت دو مرحله‌ای) را در اکانت جیمیل خود فعال کنید:

1. وارد حساب کاربری جیمیل خود شوید.
2. به صفحه تنظیمات امنیتی (Google Account Security) بروید: [Security](https://myaccount.google.com/security).
3. در بخش **Signing in to Google**، گزینه **2-Step Verification** را پیدا کرده و روی آن کلیک کنید.
4. مراحل احراز هویت دو مرحله‌ای را دنبال کنید و آن را فعال کنید.

### مرحله ۲: ایجاد **App Password** برای ارسال ایمیل

پس از فعال‌سازی احراز هویت دو مرحله‌ای، شما نیاز دارید که یک **App Password** ایجاد کنید تا BomberPlusV2 بتواند به حساب جیمیل شما برای ارسال ایمیل دسترسی داشته باشد:

1. به صفحه **Google App Passwords** بروید: [App Passwords](https://myaccount.google.com/apppasswords).
2. وارد حساب کاربری جیمیل خود شوید.
3. در بخش **Select App**، گزینه **Mail** را انتخاب کنید.
4. در بخش **Select Device**، گزینه **Other (Custom name)** را انتخاب کرده و نام دلخواه خود (مثلاً "BomberPlusV2") را وارد کنید.
5. روی **Generate** کلیک کنید. جیمیل یک رمز عبور مخصوص برای شما تولید می‌کند.
6. این رمز عبور را کپی کنید و در هنگام اجرای BomberPlusV2 به عنوان **رمز عبور فرستنده** وارد کنید.

### مرحله ۳: تنظیمات BomberPlusV2

هنگامی که BomberPlusV2 را اجرا کردید و حالت **Email Bomber** را انتخاب کردید، اطلاعات زیر را وارد کنید:

- **ایمیل فرستنده:** ایمیلی که App Password را برای آن ایجاد کردید (مثلاً your_email@gmail.com).
- **رمز عبور فرستنده:** همان App Password که در مرحله ۲ ایجاد کردید.
- **ایمیل هدف:** ایمیل فردی که می‌خواهید ایمیل‌ها را به او ارسال کنید.
- **تعداد ایمیل‌ها و تأخیر زمانی:** تعداد ایمیل‌هایی که می‌خواهید ارسال کنید و فاصله زمانی بین آن‌ها.

### نکته مهم:
شما نباید رمزی که ایجاد کردید را در اختیار کسی قرار دهید.

---

## 👨‍💻 Developer

- Developer: [*@Amirprx3*](https://t.me/Amirprx3)
- Telegram Channel: [*@Hacker_Plus_main*](https://t.me/Hacker_Plus_main)

---

## 📜 License

This project is licensed for ethical and educational use only.
