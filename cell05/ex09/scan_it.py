#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ 2 ตัวหรือไม่
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]

    count = text.count(keyword)

    if count == 0:
        print("none")
    else:
        print(count)