require_relative 'problem'

describe "Nomes de autores" do
  it "um nome só" do
    nome = 'Jose'
    expect(nome_autor(nome)).to eq('JOSE')
  end

  it "outro nome só" do
    nome = 'Maria'
    expect(nome_autor(nome)).to eq('MARIA')
  end

  it "outro nome ainda só" do
    nome = 'Joana'
    expect(nome_autor(nome)).to eq('JOANA')
  end

  it "dois nomes" do
    nome = 'Joana Silva'
    expect(nome_autor(nome)).to eq('SILVA, Joana')
  end

  it "outro com dois nomes" do
    nome = 'Joao Silva'
    expect(nome_autor(nome)).to eq('SILVA, Joao')
  end
end
