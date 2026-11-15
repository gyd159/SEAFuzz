# Experiment setup: AFL, Entropic, and 16 targets

SEAFuzz and the AFL-based DiPri port are described in [`implementation_and_baselines.md`](implementation_and_baselines.md); the same file records baseline source versions and local modifications.

This document consolidates the actual build records for all 16 targets listed in the table below.  The AFL and Entropic build pipelines are both documented in this file so that the final docs directory has one authoritative experiment setup record.

## Target Inventory

The experiment includes eight standalone projects and eight tools from
GNU binutils 2.40:

| Group                              | Target     | Input mode         | Main artifact        |
| ---------------------------------- | ---------- | ------------------ | -------------------- |
| Standalone project(From Magma)     | libpng     | File argument `@@` | `libpng_read_fuzzer` |
| Standalone project(From Magma)     | libsndfile | File argument `@@` | `sndfile_fuzzer`     |
| Standalone project(From Magma)     | Lua        | File argument `@@` | `lua`                |
| Standalone project(From Magma)     | PHP        | File argument `@@` | `parser`             |
| Standalone project(From Magma)     | Poppler    | File argument `@@` | `poppler_pdf_fuzzer` |
| Standalone project(From Magma)     | SQLite 3   | File argument `@@` | `sqlite3_fuzz`       |
| Standalone project(From FuzzBench) | Bloaty     | File argument `@@` | `fuzz_target_afl`    |
| Standalone project(From FuzzBench) | RE2        | File argument `@@` | `fuzzer_afl`         |
| binutils                           | cxxfilt    | Standard input     | `binutils/cxxfilt`   |
| binutils                           | as-new     | File argument `@@` | `gas/as-new`         |
| binutils                           | objcopy    | File argument `@@` | `binutils/objcopy`   |
| binutils                           | nm-new     | File argument `@@` | `binutils/nm-new`    |
| binutils                           | objdump    | File argument `@@` | `binutils/objdump`   |
| binutils                           | readelf    | File argument `@@` | `binutils/readelf`   |
| binutils                           | size       | File argument `@@` | `binutils/size`      |
| binutils                           | strip-new  | File argument `@@` | `binutils/strip-new` |

## 1. Target inventory and directory variables

The following variables reflect the current experiment directory layout.

``` sh
export AFL_ROOT="${AFL_ROOT:-$HOME/AFL}"
export MAGMA_ROOT="${MAGMA_ROOT:-$HOME/magma}"

export LIBPNG_ROOT="${LIBPNG_ROOT:-$HOME/fuzzing_libpng}"
export LIBSNDFILE_ROOT="${LIBSNDFILE_ROOT:-$HOME/fuzzing_libsndfile}"
export LUA_ROOT="${LUA_ROOT:-$HOME/fuzzing_lua}"
export PHP_ROOT="${PHP_ROOT:-$HOME/fuzzing_php}"
export POPPLER_ROOT="${POPLER_ROOT:-$HOME/fuzzing_poppler}"
export SQLITE_ROOT="${SQLITE_ROOT:-$HOME/fuzzing_sqlite}"
export BLOATY_ROOT="${BLOATY_ROOT:-$HOME/fuzzing_bloaty}"
export RE2_ROOT="${RE2_ROOT:-$HOME/fuzzing_re2}"
export BINUTILS_ROOT="${BINUTILS_ROOT:-$HOME/real_project}"

export PATH="$AFL_ROOT:$PATH"
export AFL_PATH="$AFL_ROOT"
```

On the original machine these variables pointed to the AFL, Magma, eight standalone-project, and binutils checkouts. 

## 2. Toolchain and dependencies

The experiment records use the LLVM wrapper from AFL 2.57b (commit `61037103ae3722c8060ff7082994836a794f978e`), Clang/LLVM 10, CMake 3.16, Autoconf 2.69, and GNU Make 4.2. Base dependencies may be adjusted for the distribution; on Ubuntu, install the following packages first:

``` sh
sudo apt-get update
sudo apt-get install -y \
  build-essential clang llvm cmake autoconf automake libtool pkg-config \
  bison flex texinfo zlib1g-dev libzstd-dev tcl python3 re2c autogen \
  libfreetype6-dev libcairo2-dev libopenjp2-7-dev libpng-dev \
  libtiff-dev libjpeg-dev liblcms2-dev libfontconfig1-dev
```

