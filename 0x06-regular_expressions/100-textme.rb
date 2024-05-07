#!/usr/bin/env ruby
matches = []

ARGV[0].gsub(/\[(?:from:|to:|flags:)(.*?)\]/) do |match|
  # Extract the captured group and add to matches
  matches << match.match(/\[(?:from:|to:|flags:)(.*?)\]/)[1]
end

puts matches.join(",")

