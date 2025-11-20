# dds_com


```bash

cd proj_cpp

# clean
rm -rf gen_c build

# mkdir
mkdir -p gen_c build

# generate C code from IDL (produces counter.c and counter.h in CWD)
idlc -l c counter.idl

# copy generated files
cp -v counter.c counter.h gen_c/


# configure & build
cmake -S . -B build \
  -DCYCLONEDDS_INCLUDE_DIR=/usr/local/include \
  -DCYCLONEDDS_LIB=/usr/local/lib/libddsc.so
cmake --build build -- -j

```