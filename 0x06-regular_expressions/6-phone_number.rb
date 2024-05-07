#!/usr/bin/env ruby
matches = []

ARGV[0].gsub(/^\d{10}$/) do |match|
  matches << match
end

puts matches.join

