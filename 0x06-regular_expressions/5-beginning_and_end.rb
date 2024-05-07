#!/usr/bin/env ruby
matches = []

ARGV[0].gsub(/h.n/) do |m|
  matches << m
end

puts matches.join

