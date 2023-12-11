## Tool Collection

### Powershell Deobfuscation:

- https://github.com/Malandrone/PowerDecode
- https://github.com/R3MRUM/PSDecode

### Zip Known-Plain-Attack:

- https://github.com/keyunluo/pkcrack
- https://github.com/kimci86/bkcrack/blob/master/example/tutorial.md

### MacOS kcpassword crack (Nếu autologon mới làm được):
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

- Cho Py 3.10++ :
  + `https://github.com/zrax/pycdc`
    ```
    git clone https://github.com/zrax/pycdc
    cd pycdc
    cmake CMakeLists.txt
    make
    ./pycdc example.pyc
    ```

### VB Deobfuscate:
- Deob kí tự đặc biệt:
```
chars = list(map(lambda x: bytes([x]), set(open('out.txt', 'rb').read())))
specialChars = set(['\x00', b'\x80', b'\x81', b'\x82', b'\x83', b'\x84', b'\x85', b'\x92', b'\x93', b'\x94', b'\x95', b'\x96', b'\x98', b'\x99', b'\x9a', b'\x9b', b'\x9c', b'\xa0', b'\xa1', b'\xa2', b'\xa3', b'\xa4', b'\xa5', b'\xa6', b'\xa7', b'\xa8', b'\xa9', b'\xaa', b'\xab', b'\xac', b'\xae', b'\xaf', b'\xb0', b'\xb2', b'\xb3', b'\xb4', b'\xb5', b'\xb6', b'\xb7', b'\xb8', b'\xb9', b'\xba', b'\xbb', b'\xbc', b'\xbd', b'\xbe', b'\xbf', b'\xc2', b'\xc3', b'\xef'])
out = open('dumped.txt', 'rb').read()

curr = b''
specialCharSet = set()
specialCharSetInOQ = set()

for i in range(len(out)):
    b = out[i]
    if bytes([b]) in specialChars:
        curr += bytes([b])
    elif len(curr):
        specialCharSet.add(curr)
        curr = b''

specialCharList = list(specialCharSet)
specialCharList.sort(key=lambda x: len(x), reverse=True)

openQuote = False
for k in range(len(specialCharList)):
    sc = specialCharList[k]
    found = True
    while found:
        found = False
        curr = b''
        for i in range(len(out)):
            b = out[i]
            if bytes([b]) in specialChars:
                curr += bytes([b])
            elif len(curr):
                if not openQuote and sc == curr:
                    out = out[:i - len(curr)] + out[i - len(curr):].replace(curr, f'a{str(k)}'.encode('utf-8'), 1)
                    found = True
                    # print(i, out[i:i+100])
                    break
                curr = b''
            if b == 34:
                openQuote = not openQuote

open('formatted1.txt', 'wb').write(bytes(out))
```
### Batch Deobfuscate:

- https://github.com/DissectMalware/batch_deobfuscator

### OSINT lỏ.

- Overview: https://osintframework.com/

- "Harvesttttttt": https://github.com/laramies/theHarvester

### PE Unmapper.

- https://github.com/hasherezade/pe_unmapper

  PE sau khi lấy ra bằng Windbg(lm -> `db địa_chỉ_start L Length` hoặc `.writemem FileName BaseAddress EndAddress`). Thì dùng tool này để unmap địa chỉ lấy binary sạch :>

### Emulator cho shellcode (Run, call windows API,... nói chung là cho emu động luôn thay vì mình ngồi phân tích tĩnh):

- https://github.com/mandiant/speakeasy#adding-api-handlers
