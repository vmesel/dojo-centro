def pitagoras(*lista)
  result = 'tripla'

  if lista.include?(3) && lista.include?(5) && lista.include?(4)
    result << ' pitagorica primitiva'
  end

  result
end