Build AFL’s LLVM instrumentation wrapper first:

``` sh
make -C "$AFL_ROOT/llvm_mode"
test -x "$AFL_ROOT/afl-clang-fast"
test -x "$AFL_ROOT/afl-clang-fast++"
```

Common ASan/AFL settings for target builds(Before running the fuzzing experiments, we executed the `afl-system-config` script from the AFL++ project to configure the Linux system environment, including CPU frequency scaling and kernel core dump settings. ):

``` sh
export AS=/usr/bin/as
export CC="$AFL_ROOT/afl-clang-fast"
export CXX="$AFL_ROOT/afl-clang-fast++"
export AFL_USE_ASAN=1
export CFLAGS="-O1 -g -fno-omit-frame-pointer -fsanitize=address"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-fsanitize=address"


sudo bash AFLplusplus/afl-system-config
export ASAN_OPTIONS='abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1'
```

## 3. Source versions and local modifications

| Target     | Baseline version                                       |
|------------|--------------------------------------------------------|
| libpng     | 1.6.38.git，`a37d4836519517bdce6cb9d956092321eca3e73b` |
| libsndfile | 1.1.0beta1，`86c9f9eb7022d186ad4d0689487e7d4f04ce2b29` |
| Lua        | 5.4.4，`dbdc74dc5502c2e05e1c1e2ac894943f418c8431`      |
| PHP        | 8.1.0-dev，`bc39abe8c3c492e29bc5d60ca58442040bbf063b`  |
| Poppler    | 21.07.0，`1d23101ccebe14261c6afc024ea14f29d209e760`    |
| SQLite     | SQLite 3.37.0 source release                           |
| Bloaty     | 1.1，`52948c107c8f81045e7f9223ec02706b19cfa882`        |
| RE2        | `b025c6a3ae05995660e3b882eb3277f4399ced1a`             |
| binutils   | GNU binutils 2.40 source release                       |

The current target trees already contain local modifications and generated files. When starting from clean source, apply the patches in the sections below first.

Magma targets normally do not define `MAGMA_ENABLE_FIXES`, because the fixes branch would mask the vulnerabilities. Enable `MAGMA_ENABLE_CANARIES` only when Canary logging is required.

``` sh
# libpng
cd "$LIBPNG_ROOT/libpng"
patch -p1 --fuzz=3 < "$MAGMA_ROOT/targets/libpng/patches/setup/libpng16.patch"
for p in "$MAGMA_ROOT"/targets/libpng/patches/bugs/PNG0*.patch; do patch -p1 < "$p"; done

# libsndfile
cd "$LIBSNDFILE_ROOT/libsndfile"
patch -p1 --fuzz=3 < "$MAGMA_ROOT/targets/libsndfile/patches/setup/libsndfile.patch"
for p in "$MAGMA_ROOT"/targets/libsndfile/patches/bugs/SND*.patch; do patch -p1 < "$p"; done

# Lua
cd "$LUA_ROOT/lua"
patch -p1 --fuzz=3 < "$MAGMA_ROOT/targets/lua/patches/setup/lua.patch"
for p in "$MAGMA_ROOT"/targets/lua/patches/bugs/LUA0*.patch; do patch -p1 < "$p"; done

# PHP
cd "$PHP_ROOT/php-src"
patch -p1 --fuzz=3 < "$MAGMA_ROOT/targets/php/patches/setup/setup.patch"
for p in "$MAGMA_ROOT"/targets/php/patches/bugs/PHP0*.patch; do patch -p1 < "$p"; done

# Poppler (no separate setup patch is recorded)
cd "$POPLER_ROOT/poppler"
for p in "$MAGMA_ROOT"/targets/poppler/patches/bugs/PDF*.patch; do patch -p1 --forward < "$p"; done

# SQLite
cd "$SQLITE_ROOT/sqlite"
patch -p1 --fuzz=3 < "$MAGMA_ROOT/targets/sqlite3/patches/setup/tclexec-ignore-stderr.patch"
for p in "$MAGMA_ROOT"/targets/sqlite3/patches/bugs/SQL0*.patch; do patch -p1 < "$p"; done
```

