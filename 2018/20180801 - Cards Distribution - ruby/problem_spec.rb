require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/pt/problems/view/2821

describe "Cards Distribution" do
  it "2 cards, 1 player" do
    cards = ['A', 'A']
    player_quantity = 1
    expect(max_sum(cards, player_quantity)).to eq(2)
  end

  it "3 cards, 1 player" do
    cards = ['A', 'A', 'A']
    player_quantity = 1
    expect(max_sum(cards, player_quantity)).to eq(3)
  end

  it "2 other cards, 1 player" do
    cards = ['A', '2']
    player_quantity = 1
    expect(max_sum(cards, player_quantity)).to eq(3)
  end

  it "still 2 cards, 1 player" do
    cards = ['A', 'J']
    player_quantity = 1
    expect(max_sum(cards, player_quantity)).to eq(12)
  end

  it "yet 2 cards, 1 player" do
    cards = ['A', 'Q']
    player_quantity = 1
    expect(max_sum(cards, player_quantity)).to eq(13)
  end

  it "another 2 cards, 1 player" do
    cards = ['A', 'K']
    player_quantity = 1
    expect(max_sum(cards, player_quantity)).to eq(14)
  end

  it "2 cards, 2 players" do
    cards = ['A', 'A']
    player_quantity = 2
    expect(max_sum(cards, player_quantity)).to eq(1)
  end

  it "other 2 cards, 2 players" do
    cards = ['A', '2']
    player_quantity = 2
    expect(max_sum(cards, player_quantity)).to eq(2)
  end

  it "still other 2 cards, 2 players" do
    cards = ['A', '3']
    player_quantity = 2
    expect(max_sum(cards, player_quantity)).to eq(3)
  end

  it "3 cards, 2 players" do
    cards = ['A', '3', '3']
    player_quantity = 2
    expect(max_sum(cards, player_quantity)).to eq(4)
  end

  it "other 3 cards, 2 players" do
    cards = ['6', '3', '3']
    player_quantity = 2
    expect(max_sum(cards, player_quantity)).to eq(6)
  end

  it "4 cards, 2 players" do
    cards = ['A', '2', '3', '6']
    player_quantity = 2
    expect(max_sum(cards, player_quantity)).to eq(6)
  end

  it "5 cards, 2 players" do
    cards = ['4', 'A', 'A', 'A', 'A']
    player_quantity = 2
    expect(max_sum(cards, player_quantity)).to eq(4)
  end

end
