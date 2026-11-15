Command line used to find this crash:

/home/gg/AFL/afl-fuzz -i /home/gg/real_project/seeds/gas -o /home/gg/real_project/output1/gas/afl/out0 -m none -d -- /home/gg/real_project/build-afl-asan/gas/as-new -o /dev/null @@

If you can't reproduce a bug outside of afl-fuzz, be sure to set the same
memory limit. The limit used for this fuzzing session was 0 B.

Need a tool to minimize test cases before investigating the crashes or sending
them to a vendor? Check out the afl-tmin that comes with the fuzzer!

Found any cool bugs in open-source tools using afl-fuzz? If yes, please drop
me a mail at <lcamtuf@coredump.cx> once the issues are fixed - I'd love to
add your finds to the gallery at:

  http://lcamtuf.coredump.cx/afl/

Thanks :-)
