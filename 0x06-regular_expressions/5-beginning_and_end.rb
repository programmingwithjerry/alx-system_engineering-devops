#!/usr/bin/env ruby
input_string = ARGV[0]

# Split into individual words or characters
parts = input_string.split(/[^a-zA-Z]/)

# Use `grep` or `select` to find matches
matches = parts.grep(/h.n/)

# Join the results
puts matches.join

