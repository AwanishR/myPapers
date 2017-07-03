Corpus Algorightm
------------------------
For each line in training file
	Find nth position of string "<START:corp" where corp ={"habit","procedure","diagnosis","drug","vital"}
	remaining_line -> line_substring [n:end of line]
	extract the corpus data 
	corp_data -> substring_of _remaining_line[startpos:endpos] 
	[where startpos = index of ">" in string remainig_line +1, endpos = index of "<" in string remainin_line]
	remove leading and trailing spaces
	Write in corpus_temp file
end