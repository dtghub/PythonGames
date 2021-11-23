import unittest
# from src.BlackJack import deal_to_player
# from src.PlayingCard import *
from src.BlackJack import *


class BlackJackTest(unittest.TestCase):

    def test_deal_to_player_under(self):
        sampleDeck = ['H3', 'D2', 'S5', 'C7']
        playerHand = ['H2', 'S2']
        testDeal = deal_to_player(sampleDeck,playerHand)
        self.assertTrue(testDeal)

    def test_deal_to_player_over(self):
        sampleDeck = ['H9', 'D8', 'S7', 'C9']
        playerHand = ['HK', 'SQ']
        testDeal = deal_to_player(sampleDeck,playerHand)
        self.assertFalse(testDeal)



    def test_find_winner_firstHand(self):
        sampleHand = [['SK', 'H5', 'S4'], ['H8', 'D3', 'S2', 'C5']]
        testFind = find_winner(sampleHand)
        self.assertEqual([0], testFind)

    def test_find_winner_second_hand(self):
        sampleHand = [['SK', 'H5', 'S4'], ['HK', 'D3', 'S2', 'C5']]
        testFind = find_winner(sampleHand)
        self.assertEqual([1], testFind)

    def test_find_winner_draw_five(self):
        sampleHand = [['SK', 'H5', 'S4'], ['H9', 'D3', 'S2', 'C5'], ['H2', 'S3', 'D2', 'H3', 'HQ']]
        testFind = find_winner(sampleHand)
        self.assertEqual([2], testFind)



    def test_score_hand(self):
        sampleHand = ['H2', 'S3', 'D2', 'H3', 'HQ']
        testScore = score_hand(sampleHand)
        self.assertEqual(20, testScore)

    def test_score_hand_ace_low(self):
        sampleHand = ['S5', 'D2', 'H3', 'HQ', 'HA']
        testScore = score_hand(sampleHand)
        self.assertEqual(21, testScore)

    def test_score_hand_ace_high(self):
        sampleHand = ['H2', 'S3', 'D2', 'H3', 'HA']
        testScore = score_hand(sampleHand)
        self.assertEqual(21, testScore)



    def test_deal_to_player_over(self):
        sampleHand = ['SK', 'H5', 'S4']
        sampleDeck = ['H9', 'D8', 'S7', 'C9']
        testDeal = deal_to_player(sampleDeck, sampleHand)
        self.assertFalse(testDeal)

    
    def test_deal_to_player_under(self):
        sampleHand = ['H2', 'S3', 'D2', 'H3']
        sampleDeck = ['H3', 'D2', 'S5', 'C7']
        testDeal = deal_to_player(sampleDeck, sampleHand)
        self.assertTrue(testDeal)




# if __name__ == '__main__':
#     unittest.main()




# class PlayingCardTest(unittest.TestCase):

#     def test_generate_deck(self):
#         self.assertEqual(52, len(generate_deck()))
