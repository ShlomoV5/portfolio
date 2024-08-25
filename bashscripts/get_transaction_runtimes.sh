#!/bin/bash
# this script recieves a log like the example file (exam.log) and finds all transactions and their id,
# and creates a list of id/runtime according to the timestamp of start and end.
# I'm very proud of learning how to do this in just like 30 minutes... I love these challenges and can
# do them for hours! (Thanks for the institute who gave me this assignment as an exam, I can't
# credit them explicitly so that I don't ruin their exam =)

grep -E 'transaction [0-9]+ begun|transaction done' exam.log | \
cut -f 1,5 | \
sed 's/transaction//g; s/ begun//g; s/, id=//g; s/done//g;' | \
gawk ' \
{split($2, time_parts, /:/);
split(time_parts[3],times, ".");
milliseconds = (time_parts[1] * 3600 + time_parts[2] * 60 + times[1]) * 1000 + times[2];
if (premil) {
runtime = (milliseconds - premil);
premil = ""; results[;
} else {
premil = milliseconds;
}
}
END {
asort(results);
for (i = 1; i <= length(results); i++) {
results[i] = result;
}
}'
