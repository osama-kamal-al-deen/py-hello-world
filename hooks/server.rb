require 'sinatra'
require 'json'
require 'net/http'
require 'uri'

uri = URI.parse("http://localhost:8080/git/notifyCommit?url=https://github.com/osama-kamal-al-deen/py-hello-world.git")

post '/payload' do
  response = Net::HTTP.get_response(uri)
end