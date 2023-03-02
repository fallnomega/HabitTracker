import requests
import pixela

my_pixela = pixela.Pixela()
# Run if this is the first time running it or don't have Pixela account.
my_pixela.create_user_account()

# # create graph if you haven't already
my_pixela.create_graph()

# Post to graph
my_pixela.post_to_graph()

my_pixela.update_graph()