Lua also contains source modifications added for experimental stability: the hash seed, `math.random`, the `table.sort` pivot, and time are fixed, while `os.execute`, `io.popen`, `os.tmpname`, and `io.tmpfile`
are disabled. 

## 4. Eight standalone projects

### 4.1 libpng

The target source is `$LIBPNG_ROOT/libpng`. The recorded target version is libpng 1.6.38.git, with `PNG001`–`PNG007` applied.

``` sh
cd "$LIBPNG_ROOT/libpng"
make distclean 2>/dev/null || make clean 2>/dev/null || true

export AS=/usr/bin/as
export CC="$AFL_ROOT/afl-clang-fast"
export CXX="$AFL_ROOT/afl-clang-fast++"
export AFL_USE_ASAN=1
export CFLAGS="-O1 -g -fno-omit-frame-pointer -fsanitize=address"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-fsanitize=address"

./configure --disable-shared --enable-static
make -j"$(nproc)"

# contrib/oss-fuzz/afl_driver.cpp is the AFL main() driver added in the experiment record
"$AFL_ROOT/afl-clang-fast++" -O1 -g -fno-omit-frame-pointer \
  -fsanitize=address -I. -Icontrib/oss-fuzz \
  contrib/oss-fuzz/libpng_read_fuzzer.cc \
  contrib/oss-fuzz/afl_driver.cpp .libs/libpng16.a -lz -lm \
  -o "$LIBPNG_ROOT/libpng_read_fuzzer"
```

Artifact: `$LIBPNG_ROOT/libpng_read_fuzzer`; invoke it at runtime as `libpng_read_fuzzer @@`.

### 4.2 libsndfile

The libsndfile build record requires running `autogen.sh` first; the actual build uses non-parallel `make`.

``` sh
cd "$LIBSNDFILE_ROOT/libsndfile"
./autogen.sh

export AS=/usr/bin/as
export CC="$AFL_ROOT/afl-clang-fast"
export CXX="$AFL_ROOT/afl-clang-fast++"
export AFL_USE_ASAN=1
export ASAN_OPTIONS=detect_leaks=0
export CFLAGS="-O1 -g -fno-omit-frame-pointer -fsanitize=address"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-fsanitize=address"

./configure --disable-shared --enable-ossfuzzers
make
test -x ossfuzz/sndfile_fuzzer
```

Artifact: `$LIBSNDFILE_ROOT/libsndfile/ossfuzz/sndfile_fuzzer`. If `/usr/bin/python` is absent, the record uses a temporary symlink to `python3`; do not commit that symlink to the repository.

### 4.3 Lua

The Lua AFL target is the interpreter itself; readline is disabled.

``` sh
cd "$LUA_ROOT/lua"
make clean 2>/dev/null || true

export AS=/usr/bin/as
export CC="$AFL_ROOT/afl-clang-fast"
export CXX="$AFL_ROOT/afl-clang-fast++"
export AFL_USE_ASAN=1
export CFLAGS="-O1 -g -fno-omit-frame-pointer -fsanitize=address"
export LDFLAGS="-fsanitize=address"

make \
  CFLAGS="$CFLAGS -std=c99 -DLUA_USE_LINUX -fno-stack-protector -fno-common -march=native" \
  MYLDFLAGS="$LDFLAGS -Wl,-E" \
  MYLIBS="-ldl"

test -x lua
test -f liblua.a
```

The runtime target is `lua @@`. 

### 4.4 PHP

The PHP record uses the PHP 8.1.0-dev fuzzer SAPI and replaces libFuzzer’s `main` with an AFL driver. If the build machine does not have libc++, set `FUZZING_CC` to `$CXX` in `sapi/fuzzer/config.m4` to avoid automatically adding `-stdlib=libc++`.

Prepare the driver first (reuses the AFL driver from libpng):

``` sh
cp "$LIBPNG_ROOT/libpng/contrib/oss-fuzz/afl_driver.cpp" "$PHP_ROOT/afl_driver.cpp"
"$AFL_ROOT/afl-clang-fast++" -O1 -g -fno-omit-frame-pointer \
  -fsanitize=address -c "$PHP_ROOT/afl_driver.cpp" \
  -o "$PHP_ROOT/afl_driver.o"
```

Build PHP:

