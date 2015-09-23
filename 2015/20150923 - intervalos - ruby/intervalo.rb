def intervalos(lista)
  resultado = []

  if lista.size > 1
    if lista[1] - lista[0] == 1
      resultado << "#{lista[0]}-#{lista[1]}"
    end

    if lista.size == 3
      resultado << lista[2].to_s
    end
  else
    lista.each do |elemento|
      resultado << elemento.to_s  
    end
  end

  resultado
end