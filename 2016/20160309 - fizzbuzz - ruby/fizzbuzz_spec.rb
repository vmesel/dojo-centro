# http://www.dojopuzzles.com/problemas/exibe/encontre-o-telefone
require_relative 'fizzbuzz'

describe 'Fizzbuzz' do
  it 'is Fizz for 3' do
    expect(fizzbuzz(3)).to eq('Fizz')
  end

  it 'is Buzz for 5' do
    expect(fizzbuzz(5)).to eq('Buzz')
  end
  
  it 'is 1 for 1' do
    expect(fizzbuzz(1)).to eq(1)
  end
end
