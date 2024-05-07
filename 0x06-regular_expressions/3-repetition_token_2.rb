#!/usr/bin/env ruby
matches = []

# Use gsub with a block to capture matches
ARGV[0].gsub(/hbt+n/) { |m| matches << m }

# Join and print the results
puts matches.join

