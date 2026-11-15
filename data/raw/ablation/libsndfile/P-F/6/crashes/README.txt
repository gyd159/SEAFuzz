Command line used to find this crash:

/home/gg/afl4_e_s_rf_ef/afl4/afl-fuzz -i /home/gg/fuzzing_libsndfile/seeds -o /home/gg/fuzzing_lib/output9/afl4_rf/libsndfile/out7 -m none -d -RF -- /home/gg/fuzzing_libsndfile/libsndfile/ossfuzz/sndfile_fuzzer @@

If you can't reproduce a bug outside of afl-fuzz, be sure to set the same
memory limit. The limit used for this fuzzing session was 0 B.

Need a tool to minimize test cases before investigating the crashes or sending
them to a vendor? Check out the afl-tmin that comes with the fuzzer!

Found any cool bugs in open-source tools using afl-fuzz? If yes, please drop
me a mail at <lcamtuf@coredump.cx> once the issues are fixed - I'd love to
add your finds to the gallery at:

  http://lcamtuf.coredump.cx/afl/

Thanks :-)
