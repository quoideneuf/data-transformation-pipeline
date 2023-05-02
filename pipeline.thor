#!/usr/bin/env ruby

class Pipeline < Thor

  desc "setup", "setup the database and directories"
  def setup
    App.setup
  end

  desc "harvest1", "harvest some records"
  def harvest1
    puts "Pretend I am harvesting from the first source and writing the data to #{ENV['DATA_DIR']}/harvest1"
  end

  desc "harvest2", "harvest some more records"
  def harvest2
    puts "Pretend I am harvesting from the second source and writing the data to #{ENV['DATA_DIR']}/harvest2"
  end

  desc "process1", "process some records"
  def process1
    puts "Pretend I am processing from the first source and writing the data to #{ENV['DATA_DIR']}/process"
  end

  desc "process2", "process some more records"
  def process2
    puts "Pretend I am processing from the second source and writing the data to #{ENV['DATA_DIR']}/process"
  end

end
