def max_sum(cards, player_quantity)
  cards_values = Hash.new { |hash, key| key.to_i }.merge({
    'A' => 1,
    'J' => 11,
    'Q' => 12,
    'K' => 13
  })

  cards = cards.map { |card| cards_values[card] }
  limit = cards.reduce(&:+)

  groups = cards.each_slice(cards.length.fdiv(player_quantity).ceil).to_a

  limit = [limit, groups.map { |group| group.reduce(&:+) }.max].min
  return limit if groups.length == 1 || groups[0].length == 1

  if groups[1].reduce(&:+) > groups[0].reduce(&:+)
    groups[0].push(groups[1].shift)
  else
    groups[1].unshift(groups[0].pop)
  end

  limit = [limit, groups.map { |group| group.reduce(&:+) }.max].min
  return limit if groups[0].length == 1 || groups[1].length == 1 

  if groups[1].reduce(&:+) > groups[0].reduce(&:+)
    groups[0].push(groups[1].shift)
  else
    groups[1].unshift(groups[0].pop)
  end

  limit = [limit, groups.map { |group| group.reduce(&:+) }.max].min
  limit
end