``` sh
cd "$PHP_ROOT/php-src"
export AS=/usr/bin/as
export CC="$AFL_ROOT/afl-clang-fast"
export CXX="$AFL_ROOT/afl-clang-fast++"
export AFL_USE_ASAN=1
export ASAN_OPTIONS=detect_leaks=0
export LSAN_OPTIONS=verbosity=0
export RE2C=/usr/bin/re2c
export CFLAGS="-O1 -g -fno-omit-frame-pointer -fsanitize=address"
export CXXFLAGS="$CFLAGS"
export EXTRA_CFLAGS="$CFLAGS -fno-sanitize=object-size"
export EXTRA_CXXFLAGS="$CXXFLAGS -fno-sanitize=object-size"
unset CFLAGS CXXFLAGS

LIB_FUZZING_ENGINE="$PHP_ROOT/afl_driver.o" ./configure \
  --disable-all --enable-option-checking=fatal --enable-fuzzer \
  --enable-exif --enable-phar --enable-intl --without-pcre-jit \
  --disable-phpdbg --disable-cgi --with-pic
make
```

The outputs are `parser`, `json`, `exif`, `unserialize`, `unserializehash`, and `execute`. 

### 4.5 Poppler

The record uses Poppler 21.07.0, Debug mode, static libraries, and ASan.
The build requires development packages for FreeType, Cairo, OpenJPEG,
PNG, TIFF, JPEG, LCMS2, and zlib.

``` sh
export AS=/usr/bin/as
export CC="$AFL_ROOT/afl-clang-fast"
export CXX="$AFL_ROOT/afl-clang-fast++"
export AFL_USE_ASAN=1
export CFLAGS="-O1 -g -fno-omit-frame-pointer -fsanitize=address"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-fsanitize=address"

export POPPLER_SRC="$POPLER_ROOT/poppler"
export POPPLER_BUILD="$POPLER_ROOT/poppler/build"
rm -rf "$POPPLER_BUILD"
cmake -S "$POPPLER_SRC" -B "$POPPLER_BUILD" \
  -DCMAKE_BUILD_TYPE=Debug -DBUILD_SHARED_LIBS=OFF \
  -DENABLE_CPP=ON \
  -DFONT_CONFIGURATION=generic -DBUILD_GTK_TESTS=OFF \
  -DBUILD_QT5_TESTS=OFF -DBUILD_CPP_TESTS=OFF \
  -DENABLE_GLIB=OFF -DENABLE_GOBJECT_INTROSPECTION=OFF \
  -DENABLE_QT5=OFF -DENABLE_LIBCURL=OFF -DWITH_NSS3=OFF \
  -DENABLE_BOOST=OFF
cmake --build "$POPPLER_BUILD"

test -f "$POPLER_ROOT/afl_driver.cpp" || \
  cp "$LIBPNG_ROOT/libpng/contrib/oss-fuzz/afl_driver.cpp" "$POPLER_ROOT/afl_driver.cpp"
"$AFL_ROOT/afl-clang-fast++" -O1 -g -fno-omit-frame-pointer -fsanitize=address \
  -I"$POPPLER_BUILD/cpp" -I"$POPPLER_SRC/cpp" \
  -I"$POPPLER_BUILD/poppler" -I"$POPPLER_SRC/poppler" \
  "$MAGMA_ROOT/targets/poppler/src/pdf_fuzzer.cc" "$POPLER_ROOT/afl_driver.cpp" \
  "$POPPLER_BUILD/cpp/libpoppler-cpp.a" "$POPPLER_BUILD/libpoppler.a" \
  -lfreetype -lcairo -lopenjp2 -lpng -ltiff -ljpeg -llcms2 -lz -lm -lpthread \
  -o "$POPLER_ROOT/poppler_pdf_fuzzer"
```

### 4.6 SQLite 3

SQLite 3.37.0 uses the Magma setup patch and `SQL001`–`SQL020`. The local `test/afl_driver.c` wraps `LLVMFuzzerTestOneInput` as an AFL file-input program.

