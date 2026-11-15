Command line used to find this crash:

/home/gg/afl4_energy_schedule/afl4/afl-fuzz -i /home/gg/fuzzing_libpng/seeds -o /home/gg/fuzzing_lib/output9/afl4_a/libpng/out5 -m none -d -P -- /home/gg/fuzzing_libpng/libpng_read_fuzzer @@

If you can't reproduce a bug outside of afl-fuzz, be sure to set the same
memory limit. The limit used for this fuzzing session was 0 B.

Need a tool to minimize test cases before investigating the crashes or sending
them to a vendor? Check out the afl-tmin that comes with the fuzzer!

Found any cool bugs in open-source tools using afl-fuzz? If yes, please drop
me a mail at <lcamtuf@coredump.cx> once the issues are fixed - I'd love to
add your finds to the gallery at:

  http://lcamtuf.coredump.cx/afl/

Thanks :-)
