from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView
from paigow.models import PGTile, PGGame

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'paigow.views.home', name='home'),
  # url(r'^paigow/', include('paigow.foo.urls')),

  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  #url(r'^admin/', include(admin.site.urls)),
  
  url(r'^$', 'paigow.views.home' ),
  url(r'^home$', 'paigow.views.home' ),
  url(r'^register$', 'paigow.views.register' ),
  url(r'^login$', 'paigow.views.login' ),
  url(r'^logout$', 'paigow.views.logout' ),
  url(r'^game/new$', 'paigow.views.new_game' ),
  url(r'^game/add$', 'paigow.views.add_game' ),
  url(r'^game/([0-9]+)$', 'paigow.views.play_game' ),
  
  # given the chars representing four tiles for a set, return
  # the labels for the two hands separated by vertical bar.
  url(r'^data/hand/', 'paigow.views.data_hand_label' ),
  
  # given the game, return the state of the
  # opponent as a string that is shown, preceded by a
  # vertical bar (to distinguish from errors of some sort).
  # first param: game ID; player ID is in request session.
  url(r'^data/game/([0-9]+)/opponent_state/', 'paigow.views.data_opponent_state' ),
  url(r'^data/game/([0-9]+)/player_state/', 'paigow.views.data_player_state' ),
  
  # given the game, mark the player as having set
  # their hands and are ready to compare.
  url(r'^data/game/([0-9]+)/tiles_are_set', 'paigow.views.tiles_are_set' ),
  
  # the player has set their tiles and wants a preview
  # of the hands.  This will return the three sets with
  # the same hands, but switched if necessary to put the
  # high-low in the right order, and within each hand, the
  # tiles are switched if necessary to high-low.
  url(r'^data/game/([0-9]+)/preview_hands', 'paigow.views.preview_hands' ),
  url(r'^data/game/([0-9]+)/unpreview_hands', 'paigow.views.unpreview_hands' ),
  
  # the player is getting the opponent's hand to show, now
  # that both players are finished setting the tiles.
  url(r'^data/game/([0-9]+)/opponent_tiles', 'paigow.views.get_opponent_tiles' ),
  
  # /tile or /tiles/ : show all the tiles
  url(r'^tiles[/]*$',
    ListView.as_view(
        queryset=PGTile.objects.order_by('-tile_rank'),
        context_object_name='tile_list',
        template_name='paigow/tile_list.html'
        )),
  
  # /tile/<id> : show tile details
  url(r'^tiles/(?P<pk>\d+)/$',
    DetailView.as_view(
        model=PGTile)),
  
)

