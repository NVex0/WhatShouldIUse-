## Tool Collection

#### Powershell Deobfuscation.

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

- Brim Security / Zui: Wireshark tập trung show các chi tiết trong các packet chi tiết hết mức có thể. Brim thì ít chi tiết hơn nên xử lí được số lượng gói tin lớn. Ngoài ra, khác wireshark, tool này giống 1 tool giám sát an ninh mạng hơn. Nó có ngôn ngữ kịch bản riêng cho phép ta tạo trình tự động hoá dựa trên loại lưu lượng được giám sát. (Mình mới đọc docs chứ vừa tiếp cận tool này, chưa thấy nó hơn wireshark ở đâu :v)
