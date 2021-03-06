# http://www.dojopuzzles.com/problemas/exibe/caixa-eletronico/
require './caixa_eletronico'

describe 'Caixa Eletronico' do
  it 'sacar 10 reais' do
    expect(sacar(10)).to eq([10])
  end

  it 'sacar 20 reais' do
    expect(sacar(20)).to eq([20])
  end

  it 'sacar 50 reais' do
    expect(sacar(50)).to eq([50])
  end

  it 'sacar 100 reais' do
    expect(sacar(100)).to eq([100])
  end

  it 'sacar 30 reais' do
    expect(sacar(30)).to eq([10, 20])
  end

  it 'sacar 60 reais' do
    expect(sacar(60)).to eq([10, 50])
  end

  it 'sacar 70 reais' do
    expect(sacar(70)).to eq([20, 50])
  end

  it 'sacar 40 reais' do
    expect(sacar(40)).to eq([20, 20])
  end
  it 'sacar 120 reais' do
    expect(sacar(120)).to eq([20, 100])
  end

  it 'sacar 150 reais' do
    expect(sacar(150)).to eq([50, 100])
  end

  it 'sacar 200 reais' do
    expect(sacar(200)).to eq([100, 100])
  end

  it 'sacar 80 reais' do
    expect(sacar(80)).to eq([10, 20, 50])
  end

  it 'sacar 90 reais' do
    expect(sacar(90)).to eq([20, 20, 50])
  end

  it 'sacar 130 reais' do
    expect(sacar(130)).to eq([10, 20, 100])
  end

  it 'sacar 140 reais' do
    expect(sacar(140)).to eq([20, 20, 100])
  end

end