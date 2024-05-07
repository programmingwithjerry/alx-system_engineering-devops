#!/usr/bin/env ruby
input_string = ARGV[0]

# Split the string into characters and select uppercase ones
matches = input_string.chars.grep(/[A-Z]/)

puts matches.join

