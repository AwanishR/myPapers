Removing duplicate entry and store in corpus file
-------------------------------------------------
create a list of seen lines say line_seen.
read line from corpus_temp file
if line is not in line_seen
	write in corpus file
	add in the list of line_seen
end