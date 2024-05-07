#!/usr/bin/env ruby
result = ""

# Using gsub to find and collect matches
ARGV[0].gsub(/hb?tn/) { |match| result += match }

puts result

