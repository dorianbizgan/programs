#  File: Poker.py

#  Description: simulates a game of poker and determines winner

#  Student's Name: Dorian Bizgan

#  Student's UT EID: dab4567

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 1/8/18

#  Date Last Modified: 1/10/18

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)

    # determine the each type of hand and print
    type_of_hand = []  # create list to store points for each hand


    for i in range(len(self.players)): # run through tests for each hand
      if self.is_royal(self.players[i]):
        type_of_hand.append(int(10))
        continue

      if self.is_straight_flush(self.players[i]):
        type_of_hand.append(int(9))
        continue

      if self.is_four_kind(self.players[i]):
        type_of_hand.append(int(8))
        continue

      if self.is_full_house(self.players[i]):
        type_of_hand.append(int(7))
        continue

      if self.is_flush(self.players[i]):
        type_of_hand.append(int(6))
        continue

      if self.is_straight(self.players[i]):
        type_of_hand.append(int(5))
        continue

      if self.is_three_kind(self.players[i]):
        type_of_hand.append(int(4))
        continue

      if self.is_two_pair(self.players[i]):
        type_of_hand.append(int(3))
        continue

      if self.is_one_pair(self.players[i]):
        type_of_hand.append(2)
        continue

      if self.is_high_card(self.players[i]):
        type_of_hand.append(1)
        continue

    #makes a list of points in same order as indeces of hands
    player_points_totals = []

    for k in range(len(type_of_hand)): 
      #number in length of list type_of_hand
      if type_of_hand[k] == 10:#royal flush
        #k also is the index of players hand hence the player[k]
        player_points_totals.append(self.royal_flush_points(self.players[k]))

      #straight flush points
      if type_of_hand[k] == 9:
        player_points_totals.append(self.straight_flush_points(self.players[k]))

      # four of a kind points
      if type_of_hand[k] == 8:
        player_points_totals.append(self.four_of_kind_points(self.players[k]))

      # full house points
      if type_of_hand[k] == 7:
        player_points_totals.append(self.full_house_points(self.players[k]))

      # flush points
      if type_of_hand[k] == 6:
        player_points_totals.append(self.flush_points(self.players[k]))

      # straight points
      if type_of_hand[k] == 5:
        player_points_totals.append(self.straight_points(self.players[k]))

      # three of a kind points
      if type_of_hand[k] == 4:
        player_points_totals.append(self.three_of_kind_points(self.players[k]))

      #two pair points
      if type_of_hand[k] == 3:
        player_points_totals.append(self.two_pair_points(self.players[k]))

      if type_of_hand[k] == 2:
        player_points_totals.append(self.one_pair_points(self.players[k]))

      if type_of_hand[k] == 1:
        player_points_totals.append(self.high_card_points(self.players[k]))



    card_type_definitions = {10:"Royal Flush",9:"Straight Flush",8:"Four of a Kind",7:"Full House",6:"Flush",5:"Straight",4:"Three of a Kind",3:"Two Pair",2:"One Pair",1:"High Card"}
    print()
    for i in range(len(player_points_totals)):
      print("Player " + str(i + 1) + ": " + str(card_type_definitions[type_of_hand[i]]))

    print()
    if player_points_totals.count(max(player_points_totals)) > 1:
      for i in range(player_points_totals.count(max(player_points))):
        print("Player", player_points_totals.index(max(player_points_totals)) + 1 + i, "wins.")
    else:
      print("Player",player_points_totals.index(max(player_points_totals)) + 1, "wins.")


  #calculate royal flush points
  def royal_flush_points(self, hand):
    total = (10 * (13 ** 5))
    for i in range(len(hand)):
      total += (hand[i].rank * (13 ** (4 - i)))
    return(total)

  #calculate straight flush points
  def straight_flush_points(self, hand):
    total = (9 * (13 ** 5))
    for i in range(len(hand)):
      total += (hand[i].rank * (13 ** (4 - i)))
    return(total)

  #calculate four of a kind points
  def four_of_kind_points(self, hand):
    total = (8 * (13 ** 5))
    if hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank:
      total += hand[4].rank 
      for i in range(4):
        total += hand[0].rank * (13 * 4 - i)
    if hand[1].rank == hand[2].rank == hand[3].rank == hand[4].rank:
      total += hand[0].rank 
      for i in range(4):
        total += hand[1].rank * (13 * 4 - i)
    return(total)

  #calculate full house points
  def full_house_points(self, hand):
    total = (7 * (13 ** 5))
    if hand[0].rank == hand[1].rank == hand[2].rank:
      for i in range(3):
        total += hand[0].rank * 13 ** (4 - i)
      for j in range(2):
        total += hand[3].rank * 13 ** (1 - i)
    if hand[2].rank == hand[3].rank == hand[4].rank:
      for i in range(3):
        total += hand[2].rank * 13 ** (4 - i)
      for j in range(2):
        total += hand[0].rank * 13 ** (1 - i)
    return(total)

  #calculate flush points
  def flush_points(self, hand):
    total = (6 * (13 ** 5))
    for i in range(len(hand)):
      total += (hand[i].rank * (13 ** (4 - i)))
    return(total)

  #calculate straight points
  def straight_points(self, hand):
    total = (5 * (13 ** 5))
    for i in range(len(hand)):
      total += (hand[i].rank * (13 ** (4 - i)))
    return(total)

  #calculated three of a kind points
  def three_of_kind_points(self, hand):
    total = (4 * (13 ** 5))
    if hand[0].rank == hand[1].rank == hand[2].rank:
      for i in range(3):
        total += hand[0].rank * 13 ** (4 - i)
      total += hand[3].rank * 13 + hand[4].rank
    if hand[2].rank == hand[3].rank == hand[4].rank:
      for i in range(3):
        total += hand[2].rank * 13 ** (4 - i)
      total += hand[0].rank * 13 + hand[1].rank
    return(total)

  #calculate two pair points
  def two_pair_points(self, hand):
    total = 3 * (13 ** 5)
    if hand[0].rank == hand[1].rank:
      total += hand[0].rank * (13 ** 4) + hand[1].rank * (13 ** 3)
      hand.pop(0)
      hand.pop(1)
      if hand[0].rank == hand[1].rank:
        total += hand[0].rank * (13 ** 2) + hand[1].rank * (13 ** 1)
        total += hand[4].rank
      else:
        total += hand[1].rank * (13 ** 2) + hand[1].rank * 13 + hand[2].rank
    else:
      total += hand[1].rank * (13 ** 4) + hand[2].rank * (13 ** 3) + hand[3].rank * (13 ** 2) + hand[4].rank * 13 + hand[0].rank
    return (total)

  #calculate one pair points
  def one_pair_points(self, hand):
    total = 2 * (13 ** 5) 
    
    if hand[0].rank == hand[1].rank:
      for i in range(len(hand)):
        total += hand[i].rank * 13 ** (4 - i)
    elif hand[1].rank == hand[2].rank:
      total += hand[1].rank * (13 ** 4) + hand[2].rank * (13 ** 3)
      hand.pop(1)
      hand.pop(1)
    elif hand[2].rank == hand[3].rank:
      total += hand[2].rank * (13 ** 4) + hand[3].rank * (13 ** 3)
      hand.pop(2)
      hand.pop(2)
    else:
      total += hand[3].rank * (13 ** 4) + hand[4].rank * (13 ** 3)
      hand.pop(3)
      hand.pop(3) 
    for i in range(3):
      total += hand[i].rank * 13 ** (3 - i)
    return (total)

  #calculate high card points
  def high_card_points(self, hand):
    return(hand[0].rank)

  # determine if a hand is a royal flush
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)
    
    return (same_suit and rank_order)


  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if not same_suit:
      return False

    numerical_order = True
    for i in range (len(hand)):
      if hand[i].rank - 1 != hand[i + 1].rank:
        return False
    return (same_suit and numerical_order)

  # determine if a hand is one pair
  def is_one_pair (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return True
        break
    return False

  def is_four_kind (self, hand):
    for i in range(2):
      if hand[i].rank == hand[i + 1].rank == hand[i + 2].rank == hand[i + 3].rank:
        return (True)
  
  
  def is_full_house (self, hand):
    if hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank == hand[4].rank or\
    hand[3].rank == hand[4].rank and hand[0].rank == hand[1].rank == hand[2].rank:
      return (True)
  
  def is_flush (self, hand):
    if hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit:
      return (True) 
  
  def is_straight (self, hand):
    is_straight_bool = True
    for i in range(len(hand) - 1):
      if hand[i].rank - 1 != hand[i + 1].rank:
        is_straight_bool = False
    return (is_straight_bool)
  
  def is_three_kind (self, hand):
    three_of_kind_bool = False
    for i in range(3):
      if hand[i].rank == hand[i + 1].rank == hand[i + 2].rank:
        three_of_kind_bool = True
    return(three_of_kind_bool)

  def is_two_pair (self, hand):
    if hand[0].rank == hand[1].rank and (hand[2].rank == hand[3].rank or hand[3].rank == hand[4].rank) or\
    hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank:
      return True
    return False

  def is_high_card (self, hand):
    max_card = [0]
    for i in range(len(hand)):
      if hand[i].rank > max_card[0]:
        max_card.pop(0)
        max_card.append(hand[i].rank)
    return(max_card)
def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))
  print()

  # create the Poker object
  game = Poker (num_players)

  # play the game (poker)
  game.play()

main()