``` sh
cd "$SQLITE_ROOT/sqlite"
make distclean 2>/dev/null || make clean 2>/dev/null || true
export CC="$AFL_ROOT/afl-clang-fast"
export CXX="$AFL_ROOT/afl-clang-fast++"
export AFL_USE_ASAN=1
export CFLAGS="-O1 -g -fno-omit-frame-pointer -fsanitize=address \
  -DSQLITE_MAX_LENGTH=128000000 -DSQLITE_MAX_SQL_LENGTH=128000000 \
  -DSQLITE_MAX_MEMORY=25000000 -DSQLITE_PRINTF_PRECISION_LIMIT=1048576 \
  -DSQLITE_DEBUG=1 -DSQLITE_MAX_PAGE_COUNT=16384"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-fsanitize=address"

./configure --disable-shared --enable-rtree
make clean
make -j"$(nproc)"
make sqlite3.c                 # Run this when tclsh is needed to generate the amalgamation

"$AFL_ROOT/afl-clang-fast" -fsanitize=address -I. \
  test/ossfuzz.c test/afl_driver.c sqlite3.o \
  -o "$SQLITE_ROOT/sqlite3_fuzz" -pthread -ldl -lm
```

The artifact is `$SQLITE_ROOT/sqlite3_fuzz`; invoke it at runtime as `sqlite3_fuzz @@`. 

### 4.7 Bloaty

The Bloaty 1.1 record uses CMake, the AFL wrapper, ASan, and `-j2`.

``` sh
export CC="$AFL_ROOT/afl-clang-fast"
export CXX="$AFL_ROOT/afl-clang-fast++"
export CFLAGS="-O1 -g -fsanitize=address -fno-omit-frame-pointer"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-fsanitize=address"

export BLOATY_SRC="$BLOATY_ROOT/bloaty"
export BLOATY_BUILD="$BLOATY_ROOT/work"
cmake -S "$BLOATY_SRC" -B "$BLOATY_BUILD" -DBUILD_TESTING=false
cmake --build "$BLOATY_BUILD" -j2 \
  --target libbloaty re2 capstone-static libprotobuf

"$CXX" -O1 -g -fsanitize=address -fno-omit-frame-pointer -std=c++17 \
  -I"$BLOATY_SRC" -I"$BLOATY_SRC/src" -I"$BLOATY_BUILD/src" \
  -I"$BLOATY_SRC/third_party/abseil-cpp" \
  -I"$BLOATY_SRC/third_party/protobuf/src" \
  -I"$BLOATY_SRC/third_party/capstone/include" \
  -I"$BLOATY_SRC/third_party/re2" \
  "$BLOATY_SRC/tests/fuzz_target.cc" "$BLOATY_SRC/tests/fuzz_driver.cc" \
  "$BLOATY_BUILD/liblibbloaty.a" \
  "$BLOATY_BUILD/third_party/re2/libre2.a" \
  "$BLOATY_BUILD/third_party/capstone/libcapstone.a" \
  "$BLOATY_BUILD/third_party/protobuf/cmake/libprotobuf.a" \
  -lz -lpthread -o "$BLOATY_BUILD/fuzz_target_afl"
```

### 4.8 RE2

The RE2 AFL harness uses FuzzBench’s `re2_fuzzer/target.cc` and the experiment-local `fuzz_driver.cc`.

``` sh
export CC="$AFL_ROOT/afl-clang-fast"
export CXX="$AFL_ROOT/afl-clang-fast++"
export CFLAGS="-O1 -g -fsanitize=address -fno-omit-frame-pointer"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-fsanitize=address"

make -C "$RE2_ROOT/re2" -j2

"$CXX" -O1 -g -fsanitize=address -fno-omit-frame-pointer \
  "$HOME/fuzzbench/benchmarks/re2_fuzzer/target.cc" \
  "$RE2_ROOT/fuzz_driver.cc" -I"$RE2_ROOT/re2" \
  "$RE2_ROOT/re2/obj/libre2.a" -lpthread \
  -o "$RE2_ROOT/fuzzer_afl"
```

If FuzzBench is not located at `$HOME/fuzzbench`, change the first source-file path to `benchmarks/re2_fuzzer/target.cc` in the corresponding checkout.

## 5. GNU binutils 2.40 and eight tools

All eight binutils targets share one source tree and build directory. The record uses `$BINUTILS_ROOT/binutils-2.40`, with `$BINUTILS_ROOT/build-afl-asan` as the configuration directory.

