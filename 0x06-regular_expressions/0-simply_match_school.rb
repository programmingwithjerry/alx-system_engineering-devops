#!/usr/bin/env ruby
input_string = ARGV[0]

# Split the string and then filter only parts with "School"
results = input_string.split(/[^a-zA-Z]/).select { |word| word == "School" }

# Join and output the results
puts results.join

