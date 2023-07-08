## Tool Collection

### Powershell Deobfuscation.

- https://github.com/Malandrone/PowerDecode

### Zip Known-Plain-Attack:

- https://github.com/keyunluo/pkcrack
- https://github.com/kimci86/bkcrack/blob/master/example/tutorial.md

### MaoOS kcpassword crack (Nếu autologon mới làm được):
Xor key: `7d895223d2bcddeaa3b91f`

### Volatility 2 profile build:
##### Ubuntu.
- Nếu chưa có file zip thì docker để make zip, follow https://beguier.eu/nicolas/articles/security-tips-3-volatility-linux-profiles.html
- Lấy zip chứa info kernel các thứ nhồi vào `volatility/tools/linux` và `volatility/volatility/plugins/overlays/linux`
### Volatility 3 build profile (json):
- Step by step: https://beguier.eu/nicolas/articles/security-tips-3-volatility-linux-profiles.html

### Network:

- Brim Security / Zui: Wireshark tập trung show các chi tiết trong các packet chi tiết hết mức có thể. Brim thì ít chi tiết hơn nên xử lí được số lượng gói tin lớn. Ngoài ra, khác wireshark, tool này giống 1 tool giám sát an ninh mạng hơn. Nó có ngôn ngữ kịch bản riêng cho phép ta tạo trình tự động hoá dựa trên loại lưu lượng được giám sát.

### Reverse Exe to Py:
- Cho các Py ver cũ (3.10 đổ xuống) :
  + Step 1: `https://github.com/extremecoders-re/pyinstxtractor/tree/master`
    
  + Step 2: Uncompile file pyc của mang tên con exe gốc, dùng `Uncompyle6` - Python3.6.

- Cho Py 3.10 :
  + `https://github.com/zrax/pycdc`
    ```
    git clone https://github.com/zrax/pycdc
    cd pycdc
    cmake CMakeLists.txt
    make
    ./pycdc example.pyc
    ```