``` sh
mkdir -p "$BINUTILS_ROOT/build-afl-asan"
cd "$BINUTILS_ROOT/build-afl-asan"

export AS=/usr/bin/as
export CC="$AFL_ROOT/afl-clang-fast"
export CXX="$AFL_ROOT/afl-clang-fast++"
export AFL_USE_ASAN=1
export ASAN_OPTIONS='abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1'

../binutils-2.40/configure \
  --disable-shared --disable-nls --disable-werror \
  CC="$CC" CXX="$CXX"
make
```

After the build, the target portion of the AFL command is as follows. `cxxfilt` reads from standard input, so its command does not use `@@`; the other seven targets read a file argument.

``` text
binutils/cxxfilt
gas/as-new -o /dev/null @@
binutils/objcopy @@ /dev/null
binutils/nm-new -a @@
binutils/objdump -d @@
binutils/readelf -a @@
binutils/size -A -x @@
binutils/strip-new -o /dev/null @@
```

## 6. Post-build checks

``` sh
test -x "$LIBPNG_ROOT/libpng_read_fuzzer"
test -x "$LIBSNDFILE_ROOT/libsndfile/ossfuzz/sndfile_fuzzer"
test -x "$LUA_ROOT/lua/lua"
for t in parser json exif unserialize unserializehash execute; do
  test -x "$PHP_ROOT/$t"
done
test -x "$POPLER_ROOT/poppler_pdf_fuzzer"
test -x "$SQLITE_ROOT/sqlite3_fuzz"
test -x "$BLOATY_ROOT/work/fuzz_target_afl"
test -x "$RE2_ROOT/fuzzer_afl"
for t in \
  "$BINUTILS_ROOT/build-afl-asan/binutils/cxxfilt" \
  "$BINUTILS_ROOT/build-afl-asan/gas/as-new" \
  "$BINUTILS_ROOT/build-afl-asan/binutils/objcopy" \
  "$BINUTILS_ROOT/build-afl-asan/binutils/nm-new" \
  "$BINUTILS_ROOT/build-afl-asan/binutils/objdump" \
  "$BINUTILS_ROOT/build-afl-asan/binutils/readelf" \
  "$BINUTILS_ROOT/build-afl-asan/binutils/size" \
  "$BINUTILS_ROOT/build-afl-asan/binutils/strip-new"; do
  test -x "$t"
done
```

Single-run AFL command template (the target must pass the checks above first):

``` sh
mkdir -p "$LIBPNG_ROOT/output/afl/out0"
"$AFL_ROOT/afl-fuzz" \
  -i "$LIBPNG_ROOT/seeds" \
  -o "$LIBPNG_ROOT/output/afl/out0" \
  -m none -d -- "$LIBPNG_ROOT/libpng_read_fuzzer" @@
```

The formal evaluation record specifies ten runs per configuration, each lasting 24 hours. 

## 7. Reproducibility notes

1.  A target directory may already contain Magma patches; applying them twice will fail. Start from a clean checkout when rebuilding.
2.  Do not set `MAGMA_ENABLE_FIXES`. Set `MAGMA_ENABLE_CANARIES` only when the canary log is intentionally required.
3.  PHP `config.m4`, SQLite `test/afl_driver.c`, the libpng/Poppler AFL drivers, and Lua’s stability changes are build inputs and must be retained.
4.  `-m none -d` is the common AFL launch setting in the recorded runs. Keep the fuzzer options and seed directory consistent within a comparison.

## 8. LibFuzzer

This document records the second compilation pipeline: LLVM libFuzzer with the Entropic power schedule. It is a separate baseline from AFL and from the entropy feedback implemented inside SEAFuzz. libFuzzer consumes a corpus directory directly; it does not use AFL’s `@@` file substitution.

## Source and common runtime

The runtime source is `compiler-rt/lib/fuzzer` from the LLVM checkout at commit `dc9be4ee30d07060a21273bdf8c64e4f34165562`. The original checkout was `/home/gg/llvm-project`. Set paths for a different checkout as follows:

``` sh
export LLVM_ROOT="${LLVM_ROOT:-$HOME/llvm-project}"
export LIBFUZZER_ROOT="$LLVM_ROOT/compiler-rt/lib/fuzzer"
export CC="${CC:-clang}"
export CXX="${CXX:-clang++}"
```

Every target script first builds the runtime explicitly:

