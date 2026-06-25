# Python Exception Chaining using `raise ... from`

## 📌 Overview

This project demonstrates **Exception Chaining** in Python using the `raise ... from` statement.
Exception chaining allows one exception to be raised while preserving information about another exception that caused it. This helps in debugging and provides better error tracing in complex applications.

In this example:

* An `AttributeError` is raised first.
* It is caught and stored as the underlying exception.
* A `ValueError` is then raised from the original exception.
* The main program accesses the original exception using the `__cause__` attribute.

---

## 🚀 Features

* Demonstrates exception chaining
* Uses `raise ... from`
* Preserves the original exception
* Accesses underlying exceptions using `__cause__`
* Beginner-friendly example of advanced exception handling

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text id="5axnzy"
├── exception_chaining.py
└── README.md
```

---

## 💻 Source Code

```python id="f8b2li"
def test():
    try:
        raise AttributeError("Underlying exception")
    except AttributeError as cause:
        raise ValueError("Main Exception") from cause


try:
    test()

except ValueError as ex:
    print("Main Exception :", ex)
    print("Underlying exception :", ex.__cause__)
```

---

## ▶️ How to Run

### Clone the Repository

```bash id="uqjjd4"
git clone https://github.com/your-username/python-exception-chaining.git
cd python-exception-chaining
```

### Run the Program

```bash id="pqvttj"
python exception_chaining.py
```

---

## 📋 Sample Output

```text id="pj1fhl"
Main Exception : Main Exception
Underlying exception : Underlying exception
```

---

## 🧠 Concepts Covered

* Exception Handling
* Exception Chaining
* `raise` Statement
* `raise ... from`
* `try-except` Blocks
* `__cause__` Attribute
* Debugging Techniques

---

## 🔍 How It Works

### Step 1: Raise Original Exception

```python id="ltc17u"
raise AttributeError("Underlying exception")
```

---

### Step 2: Catch and Chain the Exception

```python id="sksnca"
except AttributeError as cause:
    raise ValueError("Main Exception") from cause
```

The `ValueError` becomes the new exception while keeping the original `AttributeError` attached.

---

### Step 3: Access the Original Exception

```python id="92bh4x"
print(ex.__cause__)
```

Output:

```text id="0oq0ze"
Underlying exception
```

---

## 🎯 Why Use Exception Chaining?

Exception chaining is useful when:

* Wrapping low-level exceptions with more meaningful messages
* Building libraries and APIs
* Debugging large applications
* Preserving the original cause of an error

---

## 🌍 Real-World Applications

* Database applications
* Web frameworks
* REST APIs
* File handling systems
* Custom libraries and packages

---

## 🔮 Future Improvements

* Chain multiple exceptions
* Create custom exceptions with chaining
* Add logging for chained exceptions
* Demonstrate nested exception handling

---

## 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer
Aspiring Software Engineer | Python | SQL | Data Analytics

---

## 📄 License

This project is open-source and available for educational and learning purposes.

<img width="651" height="708" alt="image" src="https://github.com/user-attachments/assets/c4e2ab46-a244-44c4-9b5d-90a77112dd25" />
