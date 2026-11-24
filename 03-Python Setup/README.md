# Setting Up and Running Python Code Locally on Machine

A step-by-step guide to installing Python on your machine and running your first script — safely, correctly, and without the common setup headaches.

---

##  Overview

This guide walks through the essentials of getting Python running **on own machine**: downloading it safely, choosing the right installer, verifying the installation, and executing code both interactively and from a saved script file. By the end, you'll have a working local Python setup ready for real development.

---

##  Step 1: Download Python from the Official Source

Always download Python from the **official website** — never from third-party or unofficial sources. Unofficial installers can be corrupted or bundled with malware, which is a serious risk, especially for beginners who may not spot the warning signs.

---

##  Step 2: Choose the Right Installer

Select the installer that matches your **operating system** and **processor architecture**:

| Consideration | What to Check |
|---|---|
| **Operating System** | Windows, macOS, or Linux — pick the matching installer |
| **Processor Architecture** | 64-bit Intel/AMD vs. ARM (e.g., Apple Silicon) |

Installing the wrong version can cause failed installations or runtime errors, so verify your system specs before downloading.

---

##  Step 3: Verify the Installation

Open your terminal and run one of the following:

```bash
python --version
```

or

```bash
python3 --version
```

If Python isn't detected, it's either **not installed** or **not added to your system's PATH**. Both are common and fixable.

---

##  Step 4: Restart Your Terminal

This is the most common gotcha: **after installing Python, close and reopen your terminal**. Environment variables updated during installation don't apply to terminals that were already open — so commands will fail until you restart.

---

##  Step 5: Try the Interactive Python Prompt

Type `python` (or `python3`) in your terminal to enter the **interactive interpreter**. From there, you can run statements line-by-line:

```python
>>> print("hello")
hello
```

This is perfect for testing snippets and learning syntax quickly — no files needed.