``` sh
(cd "$LIBFUZZER_ROOT" && CXX="$CXX" ./build.sh)
test -f "$LIBFUZZER_ROOT/libFuzzer.a"
```

The recorded target builds use:

``` text
-O1 -g -fno-omit-frame-pointer -fsanitize=fuzzer-no-link,address
```

The final harness link adds `-fsanitize=address` and the explicit `libFuzzer.a`. Build/configure steps set `ASAN_OPTIONS=detect_leaks=0` and, for CMake projects, `LSAN_OPTIONS=detect_leaks=0` to prevent LeakSanitizer from interfering with configure-time test programs. During fuzzing, the recorded runtime setting is:

``` sh
ASAN_OPTIONS='abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1'
```

## Rebuild scripts and outputs

The build scripts below are the authoritative commands. They recreate their own libFuzzer build directory where applicable and place the runnable target in `out/`. Run them from any directory:

| Project       | Script                                              | Harness used                                                                 | Output                                                             | Corpus                                 |
|---------------|-----------------------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------|----------------------------------------|
| libpng        | `fuzzing_lib/fuzzing_libpng/build_libfuzzer.sh`     | `contrib/oss-fuzz/libpng_read_fuzzer.cc`                                     | `out/libpng_read_fuzzer`                                           | `fuzzing_lib/fuzzing_libpng/seeds`     |
| libsndfile    | `fuzzing_lib/fuzzing_libsndfile/build_libfuzzer.sh` | `libsndfile/ossfuzz/sndfile_fuzzer.cc`                                       | `out/sndfile_fuzzer`                                               | `fuzzing_lib/fuzzing_libsndfile/seeds` |
| Lua           | `fuzzing_lib/fuzzing_lua/build_libfuzzer.sh`        | local `lua_fuzzer.cc`                                                        | `out/lua_fuzzer`                                                   | `fuzzing_lib/fuzzing_lua/seeds`        |
| PHP           | `fuzzing_lib/fuzzing_php/build_libfuzzer.sh`        | `php-src/sapi/fuzzer`                                                        | `out/php-fuzz-*`                                                   | `fuzzing_lib/fuzzing_php/seeds`        |
| Poppler       | `fuzzing_lib/fuzzing_poppler/build_libfuzzer.sh`    | `cpp/tests/fuzzing/pdf_fuzzer.cc`                                            | `out/pdf_fuzzer`                                                   | `fuzzing_lib/fuzzing_poppler/seeds`    |
| SQLite        | `fuzzing_lib/fuzzing_sqlite/build_libfuzzer.sh`     | `sqlite/test/ossfuzz.c`                                                      | `out/sqlite3_fuzz`                                                 | `fuzzing_lib/fuzzing_sqlite/seeds`     |
| Bloaty        | `fuzzing_lib/fuzzing_bloaty/build_libfuzzer.sh`     | `tests/fuzz_target.cc`                                                       | `out/bloaty_fuzz_target`                                           | `fuzzing_lib/fuzzing_bloaty/seeds`     |
| RE2           | `fuzzing_lib/fuzzing_re2/build_libfuzzer.sh`        | `re2/re2/fuzzing/re2_fuzzer.cc`                                              | `out/re2_fuzzer`                                                   | `fuzzing_lib/fuzzing_re2/seeds`        |
| binutils 2.40 | `fuzzing_lib/real_project/build_libfuzzer.sh`       | local harnesses for cxxfilt, gas, nm, objcopy, objdump, readelf, size, strip | `out/{demangler,gas,nm,objcopy,objdump,readelf,size,strip}_fuzzer` | `real_project/seeds/<target>`          |

Run the scripts with the checkout layout used by the records:

``` sh
/home/gg/fuzzing_lib/fuzzing_libpng/build_libfuzzer.sh
/home/gg/fuzzing_lib/fuzzing_libsndfile/build_libfuzzer.sh
/home/gg/fuzzing_lib/fuzzing_lua/build_libfuzzer.sh
/home/gg/fuzzing_lib/fuzzing_php/build_libfuzzer.sh
/home/gg/fuzzing_lib/fuzzing_poppler/build_libfuzzer.sh
/home/gg/fuzzing_lib/fuzzing_sqlite/build_libfuzzer.sh
/home/gg/fuzzing_lib/fuzzing_bloaty/build_libfuzzer.sh
/home/gg/fuzzing_lib/fuzzing_re2/build_libfuzzer.sh
/home/gg/fuzzing_lib/real_project/build_libfuzzer.sh
```

