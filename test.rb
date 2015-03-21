require 'rubygems'
require 'sonos'
system = Sonos::System.new # Auto-discovers your system
speaker = system.speakers.first

puts speaker.inspect

speaker.play "https://dl.dropboxusercontent.com/u/21513800/05%20An%20Eluardian%20Instance.mp3?dl=1"
