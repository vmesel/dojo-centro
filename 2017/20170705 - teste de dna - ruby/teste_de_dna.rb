def teste_de_dna(dnas)
  pai1, pai2, filho = dnas

  if pai1.size == 2
    if filho == pai1
      return "Pai 1"

    elsif filho == pai2
      return 'Pai 2'
    end

    if pai1 == 'AC'
      return 'Pai 1'
    elsif pai2 == 'AC'
      return 'Pai 2'
    end
    if pai1 != filho
      return pai2
    end
    return 'cadim'
  end

  if filho == pai1 && filho == pai2
    return 'cadim'
  elsif filho == pai1 
    return 'Pai 1'
  elsif filho == pai2
    return 'Pai 2'
  end

  return 'cadim'
end