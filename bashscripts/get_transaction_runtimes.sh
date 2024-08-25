#!/bin/bash
# this script recieves a log like in this example:


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
