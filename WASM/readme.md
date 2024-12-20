https://github.com/WebAssembly/wabt

Linux Install:

```
git clone --recursive https://github.com/WebAssembly/wabt
cd wabt
git submodule update --init
mkdir build
cd build
cmake ..
cmake --build .
```
hoặc 
`sudo apt install wabt`

Run: bin/wasm2wat <file> -o <outfile>

