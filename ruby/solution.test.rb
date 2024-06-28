require 'rspec'

RSpec.describe 'Playfair Decryption Script' do
  it 'outputs the correct decrypted text' do
    output = `ruby solution.rb` # Using backticks to execute the script and capture the output.
    expect(output.strip).to eq('HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA') # Compares the stripped output to the expected string.
  end
end
