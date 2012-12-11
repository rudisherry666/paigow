# This file defines the Deal python class, derived from the
# django 'models.Model' class that relates python classes to
# relational database tables.
#
# A 'deal' is the ordering of a deck that implies the tiles
# dealt to each player in a game.  Since the algorithm that
# deals is the same every time, all we need to do is specify
# the ordering of the tiles and that dictates what the players
# will get.
#
# Since there are only sixteen distinct tile in terms of game
# play (regardless of what they look like), we can represent
# each tile as a hex digit and have 32 hex digits that represent
# the ordering of the tiles.
#
# We can distinguish the tiles whose individuals are different
# (like the mixed pairs or gee joon tiles) by assuming the first
# tile is one of them and the second is another, in the order
# they appear in the deck.

from django.db import models

from paigow.models import PGGame

class PGDeal( models.Model ):
  
  # make sure the DB table name is what we want
  class Meta:
    app_label = 'paigow'
  
  # This 32-character hex string defines the deal
  deck = models.CharField( max_length = 32 )
  
  # it's always part of some game, and some deal number
  game = models.ForeignKey( PGGame )
  deal_number = models.PositiveSmallIntegerField()
  
  # The deal shows as the ordering
  def __unicode__( self ):
    return self.tiles

  # Create it with an array of tiles and the game/deal#
  def create( cls, tiles, game, deal_number ):
    from models.pgtile import PGTile
    deck_vals = ""
    for tile in tiles:
      char = "0123456789ABCDEF"[tile.rank]
      deck_vals += char
    return cls( deck = deck_vals, game = game, deal_number = deal_number )