The scripts currently contain the original absolute project paths. 

## Target-specific build notes

- **libpng:** configures a static libpng and links the existing OSS-Fuzz harness against the instrumented library and `libFuzzer.a`.
- **libsndfile:** uses `--disable-shared --enable-static --enable-ossfuzzers`. Do not add `--disable-full-suite`, because that would remove the fuzzer target from this source tree’s generated Makefile.
- **Lua:** builds only the `a` target (`liblua.a`) and links the local harness. The harness limits memory and instructions and disables file/output side effects.
- **PHP:** configures `--disable-all --enable-fuzzer --with-pic   --enable-debug-assertions --enable-exif`, builds the CLI internal-functions object first, then `make fuzzer`. The script copies parser, execute, unserialize, unserializehash, exif, and any generated JSON fuzzer plus the dictionary directory.
- **Poppler:** builds static core and C++ libraries with CMake, while disabling GLib, Qt, utilities, tests, NSS, and network support. The output is the raw PDF `pdf_fuzzer` target.
- **SQLite:** compiles the amalgamation and OSS-Fuzz harness with the recorded SQLite feature macros, then links `-ldl -lz -lpthread -lm`.
- **Bloaty:** configures CMake with `BUILD_TESTING=OFF` and links its existing `tests/fuzz_target.cc` to the explicit libFuzzer runtime.
- **RE2:** builds a static `libre2.a` with CMake and links the repository’s `re2_fuzzer.cc` harness.
- **binutils:** configures instrumented binutils 2.40, builds the required object files, renames each command-line `main` symbol, and links it with a corpus-reading harness. `demangler_fuzzer` uses `seeds/cxxfilt`; the other seven targets use their matching seed directories.

## Entropic invocation

The Entropic schedule is enabled explicitly with `-entropic=1`. A short smoke run looks like this:

``` sh
ASAN_OPTIONS='abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1' \
  /home/gg/fuzzing_lib/fuzzing_libpng/out/libpng_read_fuzzer \
  -runs=1 -rss_limit_mb=0 \
  /home/gg/fuzzing_lib/fuzzing_libpng/seeds
```

The recorded comparison form is:

``` sh
mkdir -p /home/gg/fuzzing_lib/fuzzing_libpng/artifacts

ASAN_OPTIONS='abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1' \
# Bind CPU cores
taskset -c 0 \
/home/gg/fuzzing_lib/fuzzing_libpng/out/libpng_read_fuzzer \
-entropic=1 \
-rss_limit_mb=0 \
-artifact_prefix=/home/gg/fuzzing_lib/fuzzing_libpng/artifacts/ \
/home/gg/fuzzing_lib/fuzzing_libpng/seeds
```

## 9. Experimental Environment, Run Counts, and Configuration

The hardware/system information below is observable on the current reconstruction and data-audit machine. 

| Item             | Recorded value                                                                                    |
|------------------|---------------------------------------------------------------------------------------------------|
| CPU              | AMD EPYC 7B13 64-Core Processor，1 socket，64 logical CPUs                                        |
| Memory           | Approximately 62 GiB RAM and 2 GiB swap                                                           |
| Operating system | Ubuntu 20.04.6 LTS, x86_64                                                                        |
| Kernel           | Linux 5.15.0-139-generic                                                                          |
| AFL              | AFL 2.57b，commit `61037103ae3722c8060ff7082994836a794f978e`                                      |
| LLVM/Clang       | LLVM/Clang 10 is recorded; the Entropic runtime uses the recorded `compiler-rt/lib/fuzzer` commit |
| Build tools      | GNU Make 4.2, CMake 3.16, Autoconf 2.69 (experiment record)                                       |

The complete SEAFuzz configuration requires no extra options. Ablation configurations use the `-A` (scheduler-only), `-P` (energy-only), `-RF`, `-EF`, `-E` and `-R` options defined in the implementation document, together with the corresponding `AFL4_*`/`AFL_ENTROPIC*` environment variables. 

Parameter-sensitivity experiments should start from the defaults in the implementation document, use five runs per parameter configuration, and preserve the parameter grid, raw results for each run, and summary values. 
